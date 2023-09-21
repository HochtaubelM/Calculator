#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 20:00:46 2023

@author: Maria
"""

from customtkinter import CTkButton
from settings import *

# Define a custom Button class with various options
class Button(CTkButton):
    def __init__(self, parent, text, func,col, row, font,  span = 1, color = 'dark-gray'):
        super().__init__(
            master=parent, 
            command = func,
            text = text,
            corner_radius= styling['corner-radius'],
            font = font,
            fg_color= colors[color]['fg'],
            hover_color= colors[color]['hover'],
            text_color = colors[color]['text'])
        self.grid(column = col, columnspan = span,row = row, sticky= 'NSEW', padx = styling['gap'], pady = styling['gap'])

# Define specialized Button classes for:
# numeric buttons
class NumButton(Button):
    def __init__(self, parent, text, func, col, row, font, span, color = 'light-gray'):
        super().__init__(
            parent = parent,
            text = text,
            func = lambda: func(text),
            col = col,
            row = row,
            font =font,
            color = color,
            span = span)
   
# mathematical operations buttons
class MathButton(Button):
    def __init__(self, parent, text, operator, func, col, row, font, color = 'orange'):
        super().__init__(
            parent = parent,
            text = text,
            func = lambda: func(operator),
            col = col,
            row = row,
            font =font,
            color = color,
            )


# image buttons        
class ImageButton(CTkButton):
    def __init__(self, parent,  func,col, row, image , text= '', color = 'dark-gray'):
        super().__init__(
            master=parent, 
            command = func,
            text = text,
            corner_radius= styling['corner-radius'],
            image = image,
            fg_color= colors[color]['fg'],
            hover_color= colors[color]['hover'],
            text_color = colors[color]['text'])
        self.grid(column = col, row = row, sticky= 'NSEW', padx = styling['gap'], pady = styling['gap'])
        
class MathImageButton(ImageButton):
    def __init__(self, parent, operator, func, col, row, image, color = 'orange'):
        super().__init__(
            parent = parent,
            func = lambda: func(operator),
            col = col,
            row = row,
            image = image,
            color = color,
            )
