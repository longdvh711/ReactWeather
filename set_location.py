import sys
import telnetlib
import time

HOST = "127.0.0.1"

print("\nSet location for emulator")
auth = raw_input("emulator auth:")
longitude = raw_input("longitude: ")
latitude = raw_input("latitude: ")

tn = telnetlib.Telnet(HOST,5554)
tn.read_until("OK")
tn.write("auth \n" + auth)

while True:
 tn.write("geo fix "+ longitude + " " + latitude +"\n") # GOOG HQ SYD
 time.sleep(1)

tn.close()