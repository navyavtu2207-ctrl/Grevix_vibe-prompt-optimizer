import streamlit as st

st.set_page_config(page_title="Stateful Prompt Engine Pro", page_icon="⚡", layout="wide")

st.title("⚡ AI Vibe-Coding Prompt Optimizer (Stateful Engine Pro)")
st.caption("Grevix AfterCode Phase 2 | Upgraded: Semantic Gate, Structured Nodes & Sandbox")

# FIX 3: Structured Node Schema (Tracking constraints as structured dictionary objects)
if "constraint_graph" not in st.session_state:
    st.session_state.constraint_graph = {
        "core_architecture": {"state": "Stateless", "description": "Stateless system execution channels"},
        "security_compliance": {"state": "Standard", "description": "Enforce basic application security guidelines"},
        "error_handling": {"state": "Explicit", "description": "Implement explicit try-except block structures"}
    }
if "history" not in st.session_state:
    st.session_state.history = []

# Sidebar displaying active graph states
with st.sidebar:
    st.header("🕸️ Active Architectural Graph")
    st.write("Current infrastructure nodes held in memory:")
    for key, node in st.session_state.constraint_graph.items():
        st.markdown(f"**• {key.replace('_', ' ').title()}:** `{node['state']}` ({node['description']})")
    
    st.divider()
    if st.button("Reset Session Memory Layout", type="secondary"):
        st.session_state.constraint_graph = {
            "core_architecture": {"state": "Stateless", "description": "Stateless system execution channels"},
            "security_compliance": {"state": "Standard", "description": "Enforce basic application security guidelines"},
            "error_handling": {"state": "Explicit", "description": "Implement explicit try-except block structures"}
        }
        st.session_state.history = []
        st.rerun()

# Layout splits
col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Multi-Turn Constraint Iteration")
    new_request = st.text_area(
        "Input your next feature requirement or target layout constraint:", 
        placeholder="e.g., Write user session logs directly to a local file on the hard drive..."
    )
    
    # FIX 1: Expanded Semantic Check Gate (Catches variations like 'write to disk', 'hard drive', etc.)
    conflict_detected = False
    conflict_cause = ""
    
    if new_request:
        lowered_req = new_request.lower()
        stateful_intents = ["stateful", "persistent", "cache", "store", "save file", "database", "write to disk", "log history", "local file", "hard drive"]
        
        if any(intent in lowered_req for intent in stateful_intents):
            if st.session_state.constraint_graph["core_architecture"]["state"] == "Stateless":
                conflict_detected = True
                conflict_cause = "Requested stateful/persistent layer contradicts the active 'Stateless' core node configuration."

    if st.button("Process Iteration Engine Step", type="primary"):
        if new_request.strip():
            if conflict_detected:
                st.error(f"🚨 **Architectural Conflict Blocked!**\n\n**Reason:** {conflict_cause}\n\n*Platform locked: Full re-synthesis rejected to protect baseline components.*")
                
                # Generate Non-Destructive Patch
                patch = f"""### DIFFERENTIAL SPECIFICATION PATCH (NON-DESTRUCTIVE)
[UNCHANGED] security_compliance -> Enforce basic application security guidelines
[UNCHANGED] error_handling -> Implement explicit try-except block structures
[MODIFIED NODE] core_architecture -> Upgraded from [Stateless] to [Stateful Adapter Patch Layer] to handle incoming filesystem traffic."""
                
                # FIX 2: Simulation Sandbox Blueprint (A visual mock code layout displaying execution changes)
                sandbox_blueprint = """// Simulated Storage Patch Layer
function initSessionStorage() {
    console.log("Stateful patch adapter layer executed securely.");
    // Isolated local environment file cache system activated
}"""
                st.session_state.history.append({
                    "request": new_request,
                    "status": "🚨 Patched Conflict",
                    "patch": patch,
                    "blueprint": sandbox_blueprint
                })
                # Update the node safely
                st.session_state.constraint_graph["core_architecture"] = {"state": "Stateful (Patched)", "description": "Stateful Adapter Patch Layer activated"}
            else:
                st.success("✅ Requirement verified smoothly. Integrated with zero added framework latency.")
                patch = f"### SYSTEM BASELINE UPDATE\n[SUCCESS] Node context updated with entry: \"{new_request}\""
                sandbox_blueprint = """// Default running channel 
function baselineProcess() {
    console.log("System operating on baseline stateless channel.");
}"""
                st.session_state.history.append({
                    "request": new_request,
                    "status": "✅ Clean Integration",
                    "patch": patch,
                    "blueprint": sandbox_blueprint
                })
        else:
            st.warning("Please describe your iteration input constraint row first.")

with col2:
    st.subheader("🚀 Output Sandbox & Specification History")
    if not st.session_state.history:
        st.info("Your dynamic iteration trace and blueprint engine logs will render blocks here.")
    else:
        for idx, turn in enumerate(st.session_state.history):
            with st.expander(f"Turn {idx + 1}: {turn['status']}", expanded=True):
                st.markdown(f"**Input Request:** *\"{turn['request']}\"*")
                
                st.markdown("#### 📄 Specification Sheet")
                st.code(turn["patch"], language="markdown")
                
                st.markdown("#### 💻 Live Blueprint Simulation Sandbox")
                st.code(turn["blueprint"], language="javascript")
                
                # Single-click download asset
                st.download_button(
                    label="📥 Download System Spec Patch Asset",
                    data=turn["patch"] + "\n\n" + turn["blueprint"],
                    file_name=f"grevix_spec_turn_{idx+1}.md",
                    mime="text/markdown",
                    key=f"dl_pro_{idx}"
                )
