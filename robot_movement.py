import serial
import time

arduino = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)

def move_robot(direction):
    arduino.write(direction.encode())
    time.sleep(1)

while True:
    command = input("Enter movement (forward, backward, left, right, stop, exit): ").strip().lower()
    if command in ["forward", "backward", "left", "right", "stop"]:
        move_robot(command)
    elif command == "exit":
        break