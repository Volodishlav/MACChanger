#!/usr/bin/env python3

import time, os

# MACChanger
print("[1] Enter Repeater")
print("[2] Time Repeater")
print("Select option:")
OPTION = input("")

print("[1] Specific MAC")
print("[2] Random MAC")
print("Select option:")
MACTYPE = input("")

# Specific MAC
if MACTYPE == "1":
	print("Enter MAC:")
	MAC = input("")
	print("Enter interface:")
	I = input("")

	# Enter repeater
	if OPTION == "1":
		while True:
			input("Enter")
			os.system("ip link set dev " + I + " down")
			os.system("macchanger -m " + MAC + " " + I)
			os.system("ip link set dev " + I + " up")

	# Time repeater
	elif OPTION == "2":
		print("Enter TTR in seconds:")
		TTR = int(input(""))

		while True:
			os.system("ip link set dev " + I + " down")
			os.system("macchanger -m " + MAC + " " + I)
			os.system("ip link set dev " + I + " up")
			time.sleep(TTR)

# Random MAC
elif MACTYPE == "2":

	print("Enter interface:")
	I = input("")

	# Enter repeater
	if OPTION == "1":
		while True:
			input("Enter")
			os.system("ip link set dev " + I + " down")
			os.system("macchanger -r " + I)
			os.system("ip link set dev " + I + " up")

	# Time repeater
	elif OPTION == "2":
		print("Enter TTR in seconds:")
		TTR = int(input(""))

		while True:
			os.system("ip link set dev " + I + " down")
			os.system("macchanger -r " + I)
			os.system("ip link set dev " + I + " up")
			time.sleep(TTR)
