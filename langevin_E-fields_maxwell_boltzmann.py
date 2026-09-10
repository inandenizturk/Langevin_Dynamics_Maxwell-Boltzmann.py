cat << 'EOF' > boltzmann_neon.py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- Parameters ---
N = 160              # Number of particles
box_w, box_h = 10.0, 10.0
dt = 0.02
gamma = 0.8          # Friction / Drag coefficient
kBT = 1.3            # Thermal energy
g = 2.5              # Gravitational acceleration
E = 2.2              # Electric field strength

pos = np.random.uniform(1.0, 9.0, (N, 2))
vel = np.random.normal(0, np.sqrt(kBT), (N, 2))

# --- Dark Neon Red Styling ---
plt.style.use('dark_background')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 5))

bg_color = '#150204'       # Deep dark red / maroon
border_color = '#ff1a40'   # Neon red

for ax in (ax1, ax2):
    ax.set_facecolor(bg_color)
    for spine in ax.spines.values():
        spine.set_color(border_color)
        spine.set_linewidth(1.5)
    ax.tick_params(colors='#ff8093')

fig.patch.set_facecolor('#0d0102')

# Left Panel: 2D Particle Chamber under External Field
ax1.set_xlim(0, box_w)
ax1.set_ylim(0, box_h)
ax1.set_title("LANGEVIN DYNAMICS [NEON E-FIELD]", color='#ff3355', fontsize=12, pad=10, fontweight='bold')
ax1.set_xticks([])
ax1.set_yticks([])

# Neon Boundary Plates
ax1.axhline(box_h, color='#ff0033', lw=4, label="+ Plate (Anode)")
ax1.axhline(0, color='#ff6680', lw=4, ls='--', label="- Plate (Cathode)")

# Neon Particles (Outer glow layer and core scatter)
scat_glow = ax1.scatter(pos[:, 0], pos[:, 1], c='#ff0044', s=120, alpha=0.25, edgecolors='none')
scat = ax1.scatter(pos[:, 0], pos[:, 1], c='#ffdd00', s=25, edgecolors='#ff0033', linewidth=0.8)
ax1.legend(loc="upper right", facecolor='#200306', edgecolor='#ff1a40', labelcolor='#ffccd5')

# Right Panel: Speed Distribution vs Theoretical Maxwell-Boltzmann
ax2.set_xlim(0, 4.5)
ax2.set_ylim(0, 0.8)
ax2.set_xlabel("Speed (|v|)", color='#ffccd5')
ax2.set_ylabel("Probability Density", color='#ffccd5')
ax2.set_title("MAXWELL-BOLTZMANN DISTRIBUTION", color='#ff3355', fontsize=12, pad=10, fontweight='bold')

v_range = np.linspace(0, 4.5, 200)
mb_theory = (v_range / kBT) * np.exp(- (v_range**2) / (2 * kBT))
ax2.plot(v_range, mb_theory, color='#00ffff', lw=2.2, label="Theoretical Boltzmann (Neon Cyan)")
ax2.legend(loc="upper right", facecolor='#200306', edgecolor='#ff1a40', labelcolor='#ffccd5')

def update(frame):
    global pos, vel

    # Applied Net External Forces & Thermal Fluctuations
    F_net_y = -g + E
    thermal = np.random.normal(0, np.sqrt(2 * gamma * kBT / dt), (N, 2))

    # Langevin Stochastic Integration (Euler-Maruyama)
    acc = np.zeros_like(vel)
    acc[:, 1] += F_net_y
    acc += -gamma * vel + thermal

    vel += acc * dt
    pos += vel * dt

    # Boundary Collisions (Inelastic Dampening)
    for dim, limit in enumerate([box_w, box_h]):
        hit_low = pos[:, dim] < 0.2
        hit_high = pos[:, dim] > limit - 0.2
        pos[hit_low, dim] = 0.2
        vel[hit_low, dim] *= -0.7
        pos[hit_high, dim] = limit - 0.2
        vel[hit_high, dim] *= -0.7

    scat.set_offsets(pos)
    scat_glow.set_offsets(pos)

    # Frame-decimated Histogram Refresh
    if frame % 2 == 0:
        speeds = np.linalg.norm(vel, axis=1)
        [p.remove() for p in reversed(ax2.patches)]
        ax2.hist(speeds, bins=16, range=(0, 4.5), density=True,
                 color='#ff0044', edgecolor='#ff99aa', alpha=0.55)

    return scat, scat_glow

ani = animation.FuncAnimation(fig, update, frames=300, interval=25, blit=False)
plt.tight_layout()
plt.show()
EOF
python3 boltzmann_neon.py
