import streamlit as st

st.set_page_config(page_title="Stateful Prompt Optimizer", page_icon="⚡", layout="wide")

st.title("⚡ AI Vibe-Coding Prompt Optimizer (Stateful Engine)")
st.caption("Grevix AfterCode Phase 2 | Challenge Card 1: Stateful Constraint Graph & Conflict Gate")

# Initialize Stateful Constraint Graph in session memory
if "constraint_graph" not in st.session_state:
    st.session_state.constraint_graph = {
        "architecture": "Stateless system execution",
        "security": "Follow standard security guidelines",
        "error_handling": "Implement explicit exception handling blocks"
    }
if "history" not in st.session_state:
    st.session_state.history = []

# Sidebar displaying active baseline constraints (The Stateful Graph view)
with st.sidebar:
    st.header("🕸️ Active Architectural Graph")
    st.write("These are your baseline constraints saved in memory:")
    for key, val in st.session_state.constraint_graph.items():
        st.markdown(f"**• {key.replace('_', ' ').title()}:** `{val}`")
    
    if st.button("Reset Session Memory", type="secondary"):
        st.session_state.constraint_graph = {
            "architecture": "Stateless system execution",
            "security": "Follow standard security guidelines",
            "error_handling": "Implement explicit exception handling blocks"
        }
        st.session_state.history = []
        st.rerun()

# Layout splits: Input forms on left, results on right
col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Multi-Turn Feature Request Input")
    new_request = st.text_area("Enter your new system requirement / iteration step:", placeholder="e.g., Make the system maintain a persistent database connection storage cache...")
    
    # Conflict Detection Gate Logic
    conflict_detected = False
    conflict_message = ""
    
    if new_request:
        # Simple keywords gate checking for structural contradictions
        lowered_req = new_request.lower()
        if "stateful" in lowered_req or "persistent" in lowered_req or "cache" in lowered_req or "store" in lowered_req:
            if "Stateless" in st.session_state.constraint_graph["architecture"]:
                conflict_detected = True
                conflict_message = """❌ **Conflict Detected at Architectural Gate!**
                \n**New Feature:** Requesting persistent/stateful storage.
                \n**Existing Constraint:** `architecture: Stateless system execution`.
                \n*re-synthesizing the complete context from scratch is locked to preserve baseline code.*"""

    if st.button("Process Iteration Step", type="primary"):
        if new_request.strip():
            if conflict_detected:
                st.error(conflict_message)
                # Generate Non-Destructive Differential specification patch
                st.info("🛠️ **Generating Non-Destructive Differential Patch...**")
                patch = f"""
```markdown
### DIFFERENTIAL SPECIFICATION PATCH (NON-DESTRUCTIVE)
[UNCHANGED] security -> Follow standard security guidelines
[UNCHANGED] error_handling -> Implement explicit exception handling blocks
[MODIFIED PATCH] architecture -> Upgraded from [Stateless] to [Stateful Connection/Storage Cache] to accommodate new feature constraint.
```
"""
                st.session_state.history.append({"request": new_request, "type": "Conflict & Patch Applied", "patch": patch})
                # Update the graph dynamically without crashing the system
                st.session_state.constraint_graph["architecture"] = "Stateful Connection/Storage Cache (Patched)"
            else:
                st.success("✅ Requirement added smoothly with zero added latency.")
                st.session_state.history.append({"request": new_request, "type": "Smooth Addition", "patch": "No conflicts found. Single-turn baseline synthesized cleanly."})
        else:
            st.warning("Please type a new request constraint first.")

with col2:
    st.subheader("🚀 Output Specification & Patch History")
    if not st.session_state.history:
        st.info("Your multi-turn iterative history blocks will display here once you process an entry.")
    else:
        for idx, turn in enumerate(st.session_state.history):
            with st.expander(f"Turn {idx + 1}: {turn['type']}", expanded=True):
                st.markdown(f"**User Request:** *\"{turn['request']}\"*")
                if "Conflict" in turn["type"]:
                    st.code(turn["patch"], language="markdown")
                else:
                    st.caption(turn["patch"])
