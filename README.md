# Quantum-Style-Pseudo-Random-Hashing

 A**quantum-inspired cryptographic hashing simulator** built using Python and Streamlit.  
This application generates secure hash values by imitating **quantum computing concepts** such as **superposition, entanglement,** and **measurement collapse** using classical algorithms.

> Note: This project does **not** use real quantum hardware. It *simulates* quantum-like transformations to produce stronger, less predictable hash outputs.

> Features
- **Quantum Superposition Simulation:** Generates 8 parallel hash states from an input.
- **Quantum Entanglement Simulation:** Combines states using XOR operations.
- **Measurement Collapse:** Allows multiple measurement bases (Standard, Hadamard-like, Phase-Shift).
- **Multiple Quantum Rounds** to increase complexity and randomness.
- **File & Text Input Support**
- **Hash Comparison** against classical hashing algorithms:
  - SHA-256
  - SHA-512
  - MD5
  - BLAKE2b
- **Quantum State Visualization** using Matplotlib plots.
- **Streamlit Web Interface** for interactive use.


## How It Works (Concept Overview)
1. Input Stage:
The user provides data either as text or a file.
2. Initial Classical Hash:
The input is first converted to a normal SHA-256 hash, which acts as the starting state.
3. Quantum Superposition Simulation:
The initial hash is modified in 8 different ways to create 8 parallel hash states, similar to how a quantum system can exist in multiple states at once.
4. Quantum Entanglement Simulation:
All 8 generated hash states are combined using XOR operations, so every state affects the final result.
This means even a 1-bit change in input changes the final hash drastically.
5. Measurement Basis Selection:
A measurement basis (0, 1, or 2) is applied:
• Standard (0): No extra change
• Hadamard-like (1): XOR with 0xAA
• Phase-Shift (2): XOR with 0x55
This simulates how observing a quantum state affects outcomes.
6. Multiple Hashing Rounds (Security Strengthening):
The entire process can repeat 1 to 10 times, making the hash more unpredictable and secure.
7. Final Hash Output:
The result is a unique quantum-inspired hash string, displayed to the user.
8. Visualization:
The system also shows a graph of the first four quantum states to represent the simulated superposition.
9. Classical Comparison:
For understanding, the app also displays classical hashes (SHA-256, SHA-512, MD5, BLAKE2b) so users can compare differences.

## Installation
1. Clone the Repository
2. Install Dependencies
pip install -r requirements.txt
If requirements.txt not available, install manually:
pip install streamlit numpy hashlib matplotlib

⟩ Running the Application
streamlit run quantum_hash_app.py
Then open the displayed local link:
http://localhost:8501

⟩ Usage
1. Choose Text or File input.
2. Select number of Quantum Rounds (1–10 recommended).
3. Select Measurement Basis:
Standard (0) — Normal collapse
Hadamard-like (1) — XOR with 0xAA
Phase-shift (2) — XOR with 0x55
4. Click Generate Quantum Hash
5. Review:
Generated Hash Output
State Visualization Plot
Classical Hash Comparison

⟩ Example Output
d9bfe88e1d5ad0991f4cc3bd7aaf92f68c22a8f2db9b4a1f3d6c18e3c0de23c1

⟩ Real-World Applications (Conceptually)
• Quantum-resistant security research
• Cryptography education & demonstration
• Hash strengthening experiments
• Hash visualization and randomness studies



