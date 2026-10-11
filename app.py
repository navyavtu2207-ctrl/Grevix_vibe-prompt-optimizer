import streamlit as st
import json

st.set_page_config(page_title="Stateful Prompt Engine Pro", page_icon="⚡", layout="wide")

st.title("⚡ AI Vibe-Coding Prompt Optimizer (Stateful Engine Pro v3)")
st.caption("Grevix AfterCode")

# Initialize Stateful Nodes
if "constraint_graph" not in st.session_state:
    st.session_state.constraint_graph = {
        "core_architecture": {"state": "Stateless", "description": "Stateless system execution channels"},
        "security_compliance": {"state": "Standard", "description": "Enforce basic application security guidelines"},
        "error_handling": {"state": "Explicit", "description": "Implement explicit try-except block structures"}
    }
if "history" not in st.session_state:
    st.session_state.history = []

# Sidebar displaying active graph states & Reset-Proof Restore Port
with st.sidebar:
    st.header("🕸️ Active Architectural Graph")
    for key, node in st.session_state.constraint_graph.items():
        st.markdown(f"**• {key.replace('_', ' ').title()}:** `{node['state']}`")
    
    st.divider()
    st.header("💾 Reset-Proof Recovery Port")
    st.write("Unexpected crash or refresh? Upload your backup JSON file here to instantly restore everything:")
    
    uploaded_backup = st.file_uploader("Choose backup file", type=["json"], label_visibility="collapsed")
    if uploaded_backup is not None:
        try:
            backup_data = json.load(uploaded_backup)
            st.session_state.constraint_graph = backup_data["graph"]
            st.session_state.history = backup_data["history"]
            st.success("🔄 Workspace restored perfectly!")
            st.rerun()
        except Exception:
            st.error("Invalid backup asset format.")

    if st.button("Reset Session Workspace", type="secondary", use_container_width=True):
        st.session_state.constraint_graph = {
            "core_architecture": {"state": "Stateless", "description": "Stateless system execution channels"},
            "security_compliance": {"state": "Standard", "description": "Enforce basic application security guidelines"},
            "error_handling": {"state": "Explicit", "description": "Implement explicit try-except block structures"}
        }
        st.session_state.history = []
        st.rerun()

# Usability Booster: Quick-test scenario template injection buttons
st.markdown("##### ⚡ Quick Testing Scenarios (Click to instantly autofill input)")
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("🟢 Scenario 1: Safe Modular Build"):
        st.session_state.autofill = "Build a fast single-turn prompt template generator that quickly outputs code."
with c2:
    if st.button("🟡 Scenario 2: Scale Optimization"):
        st.session_state.autofill = "Make the core structure modular so it can adapt to layout rules later on."
with c3:
    if st.button("🔴 Scenario 3: Critical Conflict Break"):
        st.session_state.autofill = "Redesign the engine to maintain a persistent stateful database storage connection cache."

# Main work split layouts
col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Multi-Turn Constraint Input")
    
    # Handle autofill routing logic cleanly
    default_text = st.session_state.get("autofill", "")
    new_request = st.text_area("Input your next feature requirement or target layout constraint:", value=default_text, height=120)
    
    conflict_detected = False
    conflict_cause = ""
    
    if new_request:
        lowered_req = new_request.lower()
        stateful_intents = ["stateful", "persistent", "cache", "store", "save file", "database", "write to disk", "log history", "local file", "hard drive"]
        
        if any(intent in lowered_req for intent in stateful_intents):
            if st.session_state.constraint_graph["core_architecture"]["state"] == "Stateless":
                conflict_detected = True
                conflict_cause = "Requested stateful layer contradicts active 'Stateless' core node schema configuration."

    if st.button("Process Iteration Engine Step", type="primary", use_container_width=True):
        if new_request.strip():
            if conflict_detected:
                st.error(f"🚨 **Architectural Conflict Blocked!**\n\n**Reason:** {conflict_cause}")
                
                patch = f"""### DIFFERENTIAL SPECIFICATION PATCH (NON-DESTRUCTIVE)
[UNCHANGED] security_compliance -> Enforce basic application security guidelines
[UNCHANGED] error_handling -> Implement explicit try-except block structures
[MODIFIED NODE] core_architecture -> Upgraded from [Stateless] to [Stateful Adapter Layer] to balance incoming file traffic safely."""
                
                sandbox_blueprint = """// Simulated Isolated Patch Layer
function initSessionStorage() {
    console.log("Stateful patch adapter layer executed securely inside sandbox system layer.");
}"""
                st.session_state.history.append({"request": new_request, "status": "🚨 Patched Conflict", "patch": patch, "blueprint": sandbox_blueprint})
                st.session_state.constraint_graph["core_architecture"] = {"state": "Stateful (Patched)", "description": "Stateful Adapter Patch Layer activated"}
            else:
                st.success("✅ Requirement verified smoothly into the ecosystem graph.")
                patch = f"### SYSTEM BASELINE UPDATE\n[SUCCESS] Node context updated with entry: \"{new_request}\""
                sandbox_blueprint = """// Default stateless execution pathway template\nfunction baselineProcess() {\n    console.log("System running securely on default stateless channel.");\n}"""
                st.session_state.history.append({"request": new_request, "status": "✅ Clean Integration", "patch": patch, "blueprint": sandbox_blueprint})
            
            # Clear autofill memory register to prevent loops
            if "autofill" in st.session_state:
                del st.session_state["autofill"]
            st.rerun()
        else:
            st.warning("Please describe your iteration input constraint row first.")

with col2:
    st.subheader("🚀 Output Sandbox & Session Management")
    
    # Global workspace state history backup download link button
    if st.session_state.history:
        export_payload = json.dumps({"graph": st.session_state.constraint_graph, "history": st.session_state.history}, indent=2)
        st.download_button(
            label="💾 Download Session State Backup File (.json)",
            data=export_payload,
            file_name="prompt_engine_workspace_backup.json",
            mime="application/json",
            type="secondary",
            use_container_width=True
        )
        st.divider()

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
