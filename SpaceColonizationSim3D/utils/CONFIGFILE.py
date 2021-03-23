# [General configuration]
# Default values thickness_v-hague(0.2-0.4), thickness_normal(1)
ADD_THICKNESS_VALUE = 0.3
# Default value 200, should be a int
AMOUNT_OF_LEAVES = 500
# Default value 360-1080
POINTS_PER_SPHERE = 720
# Default value 100-500 (higher size == longer generation, and more branches)
TREE_SIZE = 350
# Default value 1
AMOUNT_OF_TREES = 10
# Default value = 400
MIN_DIST = 200  # 20 ** 2, minimal distance is squared to remove a slow square root
# Default value 2500
MAX_DIST = 2500  # 50 ** 2, maximal distance is squared to remove a slow square root
# Default value 2
SECTION_LENGTH = 2  # 2.0
# Default value 0.5
THRESHOLD = 0.75
# Default value 1, never 0. The higher the value the smaller the branches.
SPHERE_RADIUS_DIVISOR = 2

# [Center point configuration]
# Default values Normal tree (x, y ,z) (200, 0, 200)
# Default values V-hague tree (x, y ,z) (50, 0, 38)
CENTER_X = 50
CENTER_Y = 0
CENTER_Z = 38
# Default value 0, this value makes the leader off center.
CENTER_DEVIATION = 5

# [Tree species configuration]
# 0: NORMAL TREE
# 1: V-HAGUE
KIND_OF_TREE = 1

# [Normal tree configuration]
# Default values x(50, 450), y(200, 500), z(50, 450)
# Default value x(50, 450)
NORMAL_X_LOW = 50
NORMAL_X_HIGH = 450
# Default value y(200, 500)
NORMAL_Y_LOW = 75
NORMAL_Y_HIGH = 300
# Default value z(50, 450)
NORMAL_Z_LOW = 50
NORMAL_Z_HIGH = 450

# [V-hague configuration]
# Default values x1(0, 40), y1(50, 200), z1(0, 75)
# Default values x1(0, 40)
V_HAGUE_X_1_LOW = 0
V_HAGUE_X_1_HIGH = 40
# Default values y1(50, 200)
V_HAGUE_Y_1_LOW = 35
V_HAGUE_Y_1_HIGH = 100
# Default values z1(0, 75)
V_HAGUE_Z_1_LOW = 0
V_HAGUE_Z_1_HIGH = 75

# Default values x2(60, 100), y2(30, 200), z2(0, 75)
# Default values x2(60, 100)
V_HAGUE_X_2_LOW = 60
V_HAGUE_X_2_HIGH = 100
# Default values y2(30, 200)
V_HAGUE_Y_2_LOW = 25
V_HAGUE_Y_2_HIGH = 100
# Default values z2(0, 75)
V_HAGUE_Z_2_LOW = 0
V_HAGUE_Z_2_HIGH = 75
