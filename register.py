from qiskit_ibm_runtime import QiskitRuntimeService

try:
    QiskitRuntimeService.save_account(
token="p5-H5VQC2P760H35DOQKZcXPsimt0Rla0af7NXsfy0IL",
)
except:
    pass
    print("Account already exists. Skipping registration.")
