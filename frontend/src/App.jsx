import { useState } from "react";
import "./App.css";
import ReactMarkdown from "react-markdown";

const API_BASE = "http://127.0.0.1:8000";

function App() {
  const [file, setFile] = useState(null);
  const [request, setRequest] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const uploadFile = async () => {
    if (!file) return null;

    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch(`${API_BASE}/upload`, {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      throw new Error("File upload failed");
    }

    return await response.json();
  };

  const sendMessage = async () => {
    if (!request.trim()) return;

    const currentRequest = request;

    setLoading(true);

    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: currentRequest,
      },
    ]);

    try {
      let filename = null;

      if (file) {
        const uploadResult = await uploadFile();
        filename = uploadResult.filename;
      }

      const params = new URLSearchParams();
      params.append("request", currentRequest);

      if (filename) {
        params.append("filename", filename);
      }

      const response = await fetch(
        `${API_BASE}/process?${params.toString()}`,
        {
          method: "POST",
        }
      );

      if (!response.ok) {
        throw new Error("Request failed");
      }

      const result = await response.json();

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: result,
        },
      ]);

      setRequest("");
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: {
            error: error.message,
          },
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const renderAssistantMessage = (content) => {
    // Error
    if (content?.error) {
      return <p className="error-text">{content.error}</p>;
    }

    // RAG response
    const rag = content?.results?.rag_agent;

    if (rag) {
      return (
        <div className="ai-response">
          <div className="answer">
            <ReactMarkdown>
              {rag.answer}
           </ReactMarkdown>
</div>

          {rag.sources && rag.sources.length > 0 && (
            <div className="sources">
              <h4>Sources</h4>

              {rag.sources.map((source, index) => (
                <div className="source-item" key={index}>
  <span>📄 {source.document_id}</span>
  <span>Chunk {source.chunk_index}</span>
  <span>
    Relevance: {source.score.toFixed(3)}
  </span>
</div>
              ))}
            </div>
          )}
        </div>
      );
    }

    // Generation response
    const generation =
  content?.results?.generation_agent;

if (generation) {
  const filename = generation.output_file
    ? generation.output_file.split(/[\\/]/).pop()
    : null;

  return (
    <div className="ai-response">
      <p>{generation.status}</p>

      {filename && (
        <a
          className="download-button"
          href={`${API_BASE}/download/${encodeURIComponent(filename)}`}
          target="_blank"
          rel="noopener noreferrer"
        >
          ⬇️ Download File
        </a>
      )}
    </div>
  );
}
    // Editing response
    const editing =
  content?.results?.editing_agent;

if (editing) {
  const filename = editing.output_file
    ? editing.output_file.split(/[\\/]/).pop()
    : null;

  return (
    <div className="ai-response">
      <p>{editing.status}</p>

      {filename && (
        <a
          className="download-button"
          href={`${API_BASE}/download/${encodeURIComponent(filename)}`}
          target="_blank"
          rel="noopener noreferrer"
        >
          ⬇️ Download PPTX
        </a>
      )}
    </div>
  );
}

    // Research response
    const research =
      content?.results?.research_agent;

    if (research) {
      return (
        <div className="ai-response">
          <h3>{research.topic}</h3>

          <p>{research.summary}</p>

          {research.key_findings?.length > 0 && (
            <div>
              <h4>Key Findings</h4>

              <ul>
                {research.key_findings.map(
                  (finding, index) => (
                    <li key={index}>{finding}</li>
                  )
                )}
              </ul>
            </div>
          )}

          {research.sources?.length > 0 && (
            <div className="sources">
              <h4>Sources</h4>

              {research.sources.map(
                (source, index) => (
                  <div
                    className="source-item"
                    key={index}
                  >
                    <span>🔗 {source.title}</span>
                    <span>{source.url}</span>
                  </div>
                )
              )}
            </div>
          )}
        </div>
      );
    }

    // Fallback
    return (
      <pre>
        {JSON.stringify(content, null, 2)}
      </pre>
    );
  };

  return (
    <div className="app">
      <header className="header">
        <div>
          <h1>Multi-Agent AI Assistant</h1>
          <p>
            Documents • Research • RAG • PPT Generation
          </p>
        </div>
      </header>

      <main className="chat-container">
        <div className="messages">

          {messages.length === 0 && (
            <div className="welcome">
              <h2>How can I help?</h2>

              <p>
                Upload a document and ask me to analyze,
                research, generate, or edit it.
              </p>
            </div>
          )}

          {messages.map((message, index) => (
            <div
              key={index}
              className={`message ${message.role}`}
            >
              <div className="message-label">
                {message.role === "user"
                  ? "You"
                  : "AI"}
              </div>

              {message.role === "user" ? (
                <p>{message.content}</p>
              ) : (
                renderAssistantMessage(
                  message.content
                )
              )}
            </div>
          ))}

          {loading && (
            <div className="message assistant">
              <div className="message-label">
                AI
              </div>

              <p>Processing your request...</p>
            </div>
          )}
        </div>

        <div className="input-area">

          {file && (
            <div className="selected-file">
              📎 {file.name}

              <button
                onClick={() => setFile(null)}
              >
                ×
              </button>
            </div>
          )}

          <div className="input-row">

            <label className="upload-button">
              📎

              <input
                type="file"
                accept=".pdf,.docx,.ppt,.pptx,.png,.jpg,.jpeg"
                onChange={(e) =>
                  setFile(e.target.files[0])
                }
              />
            </label>

            <input
              type="text"
              placeholder="Ask something..."
              value={request}
              onChange={(e) =>
                setRequest(e.target.value)
              }
              onKeyDown={(e) => {
                if (e.key === "Enter") {
                  sendMessage();
                }
              }}
            />

            <button
              className="send-button"
              onClick={sendMessage}
              disabled={
                loading || !request.trim()
              }
            >
              {loading ? "..." : "Send"}
            </button>

          </div>
        </div>
      </main>
    </div>
  );
}

export default App;