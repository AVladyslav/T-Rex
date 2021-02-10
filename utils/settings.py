class Settings:

    # Screenshots
    rect_width = 500
    rect_height = 500
    thumb_width = 100
    thumb_height = 100
    tresh_value = 200

    # Rewards
    negative_reward = -10
    positive_reward = 1

    # Number of images in series
    n_in_series = 4

    # Frames per seconds
    FPS = 30

    # Level
    level = 1.5
    max_level = 1.5
    min_level = 1.5

    # Sizes
    logo_position = (300, 30)   # x, y
    screen_size = [1500, 500]

    # Positions
    dino_position = {'x': 50, 'y': 480}
    cactus_min_dist = int(screen_size[0] * 0.4)
    cactus_max_dist = screen_size[0]
    text_position = (1200, 50)

    # Colors
    bg_color = (243, 243, 243)
    text_color = (53, 115, 58)

    # Speeds
    cloud_speed = -5
    ground_speed = -15
    dino_jump_velocity = -10
    gravity = 1.6

    # Scale factors
    cactus_scale = 0
    cloud_scale = 0
    pterosaur_scale = 0
    logo_scale = 0
    score_scale = 0
    dino_scale = 0

    # Path to images
    images_path = 'images'

    # Images names
    cloud_image_name = 'cloud.png'
    game_over_image_name = 'game_over.png'
    ground_image_name = 'ground.png'
    logo_image_name = 'logo.png'

    # Sprite sheets names
    cactus_large_sheet_name = 'cactus-large.png'
    cactus_small_sheet_name = 'cactus-small.png'
    pterosaur_sheet_name = 'pterosaur.png'
    score_sheet_name = 'score.png'
    dino_sheet_name = 'dino.png'
    dino_ducking_sheet_name = 'dino-ducking.png'

    # Sprite sheets number of sheets
    cactus_large_n_of_sprites = 3
    cactus_small_n_of_sprites = 3
    dino_ducking_n_of_sprites = 2
    dino_n_of_sprites = 6
    pterosaur_n_of_sprites = 2
