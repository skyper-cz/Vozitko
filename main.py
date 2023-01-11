import socket
import PiMotor
import time
import RPi.GPIO as GPIO

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    pravyMotor = PiMotor.Motor("MOTOR1", 1)
    levyMotor = PiMotor.Motor("MOTOR2", 1)
    obaMotory = PiMotor.LinkedMotors(pravyMotor, levyMotor)
    ipina = "127.0.0.1"
    port = 5005

    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    sock.bind((ipina, port))

    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        print("received message: %s" % data)

        if data == "w":
            print("Vpřed")
            obaMotory.forward(100)
        elif data == "a":
            print("otoc vlevo")
            levyMotor.reverse(100)
            pravyMotor.forward(100)
        elif data == "s":
            print("Vzad")
            obaMotory.reverse(100)
        elif data == "d":
            print("otoc vpravo")
            levyMotor.forward(100)
            pravyMotor.revrese(100)
