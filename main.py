import serial
import time
import os
import subprocess

vm = 'Win10_Gaming'
sp_num = subprocess.run(['virsh', 'ttyconsole', vm], stdout=subprocess.PIPE).stdout.decode().strip()
sp = serial.Serial(sp_num, 9600, timeout=1)

try:
    while True:
        data = sp.readline().decode('utf-8').strip()

        if data == 'shutdown':
            subprocess.run(['virsh', 'shutdown', vm, '--mode', 'acpi'])
            os.system('shutdown -P 1')    
            
        time.sleep(0.5)

except serial.SerialException:
    exit()