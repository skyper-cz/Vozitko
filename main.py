import socket
import time
import PiMotor
import RPi.GPIO as GPIO

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    pravyMotor = PiMotor.Motor("MOTOR1", 1)
    levyMotor = PiMotor.Motor("MOTOR2", 1)
    sipkaVzad = PiMotor.Arrow(1)
    sipkaVlevo = PiMotor.Arrow(2)
    sipkaVpred = PiMotor.Arrow(3)
    sipkaVpravo = PiMotor.Arrow(4)
    obaMotory = PiMotor.LinkedMotors(pravyMotor, levyMotor)
    ipina = "10.20.13.91"
    port = 5005

    sock = socket.socket(socket.AF_INET,  # Internet
                         socket.SOCK_DGRAM)  # UDP
    sock.bind((ipina, port))

    while True:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        print("received message: %s" % data)
        data = data[1:].strip(b'\x00')

        pokyn = data.decode('UTF-8')

        if pokyn == 'w':
            print("Vpřed")
            sipkaVpred.on()
            sipkaVzad.off()
            sipkaVlevo.off()
            sipkaVpravo.off()
            obaMotory.forward(100)
            time.sleep(0.5)
            obaMotory.stop()
            sipkaVpred.off()
        elif pokyn == 'a':
            print("otoc vlevo")
            sipkaVpred.off()
            sipkaVzad.off()
            sipkaVlevo.on()
            sipkaVpravo.off()
            levyMotor.reverse(100)
            pravyMotor.forward(100)
            time.sleep(0.5)
            levyMotor.stop()
            pravyMotor.stop()
            sipkaVlevo.off()
        elif pokyn == 's':
            print("Vzad")
            sipkaVpred.off()
            sipkaVzad.on()
            sipkaVlevo.off()
            sipkaVpravo.off()
            obaMotory.reverse(100)
            time.sleep(0.5)
            obaMotory.stop()
            sipkaVzad.off()
        elif pokyn == 'd':
            print("otoc vpravo")
            sipkaVpred.off()
            sipkaVzad.off()
            sipkaVlevo.off()
            sipkaVpravo.on()
            levyMotor.forward(100)
            pravyMotor.reverse(100)
            time.sleep(0.5)
            levyMotor.stop()
            pravyMotor.stop()
            sipkaVpravo.off()
