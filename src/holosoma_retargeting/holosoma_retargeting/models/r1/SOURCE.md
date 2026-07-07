# Unitree R1 — asset source

Robot: **Unitree R1**, by Unitree Robotics (https://www.unitree.com).

Upstream: **`unitreerobotics/unitree_mujoco`**, path `unitree_robots/r1/`
<https://github.com/unitreerobotics/unitree_mujoco/tree/main/unitree_robots/r1>
Upstream ships `R1_C++.xml` + `scene.xml` + `meshes/` — no URDF and no
`_26dof`/`_29dof` names. R1 is in `unitree_mujoco` but not `unitree_rl_gym`,
which pins the source to `unitree_mujoco`.

Meshes are byte-identical to upstream (43 files; e.g. `pelvis_link.STL` =
1911634 B).

Files & changes from upstream (verified 2026-07-06 by `diff`):
- `r1_29dof.xml` — faithful to upstream `R1_C++.xml` (keeps the imu site, named
  free joint, `<default>`, `<actuator>`, `<sensor>`, box foot-collision) **+ foot
  contact spheres, 5 per foot** (`left/right_ankle_roll_sphere_1..5_link`).
- `r1_26dof.xml` — a URDF-derived / stripped MJCF (imu site + named joint
  removed; `<default>`/`<actuator>`/`<sensor>` dropped; mesh collisions instead
  of the box) **+ the same 5 foot spheres/foot**.
- `r1_26dof.urdf` — **holosoma-authored** (upstream has no URDF); this is the
  file the retargeter loads. 10 foot-sphere links (5/foot).

License: BSD-3-Clause (Unitree Robotics) — see `LICENSE` in this dir.
