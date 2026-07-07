# Unitree H1-2 (H1_2, 27-DOF) — asset source

Robot: **Unitree H1_2**, by Unitree Robotics (https://www.unitree.com/h1).

Upstream: **`unitreerobotics/unitree_mujoco`**, path `unitree_robots/h1_2/`
<https://github.com/unitreerobotics/unitree_mujoco/tree/main/unitree_robots/h1_2>

`h1_2_27dof.xml` derives from upstream `h1_2_handless.xml`; meshes are
byte-identical to upstream (e.g. `pelvis.STL` = 672884 B).

Changes from upstream (verified 2026-07-06 by `diff`):
- **The only holosoma modification is foot contact spheres — 5 per foot**
  (`left/right_ankle_roll_sphere_1..5_link`). The `<default>` block,
  `<actuator>`, `<sensor>`, and all collision geometry are **byte-for-byte
  upstream**.
- `h1_2_27dof.urdf` carries the same model with the 10 foot-sphere links added.

License: BSD-3-Clause (Unitree Robotics) — see `LICENSE` in this dir.
