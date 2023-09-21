#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 20:00:46 2023

@author: Maria
"""

from customtkinter import CTkButton
from settings import *

class Button(CTkButton):
    def __init__(self, parent, text, col, row):
        super().__init__(master=parent, text = text)
        self.grid(column = col, row = row, sticky= 'NSEW')
        
