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
adobe/
├── pdfs/                   # Input PDFs
│   └── file01.pdf
├── outputs/                # Output JSONs
│   └── outline_output.json
├── final_main_FIXED.py     # Main script
├── Dockerfile              # Docker config
├── requirements.txt        # Dependencies
└── README.md               # This file
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
docker build -t pdf-outline .
```

**Run the container:**

```bash
docker run --rm -v "$PWD/pdfs:/app/pdfs" -v "$PWD/outputs:/app/outputs" pdf-outline
```

> 📌 The script processes all PDFs in `pdfs/` and writes corresponding outline JSONs to `outputs/`.

---

## ⏱️ Performance

- Executes in **under 10 seconds** (tested on sample PDFs)  
- Fully offline — no internet or API dependency  

---

## 👥 Team & Collaboration

**Team Members:**

- Abhilasha Rajora  
- Drishti Chaudhary  
- Kashish Rajput  





---

## ✅ Evaluation Criteria Coverage

| Criteria                    | Covered? | Notes                           |
|-----------------------------|----------|----------------------------------|
| Fully Offline               | ✅        | Uses local parsing only          |
| PDF up to 50 pages          | ✅        | Tested                           |
| JSON output as specified    | ✅        | Matches schema                   |
| Dockerized                  | ✅        | Dockerfile included              |
| Runtime ≤ 10 seconds        | ✅        | Lightweight parsing              |
| No Internet / No Hardcoding | ✅        | All paths dynamic                |
