import socket
import time
import PiMotor
import RPi.GPIO as GPIO

if __name__ == '__main__':

    pravyMotor = PiMotor.Motor("MOTOR1", 1)
    levyMotor = PiMotor.Motor("MOTOR2", 1)
    sipkaVzad = PiMotor.Arrow(1)
    sipkaVlevo = PiMotor.Arrow(2)
    sipkaVpred = PiMotor.Arrow(3)
    sipkaVpravo = PiMotor.Arrow(4)
    obaMotory = PiMotor.LinkedMotors(pravyMotor, levyMotor)
    ipina = "10.42.0.1"
    port = 5005

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ipina, port))

    while True:
        data, addr = sock.recvfrom(1024)
        print(f"received message: {data}")

        if data == b"w":
            print("Vpřed")
            sipkaVpred.on()
            sipkaVzad.off()
            sipkaVlevo.off()
            sipkaVpravo.off()
            obaMotory.forward(100)
            time.sleep(0.1)
            obaMotory.stop()
            sipkaVpred.off()
        elif data == b"a":
            print("otoc vlevo")
            sipkaVpred.off()
            sipkaVzad.off()
            sipkaVlevo.on()
            sipkaVpravo.off()
            levyMotor.forward(100)
            pravyMotor.reverse(100)
            time.sleep(0.1)
            levyMotor.stop()
            pravyMotor.stop()
            sipkaVlevo.off()
        elif data == b"s":
            print("Vzad")
            sipkaVpred.off()
            sipkaVzad.on()
            sipkaVlevo.off()
            sipkaVpravo.off()
            obaMotory.reverse(100)
            time.sleep(0.1)
            obaMotory.stop()
            sipkaVzad.off()
        elif data == b"d":
            print("otoc vpravo")
            sipkaVpred.off()
            sipkaVzad.off()
            sipkaVlevo.off()
            sipkaVpravo.on()
            levyMotor.reverse(100)
            pravyMotor.forward(100)
            time.sleep(0.1)
            levyMotor.stop()
            pravyMotor.stop()
            sipkaVpravo.off()

        elif data == b"q":
            print("Vpred vlevo")
            sipkaVpred.on()
            sipkaVzad.off()
            sipkaVlevo.on()
            sipkaVpravo.off()
            levyMotor.forward(50)
            pravyMotor.forward(100)
            time.sleep(0.1)
            levyMotor.stop()
            pravyMotor.stop()
            sipkaVlevo.off()
            sipkaVpred.off()

        elif data == b"e":
            print("Vpred vpravo")
            sipkaVpred.on()
            sipkaVzad.off()
            sipkaVlevo.off()
            sipkaVpravo.on()
            levyMotor.reverse(100)
            pravyMotor.forward(50)
            time.sleep(0.1)
            levyMotor.stop()
            pravyMotor.stop()
            sipkaVpravo.off()
            sipkaVpred.off()
