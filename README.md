# Host Shutdown From Guest
This repo consists of a Python script, systemd service unit file and required lines to place in the qemu hook file. Combined, they allow me to trigger the shut down of my Linux (Arch OS) host when I shut down my (KVM) guest Windows VM.

Important: The VM will need to be configured with a virtual serial port.

Usage:-

- Correctly set the "vm" variable names to your target virtual machine's name in ./main.py and ./Lines to add to qemu hook file.txt
- (optional but recommended) Create a virtual environment for the python script, and install pyserial with pip. If you're not using a virtual environment then just install pyserial globally with either your package manager or pip
- Place the .venv folder (if you have created one) and ./main.py in /opt/host-shutdown-watcher
- Place ./systemd service/host-shutdown-watcher.service in /etc/systemd/system (you'll need to modify this unit file if you're not using a venv)
- Add the contents of ./Lines to add to qemu hook file.txt into the /etc/libvirt/hooks/qemu hook file
- In the terminal run "sudo systemctl daemon-reload"

From within Windows (and I guess any other OS to be honest, just my use case is Windows) you can trigger the VM and Host shutdown by sending the string "shutdown" to the appropriate serial port. e.g for Windows, the command "echo shutdown > <Serial Port Number, e.g. COM1>" does the job. The guest OS will then shut down and the host OS will shut down and power off around a minute later.

This repo isn't intended to be of any use to anyone else, it works for my purposes and is just a place for me to store the script for future reference. However if you do find any of it useful feel free to take the code and make it fit for your purposes. If want to improve on it I'm happy to help and will consider any suggestions/pull requests.
