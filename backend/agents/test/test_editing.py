from agents.editing_agent import edit_presentation


result = edit_presentation(
    input_path="uploads/1.pptx",
    instruction="Add two slides about the benefits of generative AI.",
    output_filename="edited_ai_test.pptx"
)

print("Generated:", result)