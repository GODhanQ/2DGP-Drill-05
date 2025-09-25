# Sprite animation frame coordinates
# Each tuple contains (left, bottom, width, height) for each frame
# Animation sheet: 4 rows x 8 columns, each frame is 100x100 pixels
# Structure: Sprite[action][frame][info] where info is (left, bottom, width, height)

Sprite = [
    # Action 0 - Right Idle animation
    (
        (0, 302, 100, 100),      # Frame 0
        (100, 302, 100, 100),    # Frame 1
        (200, 302, 100, 100),    # Frame 2
        (300, 302, 100, 100),    # Frame 3
        (400, 302, 100, 100),    # Frame 4
        (500, 302, 100, 100),    # Frame 5
        (600, 302, 100, 100),    # Frame 6
        (700, 302, 100, 100)     # Frame 7
    ),

    # Action 1 - Right Walk animation
    (
        (0, 202, 100, 100),      # Frame 0
        (100, 202, 100, 100),    # Frame 1
        (200, 202, 100, 100),    # Frame 2
        (300, 202, 100, 100),    # Frame 3
        (400, 202, 100, 100),    # Frame 4
        (500, 202, 100, 100),    # Frame 5
        (600, 202, 100, 100),    # Frame 6
        (700, 202, 100, 100)     # Frame 7
    ),

    # Action 2 - Right Run animation
    (
        (0, 102, 100, 100),      # Frame 0
        (100, 102, 100, 100),    # Frame 1
        (200, 102, 100, 100),    # Frame 2
        (300, 102, 100, 100),    # Frame 3
        (400, 102, 100, 100),    # Frame 4
        (500, 102, 100, 100),    # Frame 5
        (600, 102, 100, 100),    # Frame 6
        (700, 102, 100, 100)     # Frame 7
    ),

    # Action 3 - Right Jump/Action animation
    (
        (0, 2, 100, 100),        # Frame 0
        (100, 2, 100, 100),      # Frame 1
        (200, 2, 100, 100),      # Frame 2
        (300, 2, 100, 100),      # Frame 3
        (400, 2, 100, 100),      # Frame 4
        (500, 2, 100, 100),      # Frame 5
        (600, 2, 100, 100),      # Frame 6
        (700, 2, 100, 100)       # Frame 7
    )
]

# Action indices for easy access
RIGHT_IDLE = 0
LEFT_IDLE = 1
RIGHT_RUN = 2
LEFT_RUN = 3

# Frame dimensions
FRAME_WIDTH = 100
FRAME_HEIGHT = 100
FRAMES_PER_ACTION = 8
TOTAL_ACTIONS = 4
TOTAL_FRAMES = 32

def get_sprite_frame(action, frame_index):
    """
    Get specific frame coordinates from action and frame index
    Args:
        action: Action index (0=idle, 1=walk, 2=run, 3=action)
        frame_index: Frame index within the action (0-7)
    Returns: (left, bottom, width, height) tuple
    """
    if 0 <= action < len(Sprite) and 0 <= frame_index < len(Sprite[action]):
        return Sprite[action][frame_index]
    return None

def get_action_frames(action):
    """
    Get all frames for a specific action
    Args:
        action: Action index (0=idle, 1=walk, 2=run, 3=action)
    Returns: tuple of (left, bottom, width, height) tuples
    """
    if 0 <= action < len(Sprite):
        return Sprite[action]
    return ()

def get_action_by_name(action_name):
    """
    Get action index by name
    Args:
        action_name: 'idle', 'walk', 'run', 'action'
    Returns: Action index or None
    """
    action_map = {
        'idle': RIGHT_IDLE,
        'walk': LEFT_IDLE,
        'run': RIGHT_RUN,
        'action': LEFT_RUN
    }
    return action_map.get(action_name.lower())

# Usage examples with new 3D tuple structure:
# Get idle animation frame 0: Sprite[RIGHT_IDLE][0] → (0, 302, 100, 100)
# Get walk animation frame 3: Sprite[RIGHT_WALK][3] → (300, 202, 100, 100)
# Get all idle frames: Sprite[RIGHT_IDLE] → tuple of 8 frames
#
# Using helper functions:
# frame_coords = get_sprite_frame(RIGHT_IDLE, 0)  # Get idle frame 0
# all_walk_frames = get_action_frames(RIGHT_WALK)  # Get all walk frames
# action_idx = get_action_by_name('run')  # Get run action index (2)
