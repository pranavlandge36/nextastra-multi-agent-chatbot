from agents.orchestrator import execute_task
from agents.version_manager import get_current_file, get_versions


# First edit — uploaded presentation
first = execute_task(
    user_request="Add two slides about the benefits of generative AI.",
    presentation_data={
        "file_path": "uploads/1.pptx",
        "filename": "1.pptx",
        "file_type": "pptx"
    }
)

print("\nFIRST EDIT:")
print(first["results"]["editing_agent"])

print("\nCURRENT VERSION:")
print(get_current_file())


# Second edit — no uploaded file
second = execute_task(
    user_request="Add one more slide about challenges of generative AI."
)

print("\nSECOND EDIT:")
print(second["results"]["editing_agent"])

print("\nCURRENT VERSION AFTER SECOND EDIT:")
print(get_current_file())


print("\nALL VERSIONS:")
print(get_versions())