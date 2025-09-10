# visualize_circuit.py
from qiskit import QuantumCircuit
from qiskit.circuit.library import QFT
import matplotlib.pyplot as plt

def draw_shor_circuit():
    n_count = 3
    qc = QuantumCircuit(n_count + 4, n_count)

    # Superposition
    for q in range(n_count):
        qc.h(q)

    # Placeholder for U gates (modular exponentiation)
    qc.barrier()
    qc.cp(2*np.pi/16, 0, 3)
    qc.cp(2*np.pi/8, 1, 3)
    qc.cp(2*np.pi/4, 2, 3)
    qc.barrier()

    # Inverse QFT
    qc.append(QFT(n_count, inverse=True), range(n_count))

    # Draw
    qc.draw(output='mpl', filename='images/shor_circuit.png')
    plt.show()

if __name__ == "__main__":
    draw_shor_circuit()
