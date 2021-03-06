import socket
import cv2
import time
import subprocess
import os

Bash_script_location = os.path.join(os.getcwd(), "flirpi", "single_read.sh")
img_location = "/mnt/ramdisk/temp.png"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
while True:
    start_time = time.time()
    rc = subprocess.call(Bash_script_location, shell=True)
    img = cv2.imread(img_location, -1)
    b = bytearray(img)
    sock.sendto(b, ("192.168.31.255", 5002))
    time.sleep(0.1)
    end_time = time.time()
    # print("Frame sent in %.4f" % (end_time - start_time))
