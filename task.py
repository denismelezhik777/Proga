import pygame
import pygame as pg
import socket
import struct
import cv2
import numpy as np

UDP_IP = "169.254.76.105"
UDP_PORT = 5000
sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)


class Сommunication:
    def __init__(self):
        pg.font.init()
        pygame.init()
        pygame.display.init()
        pygame.joystick.init()
        pygame.joystick.Joystick(0).init()
        # pygame инициализация модулей
        self.x = 0  # 0
        self.y = 0  # 1
        self.w = 0  # 2
        self.z = 0  # 3
        self.l = 0  # 4

        self.but_1_g2 = False
        self.but_2_g2 = False
        self.but_3_g2 = False
        self.but_4_g2 = False
        self.but_5_g2 = False
        self.but_6_g2 = False

        self.but_1_g1 = False
        self.but_2_g1 = False
        self.but_3_g1 = False
        self.but_4_g1 = False
        self.but_10 = False
        self.but_11 = False
        self.os_data = [self.x, self.y, self.w, self.z, self.l]
        self.rotarycamera = (0, 0)
        self.bool_buttons = [self.but_1_g2, self.but_2_g2, self.but_3_g2,
                             self.but_4_g2, self.but_5_g2, self.but_6_g2,
                             self.but_1_g1, self.but_2_g1, self.but_3_g1,
                             self.but_4_g1, self.but_10, self.but_11]

    def Jostik_info(self):
        #  self.JoyName = pygame.joystick.Joystick(0).get_name()
        # JoyAx = pygame.joystick.Joystick(0).get_numaxes()
        # Joybutton = pygame.joystick.Joystick(0).get_numbuttons()
        # Joynumhats = pygame.joystick.Joystick(0).get_numhats()
        self.w = pygame.joystick.Joystick(0).get_axis(2)
        if self.w == -3.0517578125e-05:
            self.w = 0.0
        self.w = int(self.w * 100)
        if self.w == 99:
            self.w = 100

        self.l = pygame.joystick.Joystick(0).get_axis(4)
        if self.l == -3.0517578125e-05:
            self.l = 0.0
        self.l = int(self.l * 100)
        if self.l == 99:
            self.l = 100

        self.x = pygame.joystick.Joystick(0).get_axis(0)
        if self.x == -3.0517578125e-05:
            self.x = 0.0
        self.x = int(self.x * 100)
        if self.x == 99:
            self.x = 100

        self.y = pygame.joystick.Joystick(0).get_axis(1)
        if self.y == -3.0517578125e-05:
            self.y = 0.0
        self.y = int(self.y * 100)
        if self.y == 99:
            self.y = 100

        self.z = pygame.joystick.Joystick(0).get_axis(3)
        if self.z == -3.0517578125e-05:
            self.z = 0.0
        self.z = int(self.z * 100)
        if self.z == 99:
            self.z = 100

        self.but_1_g2 = bool(pygame.joystick.Joystick(0).get_button(4))
        self.but_2_g2 = bool(pygame.joystick.Joystick(0).get_button(5))
        self.but_3_g2 = bool(pygame.joystick.Joystick(0).get_button(6))
        self.but_4_g2 = bool(pygame.joystick.Joystick(0).get_button(7))
        self.but_5_g2 = bool(pygame.joystick.Joystick(0).get_button(8))
        self.but_6_g2 = bool(pygame.joystick.Joystick(0).get_button(9))
        # !!
        self.but_1_g1 = bool(pygame.joystick.Joystick(0).get_button(0))
        self.but_2_g1 = bool(pygame.joystick.Joystick(0).get_button(1))
        self.but_3_g1 = bool(pygame.joystick.Joystick(0).get_button(2))
        self.but_4_g1 = bool(pygame.joystick.Joystick(0).get_button(3))
        self.rotarycamera = pygame.joystick.Joystick(0).get_hat(0)
        # !!
        self.but_10 = bool(pygame.joystick.Joystick(0).get_button(10))
        self.but_11 = bool(pygame.joystick.Joystick(0).get_button(11))

    def display(self, data):
        size = 1280, 820
        self.win = pg.display.set_mode([1280, 720])
        pg.display.set_caption('Джостик')
        f1 = pygame.font.Font(None, 24)
        pygame.event.pump()
        self.win.fill([255, 255, 255])
        ret, frame = camera.read()
        frame = cv2.resize(frame, size)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = np.rot90(frame)
        frame = pygame.surfarray.make_surface(frame)
        self.win.blit(frame, (0, -100))

        os2_1_g2_text = f1.render(f'ось w: {self.w}', 1, (180, 0, 0))
        os4_ = f1.render(f'ось t: {self.l}', 1, (180, 0, 0))
        but_1_g2_text = f1.render(f'Скорость 1 кнопка: {self.but_1_g2}', 1, (180, 0, 0))
        but_2_g2_text = f1.render(f'Скорость 2 кнопка: {self.but_2_g2}', 1, (180, 0, 0))
        but_3_g2_text = f1.render(f'Скорость 3 кнопка: {self.but_3_g2}', 1, (180, 0, 0))
        but_4_g2_text = f1.render(f'Скорость 4 кнопка: {self.but_4_g2}', 1, (180, 0, 0))
        but_5_g2_text = f1.render(f'Скорость 5 кнопка: {self.but_5_g2}', 1, (180, 0, 0))
        but_6_g2_text = f1.render(f'Скорость 6 кнопка: {self.but_6_g2}', 1, (180, 0, 0))

        os0_g1_text = f1.render(f'x ось: {self.x}', 1, (180, 0, 0))
        os1_g1_text = f1.render(f'y ось: {self.y}', 1, (180, 0, 0))
        os3_g1_text = f1.render(f'z ось: {self.z}', 1, (180, 0, 0))
        but_1_g1_text = f1.render(f'Управление 1 кнопка: {self.but_1_g1}', 1, (180, 0, 0))
        but_2_g1_text = f1.render(f'Управление 2 кнопка: {self.but_2_g1}', 1, (180, 0, 0))
        but_3_g1_text = f1.render(f'Управление 3 кнопка: {self.but_3_g1}', 1, (180, 0, 0))
        but_4_g1_text = f1.render(f'Управление 4 кнопка: {self.but_4_g1}', 1, (180, 0, 0))
        rotarycamera = f1.render(f'rotarycamera: {self.rotarycamera}', 1, (180, 0, 0))

        but_10_text = f1.render(f'Доп. кнопка 1: {self.but_10}', 1, (180, 0, 0))
        but_11_text = f1.render(f'Доп. кнопка 2: {self.but_11}', 1, (180, 0, 0))

        self.win.blit(os2_1_g2_text, (10, 50))
        self.win.blit(os4_, (10, 75))

        self.win.blit(but_1_g2_text, (10, 100))
        self.win.blit(but_2_g2_text, (10, 125))
        self.win.blit(but_3_g2_text, (10, 150))
        self.win.blit(but_4_g2_text, (10, 175))
        self.win.blit(but_5_g2_text, (10, 200))
        self.win.blit(but_6_g2_text, (10, 225))
        # !!
        self.win.blit(os0_g1_text, (300, 50))
        self.win.blit(os1_g1_text, (300, 75))
        self.win.blit(os3_g1_text, (300, 100))

        self.win.blit(but_1_g1_text, (300, 125))
        self.win.blit(but_2_g1_text, (300, 150))
        self.win.blit(but_3_g1_text, (300, 175))
        self.win.blit(but_4_g1_text, (300, 200))
        self.win.blit(rotarycamera, (300, 225))
        # !!
        self.win.blit(but_10_text, (300, 400))
        self.win.blit(but_11_text, (300, 425))

        yaw = f1.render(f'Yaw: {data[0]}', 1, (180, 0, 0))
        self.win.blit(yaw, (600, 100))

        depth = f1.render(f'Depth: {data[1]}', 1, (180, 0, 0))
        self.win.blit(depth, (600, 125))

        roll = f1.render(f'Roll: {data[2]}', 1, (180, 0, 0))
        self.win.blit(roll, (600, 150))

        pitch = f1.render(f'Pitch: {data[3]}', 1, (180, 0, 0))
        self.win.blit(pitch, (600, 175))
        pg.display.update()

    def return_os(self):
        self.os_data = [self.x, self.y, self.w, self.z, self.l]
        return self.os_data

    def return_buttons(self):
        self.bool_buttons = [self.but_1_g2, self.but_2_g2, self.but_3_g2,
                             self.but_4_g2, self.but_5_g2, self.but_6_g2,
                             self.but_1_g1, self.but_2_g1, self.but_3_g1,
                             self.but_4_g1, self.but_10, self.but_11]
        return self.bool_buttons

    def return_rotarycamera(self):
        return self.rotarycamera


class InputPacket:
    def __init__(self):
        # данные храняться в байтовом виде в кучке
        self.W1_data = bytearray()

    # def return_(self):
    #     return self.W1_data

    def input_(self, os_data): # , bool_buttons, rotarycamera
        # self.W1_data = bytearray()
        # for i in os_data:
        #     self.W1_data += struct.pack("b", i)
        #
        # for i in bool_buttons:
        #     self.W1_data += struct.pack("b", i)
        #
        # for i in rotarycamera:
        #     self.W1_data += struct.pack("b", i)
        self.W1_data = struct.pack('>bbbb', os_data[0], os_data[1], os_data[2], os_data[3])
        return self.W1_data


class OutputPacket:
    def __init__(self):
        self.W2_data = []

    def return_(self):
        return self.W2_data

    def input_(self, data_r):
        self.W2_data = struct.unpack('<ffff', data_r)


com = Сommunication()
InPac = InputPacket()
Outpac = OutputPacket()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    com.Jostik_info()
    data, addr = sock.recvfrom(1024)
    Outpac.input_(data)

    sock.connect(addr)
    sock.send(InPac.input_(com.return_os()))

    com.display(Outpac.return_())

