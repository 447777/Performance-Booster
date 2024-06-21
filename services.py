import logging
from utils import run_command
from config import UNNECESSARY_SERVICES, SERVICES_TO_OPTIMIZE

def disable_unnecessary_services():
    for service in UNNECESSARY_SERVICES:
        run_command(['sc', 'config', service, 'start=disabled'])
        logging.info(f"Disabled service: {service}")

def optimize_services():
    for service, start_type in SERVICES_TO_OPTIMIZE.items():
        run_command(['sc', 'config', service, f'start={start_type}'])
        logging.info(f"Set {service} to start type: {start_type}")
