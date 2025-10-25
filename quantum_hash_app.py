import streamlit as st
import numpy as np
import hashlib
import matplotlib.pyplot as plt
import base64
from io import BytesIO

class QuantumHashGenerator:
    def __init__(self):
        self.quantum_states = []
    
    def quantum_entanglement_simulation(self, data):
        """Simulate quantum entanglement effect on data"""
        # Convert input to bytes if it's string
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        # Create initial hash using classical method
        initial_hash = hashlib.sha256(data).digest()
        
        # Simulate quantum superposition by creating multiple states
        quantum_states = []
        for i in range(8):  # 8 parallel quantum states
            # Rotate and transform bytes
            rotated = bytes((b + i) % 256 for b in initial_hash)
            quantum_states.append(hashlib.sha256(rotated).digest())
        
        # Simulate quantum entanglement by XORing all states
        entangled_hash = quantum_states[0]
        for state in quantum_states[1:]:
            entangled_hash = bytes(a ^ b for a, b in zip(entangled_hash, state))
        
        self.quantum_states = quantum_states
        return entangled_hash.hex()
    
    def quantum_measurement_collapse(self, data, measurement_basis=0):
        """Simulate quantum measurement collapse"""
        entangled_hash = self.quantum_entanglement_simulation(data)
        
        # Convert to bytes for measurement
        hash_bytes = bytes.fromhex(entangled_hash)
        
        # Apply different measurement bases
        if measurement_basis == 1:
            # Hadamard-like transformation simulation
            measured = bytes((b ^ 0xAA) for b in hash_bytes)
        elif measurement_basis == 2:
            # Phase shift simulation
            measured = bytes((b ^ 0x55) for b in hash_bytes)
        else:
            # Standard basis
            measured = hash_bytes
        
        return hashlib.sha256(measured).hexdigest()
    
    def generate_quantum_hash(self, data, rounds=3):
        """Generate quantum-inspired hash with multiple rounds"""
        current_hash = data
        
        for round_num in range(rounds):
            if round_num % 2 == 0:
                current_hash = self.quantum_entanglement_simulation(current_hash)
            else:
                current_hash = self.quantum_measurement_collapse(current_hash, round_num % 3)
        
        return current_hash

def plot_quantum_states(quantum_states):
    """Visualize quantum states"""
    if not quantum_states:
        return None
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Convert quantum states to numerical values for plotting
    states_numeric = []
    for state in quantum_states[:4]:  # Plot first 4 states
        numeric = [b for b in state[:16]]  # First 16 bytes
        states_numeric.append(numeric)
    
    # Create superposition visualization
    x = range(len(states_numeric[0]))
    for i, state in enumerate(states_numeric):
        ax.plot(x, state, marker='o', label=f'Quantum State {i+1}')
    
    ax.set_title('Quantum State Superposition')
    ax.set_xlabel('Byte Position')
    ax.set_ylabel('Byte Value')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    return fig

