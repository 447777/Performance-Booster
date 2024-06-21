import os

# Directories to back up
DIRECTORIES_TO_BACKUP = [
    os.path.join(os.getenv("USERPROFILE"), 'Documents'),
    os.path.join(os.getenv("USERPROFILE"), 'Documents', 'Pictures')
]

# Backup location
BACKUP_LOCATION = os.path.join(os.getenv("USERPROFILE"), 'Documents', 'Backup')

# List of unnecessary services to disable
UNNECESSARY_SERVICES = [
    "DiagTrack",
    "WMPNetworkSvc",
    "fax",
    "PhoneSvc",
    "PrintNotify",
]

# Advanced service optimizations
SERVICES_TO_OPTIMIZE = {
    "SysMain": "manual",  # Superfetch
    "Spooler": "manual",  # Print Spooler
    "WSearch": "manual",  # Windows Search
}

# Registry tweaks
REGISTRY_TWEAKS = {
    "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management": {
        "LargeSystemCache": 1,
        "IoPageLockLimit": 2048
    },
    "HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters": {
        "Tcp1323Opts": 1,
        "TCPWindowSize": 131072
    }
}
