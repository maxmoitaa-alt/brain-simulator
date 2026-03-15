# Brain Simulator

Brain Simulator is an open source neural experimentation project that allows users to explore artificial neuron behavior, create connections, and observe how neural systems evolve over time.

The purpose of this project is to provide a simple environment for experimenting with neural networks and understanding how neuron interactions influence system dynamics.

The project is currently in **Beta 0.10**.

---

## Overview

Brain Simulator provides a graphical interface where neurons interact through weighted connections. The simulation evolves continuously and allows the user to influence learning through external signals.

The project is designed primarily as a learning and experimentation tool rather than a production machine learning framework.

---

## Features

- Artificial neuron network simulation
- Dynamic synaptic connections
- Real-time neural activity visualization
- Adjustable neuron count
- Learning through reward and punishment signals
- Multiple visualization modes

---

## Visualization Modes

### Graph Mode

Graph Mode displays neurons as nodes connected by synapses.  
Connection strength influences the thickness and color of the lines, allowing the user to observe how relationships between neurons evolve over time.

### Column Mode

Column Mode shows the global activity of the neural network as a continuous signal over time.  
This mode helps visualize overall network behavior and activity fluctuations.

---

## Technologies

The current version uses the following technologies:

- Python
- NumPy
- Tkinter
- Brian2 (planned or experimental support)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/maxmoitaa-alt/brain-simulator.git
cd brain-simulator
```

Install dependencies:

```bash
pip install numpy brian2
```

Run the simulator:

```bash
python brain_simulator.py
```

---

## Project Status

Current version: **Beta 0.10**

The project is still experimental and under active development. Features and internal structures may change.

---

## Goals

The long term goals of this project include:

- Creating a visual neural experimentation environment
- Allowing interactive manipulation of artificial neural systems
- Studying emergent neural behavior
- Providing a simple platform for educational neural network exploration

---

## Contributing

Contributions, experiments, and improvements are welcome.  
Users are encouraged to fork the repository and submit pull requests.

---

## License

This project is distributed as open source software. See the repository license for more information.
