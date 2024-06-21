import logging
from utils import run_command, clear_temp_files

def defrag_and_optimize():
    try:
        run_command(['defrag', 'C:', '/O'])
        logging.info("Drive defragmented and optimized")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to defragment and optimize drive: {e}")
