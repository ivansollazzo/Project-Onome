import os
import serial
import time

arduinoSerialData = serial.Serial('/dev/ttyACM0',9600)

print "[Onome] Starting script for system restart..."
print "[Onome] Creating output file for system restart script..."
os.system("touch /var/www/html/OnomeWeb/resources/data/tmp/sys_restart_log")
time.sleep(0.5)
os.system("sudo echo Stopping\ all\ services > /var/www/html/OnomeWeb/resources/data/tmp/sys_restart_log")
time.sleep(0.5)
os.system("sudo pkill -f RFIDRead.py")
os.system("sudo pkill -f rpscheck.py")
os.system("sudo pkill -f sys_monitor.py")
time.sleep(0.5)
os.system("sudo echo Triggering\ microcontroller\ for\ acoustic\ signal > /var/www/html/OnomeWeb/resources/data/tmp/sys_restart_log")
time.sleep(0.5)
arduinoSerialData.write('S')
time.sleep(0.2)
os.system("sudo echo Restarting\ system > /var/www/html/OnomeWeb/resources/data/tmp/sys_restart_log")
time.sleep(0.5)
os.system("sudo reboot")