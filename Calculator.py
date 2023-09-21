#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 16:15:53 2023

@author: Maria
"""
import os 

os.chdir('/Users/marysia/Desktop/Portfolio project')
path = os.getcwd()

import customtkinter as ctk
import darkdetect
from buttons import Button, ImageButton, NumButton, MathButton, MathImageButton
from PIL import Image
from settings import *

# Define the Calculator class
class Calculator(ctk.CTk):
    def __init__(self, is_dark):
        # Setup the main app window
        super().__init__(fg_color=(white, black))
        # set apperance to dark or light depending on is_dark
        ctk.set_appearance_mode(f'{"dark" if is_dark else "light"}')
       
        self.geometry(f'{app_size[0]}x{app_size[1]}')
        self.resizable(False, False)
        # Hide the title and icon
        self.title('')
        self.iconbitmap('empty.png')
        
        # Configure grid layout
        self.rowconfigure(list(range(main_rows)), weight = 1, uniform = 'a')
        self.columnconfigure(list(range(main_columns)), weight = 1, uniform = 'a')
        
        # Data 
        self.result_string = ctk.StringVar(value = '0')
        self.formula_string = ctk.StringVar(value = '')
        self.display_nums = []
        self.fulll_operation = []
        
        self.create_widgets()
        
        self.mainloop()
        
# Create widgets
    def create_widgets(self):
        # Fonts
        main_font = ctk.CTkFont(family = FONT, size = normal_font_size)
        result_font = ctk.CTkFont(family= FONT, size = output_font_size)
        
        OutputLabel(self, 0, 'SE', main_font, self.formula_string)# for formula, SE - bottom right
        OutputLabel(self, 1, 'E', result_font, self.result_string)
        # clear (AC) Button
        
        Button(
            parent = self, 
            func = self.clear,
            text = operators['clear']['text'], 
            col= operators['clear']['col'], 
            row= operators['clear']['row'],
            font= main_font)
        # percent button
        Button(
            parent = self,
            func = self.percent,
            text = operators['percent']['text'],
            col = operators['percent']['col'],
            row = operators['percent']['row'], 
            font = main_font)
        #invert button
        invert_image = ctk.CTkImage(light_image= Image.open(operators['invert']['image path']['dark']),
                                    dark_image= Image.open(operators['invert']['image path']['light']))
        ImageButton(parent= self,
                    func = self.invert,
                    col= operators['invert']['col'],
                    row = operators['invert']['row'],
                    image = invert_image)
        
        # number buttons
        for num, data in num_position.items():
            NumButton(
                parent = self,
                text = num,
                func = self.num_press,
                col = data['col'], 
                row = data['row'],
                font = main_font,
                span = data['span'])
            
        # Math buttons
        for operator , data in math_positions.items():
            if data['image path']:
                divide_image = ctk.CTkImage(light_image= Image.open(data['image path']['dark']),
                                            dark_image= Image.open(data['image path']['light']))
                MathImageButton(
                    parent = self,
                    operator = operator, 
                    func = self.math_press,
                    col = data['col'],
                    row = data['row'],
                    image  = divide_image)
            else:
                MathButton(
                    parent = self,
                    text = data['character'],
                    operator = operator,
                    func = self.math_press,
                    col = data['col'],
                    row = data['row'],
                    font = main_font)
            
            
        
    def num_press(self, value):
        self.display_nums.append(str(value))
        full_number = ''.join(self.display_nums)
        self.result_string.set(full_number)
        
    def math_press(self, value):
        current_umber = ''.join(self.display_nums)
        print(current_umber)
        if current_umber:
            self.fulll_operation.append(current_umber)
            if value != '=':
                # update data
                self.fulll_operation.append(value)
                self.display_nums.clear()
                #update output
                self.result_string.set('')
                self.formula_string.set(' '.join(self.fulll_operation))
            else:
                formula = ' '.join(self.fulll_operation)
                result =eval(formula)
                # format the result
                if isinstance(result, float):
                    # integer formatted like a float
                    if result.is_integer():
                        result = int(result)
                    else:
                        result = round(result,3)
                #update data
                self.fulll_operation.clear()
                self.display_nums = [str(result)]
                #update output
                self.result_string.set(result)
                self.formula_string.set(formula)
                
# Clear button       
    def clear(self):
        # clear the output
        self.result_string.set(0)
        self.formula_string.set('')
        # clear the data
        self.display_nums.clear()
        self.fulll_operation.clear()
# Percent button       
    def percent(self):
        if self.display_nums:
            current_number = float(''.join(self.display_nums))
            percent_num = current_number / 100
            # update the data and output
            self.display_nums = list(str(percent_num))
            self.result_string.set(''.join(self.display_nums))
# Invert button        
    def invert(self):
        current_number = ''.join(self.display_nums)
        if current_number:
            if float(current_number) > 0:
                self.display_nums.insert(0, '-')
            else:
                del self.display_nums[0]
                
            self.result_string.set(''.join(self.display_nums))
                
    
class OutputLabel(ctk.CTkLabel):
    def __init__(self, parent, row, anchor, font, string_var):
        super().__init__(master= parent, font = font, textvariable = string_var)
        self.grid(column = 0, columnspan = 4, row = row, sticky = anchor, padx = 10)
    
    
if __name__ == '__main__':
    Calculator(darkdetect.isDark())


# #print(darkdetect.isDark())
# Calculator()
