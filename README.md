# PDF Outline Extractor 🧠📄

This project is part of Adobe India Hackathon 2025 - Round 1A: "Connecting the Dots".  
It extracts structured outlines (Title, H1, H2, H3) with page numbers from any PDF file and outputs it in a clean, valid JSON format.

## 🛠 Features

- Detects and classifies headings (Title, H1, H2, H3)
- Associates page numbers with each heading
- Outputs structured JSON
- Fully Dockerized for platform independence
- Lightweight, fast, and accurate

## 🗂 Output Format (JSON)
```json
{
  "title": "Document Title",
  "headings": [
    {
      "level": "H1",
      "text": "Section Heading",
      "page_number": 2
    },
    {
      "level": "H2",
      "text": "Subsection Heading",
      "page_number": 3
    }
  ]
}
```

## 📁 Folder Structure

```
pdf_outline_extractor/
├── input/                  # Place input PDF files here
├── output/                 # Extracted JSON files are saved here
├── extractor.py            # Main script to extract outlines
├── Dockerfile              # Docker container definition
├── requirements.txt        # Python dependencies
└── README.md               # Project overview (this file)
```

## 🚀 Usage (via Docker)

### Step 1: Build the Docker Image
```bash
docker build -t pdfoutliner:latest .
```

### Step 2: Run the Docker Container
```bash
docker run --rm -v "%cd%/input:/app/input" -v "%cd%/output:/app/output" pdfoutliner:latest
```

- Replace `%cd%` with your actual path on Windows CMD or use `$PWD` on Unix systems.

## 👨‍💻 Author

Viswajith Gupta ([@Viswajith2005](https://github.com/Viswajith2005))

## 📜 License

This project is for Adobe Hackathon submission use only.
