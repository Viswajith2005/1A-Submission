import fitz  # PyMuPDF
import os
import json

def extract_outline_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    headings = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" not in block:
                continue

            for line in block["lines"]:
                line_text = ""
                font_sizes = []
                for span in line["spans"]:
                    line_text += span["text"].strip()
                    font_sizes.append(span["size"])

                if not line_text.strip():
                    continue

                avg_font_size = sum(font_sizes) / len(font_sizes)
                heading_level = None

                # Heuristics to decide H1, H2, H3 based on font size
                if avg_font_size >= 16:
                    heading_level = "H1"
                elif 13 <= avg_font_size < 16:
                    heading_level = "H2"
                elif 11 <= avg_font_size < 13:
                    heading_level = "H3"

                if heading_level:
                    headings.append({
                        "level": heading_level,
                        "text": line_text,
                        "page": page_num + 1
                    })

    # Auto-assign first H1 as title (if exists)
    title = "[ ]"
    for i, h in enumerate(headings):
        if h["level"] == "H1":
            title = h["text"]
            del headings[i]  # Remove from outline
            break

    return {
        "title": title,
        "outline": headings
    }

def main():
    input_dir = "input"
    output_dir = "output"

    os.makedirs(output_dir, exist_ok=True)

    for file_name in os.listdir(input_dir):
        if file_name.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, file_name)
            output_data = extract_outline_from_pdf(pdf_path)

            json_filename = os.path.splitext(file_name)[0] + ".json"
            json_path = os.path.join(output_dir, json_filename)

            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(output_data, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
