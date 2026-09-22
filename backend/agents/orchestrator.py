from agents.supervisor import route_task
from agents.document_agent import analyze_doc
from agents.ppt_agent import analyze_presentation
from agents.research_agent import research_topic
from agents.editing_agent import edit_presentation
from rag.rag_agent import answer_question
from agents.generation_agent import generate_output
from agents.version_manager import get_current_file
from pathlib import Path

def execute_task(
    user_request: str,
    document_data: dict | None = None,
    presentation_data: dict | None = None
):

    if presentation_data is not None:
        file_type = presentation_data.get("file_type")

    elif document_data is not None:
        file_type = document_data.get("file_type")

    else:
        current_file = get_current_file()

        if current_file:
            file_type = Path(current_file).suffix.lower().lstrip(".")
        else:
            file_type = None


    decision = route_task(
    user_request=user_request,
    file_type=file_type
)
    
    results = {
        "decision": decision,
        "results": {}
    }

    for agent in decision.agents:

        if agent == "document_agent":

            if document_data is None:
                results["results"]["document_agent"] = {
                    "error": "No document data provided"
                }
            else:
                result = analyze_doc(document_data)

                results["results"]["document_agent"] = result


        elif agent == "ppt_agent":

            if presentation_data is None:
                results["results"]["ppt_agent"] = {
                    "error": "No presentation data provided"
                }
            else:
                result = analyze_presentation(presentation_data)

                results["results"]["ppt_agent"] = result

        elif agent == "research_agent":
            result = research_topic(user_request)

            results["results"]["research_agent"] = result
        elif agent == "editing_agent":
            file_path = None

    # If a presentation was uploaded in this request,
    # use that file.
            if presentation_data is not None:
                file_path = presentation_data.get("file_path")

    # Otherwise use the latest generated version.
            if file_path is None:
                file_path = get_current_file()

            if file_path is None:
                results["results"]["editing_agent"] = {
            "error": "No presentation available to edit"
        }

            else:
                output_path = edit_presentation(
            input_path=file_path,
            instruction=user_request
        )

                results["results"]["editing_agent"] = {
            "status": "Presentation edited successfully",
            "input_file": file_path,
            "output_file": output_path
        }
        elif agent == "rag_agent":
            if document_data is None and presentation_data is None:
                results["results"]["rag_agent"] = {
            "error": "No document provided"
        }
            else:
                document_id = None

                if presentation_data is not None:
                    document_id = presentation_data.get("filename")

                elif document_data is not None:
                    document_id = document_data.get("filename")

                rag_result = answer_question(
            question=user_request,
            document_id=document_id
        )

                results["results"]["rag_agent"] = rag_result
        elif agent == "generation_agent":
            research_result = results["results"].get("research_agent")

            if research_result is None:
                results["results"]["generation_agent"] = {
            "error": "No research result available for generation"
        }
            else:
                output_format = "docx"

                if "powerpoint" in user_request.lower() or "ppt" in user_request.lower():
                    output_format = "pptx"

                output_file = generate_output(
                    research_result=research_result,
                    output_format=output_format
        )

                results["results"]["generation_agent"] = {
                             "status": "File generated successfully",
                             "output_file": output_file
        }
    
        elif agent == "research_agent":
            research_result = research_topic(user_request)

            results["results"]["research_agent"] = research_result
        else:

            results["results"][agent] = {
                "status": "Agent not implemented yet"
            }

    return results