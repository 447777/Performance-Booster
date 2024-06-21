import os


DIRECTORIES_TO_BACKUP = [
    os.path.join(os.getenv("USERPROFILE"), 'Documents'),
    os.path.join(os.getenv("USERPROFILE"), 'Documents', 'Pictures')
]


BACKUP_LOCATION = os.path.join(os.getenv("USERPROFILE"), 'Documents', 'Backup')


UNNECESSARY_SERVICES = [
    "DiagTrack",
    "WMPNetworkSvc",
    "fax",
    "PhoneSvc",
    "PrintNotify",
]


SERVICES_TO_OPTIMIZE = {
    "SysMain": "manual",  
    "Spooler": "manual",  
    "WSearch": "manual",  
}


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
