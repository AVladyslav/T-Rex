class Settings:

    # Frames per seconds
    FPS = 30

    # Sizes
    logo_position = (300, 30)   # x, y
    screen_size = [1500, 500]

    # Positions
    dino_position = {'x': 50, 'y': 480}

    # Colors
    bg_color = (243, 243, 243)

    # Speeds
    cloud_speed = -5
    ground_speed = -15
    dino_jump_velocity = -10
    gravity = 0.9

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
