""" Simulating quantum OR gate """
import numpy as np

# PauliX gate operator applied to the first of three qubits
X1_3 = np.kron(np.kron(np.array([[0, 1], [1, 0]]), np.eye(2)), np.eye(2))
# PauliX gate operator applied to the second of three qubits
X2_3 = np.kron(np.kron(np.eye(2), np.array([[0, 1], [1, 0]])), np.eye(2))
# # PauliX gate operator applied to the third of three qubits
# X3_3 = np.kron(np.kron(np.eye(2), np.eye(2)), np.array([[0, 1], [1, 0]]))

# Toffoli gate operator
Toffoli = np.array(
    [
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0],
    ]
)

states = [
    # |0,0,0> state
    np.array([1, 0, 0, 0, 0, 0, 0, 0]),
    # |0,1,0> state
    np.array([0, 0, 1, 0, 0, 0, 0, 0]),
    # |1,0,0> state
    np.array([0, 0, 0, 0, 1, 0, 0, 0]),
    # |1,1,0> state
    np.array([0, 0, 0, 0, 0, 0, 1, 0]),
]

# After applying OR on first two qubits, the expected outputs are:
expected_outputs = [
    # |0,0,0>
    np.array([1, 0, 0, 0, 0, 0, 0, 0]),
    # |0,1,1>
    np.array([0, 0, 0, 1, 0, 0, 0, 0]),
    # |1,0,1>
    np.array([0, 0, 0, 0, 0, 1, 0, 0]),
    # |1,1,1> state
    np.array([0, 0, 0, 0, 0, 0, 0, 1]),
]


# Implementing a gate that maps from states to expected_outputs
# using the following gates: X1_3, X2_3, X3_3, Toffoli
def logic_gate_or(state):
    return Toffoli @ X2_3 @ Toffoli @ X2_3 @ X1_3 @ Toffoli @ X1_3 @ state


# Check that the circuit adheres to the expected outputs
for i, state in enumerate(states):
    assert np.allclose(
        logic_gate_or(state), expected_outputs[i]
    ), f"Test failed for state {state}"


def print_proba(state):
    for i, prob in enumerate(np.abs(state) ** 2):
        bitstring = f"{i:b}".zfill(3)
        print(f"{bitstring}: {prob:.2f}")


# Example: Applying the OR gate to the |+,0,0> state
# Hadamard gate
H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)

# Hadamard gate when applied to the first of three qubits
H1_3 = np.kron(np.kron(H, np.eye(2)), np.eye(2))

# Prepare |0,0,0> state: 100% probability to measure three zero bits.
state = np.array([1, 0, 0, 0, 0, 0, 0, 0])

# Apply the Hadamard gate to the first qubit:
# 50% probability to measure 0 and 50% probability to measure 1
# on the first qubit (|+> state)
state = H1_3 @ state

print("Input 1 |+,0,0>")
print(state)

# Apply the OR gate to the |+,0,0> state
state = logic_gate_or(state)

print("Resulting state vector:")
print(state)
print("Measuring probabilities:")
print_proba(state)
print()


# Example: Applying the OR gate to the |+,+,0> state
# Prepare a fresh |0,0,0> state: 100% probability to measure three zero bits.
state = np.array([1, 0, 0, 0, 0, 0, 0, 0])

H2_3 = np.kron(np.kron(np.eye(2), H), np.eye(2))
# Prepare |+,+,0> state by applying Hadamard gate to the first two qubits.
state = H2_3 @ H1_3 @ state

print("Input 2 |+,+,0>")
print(state)

# Apply the OR gate to the |+,+,0> state
state = logic_gate_or(state)

print("Resulting state vector:")
print(state)
print("Measuring probabilities:")
print_proba(state)
print()
