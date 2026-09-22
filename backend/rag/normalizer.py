from typing import Any


def normalize_document(data: Any) -> str:

    # Already plain text
    if isinstance(data, str):
        return data

    # PDF / DOCX style output
    if isinstance(data, dict):

        # Common direct text field
        if "text" in data and isinstance(data["text"], str):
            return data["text"]

        # PPTX output
        if "slides" in data:
            parts = []

            for slide in data["slides"]:

                slide_number = slide.get("slide_number", "")
                parts.append(f"Slide {slide_number}")

                texts = slide.get("texts", [])

                if isinstance(texts, list):
                    parts.extend(str(text) for text in texts)
                else:
                    parts.append(str(texts))

            return "\n".join(parts)

    raise ValueError(
        "Unsupported document parser output format."
    )