from agents.orchestrator import execute_task


presentation_data = {
    "file_type": "pptx",
    "file_path": "uploads/1.pptx"
}


result = execute_task(
    user_request="Modify the presentation and add two slides about the benefits of generative AI.",
    presentation_data=presentation_data
)


print("\nSUPERVISOR:")
print(result["decision"])

print("\nAGENT RESULTS:")

for agent, output in result["results"].items():

    print(f"\n{agent}:")
    print(output)