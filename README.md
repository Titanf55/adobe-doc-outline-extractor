# adobe-doc-outline-extractor

**Adobe Document Intelligence Hackathon — Track 1A**  
🎯 *Understand Your Document — PDF Outline Extractor (Offline)*

---

## 🔍 Objective

Build a fully offline PDF outline extractor that:

- Accepts a single PDF (≤ 50 pages)  
- Extracts the document title and a structured outline of headings  
- Classifies heading levels (`H1`, `H2`, `H3`) based on font size heuristics  
- Outputs a JSON in the following format:

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "Background", "page": 1 }
    
  ]
}
```

---

## 🛠️ Tech Stack

- Python 3.10  
- pdfplumber  
- Docker

- Used Google Colab for shared development  
- Final solution packaged in Docker for submission   

---

## 🚀 How It Works

- Uses `pdfplumber` to parse PDFs  
- Extracts character-level metadata (text, font size, position)  
- Groups characters into lines  
- Calculates average font size per line  
- Applies heuristics:
  - Largest font = Title  
  - Font size thresholds determine `H1`, `H2`, `H3`  
  - Boldness approximated via all-caps or short uppercase lines  
- Produces JSON with heading hierarchy and page number

---

## 📁 Folder Structure

```
📁 adobe-doc-outline-extractor/
│
├── Dockerfile
├── requirements.txt
├── pdf_parser.py
├── input/
├── output/
└── README.md
```

---

## ⚙️ Requirements

- Python 3.10+  
- `pdfplumber==0.10.2`

Install locally (optional):

```bash
pip install -r requirements.txt
```

---

## 🐳 Docker Instructions (Offline Mode)

**Build the Docker image:**

```bash
docker build --platform linux/amd64 -t mysolution:debug .
```

**Run the container:**

```For Windows (CMD):
docker run -v %cd%\input:/app/input -v %cd%\output:/app/output mysolution:debug

```

> 📌 The script processes all PDFs in `input/` and writes corresponding outline JSONs to `output/`.

---

## 🌐 Multilingual Support
Our solution supports Unicode-based, text-layered PDFs.

- ✅ English
- ✅ Chinese (Simplified & Traditional)

```
⚠️ Note: Only English and Chinese-language PDFs were tested. Other languages may not produce reliable results, especially if their text structure or encoding varies.
```

The model works independently of word meaning, focusing on font size and layout — making it robust across well-formatted, searchable PDFs.

### 📄 Chinese PDF Sample Output

Input PDF: `與文學場域的建構.pdf`  
Extracted JSON:

```json
{
  "title": "與文學場域的建構",
  "outline": [
    { "level": "H1", "text": "一　前言", "page": 1 },
    { "level": "H2", "text": "二　文學資源的選擇", "page": 2 }
  ]
}
```

## ⏱️ Performance

- Executes in **under 10 seconds** (tested on sample PDFs)  
- Fully offline — no internet or API dependency  

---

## 👥 Team & Collaboration

**Team Members:**

- Abhilasha Rajora  
- Drishti Chaudhary  
- Kashish Rajput  

## ⚠️ Limitations

- ❌ Does not support image-based (scanned) PDFs

- 🔤 Heading detection is based purely on font size and formatting, not semantic content

- 🧾 Output assumes clean document structure — noisy PDFs may require post-cleaning

- 🛠 No OCR layer yet (could be future work)

---

## 🚧 Future Improvements

- Add OCR (e.g., Tesseract) for scanned PDFs

- GUI tool using Streamlit or Flask

- Export output as HTML visual outline

- Allow user-defined heading thresholds

---

## ✅ Evaluation Criteria Coverage

| Criteria                         | Covered? | Notes                                                                 |
|----------------------------------|----------|-----------------------------------------------------------------------|
| Fully Offline                    | ✅        | Uses local PDF parsing only — no cloud or APIs                        |
| PDF up to 50 pages               | ✅        | Tested with documents of various lengths                              |
| JSON output as specified         | ✅        | Matches required schema with title, headings, and page numbers        |
| Dockerized                       | ✅        | Includes Dockerfile — containerized for portability and testing       |
| Runtime ≤ 10 seconds             | ✅        | Optimized logic for fast execution                                    |
| No Internet / No Hardcoding      | ✅        | All paths and files handled dynamically                               |
| **Multilingual Support**         | ✅        | Handles English and Chinese (Unicode-based PDFs only)                 |
| **Limitations Clearly Declared** | ✅        | Outlines unsupported cases like image-based PDFs (no OCR yet)         |
