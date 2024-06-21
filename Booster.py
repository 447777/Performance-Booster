import logging
import ctypes
from restore import create_restore_point, backup_data, backup_directories
from services import disable_unnecessary_services
from startup import disable_startup_programs
from gpu import optimize_gpu_settings, detect_gpu, install_latest_drivers
from registry import registry_tweaks
from filesystem import clear_temp_files, defrag_and_optimize
from utils import is_admin, set_high_performance_power_mode

logging.basicConfig(filename='roblox_booster.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

def main():
    if not is_admin():
        logging.error("Please run the script as an administrator.")
        return

    logging.info("Starting advanced optimizations...")
    create_restore_point()
    backup_data()
    backup_directories()
    set_high_performance_power_mode()
    clear_temp_files()
    disable_unnecessary_services()
    gpu_vendor = detect_gpu()
    install_latest_drivers(gpu_vendor)
    optimize_gpu_settings(gpu_vendor)
    registry_tweaks()
    defrag_and_optimize()
    disable_startup_programs()
    logging.info("Advanced optimizations completed")

if __name__ == "__main__":
    main()
