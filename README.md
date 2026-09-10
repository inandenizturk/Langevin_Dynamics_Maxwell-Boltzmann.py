cat << 'EOF' > README.md
# 2D Langevin Dynamics & Maxwell-Boltzmann Simulation

A real-time stochastic dynamics simulation written in Python. This project models particle transport under external forces (gravity and an electric field), viscous drag, and thermal fluctuations using the Langevin stochastic differential equation solved via the Euler-Maruyama method.

![Simulation Demo](docs/preview.png)

---

## Physical Background

The motion of each particle in the fluid chamber is governed by the Langevin equation:

m * dv/dt = F_ext - gamma * v + eta(t)

Where:
* F_ext = (E - g) * j accounts for the electric field and gravitational forces along the vertical axis.
* -gamma * v is the viscous drag force (Stokes' law).
* eta(t) represents Gaussian thermal fluctuations satisfying the Fluctuation-Dissipation Theorem:
  <eta_i(t) * eta_j(t')> = 2 * gamma * k_B * T * delta_ij * delta(t - t')

### Emergent Equilibrium
Despite nonequilibrium boundary reflections and constant directional forces, the system's thermal equilibrium produces an emergent 2D Maxwell-Boltzmann speed distribution:

f(v) = (v / (k_B * T)) * exp(-v^2 / (2 * k_B * T))

---

## Features

* Euler-Maruyama Numerical Solver: Numerically integrates stochastic accelerations at stable time steps (dt = 0.02).
* Real-Time Statistical Verification: Live histogram rendering fitted dynamically against the analytical Maxwell-Boltzmann curve.
* Cyberpunk Neon Visuals: Custom matplotlib theme featuring layered glow effects and high-contrast boundaries.
* Inelastic Boundary Handling: Momentum-dampened boundary reflections (v_perp -> -0.7 * v_perp) ensuring physical stability inside the chamber.

---

## Run Directly from Terminal

Clone the repository, install dependencies, and run the script with a single terminal command:

```bash
git clone [https://github.com/](https://github.com/)<your-username>/langevin-maxwell-boltzmann.git
cd langevin-maxwell-boltzmann
pip install numpy matplotlib
python boltzmann_neon.py
