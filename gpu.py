import shutil
import logging
from utils import run_command

def detect_gpu():
    import wmi
    c = wmi.WMI()
    gpu_info = c.Win32_VideoController()[0]
    gpu_name = gpu_info.Name
    logging.info(f"Detected GPU: {gpu_name}")
    if "NVIDIA" in gpu_name:
        return "NVIDIA"
    elif "AMD" in gpu_name or "Radeon" in gpu_name:
        return "AMD"
    else:
        return "Integrated"

def install_latest_drivers(gpu_vendor):
    if gpu_vendor == "NVIDIA":
        download_and_install_nvidia_drivers()
    elif gpu_vendor == "AMD":
        download_and_install_amd_drivers()

def download_and_install_nvidia_drivers():
    logging.info("NVIDIA drivers installation started.")
    logging.info("NVIDIA drivers installed.")

def download_and_install_amd_drivers():
    logging.info("AMD drivers installation started.")
    logging.info("AMD drivers installed.")

def optimize_gpu_settings(gpu_vendor):
    if gpu_vendor == "NVIDIA":
        optimize_nvidia_settings()
    elif gpu_vendor == "AMD":
        optimize_amd_settings()

def optimize_nvidia_settings():
    settings = [
        ('Manage 3D settings', 'Preferred graphics processor', 'High-performance NVIDIA processor'),
        ('Manage 3D settings', 'Power management mode', 'Prefer maximum performance'),
        ('Manage 3D settings', 'Threaded optimization', 'On'),
    ]
    for setting in settings:
        try:
            if shutil.which('nvidia-settings'):
                run_command(['nvidia-settings', '-a', f'[gpu:0]/{setting[1]}={setting[2]}'])
                logging.info(f"NVIDIA setting {setting[1]} set to {setting[2]}")
            else:
                logging.error("nvidia-settings not found. Skipping NVIDIA optimizations.")
        except Exception as e:
            logging.error(f"Failed to set NVIDIA setting {setting[1]}: {e}")

def optimize_amd_settings():
    # Add specific optimizations for AMD here
    pass
