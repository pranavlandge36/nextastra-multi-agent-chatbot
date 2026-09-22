from agents.supervisor import route_task


# requests = [
#     'What are the cybersecurity challenges in this presentation?',
#     'Add two slides about blockchain advantages.'
# ]


# for request in requests:

#     print("\nUSER REQUEST:")
#     print(request)

#     result = route_task(request)

#     print("\nSUPERVISOR DECISION:")
#     print(result)

#     print("\nDICTIONARY:")
#     print(result.model_dump())

#     print("-" * 70)
decision = route_task(
    user_request="Add two slides about blockchain advantages.",
    file_type="pptx"
)
print("\nSUPERVISOR DECISION:")
print(decision)