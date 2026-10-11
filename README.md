# 🕸️ AI Vibe-Coding Prompt Optimizer (Dashboard Pro)

A live, cloud-connected web application designed to act as an automated architectural governance layer for developer-AI workflows. Developed for the **Grevix AfterCode Hackathon 2026**.

## 🔗 Live Assets
- **Working Live Demo App:** https://grevixvibe-prompt-optimizergit-exnzf96agfuoaqr5xxnfdi.streamlit.app/
- **Public GitHub Repository Source:** https://github.com/navyavtu2207-ctrl/Grevix_vibe-prompt-optimizer.git
---

## 🚨 The Core Problem: "Context Destruction"
With tools like Cursor and ChatGPT, developers heavily rely on natural language ("Vibe-Coding") to spin up projects rapidly. However, during long, multi-turn AI chat loops, standard models frequently suffer from **Context Destruction**. The AI loses track of initial architecture constraints, baseline setup rules, or blindly overwrites working systems when a new requirement is introduced, causing heavy technical debt and regressions.

## 💻 The Solution
This engine acts as a defensive safety guardrail between the developer and generative code models. It enforces system integrity dynamically in local memory without adding latency to development workflows.

### ✨ Key Features Built
* **Stateful Context Memory Graph:** A tracking matrix that pins core architectural setup constraints (e.g., maintaining a strict stateless application layout) firmly across chat iteration loops.
* **Semantic Conflict-Detection Gate:** Intercepts logical contradictions (e.g., trying to write local storage arrays on a stateless backend node) with **0ms added latency**.
* **Non-Destructive Differential Patches:** Generates clean, isolated specification patch blocks and JavaScript simulation sandboxes instead of erasing full baselines.
* **Shared Feedback Feed Panel:** A cloud-connected analytics portal allowing peer testers from *any device anywhere* to stream honest reviews onto the admin dashboard feed in real-time.

---

## 🛠️ Tech Stack & AI Toolkit
- **Backend & Core Logic:** Python 3
- **Frontend Interface:** Streamlit UI Framework
- **Data Integration & Storage:** KVBin REST API Architecture Channels (Shared Live Feedback Syncing)
- **Primary IDE:** Cursor Code Editor

---

## 📈 Hackathon Build & Evolution Log

### 🟢 Initial Baseline Setup
Developed the core local stateful constraint graph engine running verification logic for inbound textual instructions against fixed system variables.

### 🟡 Challenge Card 1 Adaptation
Replaced a clunky, manual JSON upload/download state recovery system with a completely automated, error-proof **Anti-Cache Reset Guard** using the browser runtime (`st.session_state`). This eliminated file corruption risks, expanded keyword matching arrays, and cleanly retained input state memory during scenario walkthroughs.

### 🔴 Challenge Card 2 Adaptation (Real-World Peer Review Loop)
Upgraded the single-user local prototype into a **Live Shared Peer Review Dashboard**. Connected a zero-authentication cloud text channel API to the interface backend. Review submissions made by users testing the platform on completely separate computers or phone links now stream dynamically straight into the live global timeline log dashboard view.
