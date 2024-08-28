from pathlib import Path


class Configuration:
    tile_gen_dir = Path('/data/ofm/tile_gen')

    tile_gen_bin = tile_gen_dir / 'bin'
    tile_gen_scripts_dir = tile_gen_bin / 'scripts'

    planetiler_bin = tile_gen_dir / 'planetiler'
    planetiler_path = planetiler_bin / 'planetiler.jar'

    runs_dir = tile_gen_dir / 'runs'

    rclone_config = Path('/data/ofm/config/rclone.conf')

    areas = ['planet', 'monaco']


config = Configuration()