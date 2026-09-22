# Multi-Agent AI Chatbot for Document & PPT Generation


An enterprise-style multi-agent AI assistant that can understand uploaded documents and presentations, answer questions using RAG, perform web research, generate DOCX/PPTX files, and edit PowerPoint presentations conversationally.


## Features


- 📄 Upload PDF, DOCX, PPTX and image files
- 🔍 Document and presentation parsing
- 🧠 Multi-agent task routing
- 📚 Retrieval-Augmented Generation (RAG)
- 🗃️ Pinecone vector database
- 🔎 Semantic search using HuggingFace embeddings
- 🌐 Real-time web research
- 📊 PowerPoint analysis
- ✏️ Conversational PowerPoint editing
- 🔄 Version management for edited presentations
- 📝 DOCX generation
- 📽️ PPTX generation
- ⬇️ Generated file downloads
- 💬 React-based conversational interface
- 🔗 Source traceability for RAG responses


## Architecture


```text
                    ┌──────────────────────┐
                    │     React Frontend   │
                    │      Chat Interface  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      FastAPI API     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Supervisor Agent   │
                    └──────────┬───────────┘
                               │
             ┌─────────────────┼─────────────────┐
             ▼                 ▼                 ▼
      ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
      │ RAG Agent   │   │ Research    │   │ Editing     │
      │             │   │ Agent       │   │ Agent       │
      └──────┬──────┘   └─────────────┘   └──────┬──────┘
             │                                    │
             ▼                                    ▼
      ┌─────────────┐                       ┌─────────────┐
      │  Pinecone   │                       │  python-pptx│
      │ Vector DB   │                       └──────┬──────┘
      └─────────────┘                              │
                                                  ▼
                                           Version Manager


             ┌─────────────────────────────────────┐
             │        Generation Agent              │
             │      DOCX / PPTX Generation         │
             └─────────────────────────────────────┘

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   # Multi-Agent AI Chatbot for Document & PPT Generation  An enterprise-style multi-agent AI assistant that can understand uploaded documents and presentations, answer questions using RAG, perform web research, generate DOCX/PPTX files, and edit PowerPoint presentations conversationally.  ## Features  - 📄 Upload PDF, DOCX, PPTX and image files  - 🔍 Document and presentation parsing  - 🧠 Multi-agent task routing  - 📚 Retrieval-Augmented Generation (RAG)  - 🗃️ Pinecone vector database  - 🔎 Semantic search using HuggingFace embeddings  - 🌐 Real-time web research  - 📊 PowerPoint analysis  - ✏️ Conversational PowerPoint editing  - 🔄 Version management for edited presentations  - 📝 DOCX generation  - 📽️ PPTX generation  - ⬇️ Generated file downloads  - 💬 React-based conversational interface  - 🔗 Source traceability for RAG responses  ## Architecture  ```text                      ┌──────────────────────┐                      │     React Frontend   │                      │      Chat Interface  │                      └──────────┬───────────┘                                 │                                 ▼                      ┌──────────────────────┐                      │      FastAPI API     │                      └──────────┬───────────┘                                 │                                 ▼                      ┌──────────────────────┐                      │   Supervisor Agent   │                      └──────────┬───────────┘                                 │               ┌─────────────────┼─────────────────┐               ▼                 ▼                 ▼        ┌─────────────┐   ┌─────────────┐   ┌─────────────┐        │ RAG Agent   │   │ Research    │   │ Editing     │        │             │   │ Agent       │   │ Agent       │        └──────┬──────┘   └─────────────┘   └──────┬──────┘               │                                    │               ▼                                    ▼        ┌─────────────┐                       ┌─────────────┐        │  Pinecone   │                       │  python-pptx│        │ Vector DB   │                       └──────┬──────┘        └─────────────┘                              │                                                    ▼                                             Version Manager               ┌─────────────────────────────────────┐               │        Generation Agent              │               │      DOCX / PPTX Generation         │               └─────────────────────────────────────┘   `

Agent Responsibilities
----------------------

### Supervisor Agent

Determines which agent or combination of agents should handle the user's request.

### Document Agent

Analyzes uploaded PDF and DOCX documents.

### PPT Agent

Analyzes PowerPoint structure, layout, style and presentation content.

### RAG Agent

Retrieves relevant chunks from the uploaded document using semantic search and generates an answer using the retrieved context.

### Research Agent

Performs web research and returns structured research results with sources.

### Editing Agent

Understands conversational editing requests and modifies existing PowerPoint presentations.

### Generation Agent

Generates editable DOCX and PPTX files from research results.

### Version Manager

Maintains versions of edited presentations and tracks the current file.

RAG Pipeline
---------------------
Uploaded Document
       ↓
Document Parser
       ↓
Text Normalization
       ↓
Recursive Chunking
       ↓
HuggingFace Embeddings
       ↓
Pinecone Vector Database
       ↓
Similarity Search
       ↓
Relevant Context
       ↓
NVIDIA Nemotron LLM
       ↓
Answer + Sources


Technology Stack
----------------

### Backend

*   Python
    
*   FastAPI
    
*   LangChain
    
*   Pydantic
    
*   python-pptx
    
*   python-docx
    

### AI / ML

*   NVIDIA Nemotron
    
*   HuggingFace Sentence Transformers
    
*   Retrieval-Augmented Generation
    
*   LangChain structured output
    

### Vector Database

*   Pinecone
    

### Research

*   LangSearch Web Search API
    

### Frontend

*   React
    
*   Vite
    
*   JavaScript
    
*   CSS
    

### Deployment / Development

*   Git
    
*   GitHub
    
*   Docker-ready backend
    

Project Structure
-----------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Nextastra/  │  ├── backend/  │   ├── agents/  │   ├── generators/  │   ├── parsers/  │   ├── research/  │   ├── rag/  │   ├── uploads/  │   ├── outputs/  │   ├── main.py  │   └── requirements.txt  │  ├── frontend/  │   ├── src/  │   ├── package.json  │   └── ...  │  ├── README.md  └── .gitignore   `

