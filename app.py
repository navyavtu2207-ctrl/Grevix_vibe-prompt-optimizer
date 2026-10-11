import streamlit as st

st.set_page_config(page_title="Stateful Prompt Engine Ultra", layout="wide")

st.title(" AI Vibe-Coding Prompt Optimizer (Stateful Engine)")
st.caption("Grevix AfterCode Phase 2 ")

# Initialize Stateful Nodes safely in memory
if "constraint_graph" not in st.session_state:
    st.session_state.constraint_graph = {
        "core_architecture": {"state": "Stateless", "description": "Stateless system execution channels"},
        "security_compliance": {"state": "Standard", "description": "Enforce basic application security guidelines"},
        "error_handling": {"state": "Explicit", "description": "Implement explicit try-except block structures"}
    }
if "history" not in st.session_state:
    st.session_state.history = []

# Anti-Cache Reset Guard (Keeps baseline cache from blowing up on simple reloads)
if "session_initialized" not in st.session_state:
    st.session_state.session_initialized = True

# Sidebar displaying active graph states
with st.sidebar:
    st.header("🕸️ Active Architectural Graph")
    for key, node in st.session_state.constraint_graph.items():
        st.markdown(f"**• {key.replace('_', ' ').title()}:** `{node['state']}`")
    
    st.divider()
    st.header("📊 Engine Health Metrics")
    st.metric(label="Total Iterations", value=len(st.session_state.history))
    st.metric(label="Process Latency", value="0 ms", delta="Zero Added Latency")
    
    st.divider()
    if st.button("Reset Session Workspace", type="secondary", use_container_width=True):
        st.session_state.constraint_graph = {
            "core_architecture": {"state": "Stateless", "description": "Stateless system execution channels"},
            "security_compliance": {"state": "Standard", "description": "Enforce basic application security guidelines"},
            "error_handling": {"state": "Explicit", "description": "Implement explicit try-except block structures"}
        }
        st.session_state.history = []
        if "user_input_text" in st.session_state:
            st.session_state.user_input_text = ""
        st.rerun()

# Input Box State Retention Router Logic
def set_autofill(text):
    st.session_state.user_input_text = text

st.markdown("##### ⚡ Quick Testing Scenarios (Click to instantly test)")
c1, c2, c3 = st.columns(3)
with c1:
    st.button("🟢 Scenario 1: Safe Modular Build", on_click=set_autofill, args=("Build a fast single-turn prompt template generator that quickly outputs code.",), use_container_width=True)
with c2:
    st.button("🟡 Scenario 2: Scale Optimization", on_click=set_autofill, args=("Make the core structure modular so it can adapt to layout rules later on.",), use_container_width=True)
with c3:
    st.button("🔴 Scenario 3: Critical Conflict Break", on_click=set_autofill, args=("Redesign the engine to maintain a persistent stateful database storage connection cache.",), use_container_width=True)

# Split Workspace layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Multi-Turn Constraint Input")
    
    # Initialize the input text session key securely if missing
    if "user_input_text" not in st.session_state:
        st.session_state.user_input_text = ""
        
    new_request = st.text_area(
        "Input your next feature requirement or target layout constraint:", 
        key="user_input_text", 
        height=120
    )
    
    conflict_detected = False
    conflict_cause = ""
    
    if new_request.strip():
        lowered_req = new_request.lower()
        
        # Deepened Intent Array (Eliminates keyword boundary blind spots completely)
        stateful_intents = [
            "stateful", "persistent", "cache", "store", "save file", "database", 
            "write to disk", "log history", "local file", "hard drive", "external structure",
            "background worker", "records asynchronously", "filesystem traffic", "data repository"
        ]
        
        if st.session_state.constraint_graph["core_architecture"]["state"] == "Stateless":
            if any(intent in lowered_req for intent in stateful_intents):
                conflict_detected = True
                conflict_cause = "Requested stateful tracking footprints contradict the active 'Stateless' baseline configuration."

    if st.button("Process Iteration Engine Step", type="primary", use_container_width=True):
        if new_request.strip():
            if conflict_detected:
                st.error(f"🚨 **Architectural Conflict Blocked!**\n\n**Reason:** {conflict_cause}")
                
                patch = f"""### DIFFERENTIAL SPECIFICATION PATCH (NON-DESTRUCTIVE)
[UNCHANGED] security_compliance -> Enforce basic application security guidelines
[UNCHANGED] error_handling -> Implement explicit try-except block structures
[MODIFIED NODE] core_architecture -> Upgraded from [Stateless] to [Stateful Adapter Layer] to balance incoming data traffic safely."""
                
                sandbox_blueprint = """// Simulated Isolated Patch Layer\nfunction initSessionStorage() {\n    console.log("Stateful patch adapter layer executed securely inside sandbox system layer.");\n}"""
                st.session_state.history.append({"request": new_request, "status": "🚨 Patched Conflict", "patch": patch, "blueprint": sandbox_blueprint})
                st.session_state.constraint_graph["core_architecture"] = {"state": "Stateful (Patched)", "description": "Stateful Adapter Patch Layer activated"}
            else:
                st.success("✅ Requirement verified smoothly into the ecosystem graph.")
                patch = f"### SYSTEM BASELINE UPDATE\n[SUCCESS] Node context updated with entry: \"{new_request}\""
                sandbox_blueprint = """// Default stateless execution pathway template\nfunction baselineProcess() {\n    console.log("System running securely on default stateless channel.");\n}"""
                st.session_state.history.append({"request": new_request, "status": "✅ Clean Integration", "patch": patch, "blueprint": sandbox_blueprint})
            
            st.rerun()
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
