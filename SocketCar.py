import socket
import subprocess
from threading import Thread, Event
import os
import signal
import time
#import psutil
import RPi.GPIO as GPIO

class KlientRPI:
    '''Весь набор функционала'''
    def __init__(self):
        self.PIN_IN_1_A = 4  # pin11
        self.PIN_IN_2_A = 17  # pin12
        self.PIN_EN_A = 23  # pin13

        self.PIN_IN_1_B = 27  # pin11
        self.PIN_IN_2_B = 22  # pin12
        self.PIN_EN_B = 24  # pin13

    def Swith(self, message):
        print("command: ", message)
        if message == b"run_up":
            self.run_up()

        if message == b"run_rigth":
            self.run_rigth()
        if message == b"run_left":
            self.run_left()
        if message == b"run_back":
            self.run_back()

        self.run_up(0)

    def run_up(self, spead=50):
        print("run_up")
        pwm[0].ChangeDutyCycle(spead)
        pwm[1].ChangeDutyCycle(spead)

        GPIO.output(self.PIN_IN_1_A, GPIO.HIGH)  # clockwise
        GPIO.output(self.PIN_IN_2_A, GPIO.LOW)

        GPIO.output(self.PIN_IN_1_B, GPIO.HIGH)  # clockwise
        GPIO.output(self.PIN_IN_2_B, GPIO.LOW)
        time.sleep(5)
        pass

    def run_rigth(self, spead_A=50, spead_B=50):
        pwm[0].ChangeDutyCycle(spead_A)
        pwm[1].ChangeDutyCycle(spead_B)

        GPIO.output(self.PIN_IN_1_A, GPIO.HIGH)  # clockwise
        GPIO.output(self.PIN_IN_2_A, GPIO.LOW)

        GPIO.output(self.PIN_IN_1_B, GPIO.LOW)  # clockwise
        GPIO.output(self.PIN_IN_2_B, GPIO.HIGH)
        time.sleep(5)
        print("run_rigth")

    def run_left(self, spead_A=50, spead_B=50):
        pwm[0].ChangeDutyCycle(spead_A)
        pwm[1].ChangeDutyCycle(spead_B)

        GPIO.output(self.PIN_IN_1_A, GPIO.LOW)  # clockwise
        GPIO.output(self.PIN_IN_2_A, GPIO.HIGH)

        GPIO.output(self.PIN_IN_1_B, GPIO.HIGH)  # clockwise
        GPIO.output(self.PIN_IN_2_B, GPIO.LOW)
        time.sleep(5)
        print("run_left")

    def run_back(self, spead=50):
        pwm[0].ChangeDutyCycle(spead)
        pwm[1].ChangeDutyCycle(spead)

        GPIO.output(self.PIN_IN_1_A, GPIO.LOW)  # clockwise
        GPIO.output(self.PIN_IN_2_A, GPIO.HIGH)

        GPIO.output(self.PIN_IN_1_B, GPIO.LOW)  # clockwise
        GPIO.output(self.PIN_IN_2_B, GPIO.HIGH)
        time.sleep(5)
        print("run_back")

    def test(self):
            self.run_up()
            self.run_back()
            self.run_rigth()
            self.run_left()


    def setup(self):
        GPIO.setmode(GPIO.BCM)  # Numbers GPIOs by physical location
        # GPIO.setwarnings(False)

        GPIO.setup(self.PIN_IN_1_A, GPIO.OUT)  # mode --- output motor A
        GPIO.setup(self.PIN_IN_2_A, GPIO.OUT)
        GPIO.setup(self.PIN_EN_A, GPIO.OUT)

        GPIO.setup(self.PIN_IN_1_B, GPIO.OUT)  # mode --- output motor B
        GPIO.setup(self.PIN_IN_2_B, GPIO.OUT)
        GPIO.setup(self.PIN_EN_B, GPIO.OUT)

        self.pwm_A = GPIO.PWM(self.PIN_EN_A, 10)
        self.pwm_A.start(0)

        self.pwm_B = GPIO.PWM(self.PIN_EN_B, 10)
        self.pwm_B.start(0)

        return (self.pwm_A, self.pwm_B)

    def loop(self):
        i = 10
        while True:
            print
            'Press Ctrl+C to end the program...'

            print("i= ", i)

            pwm[0].ChangeDutyCycle(i)
            pwm[1].ChangeDutyCycle(i)
            GPIO.output(self.PIN_IN_1_A, GPIO.HIGH)  # clockwise
            GPIO.output(self.PIN_IN_2_A, GPIO.LOW)
            time.sleep(5)
            i = i + 10

            if i == 100:
                break

    def destroy(self, pwm):
        GPIO.output(self.PIN_EN_A, GPIO.LOW)  # motor stop
        GPIO.output(self.PIN_EN_B, GPIO.LOW)

        pwm[0].stop()
        pwm[1].stop()

        GPIO.cleanup()  # Release resource

class klient(Thread, KlientRPI):  #Класс поток
    def __init__(self, sock, eventStop):

        Thread.__init__(self)

        self.PIN_IN_1_A = 4  # pin11
        self.PIN_IN_2_A = 17  # pin12
        self.PIN_EN_A = 23  # pin13

        self.PIN_IN_1_B = 27  # pin11
        self.PIN_IN_2_B = 22  # pin12
        self.PIN_EN_B = 24  # pin13


        self.sock = sock  # Глобализация переменной
        self.eventStop = eventStop  # Глобализация переменной

    def run(self):  # Запуск и остановка потока
        print("___________________Start potok___________________")
        while True:  #self.eventStop.is_set()
            data = sock.recv(1024)
            self.Swith(data)
            # print("da", data)
            # if not data:
            #     continue

        #print("___________________Stop potok___________________")



if __name__ == '__main__':
    KlientRPI = KlientRPI()
    pwm = KlientRPI.setup()
    sock = socket.socket()  #Создаём сокет
    eventStop = Event()  #Создаём логические сигналы
    eventStop.set()  #True

    objKlient = klient(sock, eventStop)  # Создаём объект класса и передаём ему аргументы(текущие соединение и сигнал на остановку)
    objKlient.start()  # Запускаем поток
    #KlientRPI.test()
    try:
        while True:
            #try:
                try:
                    print("Повтор подключения")
                    sock.connect(('192.168.1.100', 9090))  #Подключаемся к главному компу
                    print('try connect')
                except TimeoutError as e:  #Отлавливаем временную ошибку
                    sock = socket.socket()  #Создаём сокет
                    print("error " + str(e))
                    if "objKlient" in locals():  #Проверяем есть ли переменная objKlient
                        eventStop.clear()  #False
                    else:
                        print("objKlient - нет такой переменной")
                #else:
                    #eventStop.set()  # True

                    #objKlient.join()  #Ждёт пока закончится поток(чтобы не перескакивал на след строчку
            # except BaseException as be:  ##Отлавливаем базовую ошибку
            #     sock = socket.socket()  #Создаём сокет
            #     print("error BE: " + str(be))
            #     if "objKlient" in locals():  #Проверяем есть ли переменная objKlient
            #         eventStop.clear()  #False
            #     else:
            #         print("objKlient - нет такой переменной")
            # else:
            #     pass
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        KlientRPI.destroy(pwm)