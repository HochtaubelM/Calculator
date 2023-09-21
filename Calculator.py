#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 16:15:53 2023

@author: marysia
"""

import os 

os.chdir('/Users/marysia/Desktop/Portfolio project')
path = os.getcwd()

import customtkinter as ctk
import darkdetect
from buttons import Button
from settings import *

class Calculator(ctk.CTk):
    def __init__(self, is_dark):
        #setup
        super().__init__(fg_color=(white, black))
        # exercise:
        # 1. set apperance to dark or light depending on is_dark
        ctk.set_appearance_mode(f'{"dark" if is_dark else "light"}')
        # 2. fg_color = white or black
        # 3. get the start window size from the settings and disable window resizing
        self.geometry(f'{app_size[0]}x{app_size[1]}')
        self.resizable(False, False)
        # 4. hide the title and icon
        self.title('')
        self.iconbitmap('empty.png')
        
        #grid layout - 7 rows and 4 columns
        self.rowconfigure(list(range(main_rows)), weight = 1, uniform = 'a')
        self.columnconfigure(list(range(main_columns)), weight = 1, uniform = 'a')
        
        # Data
        self.result_string = ctk.StringVar(value = '0')
        self.formula_string = ctk.StringVar(value = '')
        
        
        
        self.create_widgets()
        self.mainloop()
        # widgets
    def create_widgets(self):
        # Fonts
        main_font = ctk.CTkFont(family = FONT, size = normal_font_size)
        result_font = ctk.CTkFont(family= FONT, size = output_font_size)
        
        OutputLabel(self, 0, 'SE', main_font, self.formula_string)# for formula, SE - bottom right
        OutputLabel(self, 1, 'E', result_font, self.result_string)
        # clear (AC) Button
        
        Button(parent = self, text = 'AC', col= 0, row= 2)
        
        
        
        
    
class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, anchor, font, string_var):
        super().__init__(master= parent, font = font, textvariable = string_var)
        self.grid(column = 0, columnspan = 4, row = row, sticky = anchor, padx = 10)
    
    
if __name__ == '__main__':
    Calculator(darkdetect.isDark())


# #print(darkdetect.isDark())
# Calculator()