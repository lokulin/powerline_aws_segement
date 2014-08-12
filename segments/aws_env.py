import os

def add_virtual_env_segment():
    env = os.getenv('AWS_ROLE')
    if env is None:
        return

    env_name = os.path.basename(env)

    env_color_key = env_name.split("-")[1]

    bgcolors = {
        'Prod': Color.AWS_ENV_BG_PROD,
	'Staging': Color.AWS_ENV_BG_STAGING,
        'Dev': Color.AWS_ENV_BG_DEV
    }

    fgcolors = {
        'Prod': Color.AWS_ENV_FG_PROD,
	'Staging': Color.AWS_ENV_FG_STAGING,
        'Dev': Color.AWS_ENV_FG_DEV
    }

    bg = bgcolors[env_color_key]
    fg = fgcolors[env_color_key]
    powerline.append(' %s ' % env_name, fg, bg)

add_virtual_env_segment()
