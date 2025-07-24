# adobe-doc-outline-extractor
Adobe Document Intelligence Hackathon — Track 1A
🎯 Understand Your Document — PDF Outline Extractor (Offline)

🔍 Objective
Build a fully offline PDF outline extractor that:

Accepts a single PDF (≤ 50 pages)

Extracts the document title and a structured outline of headings

Classifies heading levels (H1, H2, H3) based on font size heuristics

Outputs a JSON in the following format:

Example:

json
Copy
Edit
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "Background", "page": 1 },
    ...
  ]
}
🛠️ Tech Stack
Python 3.10

pdfplumber

Docker

🚀 How It Works
Uses pdfplumber to parse each PDF

Extracts character-level metadata (text, font size, position)

Groups characters into lines

Calculates average font size per line

Applies heuristics:

Largest font = Title

Font size thresholds determine H1, H2, H3

Boldness is approximated using all-caps or short uppercase lines

Produces clean JSON output with heading hierarchy and page number

📁 Folder Structure
bash
Copy
Edit
adobe/
│
├── pdfs/                   # Input PDFs (you can add more here)
│   └── file01.pdf
│
├── outputs/                # Output folder for generated JSONs
│   └── outline_output.json
│
├── final_main_FIXED.py     # Main script
├── Dockerfile              # Docker config
├── requirements.txt        # pip dependencies
└── README.md               # This file
⚙️ Requirements
Python 3.10+

pdfplumber==0.10.2

Install dependencies locally (optional):

bash
Copy
Edit
pip install -r requirements.txt
🐳 Docker Instructions (Offline Mode)
Build Docker image:

bash
Copy
Edit
docker build -t pdf-outline .
Run the container:

bash
Copy
Edit
docker run --rm -v "$PWD/pdfs:/app/pdfs" -v "$PWD/outputs:/app/outputs" pdf-outline
📌 Note: The script will process all PDFs in pdfs/ and write a corresponding outline JSON to outputs/.

⏱️ Performance
Execution completes in under 10 seconds (tested on sample inputs)

Fully offline: No internet access or external API required

👥 Team & Collaboration
Team Members: Add your teammates' names here

Google Colab used during development for shared iteration

Final code is self-contained in Docker for submission

✅ Evaluation Criteria Coverage
Criteria	Covered?	
Notes Fully Offline	
✅	Uses local parsing only
PDF up to 50 pages	✅	Tested
JSON output as specified	✅	Matches schema
Dockerized	✅	Dockerfile included
Runtime ≤ 10 seconds	✅	Lightweight parsing
No Internet / No Hardcoding	✅	All paths dynamic
