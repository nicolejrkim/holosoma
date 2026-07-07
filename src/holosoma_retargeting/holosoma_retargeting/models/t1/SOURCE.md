# Booster T1 (23-DOF) — asset source

Robot: **Booster T1**, by Booster Robotics (https://www.boosterobotics.com).

Upstream: **`BoosterRobotics/booster_assets`**, path `robots/T1/`
<https://github.com/BoosterRobotics/booster_assets/tree/main/robots/T1>
The `T1_23dof.urdf` / `T1_23dof.xml` filenames exist only in `booster_assets`
(`booster_gym` uses `T1_serial`/`T1_locomotion`; `mujoco_menagerie` uses
`t1.xml`), which pins the source.

**T1 is the most heavily modified robot in this tree.** Changes from upstream
(verified 2026-07-06 by `diff`):
- Foot contact spheres, 5 per foot (`left/right_foot_sphere_1..5_link`) — the
  holosoma convention shared by the other robots — **plus 2 hand spheres**
  (`left/right_hand_sphere_link`). T1 is the only robot here with hand spheres.
- `t1_23dof.xml` re-authored: added `<option integrator="implicitfast">`, two
  `<default>` blocks of motor classes (waist / leg / ankle / arm / head) + a
  `t1` class, and `<material>` defs; the upstream skybox + checker scene is
  **stripped** to a bare ground plane + one light; the `Logo` mesh is dropped.
- `t1_23dof.urdf` re-authored: collision geometry **swapped from upstream
  primitives (box/cylinder) to full mesh collisions** using holosoma-generated
  `*_from_STL.obj` conversions; the commented `world` link + `<mujoco>` block
  removed.
- Meshes are **not** a clean copy: 32 `*_from_STL.obj` conversions and
  `left/right_rubber_hand.STL` added; a few STLs regenerated (`Trunk.STL`,
  `AL1.STL` differ from upstream by a few hundred bytes); `Logo.STL` dropped.
- `t1_23dof_w_largebox.xml` = `t1_23dof.xml` + a free-floating `largebox_link`
  manipulation object (mirrors `g1_29dof_w_largebox.xml`), not a robot edit.

License: BSD-3-Clause (Booster Robotics) — see `LICENSE` in this dir.
