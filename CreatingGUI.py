'''
	Author: Stefan Popovic
	Date  : 16/05/2021

	Resources: pyautogui documentation, tkinter documentation
	
	About: Learning to create a GUI with Python libraries and possibly create
		   applications and full user interfaces for software.
		   Possible use pyautogui, tkinter or pysimplegui

	TODO: ----
'''

#import pyautogui
#import tkinter
import PySimpleGUI as sg

def main():

	popup()
	someWindow()





# Window asking for text and displaying it
def someWindow():
	sg.theme('DarkAmber') 

	layout = [	[sg.Text('Some text on Row 1')],
				[sg.Text('Enter somethng on Row 2'), sg.InputText()],
				[sg.Button('Ok'), sg.Button('Cancel')]	]

	window = sg.Window('Window Title', layout)

	while True:
		event, values = window.read()
		if event == sg.WIN_CLOSED or event == 'Cancel':
			break
		print('You entered ', values[0])

# Popup window with a custom message
def popup():
	sg.theme('SystemDefault')
	sg.popup('ERROR: 0x4FA1F', 'Your PC is shutting down in 1 minute...')




main()