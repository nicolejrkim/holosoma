# Booster K1 (22-DOF) — asset source

Robot: **Booster K1**, by Booster Robotics (https://www.boosterobotics.com).

Upstream: **`BoosterRobotics/booster_assets`**, path `robots/K1/`
<https://github.com/BoosterRobotics/booster_assets/tree/main/robots/K1>

`k1_22dof.urdf` / `k1_22dof.xml` derive from upstream `K1_22dof.urdf` /
`K1_22dof.xml` (SolidWorks-to-URDF export, `<robot name="K1">`). Meshes are
byte-identical to upstream (52 files, incl. `K1logo.STL`, `K1_left_foot.STL`;
the `*_Collision.STL` and `Head_2_ZED.STL` variants are **upstream**, not added
here).

Changes from upstream (verified 2026-07-06 by `diff`):
- **The only holosoma modification is foot contact spheres — 5 per foot**
  (`left/right_foot_sphere_1..5_link`), registered as foot-sticking IK targets.
- The MuJoCo scene (skybox / checker floor / lights), the `<default>` block,
  `<actuator>`, `<sensor>`, and the box/cylinder collision geoms are **all
  upstream and unchanged**.

License: BSD-3-Clause (Booster Robotics) — see `LICENSE` in this dir.
