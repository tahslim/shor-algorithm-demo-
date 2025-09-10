# run_demo.py
from shor import shor_quantum_period

print("🔍 Quantum Factorization using Shor's Algorithm")
print("🎯 Factoring N = 15 with base a = 7\n")

f1, f2 = shor_quantum_period(n_count=3)

if f1 and f2:
    print(f"\n🎉 Success: 15 = {f1} × {f2}")
else:
    print("\n❌ No valid factors found. Try increasing shots or qubits.")
