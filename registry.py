import logging
from utils import run_command
from config import REGISTRY_TWEAKS

def registry_tweaks():
    for key, values in REGISTRY_TWEAKS.items():
        for value_name, value_data in values.items():
            run_command(['reg', 'add', key, '/v', value_name, '/t', 'REG_DWORD', '/d', str(value_data), '/f'])
            logging.info(f"Set {value_name} to {value_data} in {key}")
