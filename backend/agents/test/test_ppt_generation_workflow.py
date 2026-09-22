from agents.orchestrator import execute_task


result = execute_task(
    user_request=(
        "Research the latest trends in generative AI "
        "and create a PowerPoint presentation."
    )
)

print("\nSUPERVISOR:")
print(result["decision"])

print("\nAGENT RESULTS:")

for agent, output in result["results"].items():
    print(f"\n{agent}:")
    print(output)