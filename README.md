cat << 'EOF' > README.md
# Langevin Dynamics & Maxwell-Boltzmann (Neon Red)

Real-time 2D Langevin dynamics simulation written in Python. Solves Brownian motion with thermal noise, drag, and an electric field, demonstrating an emergent Maxwell-Boltzmann velocity distribution.

![Preview](docs/preview.png)

## Run Directly from Terminal

Navigate to the project directory and run:

```bash
pip install numpy matplotlib
python boltzmann_neon.py


Physics & Features
Langevin SDE: Solved numerically via the Euler-Maruyama method.
Fluctuation-Dissipation: Thermal noise balanced against viscous drag.
Live Stats: Real-time speed histogram fitted against the 2D Maxwell-Boltzmann distribution.
Theme: Cyberpunk dark-neon aesthetic in Matplotlib.
