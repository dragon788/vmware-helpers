import os
import string
from ctypes import windll

# This is a simple python script to find and "print" a list of .vmx files
# This can be piped to a text file and then used to manage VMware-kvm commands

#def paths_to_search():
#    paths = []
#    paths.prompt()

# drives = [] # drive letters passed in by the user
# folders = [] # folder names to narrow down the search for VMs eg \Virtual Machines or \VMS
# extensions = [] # virtual machine types to search for, defaults to .vmx/.vdi?

def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives

# gets a list of VMs in the selected path(s)
for letter in get_drives():
    #for root, dirs, files in os.walk(letter + ":\"):
    for root, dirs, files in os.walk(letter + ":\Virtual Machines"):
        for file in files:
            if file.lower().endswith(".vmx"):
                print os.path.join(root, file)

# this section will either built .bat files or present options in a GUI for vmware-kvm.exe
"""
for vm in vms:
    #TODO Build out logic for finding VMware Workstation executable.
    print (/OS/Path/To/VMware/Workstation/vmware-kvm.exe + " " + vm)

    """