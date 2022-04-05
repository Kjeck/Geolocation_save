# -*- coding: utf-8 -*-
# !/usr/bin/python3.10
''' Saves geolocation on the map to html file & creat QR-code '''

__version__ = '1.1'

from termcolor import cprint
from pyfiglet import Figlet
import folium
import os
import colorama
import qrcode

# Enable AHCI support for color text in the console when compiling in win app
colorama.init()


def save_location_qr(lat, lon):
    data = f'https://maps.google.com/local?q={lat},{lon}'
    file_name = f'location_{lat}_{lon}.png'
    img = qrcode.make(data)
    try:
        img.save(file_name)
        cprint('QR-code save to:     ' + file_name, 'yellow')
        print()
    except:
        cprint('\nНе удалось сохранить QR-code\n', 'red')
        print()


def save_location_html(lat, lon):
    try:
        coordinates = (lat, lon)
        file_name = f'location_{lat}_{lon}.html'

        map = folium.Map(location=coordinates, zoom_start=12)
        folium.Marker(location=coordinates,
                      icon=folium.Icon(color='red')).add_to(map)
        map.save(file_name)
        cprint('Geolocation save to: ' + file_name, 'yellow')

        save_location_qr(lat, lon)
        try:
            os.startfile(file_name)
        except:
            pass
    except:
        cprint('\nНе удалось сохранить локацию в файл\n', 'red')


def input_location():
    loop_run = True
    while loop_run:
        cprint('Введите через пробел Широту Долготу (<Q> для выхода)', 'green')
        location = input('> ')
        if location[:1] not in ['Q', 'q', 'Й', 'й']:
            if location.find(' ') > 0:
                try:
                    lat, lon = location.split()
                except:
                    cprint('Не верный ввод координат!', 'red')
                    input_location()

                lat = lat.replace(',', '.')
                lon = lon.replace(',', '.')
                save_location_html(lat, lon)
            else:
                cprint('Введите координаты через пробел!', 'red')
        else:
            loop_run = False


def print_info(type='copyright', font='slant', color='yellow'):

    if type == 'head':
        text = 'SAVE LACATION ON THE MAP'
        f = Figlet(font=font)
        cprint(f.renderText(text), color)
    elif type == 'copyright':
        cprint('\nSee you later ...', color)
        print()
        cprint('© Evgeniy Kotelnikov (Kjeck)  ', 'white', 'on_cyan')
        cprint('  https://github.com/Kjeck    \n', 'white', 'on_cyan')


def main():
    os.system('CLS')
    print_info('head')
    input_location()
    print_info()


if __name__ == '__main__':
    main()
