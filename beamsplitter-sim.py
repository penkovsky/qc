""" Simulating all four stages of quantum computation:

1. Encode a qubit.
2. Apply quantum logic gates.
3. Obtain a theoretical probability distribution (this does quantum hardware).
4. Sample from the distribution to obtain a measurement outcome.
"""
import numpy as np


def prepare_state():
    """
    Prepare a qubit in the |0> state
    """
    return np.array([1, 0])


def bs(state):
    """Simulate a beam splitter"""
    Hadamard = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    return np.dot(Hadamard, state)


def measure_state(state, n):
    """
    Measure a quantum state n times.
    """
    return np.random.choice(
        [0, 1],
        n,
        # Convert the amplitudes to probabilities
        p=[np.abs(state[0]) ** 2, np.abs(state[1]) ** 2],
    )


def main():
    """A minimal quantum computing example."""
    # A qubit in the |0> state
    state = prepare_state()
    # Simulate a beam splitter
    state = bs(state)
    # Measure the state
    n = 1000
    results = measure_state(state, n)
    print(f"Measured {results.sum()} ones out of {n} measurements")


if __name__ == "__main__":
    main()
