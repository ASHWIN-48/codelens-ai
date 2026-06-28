import { useState } from "react";
import axios from "axios";

const API = "http://localhost:3000";

export default function App() {
  const [repoUrl, setRepoUrl] = useState("");
  const [ingesting, setIngesting] = useState(false);
  const [ingested, setIngested] = useState(false);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [asking, setAsking] = useState(false);
  const [filePath, setFilePath] = useState("");
  const [docs, setDocs] = useState("");
  const [docsLoading, setDocsLoading] = useState(false);
  const [tab, setTab] = useState("ask");
  const [error, setError] = useState("");

  async function handleIngest() {
    if (!repoUrl) return;
    setIngesting(true);
    setError("");
    try {
      await axios.post(`${API}/api/ingest`, { repo_url: repoUrl });
      setIngested(true);
    } catch (e) {
      setError("Ingestion failed. Check the repo URL.");
    } finally {
      setIngesting(false);
    }
  }

  async function handleAsk() {
    if (!question) return;
    setAsking(true);
    setAnswer("");
    setError("");
    try {
      const res = await axios.post(`${API}/api/ask`, { question });
      setAnswer(res.data.answer);
    } catch (e) {
      setError("Failed to get answer.");
    } finally {
      setAsking(false);
    }
  }

  async function handleDocs() {
    if (!filePath) return;
    setDocsLoading(true);
    setDocs("");
    setError("");
    try {
      const res = await axios.post(`${API}/api/docs`, { file_path: filePath });
      setDocs(res.data.documentation);
    } catch (e) {
      setError("Failed to generate docs.");
    } finally {
      setDocsLoading(false);
    }
  }

  return (
    <div style={styles.container}>
      <div style={styles.header}>
        <h1 style={styles.title}>CodeLens</h1>
        <p style={styles.subtitle}>AI-powered code intelligence</p>
      </div>

      <div style={styles.ingestBox}>
        <input
          style={styles.input}
          placeholder="GitHub repo URL (e.g. https://github.com/user/repo)"
          value={repoUrl}
          onChange={e => setRepoUrl(e.target.value)}
        />
        <button
          style={ingested ? styles.btnSuccess : styles.btn}
          onClick={handleIngest}
          disabled={ingesting}
        >
          {ingesting ? "Ingesting..." : ingested ? "✓ Ingested" : "Ingest Repo"}
        </button>
      </div>

      {error && <p style={styles.error}>{error}</p>}

      <div style={styles.tabs}>
        <button
          style={tab === "ask" ? styles.tabActive : styles.tabInactive}
          onClick={() => setTab("ask")}
        >
          Ask
        </button>
        <button
          style={tab === "docs" ? styles.tabActive : styles.tabInactive}
          onClick={() => setTab("docs")}
        >
          Generate Docs
        </button>
      </div>

      {tab === "ask" && (
        <div style={styles.panel}>
          <div style={styles.inputRow}>
            <input
              style={styles.input}
              placeholder="Ask anything about the codebase..."
              value={question}
              onChange={e => setQuestion(e.target.value)}
              onKeyDown={e => e.key === "Enter" && handleAsk()}
            />
            <button style={styles.btn} onClick={handleAsk} disabled={asking}>
              {asking ? "Thinking..." : "Ask"}
            </button>
          </div>
          {answer && (
            <div style={styles.answerBox}>
              <p style={styles.answerText}>{answer}</p>
            </div>
          )}
        </div>
      )}

      {tab === "docs" && (
        <div style={styles.panel}>
          <div style={styles.inputRow}>
            <input
              style={styles.input}
              placeholder="File path (e.g. src/flask/app.py)"
              value={filePath}
              onChange={e => setFilePath(e.target.value)}
            />
            <button style={styles.btn} onClick={handleDocs} disabled={docsLoading}>
              {docsLoading ? "Generating..." : "Generate"}
            </button>
          </div>
          {docs && (
            <div style={styles.answerBox}>
              <pre style={styles.docsText}>{docs}</pre>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

const styles = {
  container: {
    minHeight: "100vh",
    background: "#0a0a0f",
    color: "#e2e2f0",
    fontFamily: "'Inter', sans-serif",
    padding: "40px 24px",
    maxWidth: "800px",
    margin: "0 auto",
  },
  header: {
    textAlign: "center",
    marginBottom: "40px",
  },
  title: {
    fontSize: "48px",
    fontWeight: "800",
    background: "linear-gradient(135deg, #a855f7, #3b82f6)",
    WebkitBackgroundClip: "text",
    WebkitTextFillColor: "transparent",
    margin: "0 0 8px 0",
  },
  subtitle: {
    color: "#6b6b8a",
    fontSize: "16px",
    margin: 0,
  },
  ingestBox: {
    display: "flex",
    gap: "12px",
    marginBottom: "16px",
  },
  inputRow: {
    display: "flex",
    gap: "12px",
    marginBottom: "16px",
  },
  input: {
    flex: 1,
    background: "#111118",
    border: "1px solid #1e1e2e",
    borderRadius: "8px",
    padding: "12px 16px",
    color: "#e2e2f0",
    fontSize: "14px",
    outline: "none",
  },
  btn: {
    background: "#a855f7",
    color: "#fff",
    border: "none",
    borderRadius: "8px",
    padding: "12px 20px",
    fontSize: "14px",
    fontWeight: "600",
    cursor: "pointer",
    whiteSpace: "nowrap",
  },
  btnSuccess: {
    background: "#22c55e",
    color: "#fff",
    border: "none",
    borderRadius: "8px",
    padding: "12px 20px",
    fontSize: "14px",
    fontWeight: "600",
    cursor: "pointer",
    whiteSpace: "nowrap",
  },
  tabs: {
    display: "flex",
    gap: "8px",
    marginBottom: "24px",
  },
  tabActive: {
    background: "#1e1e2e",
    color: "#a855f7",
    border: "1px solid #a855f7",
    borderRadius: "8px",
    padding: "8px 20px",
    fontSize: "14px",
    fontWeight: "600",
    cursor: "pointer",
  },
  tabInactive: {
    background: "transparent",
    color: "#6b6b8a",
    border: "1px solid #1e1e2e",
    borderRadius: "8px",
    padding: "8px 20px",
    fontSize: "14px",
    cursor: "pointer",
  },
  panel: {
    background: "#111118",
    border: "1px solid #1e1e2e",
    borderRadius: "12px",
    padding: "24px",
  },
  answerBox: {
    background: "#0a0a0f",
    border: "1px solid #1e1e2e",
    borderRadius: "8px",
    padding: "16px",
    marginTop: "8px",
  },
  answerText: {
    color: "#b0b0cc",
    fontSize: "14px",
    lineHeight: "1.7",
    margin: 0,
    whiteSpace: "pre-wrap",
  },
  docsText: {
    color: "#b0b0cc",
    fontSize: "13px",
    lineHeight: "1.7",
    margin: 0,
    whiteSpace: "pre-wrap",
    fontFamily: "monospace",
  },
  error: {
    color: "#f87171",
    fontSize: "14px",
    marginBottom: "16px",
  },
};