#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 16:19:24 2023

@author: marysia
"""

# define size

app_size = (400,700)
main_rows = 7
main_columns = 4

# Define text
FONT = 'Calibri'
output_font_size = 70
normal_font_size = 32

styling = {'gap' : 0.5, 
           'corner-radius' : 0}

num_position = {
    '.' : {'col' : 2, 'row' : 6, 'span' : 1},
    '0' : {'col' : 0, 'row' : 6, 'span' : 1},
    '1' : {'col' : 0, 'row' : 5, 'span' : 1},
    '2' : {'col' : 1, 'row' : 5, 'span' : 1},
    '3' : {'col' : 2, 'row' : 5, 'span' : 1},
    '4' : {'col' : 0, 'row' : 4, 'span' : 1},
    '5' : {'col' : 1, 'row' : 4, 'span' : 1},
    '6' : {'col' : 2, 'row' : 4, 'span' : 1},
    '7' : {'col' : 0, 'row' : 3, 'span' : 1},
    '8' : {'col' : 1, 'row' : 3, 'span' : 1},
    '9' : {'col' : 2, 'row' : 3, 'span' : 1}}

math_positions = {
    '/' : {'col' : 3, 'row' : 2, 'character' : '' , 'operator' : '/', 'image path' : {'light' : 'images/divide_light.png', 'dark': 'images/divide_dark.png'}},
    '*' : {'col' : 3, 'row' : 3, 'character' : 'x' , 'operator' : '*', 'image path' :None},
    '-' : {'col' : 3, 'row' : 4, 'character' : '-' , 'operator' : '-', 'image path' :None},
    '+' : {'col' : 3, 'row' : 5, 'character' : '+' , 'operator' : '+', 'image path' :None},
    '+' : {'col' : 3, 'row' : 6, 'character' : '=' , 'operator' : '=', 'image path' :None}}

operators = {
    'clear' : {'col' : 0, 'row' : 2, 'text' : 'AC' , 'image path' :None},
    'invert' :  {'col' : 1, 'row' : 2, 'text' : '' , 'image path' :{'light' : 'images/invert_light.png', 'dark' : 'images/invert_dark.png'}},
    'percent' : {'col' : 2, 'row' : 2, 'text' : '%' , 'image path' :None}}

colors = {
    'light-gray' : { 'fg' : ('#505050', '#D4D4D2'), 'hover' : ('#686868', '#efefed'), 'text' : ('white', 'black')},
    'dark-gray' : { 'fg' : ('#D4D4D2', '#505050'), 'hover' : ('#efefed', '#686868'), 'text' : ('black', 'white')},
    'orange' : { 'fg' : '#FF9500', 'hover' : 'ffb143', 'text' : ('white', 'black')},
    'orange-highlight' : { 'fg' : 'white', 'hover' : 'white', 'text' : ('black', '#FF9500')}}

title_bar_hex_colors = {'dark': 0x00000000, 'light': 0x00EEEEEE}

black = '#000000'
white = '#EEEEEE'


 