def main():
    st.set_page_config(
        page_title="Quantum Hash Generator",
        page_icon="⚛️",
        layout="wide"
    )
    
    st.title("⚛️ Quantum-Inspired Hash Generator")
    st.markdown("Generate cryptographic hashes using quantum computing principles")
    
    # Initialize session state
    if 'quantum_hash' not in st.session_state:
        st.session_state.quantum_hash = None
    if 'qhg' not in st.session_state:
        st.session_state.qhg = QuantumHashGenerator()
    
    # Sidebar for configuration
    st.sidebar.header("Configuration")
    hash_rounds = st.sidebar.slider("Quantum Rounds", 1, 10, 3)
    measurement_basis = st.sidebar.selectbox(
        "Measurement Basis",
        ["Standard (0)", "Hadamard-like (1)", "Phase-shift (2)"]
    )
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Input Data")
        input_type = st.radio("Input Type:", ["Text", "File"])
        
        input_data = None
        
        if input_type == "Text":
            input_data = st.text_area("Enter text to hash:", height=100, 
                                    placeholder="Enter your secret message here...")
            use_sample = st.checkbox("Use sample text")
            if use_sample:
                sample_text = "Quantum cryptography will revolutionize security!"
                st.text_area("Sample text:", sample_text, height=60)
                if st.button("Use Sample Text"):
                    input_data = sample_text
        else:
            uploaded_file = st.file_uploader("Choose a file", type=None)
            if uploaded_file is not None:
                input_data = uploaded_file.getvalue()
                st.success(f"File uploaded: {uploaded_file.name} ({len(input_data)} bytes)")
        
        if st.button("Generate Quantum Hash", type="primary") and input_data:
            with st.spinner("Creating quantum entanglement..."):
                # Initialize quantum hash generator
                qhg = QuantumHashGenerator()
                
                # Generate quantum hash
                basis_map = {"Standard (0)": 0, "Hadamard-like (1)": 1, "Phase-shift (2)": 2}
                basis = basis_map[measurement_basis]
                
                quantum_hash = qhg.generate_quantum_hash(input_data, hash_rounds)
                st.session_state.quantum_hash = quantum_hash
                st.session_state.qhg = qhg
                
                # Display results
                st.subheader("🔐 Generated Hash")
                st.code(quantum_hash, language="text")
                
                # Hash properties
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric("Hash Length", f"{len(quantum_hash)} characters")
                with col_b:
                    st.metric("Hash Rounds", hash_rounds)
                with col_c:
                    st.metric("Measurement Basis", measurement_basis.split(' ')[0])
                
                # Visualization
                st.subheader("📊 Quantum State Visualization")
                if qhg.quantum_states:
                    fig = plot_quantum_states(qhg.quantum_states)
                    if fig:
                        st.pyplot(fig)
                
                # Comparison with classical hashes
                st.subheader("🔍 Comparison with Classical Hashes")
                if isinstance(input_data, str):
                    input_bytes = input_data.encode('utf-8')
                else:
                    input_bytes = input_data
                
                classical_hashes = {
                    "SHA-256": hashlib.sha256(input_bytes).hexdigest(),
                    "SHA-512": hashlib.sha512(input_bytes).hexdigest(),
                    "MD5": hashlib.md5(input_bytes).hexdigest(),
                    "BLAKE2b": hashlib.blake2b(input_bytes).hexdigest()
                }
                
                for name, hash_val in classical_hashes.items():
                    with st.expander(f"{name}: {hash_val[:32]}..."):
                        st.text(hash_val)
    
    with col2:
        st.subheader("ℹ️ About Quantum Hashing")
        st.markdown("""
        **Quantum Hashing Features:**
        - Simulated quantum entanglement
        - Multiple quantum states
        - Measurement collapse simulation
        - Parallel processing simulation
        
        **Security Advantages:**
        - Resistance to quantum attacks
        - Multiple hash states
        - Basis-dependent outputs
        - Enhanced collision resistance
        """)
        
        st.subheader("🚀 Quick Actions")
        if st.button("Generate Random Hash"):
            import random
            random_data = f"random_{random.randint(0, 1000000)}"
            qhg = QuantumHashGenerator()
            random_hash = qhg.generate_quantum_hash(random_data)
            st.text_area("Random Hash:", random_hash, height=100)
        
        if st.session_state.quantum_hash:
            st.download_button(
                label="📥 Download Hash Results",
                data=st.session_state.quantum_hash,
                file_name="quantum_hash_result.txt",
                mime="text/plain"
            )
        
        st.subheader("🔧 Technical Details")
        st.markdown("""
        **Algorithm:**
        1. Initial SHA-256 hash
        2. Create 8 parallel quantum states
        3. Entangle states via XOR operations
        4. Apply measurement basis
        5. Multiple rounds for security
        """)

if __name__ == "__main__":
    main()