import subprocess
import logging
import os
import shutil
import ctypes

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
        logging.info(f"Executed: {' '.join(command)}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed: {e}")

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def backup_directories():
    try:
        from config import DIRECTORIES_TO_BACKUP, BACKUP_LOCATION
        if not os.path.exists(BACKUP_LOCATION):
            os.makedirs(BACKUP_LOCATION)
        for directory in DIRECTORIES_TO_BACKUP:
            shutil.copytree(directory, os.path.join(BACKUP_LOCATION, os.path.basename(directory)), dirs_exist_ok=True)
        logging.info("Backup completed successfully")
    except Exception as e:
        logging.error(f"Failed to backup directories: {e}")

def clear_temp_files():
    temp_folders = [os.getenv('TEMP'), os.getenv('TMP'), r'C:\Windows\Temp']
    for folder in temp_folders:
        try:
            for filename in os.listdir(folder):
                file_path = os.path.join(folder, filename)
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            logging.info(f"Cleared {folder}")
        except Exception as e:
            logging.error(f"Failed to clear {folder}: {e}")

def set_high_performance_power_mode():
    run_command(['powercfg', '-setactive', 'SCHEME_MIN'])
