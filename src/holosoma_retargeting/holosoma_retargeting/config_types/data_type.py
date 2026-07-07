"""Configuration types for motion data format."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, TypedDict

from holosoma_retargeting.config_types.robot import (
    RobotDefaults,
    _default_robot_defaults,
    _validate_robot_type,
)

# Pre-defined constants for each data format
LAFAN_DEMO_JOINTS = [
    "Hips",
    "RightUpLeg",
    "RightLeg",
    "RightFoot",
    "RightToeBase",
    "LeftUpLeg",
    "LeftLeg",
    "LeftFoot",
    "LeftToeBase",
    "Spine",
    "Spine1",
    "Spine2",
    "Neck",
    "Head",
    "RightShoulder",
    "RightArm",
    "RightForeArm",
    "RightHand",
    "LeftShoulder",
    "LeftArm",
    "LeftForeArm",
    "LeftHand",
]

SMPLH_DEMO_JOINTS = [
    "Pelvis",
    "L_Hip",
    "L_Knee",
    "L_Ankle",
    "L_Toe",
    "R_Hip",
    "R_Knee",
    "R_Ankle",
    "R_Toe",
    "Torso",
    "Spine",
    "Chest",
    "Neck",
    "Head",
    "L_Thorax",
    "L_Shoulder",
    "L_Elbow",
    "L_Wrist",
    "L_Index1",
    "L_Index2",
    "L_Index3",
    "L_Middle1",
    "L_Middle2",
    "L_Middle3",
    "L_Pinky1",
    "L_Pinky2",
    "L_Pinky3",
    "L_Ring1",
    "L_Ring2",
    "L_Ring3",
    "L_Thumb1",
    "L_Thumb2",
    "L_Thumb3",
    "R_Thorax",
    "R_Shoulder",
    "R_Elbow",
    "R_Wrist",
    "R_Index1",
    "R_Index2",
    "R_Index3",
    "R_Middle1",
    "R_Middle2",
    "R_Middle3",
    "R_Pinky1",
    "R_Pinky2",
    "R_Pinky3",
    "R_Ring1",
    "R_Ring2",
    "R_Ring3",
    "R_Thumb1",
    "R_Thumb2",
    "R_Thumb3",
]

MOCAP_DEMO_JOINTS = [
    "Hips",
    "Spine",
    "Spine1",
    "Neck",
    "Head",
    "LeftShoulder",
    "LeftArm",
    "LeftForeArm",
    "LeftHand",
    "LeftHandThumb1",
    "LeftHandThumb2",
    "LeftHandThumb3",
    "LeftHandIndex1",
    "LeftHandIndex2",
    "LeftHandIndex3",
    "LeftHandMiddle1",
    "LeftHandMiddle2",
    "LeftHandMiddle3",
    "LeftHandRing1",
    "LeftHandRing2",
    "LeftHandRing3",
    "LeftHandPinky1",
    "LeftHandPinky2",
    "LeftHandPinky3",
    "RightShoulder",
    "RightArm",
    "RightForeArm",
    "RightHand",
    "RightHandThumb1",
    "RightHandThumb2",
    "RightHandThumb3",
    "RightHandIndex1",
    "RightHandIndex2",
    "RightHandIndex3",
    "RightHandMiddle1",
    "RightHandMiddle2",
    "RightHandMiddle3",
    "RightHandRing1",
    "RightHandRing2",
    "RightHandRing3",
    "RightHandPinky1",
    "RightHandPinky2",
    "RightHandPinky3",
    "LeftUpLeg",
    "LeftLeg",
    "LeftFoot",
    "LeftToeBase",
    "RightUpLeg",
    "RightLeg",
    "RightFoot",
    "RightToeBase",
    "LeftFootMod",
    "RightFootMod",
]

SMPLX_DEMO_JOINTS = [
    "Pelvis",
    "L_Hip",
    "R_Hip",
    "Spine1",
    "L_Knee",
    "R_Knee",
    "Spine2",
    "L_Ankle",
    "R_Ankle",
    "Spine3",
    "L_Foot",
    "R_Foot",
    "Neck",
    "L_Collar",
    "R_Collar",
    "Head",
    "L_Shoulder",
    "R_Shoulder",
    "L_Elbow",
    "R_Elbow",
    "L_Wrist",
    "R_Wrist",
]

SEED_DEMO_JOINTS = [
    "Root",
    "Hips",
    "Spine1",
    "Spine2",
    "Chest",
    "Neck1",
    "Neck2",
    "Head",
    "HeadEnd",
    "Jaw",
    "LeftEye",
    "RightEye",
    "LeftShoulder",
    "LeftArm",
    "LeftForeArm",
    "LeftHand",
    "LeftHandThumb1",
    "LeftHandThumb2",
    "LeftHandThumb3",
    "LeftHandThumbEnd",
    "LeftHandIndex1",
    "LeftHandIndex2",
    "LeftHandIndex3",
    "LeftHandIndex4",
    "LeftHandIndexEnd",
    "LeftHandMiddle1",
    "LeftHandMiddle2",
    "LeftHandMiddle3",
    "LeftHandMiddle4",
    "LeftHandMiddleEnd",
    "LeftHandRing1",
    "LeftHandRing2",
    "LeftHandRing3",
    "LeftHandRing4",
    "LeftHandRingEnd",
    "LeftHandPinky1",
    "LeftHandPinky2",
    "LeftHandPinky3",
    "LeftHandPinky4",
    "LeftHandPinkyEnd",
    "RightShoulder",
    "RightArm",
    "RightForeArm",
    "RightHand",
    "RightHandThumb1",
    "RightHandThumb2",
    "RightHandThumb3",
    "RightHandThumbEnd",
    "RightHandIndex1",
    "RightHandIndex2",
    "RightHandIndex3",
    "RightHandIndex4",
    "RightHandIndexEnd",
    "RightHandMiddle1",
    "RightHandMiddle2",
    "RightHandMiddle3",
    "RightHandMiddle4",
    "RightHandMiddleEnd",
    "RightHandRing1",
    "RightHandRing2",
    "RightHandRing3",
    "RightHandRing4",
    "RightHandRingEnd",
    "RightHandPinky1",
    "RightHandPinky2",
    "RightHandPinky3",
    "RightHandPinky4",
    "RightHandPinkyEnd",
    "LeftLeg",
    "LeftShin",
    "LeftFoot",
    "LeftToeBase",
    "LeftToeEnd",
    "RightLeg",
    "RightShin",
    "RightFoot",
    "RightToeBase",
    "RightToeEnd",
]

# Joint mappings - organized by (data_format, robot_type)
JOINTS_MAPPINGS = {
    ("lafan", "g1"): {
        "Spine1": "pelvis_contour_link",
        "LeftUpLeg": "left_hip_pitch_link",
        "RightUpLeg": "right_hip_pitch_link",
        "LeftLeg": "left_knee_link",
        "RightLeg": "right_knee_link",
        "LeftArm": "left_shoulder_roll_link",
        "RightArm": "right_shoulder_roll_link",
        "LeftForeArm": "left_elbow_link",
        "RightForeArm": "right_elbow_link",
        "LeftFoot": "left_ankle_intermediate_1_link",
        "RightFoot": "right_ankle_intermediate_1_link",
        "LeftToeBase": "left_ankle_roll_sphere_5_link",
        "RightToeBase": "right_ankle_roll_sphere_5_link",
        "LeftHand": "left_rubber_hand_link",
        "RightHand": "right_rubber_hand_link",
    },
    ("lafan", "t1"): {
        "Spine1": "Trunk",
        "LeftUpLeg": "Hip_Pitch_Left",
        "RightUpLeg": "Hip_Pitch_Right",
        "LeftLeg": "Shank_Left",
        "RightLeg": "Shank_Right",
        "LeftArm": "AL1",
        "RightArm": "AR1",
        "LeftForeArm": "left_hand_link",
        "RightForeArm": "right_hand_link",
        "LeftFoot": "Ankle_Cross_Left",
        "RightFoot": "Ankle_Cross_Right",
        "LeftToeBase": "left_foot_sphere_5_link",
        "RightToeBase": "right_foot_sphere_5_link",
        "LeftHand": "left_hand_sphere_link",
        "RightHand": "right_hand_sphere_link",
    },
    ("smplh", "g1"): {
        "Pelvis": "pelvis_contour_link",
        "L_Hip": "left_hip_pitch_link",
        "R_Hip": "right_hip_pitch_link",
        "L_Knee": "left_knee_link",
        "R_Knee": "right_knee_link",
        "L_Shoulder": "left_shoulder_roll_link",
        "R_Shoulder": "right_shoulder_roll_link",
        "L_Elbow": "left_elbow_link",
        "R_Elbow": "right_elbow_link",
        "L_Ankle": "left_ankle_intermediate_1_link",
        "R_Ankle": "right_ankle_intermediate_1_link",
        "L_Toe": "left_ankle_roll_sphere_5_link",
        "R_Toe": "right_ankle_roll_sphere_5_link",
        "L_Wrist": "left_rubber_hand_link",
        "R_Wrist": "right_rubber_hand_link",
    },
    ("smplh", "t1"): {
        "Pelvis": "Trunk",
        "L_Hip": "Hip_Pitch_Left",
        "R_Hip": "Hip_Pitch_Right",
        "L_Knee": "Shank_Left",
        "R_Knee": "Shank_Right",
        "L_Shoulder": "AL1",
        "R_Shoulder": "AR1",
        "L_Elbow": "left_hand_link",
        "R_Elbow": "right_hand_link",
        "L_Ankle": "Ankle_Cross_Left",
        "R_Ankle": "Ankle_Cross_Right",
        "L_Toe": "left_foot_sphere_5_link",
        "R_Toe": "right_foot_sphere_5_link",
        "L_Wrist": "left_hand_sphere_link",
        "R_Wrist": "right_hand_sphere_link",
    },
    ("smplx", "t1"): {
        "Pelvis": "Trunk",
        "L_Hip": "Hip_Pitch_Left",
        "R_Hip": "Hip_Pitch_Right",
        "L_Knee": "Shank_Left",
        "R_Knee": "Shank_Right",
        "L_Shoulder": "AL1",
        "R_Shoulder": "AR1",
        "L_Elbow": "left_hand_link",
        "R_Elbow": "right_hand_link",
        "L_Ankle": "Ankle_Cross_Left",
        "R_Ankle": "Ankle_Cross_Right",
        "L_Foot": "left_foot_sphere_5_link",
        "R_Foot": "right_foot_sphere_5_link",
        "L_Wrist": "left_hand_sphere_link",
        "R_Wrist": "right_hand_sphere_link",
    },
    ("smplx", "g1"): {
        "Pelvis": "pelvis_contour_link",
        "L_Hip": "left_hip_pitch_link",
        "R_Hip": "right_hip_pitch_link",
        "L_Knee": "left_knee_link",
        "R_Knee": "right_knee_link",
        "L_Shoulder": "left_shoulder_roll_link",
        "R_Shoulder": "right_shoulder_roll_link",
        "L_Elbow": "left_elbow_link",
        "R_Elbow": "right_elbow_link",
        "L_Ankle": "left_ankle_intermediate_1_link",
        "R_Ankle": "right_ankle_intermediate_1_link",
        "L_Foot": "left_ankle_roll_sphere_5_link",
        "R_Foot": "right_ankle_roll_sphere_5_link",
        "L_Wrist": "left_rubber_hand_link",
        "R_Wrist": "right_rubber_hand_link",
    },
    ("smplx", "r1"): {
        "Pelvis": "pelvis_link",
        "L_Hip": "left_hip_pitch_link",
        "R_Hip": "right_hip_pitch_link",
        "L_Knee": "left_knee_link",
        "R_Knee": "right_knee_link",
        "L_Shoulder": "left_shoulder_roll_link",
        "R_Shoulder": "right_shoulder_roll_link",
        "L_Elbow": "left_elbow_link",
        "R_Elbow": "right_elbow_link",
        "L_Ankle": "left_ankle_pitch_link",
        "R_Ankle": "right_ankle_pitch_link",
        "L_Foot": "left_ankle_roll_sphere_5_link",
        "R_Foot": "right_ankle_roll_sphere_5_link",
        "L_Wrist": "left_wrist_roll_link",
        "R_Wrist": "right_wrist_roll_link",
    },
    ("lafan", "r1"): {
        "Spine1": "pelvis_link",
        "LeftUpLeg": "left_hip_pitch_link",
        "RightUpLeg": "right_hip_pitch_link",
        "LeftLeg": "left_knee_link",
        "RightLeg": "right_knee_link",
        "LeftArm": "left_shoulder_roll_link",
        "RightArm": "right_shoulder_roll_link",
        "LeftForeArm": "left_elbow_link",
        "RightForeArm": "right_elbow_link",
        "LeftFoot": "left_ankle_pitch_link",
        "RightFoot": "right_ankle_pitch_link",
        "LeftToeBase": "left_ankle_roll_sphere_5_link",
        "RightToeBase": "right_ankle_roll_sphere_5_link",
        "LeftHand": "left_wrist_roll_link",
        "RightHand": "right_wrist_roll_link",
    },
    ("smplx", "h1_2"): {
        "Pelvis": "pelvis",
        "L_Hip": "left_hip_pitch_link",
        "R_Hip": "right_hip_pitch_link",
        "L_Knee": "left_knee_link",
        "R_Knee": "right_knee_link",
        "L_Shoulder": "left_shoulder_roll_link",
        "R_Shoulder": "right_shoulder_roll_link",
        "L_Elbow": "left_elbow_link",
        "R_Elbow": "right_elbow_link",
        "L_Ankle": "left_ankle_pitch_link",
        "R_Ankle": "right_ankle_pitch_link",
        "L_Foot": "left_ankle_roll_sphere_5_link",
        "R_Foot": "right_ankle_roll_sphere_5_link",
        "L_Wrist": "left_wrist_yaw_link",
        "R_Wrist": "right_wrist_yaw_link",
    },
    ("lafan", "h1_2"): {
        "Spine1": "pelvis",
        "LeftUpLeg": "left_hip_pitch_link",
        "RightUpLeg": "right_hip_pitch_link",
        "LeftLeg": "left_knee_link",
        "RightLeg": "right_knee_link",
        "LeftArm": "left_shoulder_roll_link",
        "RightArm": "right_shoulder_roll_link",
        "LeftForeArm": "left_elbow_link",
        "RightForeArm": "right_elbow_link",
        "LeftFoot": "left_ankle_pitch_link",
        "RightFoot": "right_ankle_pitch_link",
        "LeftToeBase": "left_ankle_roll_sphere_5_link",
        "RightToeBase": "right_ankle_roll_sphere_5_link",
        "LeftHand": "left_wrist_yaw_link",
        "RightHand": "right_wrist_yaw_link",
    },
    ("smplx", "k1"): {
        "Pelvis": "Trunk",
        "L_Hip": "Left_Hip_Pitch",
        "R_Hip": "Right_Hip_Pitch",
        "L_Knee": "Left_Shank",
        "R_Knee": "Right_Shank",
        "L_Shoulder": "Left_Arm_3",
        "R_Shoulder": "Right_Arm_3",
        "L_Elbow": "left_hand_link",
        "R_Elbow": "right_hand_link",
        "L_Ankle": "Left_Ankle_Cross",
        "R_Ankle": "Right_Ankle_Cross",
        "L_Foot": "left_foot_sphere_5_link",
        "R_Foot": "right_foot_sphere_5_link",
    },
    ("lafan", "k1"): {
        "Spine1": "Trunk",
        "LeftUpLeg": "Left_Hip_Pitch",
        "RightUpLeg": "Right_Hip_Pitch",
        "LeftLeg": "Left_Shank",
        "RightLeg": "Right_Shank",
        "LeftArm": "Left_Arm_3",
        "RightArm": "Right_Arm_3",
        "LeftForeArm": "left_hand_link",
        "RightForeArm": "right_hand_link",
        "LeftFoot": "Left_Ankle_Cross",
        "RightFoot": "Right_Ankle_Cross",
        "LeftToeBase": "left_foot_sphere_5_link",
        "RightToeBase": "right_foot_sphere_5_link",
    },
    ("seed", "g1"): {
        "Hips": "pelvis_contour_link",
        "Chest": "torso_link",
        "LeftLeg": "left_hip_roll_link",
        "LeftToeBase": "left_ankle_roll_sphere_5_link",
        "LeftShin": "left_knee_link",
        "LeftFoot": "left_ankle_roll_link",
        "LeftArm": "left_shoulder_roll_link",
        "LeftForeArm": "left_elbow_link",
        "LeftHand": "left_wrist_yaw_link",
        "RightLeg": "right_hip_roll_link",
        "RightToeBase": "right_ankle_roll_sphere_5_link",
        "RightShin": "right_knee_link",
        "RightFoot": "right_ankle_roll_link",
        "RightArm": "right_shoulder_roll_link",
        "RightForeArm": "right_elbow_link",
        "RightHand": "right_wrist_yaw_link",
    },
    ("seed", "r1"): {
        "Spine1": "pelvis_link",
        "LeftLeg": "left_hip_pitch_link",
        "LeftShin": "left_knee_link",
        "LeftFoot": "left_ankle_pitch_link",
        "LeftToeBase": "left_ankle_roll_sphere_5_link",
        "LeftArm": "left_shoulder_roll_link",
        "LeftForeArm": "left_elbow_link",
        "LeftHand": "left_wrist_roll_link",
        "RightLeg": "right_hip_pitch_link",
        "RightShin": "right_knee_link",
        "RightFoot": "right_ankle_pitch_link",
        "RightToeBase": "right_ankle_roll_sphere_5_link",
        "RightArm": "right_shoulder_roll_link",
        "RightForeArm": "right_elbow_link",
        "RightHand": "right_wrist_roll_link",
    },
    ("seed", "h1_2"): {
        "Spine1": "pelvis",
        "LeftLeg": "left_hip_pitch_link",
        "LeftShin": "left_knee_link",
        "LeftFoot": "left_ankle_pitch_link",
        "LeftToeBase": "left_ankle_roll_sphere_5_link",
        "LeftArm": "left_shoulder_roll_link",
        "LeftForeArm": "left_elbow_link",
        "LeftHand": "left_wrist_yaw_link",
        "RightLeg": "right_hip_pitch_link",
        "RightShin": "right_knee_link",
        "RightFoot": "right_ankle_pitch_link",
        "RightToeBase": "right_ankle_roll_sphere_5_link",
        "RightArm": "right_shoulder_roll_link",
        "RightForeArm": "right_elbow_link",
        "RightHand": "right_wrist_yaw_link",
    },
    ("seed", "k1"): {
        "Spine1": "Trunk",
        "LeftLeg": "Left_Hip_Pitch",
        "LeftShin": "Left_Shank",
        "LeftFoot": "Left_Ankle_Cross",
        "LeftToeBase": "left_foot_sphere_5_link",
        "LeftArm": "Left_Arm_3",
        "LeftForeArm": "left_hand_link",
        "RightLeg": "Right_Hip_Pitch",
        "RightShin": "Right_Shank",
        "RightFoot": "Right_Ankle_Cross",
        "RightToeBase": "right_foot_sphere_5_link",
        "RightArm": "Right_Arm_3",
        "RightForeArm": "right_hand_link",
    },
    ("mocap", "g1"): {
        "Spine1": "pelvis_contour_link",
        "LeftUpLeg": "left_hip_pitch_link",
        "LeftLeg": "left_knee_link",
        "LeftToeBase": "left_ankle_roll_sphere_5_link",
        "RightUpLeg": "right_hip_pitch_link",
        "RightLeg": "right_knee_link",
        "RightToeBase": "right_ankle_roll_sphere_5_link",
        "LeftArm": "left_shoulder_roll_link",
        "LeftForeArm": "left_elbow_link",
        "LeftHandMiddle3": "left_sphere_hand_link",
        "RightArm": "right_shoulder_roll_link",
        "RightForeArm": "right_elbow_link",
        "RightHandMiddle3": "right_sphere_hand_link",
        "LeftFoot": "left_ankle_intermediate_1_link",
        "RightFoot": "right_ankle_intermediate_1_link",
    },
    ("mocap", "t1"): {
        "Spine1": "Trunk",
        "LeftUpLeg": "Hip_Pitch_Left",
        "LeftLeg": "Shank_Left",
        "LeftToeBase": "left_foot_sphere_5_link",
        "RightUpLeg": "Hip_Pitch_Right",
        "RightLeg": "Shank_Right",
        "RightToeBase": "right_foot_sphere_5_link",
        "LeftArm": "AL1",
        "LeftForeArm": "left_hand_link",
        "LeftHandMiddle3": "left_hand_sphere_link",
        "RightArm": "AR1",
        "RightForeArm": "right_hand_link",
        "RightHandMiddle3": "right_hand_sphere_link",
        "LeftFoot": "Ankle_Cross_Left",
        "RightFoot": "Ankle_Cross_Right",
    },
}

# Data format specific constants
TOE_NAMES_BY_FORMAT = {
    "lafan": ["LeftToeBase", "RightToeBase"],
    "seed": ["LeftToeBase", "RightToeBase"], # Question should we add LeftToeEnd? RightToeEnd too?
    "smplh": ["L_Toe", "R_Toe"],
    "mocap": ["LeftToeBase", "RightToeBase"],
    "smplx": ["L_Foot", "R_Foot"],
}


# Data format specific scaling/preprocessing constants
class FormatConstants(TypedDict, total=False):
    default_scale_factor: float | None
    default_human_height: float | None


DATA_FORMAT_CONSTANTS: dict[str, FormatConstants] = {
    "lafan": {
        "default_scale_factor": 1.27 / 1.7,
    },
    "seed": {
        "default_human_height": 1.70,
    },
    "mocap": {
        "default_human_height": 1.78,
    },
}

# Unified registry: Maps format name to demo joints
# This is the SINGLE PLACE to add new formats - just add an entry here!
# No need to update any Literal types - DataFormat is now str with runtime validation
DEMO_JOINTS_REGISTRY: dict[str, list[str]] = {
    "lafan": LAFAN_DEMO_JOINTS,
    "seed": SEED_DEMO_JOINTS,
    "smplh": SMPLH_DEMO_JOINTS,
    "mocap": MOCAP_DEMO_JOINTS,
    "smplx": SMPLX_DEMO_JOINTS,
}

# Type alias for data formats - use str to allow dynamic data formats via DEMO_JOINTS_REGISTRY
# No need to update this when adding new formats - just add to DEMO_JOINTS_REGISTRY above
DataFormat = str


def _validate_data_format(data_format: str) -> None:
    """Validate that data_format exists in DEMO_JOINTS_REGISTRY."""
    if data_format not in DEMO_JOINTS_REGISTRY:
        available = ", ".join(sorted(DEMO_JOINTS_REGISTRY.keys()))
        raise ValueError(
            f"Invalid data_format: '{data_format}'. "
            f"Available data formats: {available}. "
            f"Add your format to DEMO_JOINTS_REGISTRY in config_types/data_type.py"
        )


@dataclass(frozen=True)
class MotionDataConfig:
    # Use str instead of Literal to allow dynamic data formats via DEMO_JOINTS_REGISTRY
    data_format: str = "smplh"
    # Use str instead of Literal to allow dynamic robot types
    robot_type: str = "g1"
    robot_defaults: dict[str, RobotDefaults] = field(default_factory=_default_robot_defaults)

    def __post_init__(self) -> None:
        """Validate data_format and robot_type."""
        _validate_data_format(self.data_format)

        _validate_robot_type(self.robot_type, self.robot_defaults)

    # Optional overrides - if None, will use defaults from data_format
    demo_joints: list[str] | None = None
    joints_mapping: dict[str, str] | None = None

    @property
    def resolved_demo_joints(self) -> list[str]:
        """Get demo joints - use override if provided, else use data_format default."""
        if self.demo_joints is not None:
            return self.demo_joints

        if self.data_format not in DEMO_JOINTS_REGISTRY:
            raise ValueError(
                f"Unknown data_format: {self.data_format}. "
                f"Available formats: {list(DEMO_JOINTS_REGISTRY.keys())}. "
                f"Add your format to DEMO_JOINTS_REGISTRY in config_types/data_type.py"
            )
        return DEMO_JOINTS_REGISTRY[self.data_format]

    @property
    def resolved_joints_mapping(self) -> dict[str, str]:
        """Get joints mapping - use override if provided, else lookup by (data_format, robot_type)."""
        if self.joints_mapping is not None:
            return self.joints_mapping

        key = (self.data_format, self.robot_type)
        if key in JOINTS_MAPPINGS:
            return JOINTS_MAPPINGS[key]

        raise ValueError(f"No joint mapping found for data_format={self.data_format}, robot_type={self.robot_type}")

    @property
    def toe_names(self) -> list[str]:
        """Get toe joint names for this data format."""
        if self.data_format not in TOE_NAMES_BY_FORMAT:
            raise ValueError(
                f"Toe names not defined for data_format: {self.data_format}. "
                f"Add entry to TOE_NAMES_BY_FORMAT in config_types/data_type.py"
            )
        return TOE_NAMES_BY_FORMAT[self.data_format]

    @property
    def default_scale_factor(self) -> float | None:
        """Get default scale factor for this data format (None if calculated per subject)."""
        format_constants: FormatConstants = DATA_FORMAT_CONSTANTS.get(self.data_format, {})
        return format_constants.get("default_scale_factor")

    @property
    def default_human_height(self) -> float | None:
        """Get default human height for this data format (None if not applicable)."""
        format_constants: FormatConstants = DATA_FORMAT_CONSTANTS.get(self.data_format, {})
        return format_constants.get("default_human_height")

    @property
    def resolved_scale_factor(self) -> float | None:
        """Scale factor for formats that use a fixed default (lafan).

        Robots listed in LAFAN_ROBOT_SCALE_OVERRIDES use a per-robot scale so their feet plant on
        a common ground; all other robots keep the format default unchanged. SEED does not use this
        path -- it scales height-based (ROBOT_HEIGHT / default_human_height) in the loader.
        """
        if self.data_format == "lafan":
            override = LAFAN_ROBOT_SCALE_OVERRIDES.get(self.robot_type)
            if override is not None:
                return override
        return self.default_scale_factor

    def legacy_constants(self) -> dict[str, Any]:
        """Return uppercase legacy constants for backward compatibility."""
        return {
            "DEMO_JOINTS": self.resolved_demo_joints,
            "JOINTS_MAPPING": self.resolved_joints_mapping,
            "TOE_NAMES": self.toe_names,
            "DEFAULT_SCALE_FACTOR": self.default_scale_factor,
            "DEFAULT_HUMAN_HEIGHT": self.default_human_height,
        }
