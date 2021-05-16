'''
	Author: Stefan Popovic
	Date  : 16/05/2021

	Resources: pyautogui documentation, tkinter documentation
	
	About: Learning to create a GUI with Python libraries and possibly create
		   applications and full user interfaces for software.
		   Possible use pyautogui, tkinter or pysimplegui

	TODO: ----
'''

import pyautogui
import tkinter
import pysimplegui as sg

sg.theme('DarkAmber') 

layout = [	[sg.Text('Some text on Row 1')],
			[sg.Text('Enter somethng on Row 2')],
			[sg.Button('Ok'), sg.Button('Cancel')]	]