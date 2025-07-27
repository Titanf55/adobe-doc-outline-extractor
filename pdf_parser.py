import pdfplumber
import json
import os
from collections import defaultdict
from itertools import groupby

def detect_bold_italic(lines):
    for line in lines:
        text = line["text"].strip()
        is_all_caps = text.isupper()
        is_large_font = line.get("avg_font_size", 0) >= 13
        is_short_text = len(text) <= 40
        line["is_bold"] = is_all_caps or is_large_font or is_short_text
    return lines

def group_chars_to_lines(char_list, y_tolerance=3):
    char_list = sorted(char_list, key=lambda c: (-c['top'], c['x0']))
    lines = []
    for _, line_chars in groupby(char_list, key=lambda c: round(c['top'] / y_tolerance)):
        line_chars = list(line_chars)
        line_chars = sorted(line_chars, key=lambda c: c['x0'])
        text = "".join(c['text'] for c in line_chars).strip()
        font_sizes = [float(c.get("size", 0)) for c in line_chars]
        avg_font_size = sum(font_sizes) / len(font_sizes) if font_sizes else 0
        x0 = min(c['x0'] for c in line_chars)
        top = min(c['top'] for c in line_chars)
        x1 = max(c['x1'] for c in line_chars)
        bottom = max(c['bottom'] for c in line_chars)
        lines.append({
            "text": text,
            "avg_font_size": avg_font_size,
            "coordinates": (x0, top, x1, bottom)
        })
    return lines

def classify_heading(line, largest_font):
    size = line["avg_font_size"]
    if size == largest_font:
        return "title"
    elif size >= 18:
        return "H1"
    elif size >= 14:
        return "H2"
    elif size >= 12:
        return "H3"
    else:
        return None

def process_pdf(input_pdf, output_json):
    all_lines = []
    with pdfplumber.open(input_pdf) as pdf:
        for page_num, page in enumerate(pdf.pages, start=1):
            chars = page.chars
            for char in chars:
                char["page_num"] = page_num
            grouped = group_chars_to_lines(chars)
            for line in grouped:
                line["page_num"] = page_num
                all_lines.append(line)

    all_lines = detect_bold_italic(all_lines)

    for line in all_lines:
        line["type"] = "heading" if line['avg_font_size'] >= 14 else "body"

    largest_font = max(line["avg_font_size"] for line in all_lines)
    title = ""
    outline = []
    for line in all_lines:
        level = classify_heading(line, largest_font)
        if level == "title" and not title:
            title = line["text"]
        elif level:
            outline.append({
                "level": level,
                "text": line["text"],
                "page": line["page_num"]
            })

    document_structure = {
        "title": title,
        "outline": outline
    }

    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(document_structure, f, indent=2, ensure_ascii=False)

    print(f"✅ Saved: {output_json}")

def main():
    input_folder = "input"       # renamed from "pdfs"
    output_folder = "output"     # renamed from "outputs"
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".pdf"):
            input_pdf = os.path.join(input_folder, filename)
            output_json = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.json")
            print(f"📄 Processing: {filename}")
            process_pdf(input_pdf, output_json)

if __name__ == "__main__":
    main()
