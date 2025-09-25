# Sprite animation frame coordinates
# Each tuple contains (left, bottom, width, height) for each frame
# Animation sheet: 4 rows x 8 columns, each frame is 100x100 pixels

# Individual frame coordinates as tuples (left, bottom, width, height)
Sprite = [
    # Row 0 - Standing/Idle animation
    (0, 302, 100, 100),      # Frame 0
    (100, 302, 100, 100),    # Frame 1
    (200, 302, 100, 100),    # Frame 2
    (300, 302, 100, 100),    # Frame 3
    (400, 302, 100, 100),    # Frame 4
    (500, 302, 100, 100),    # Frame 5
    (600, 302, 100, 100),    # Frame 6
    (700, 302, 100, 100),    # Frame 7

    # Row 1 - Walking animation
    (0, 202, 100, 100),      # Frame 8
    (100, 202, 100, 100),    # Frame 9
    (200, 202, 100, 100),    # Frame 10
    (300, 202, 100, 100),    # Frame 11
    (400, 202, 100, 100),    # Frame 12
    (500, 202, 100, 100),    # Frame 13
    (600, 202, 100, 100),    # Frame 14
    (700, 202, 100, 100),    # Frame 15

    # Row 2 - Running animation
    (0, 102, 100, 100),      # Frame 16
    (100, 102, 100, 100),    # Frame 17
    (200, 102, 100, 100),    # Frame 18
    (300, 102, 100, 100),    # Frame 19
    (400, 102, 100, 100),    # Frame 20
    (500, 102, 100, 100),    # Frame 21
    (600, 102, 100, 100),    # Frame 22
    (700, 102, 100, 100),    # Frame 23

    # Row 3 - Jumping/Action animation
    (0, 2, 100, 100),        # Frame 24
    (100, 2, 100, 100),      # Frame 25
    (200, 2, 100, 100),      # Frame 26
    (300, 2, 100, 100),      # Frame 27
    (400, 2, 100, 100),      # Frame 28
    (500, 2, 100, 100),      # Frame 29
    (600, 2, 100, 100),      # Frame 30
    (700, 2, 100, 100),      # Frame 31
]

# Animation sequences - frame indices for each animation type
IDLE_FRAMES = list(range(0, 8))        # Frames 0-7
WALK_FRAMES = list(range(8, 16))       # Frames 8-15
RUN_FRAMES = list(range(16, 24))       # Frames 16-23
ACTION_FRAMES = list(range(24, 32))    # Frames 24-31

# Animation row definitions
IDLE_ROW = 0
WALK_ROW = 1
RUN_ROW = 2
ACTION_ROW = 3

# Frame dimensions
FRAME_WIDTH = 100
FRAME_HEIGHT = 100
FRAMES_PER_ROW = 8
TOTAL_ROWS = 4
TOTAL_FRAMES = 32

def get_frame(frame_index):
    """
    Get frame coordinates by index
    Returns: (left, bottom, width, height)
    """
    if 0 <= frame_index < len(FRAMES):
        return FRAMES[frame_index]
    return None

def get_row_frames(row_index):
    """
    Get all frames for a specific row
    Returns: list of (left, bottom, width, height) tuples
    """
    start_idx = row_index * FRAMES_PER_ROW
    end_idx = start_idx + FRAMES_PER_ROW
    return FRAMES[start_idx:end_idx]

def get_animation_frames(animation_type):
    """
    Get frames for specific animation type
    animation_type: 'idle', 'walk', 'run', 'action'
    Returns: list of (left, bottom, width, height) tuples
    """
    animation_map = {
        'idle': IDLE_FRAMES,
        'walk': WALK_FRAMES,
        'run': RUN_FRAMES,
        'action': ACTION_FRAMES
    }

    if animation_type in animation_map:
        frame_indices = animation_map[animation_type]
        return [FRAMES[i] for i in frame_indices]
    return []

# Usage examples:
# frame_coords = get_frame(0)  # Get first frame: (0, 302, 100, 100)
# idle_animation = get_animation_frames('idle')  # Get all idle frames
# first_row = get_row_frames(0)  # Get all frames from first row
