import logging
from utils import run_command, backup_directories
from config import DIRECTORIES_TO_BACKUP, BACKUP_LOCATION

def create_restore_point():
    try:
        run_command(['powershell', '-Command', 'Checkpoint-Computer -Description "BeforeOptimizations" -RestorePointType "Modify_Settings"'])
        logging.info("System restore point created")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to create system restore point: {e}")

def backup_data():
    logging.info("Please ensure all important data is backed up to an external drive or cloud storage.")
