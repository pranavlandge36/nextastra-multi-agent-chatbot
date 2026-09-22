import os


from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

from agents.schemas import SupervisorDecision


load_dotenv()

model = ChatOpenAI(
    model="nvidia/nemotron-3-super-120b-a12b",
    api_key=os.getenv("NVIDIA_API_KEY"),
    base_url="https://integrate.api.nvidia.com/v1",
    temperature=0
)

structured_model = model.with_structured_output(
    SupervisorDecision
)

def route_task(user_request: str,file_type: str | None = None) -> SupervisorDecision:

    prompt = f"""
You are the supervisor of a multi-agent AI system.

Your job is to understand the user's request and decide
which specialized agents are required.

Available agents:

1. document_agent
   - analyzes PDF and DOCX documents

2. ppt_agent
   - analyzes PowerPoint presentations and templates

3. research_agent
   - performs web research

4. rag_agent
   - retrieves relevant information from the knowledge base

5. generation_agent
   - generates DOCX or PPTX files

6. editing_agent
   - modifies previously generated documents or presentations

User request:

{user_request}

Uploaded file type:

{file_type}

Determine:

- the type of task
- which agents are required
- a short reason for the routing decision

Only select agents that are actually needed.
ROUTING RULES:

1. If the user wants to MODIFY, EDIT, UPDATE, CHANGE, ADD, REMOVE,
   or REWRITE an existing presentation or document:
   use editing_agent.

2. If the user asks a QUESTION about the CONTENT of an uploaded
   document or presentation:
   use rag_agent.

3. If the user wants to ANALYZE the structure, layout, style,
   fonts, design, or template of an uploaded PowerPoint:
   use ppt_agent.

4. If the user wants to ANALYZE the structure or content of an
   uploaded PDF or DOCX:
   use document_agent.

5. If the user wants to RESEARCH a topic using current web information:
   use research_agent.

6. If the user wants to CREATE a new presentation or report from
   research:
   use research_agent and generation_agent.


IMPORTANT PRIORITY:

- MODIFY / EDIT / ADD / REMOVE / UPDATE → editing_agent
- CONTENT QUESTION → rag_agent
- PPT DESIGN / LAYOUT / STYLE ANALYSIS → ppt_agent
- PDF / DOCX ANALYSIS → document_agent
- WEB RESEARCH → research_agent
- NEW FILE GENERATION → generation_agent


FILE CONTEXT RULE:

If an uploaded file type is provided and the user requests an
editing operation, assume the user wants to modify that uploaded
file and select editing_agent.

Do NOT route an editing request to research_agent or generation_agent
when an existing file is provided.

Examples:

"What are the cybersecurity challenges in this presentation?"
→ rag_agent

"Summarize this presentation."
→ rag_agent

"Analyze the layout and fonts of this PowerPoint."
→ ppt_agent

"Add two slides to this presentation."
→ editing_agent

"Modify the presentation and add a slide about advantages."
→ editing_agent

"Analyze this PDF."
→ document_agent

"Research the latest AI trends."
→ research_agent

"Create a PowerPoint about the latest AI trends."
→ research_agent + generation_agent
"""
    response = structured_model.invoke(prompt)

    return response