Setup
-----

### Backend

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   cd backend  python -m venv venv  # Windows  venv\Scripts\activate  pip install -r requirements.txt   `

Create a .env file:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   NVIDIA_API_KEY=your_nvidia_api_key  PINECONE_API_KEY=your_pinecone_api_key  LANGSEARCH_API_KEY=your_langsearch_api_key   `

Start the backend:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python -m uvicorn main:app --reload   `

Backend:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   http://127.0.0.1:8000   `

Frontend
--------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   cd frontend  npm install  npm run dev   `

Frontend:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   http://localhost:5173   `

Example Workflow
----------------

### 1\. Upload a presentation

Upload a .pptx file through the React interface.

The backend automatically parses and indexes the document.

### 2\. Ask a question

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   What are the cybersecurity challenges?   `

The Supervisor routes the request to the RAG Agent.

The system retrieves relevant document chunks from Pinecone and generates an answer with source information.

### 3\. Edit the presentation

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Add 2 slides about blockchain applications in cybersecurity.   `

The Supervisor routes the request to the Editing Agent.

The presentation is modified and a new version is created.

### 4\. Continue editing

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   Add one more slide about the challenges.   `

The system uses the current presentation version and creates another version.

### 5\. Download

The generated presentation can be downloaded directly from the chatbot interface.

Example Multi-Agent Routing
---------------------------

User RequestAgentSummarize this PPTRAG AgentWhat are the cybersecurity challenges?RAG AgentAnalyze the presentation layoutPPT AgentAnalyze this PDFDocument AgentResearch the latest AI trendsResearch AgentCreate a PPT about AI trendsResearch + GenerationAdd two slidesEditing Agent

Version Management
------------------

Edited presentations are stored as separate versions.

Example:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   outputs/  ├── edited_presentation_v1.pptx  ├── edited_presentation_v2.pptx  └── versions.json   `

The version manager tracks:

*   Version number
    
*   File path
    
*   Current presentation
    

API Endpoints
-------------

### Upload

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   POST /upload   `

Uploads and automatically indexes supported documents.

### Query

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   POST /query   `

Queries an indexed document using RAG.

### Process

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   POST /process   `

Routes a user request through the multi-agent system.

### Download

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   GET /download/{filename}   `

Downloads generated DOCX/PPTX files.

### Parse

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   GET /parse/{filename}   `

Parses an uploaded document.

Security
--------

API keys are stored in environment variables and should never be committed to GitHub.

The .env file is excluded through .gitignore.

Future Improvements
-------------------

*   DOCX ↔ PPTX conversion
    
*   More advanced template/style preservation
    
*   Improved slide-level citations
    
*   OCR improvements for scanned documents
    
*   Authentication and authorization
    
*   Cloud deployment
    
*   Persistent conversation storage
    
*   More advanced document versioning
    

Author
------

Pranav Sanjay Landge
