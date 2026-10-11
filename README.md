# ⚡ AI Vibe-Coding Prompt Optimizer (Stateful Engine)

Built by a 1st-year engineering student for the **Grevix AfterCode** hackathon (October 2026).

## 🚨 The Core Problem
With the massive rise of Generative AI tools like ChatGPT and Cursor, many beginner developers try to write application code using standard conversational English. However, regular prompts lack strict engineering constraints, leading to broken execution blocks, unexpected bugs, or total architectural degradation during longer development chats.

## 💡 The Solution
This web application acts as a defensive guardrail layer between the engineer and code generation tools. It translates simple "vibe-coding" ideas into enterprise-grade system prompts featuring explicit error handling, clean structures, and strict modular patterns.

### ✨ Unique Engineering Implementations (Phase 2 Upgrade)
- **Stateful Architectural Graph:** Maintains persistent infrastructure states (`Stateless system execution`) in local session memory, preventing context drift across multi-turn iterations.
- **Conflict-Detection Gate:** Actively inspects incoming text requirements against saved graph dependencies to catch design violations early.
- **Differential Specification Patches:** Generates clean, isolated non-destructive markup updates rather than breaking baseline configurations or executing expensive full-system context rewrites.

## 🛠️ Step-by-Step Setup
Ensure you have Python 3.12+ and Streamlit installed on your machine.

1. Install the required module dependencies:
```bash
pip install streamlit
```

2. Run the application instance locally:
```bash
streamlit run app.py
```
