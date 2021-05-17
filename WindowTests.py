'''
	Author: Stefan Popovic
	Date  : 17/05/2021

	About : More in-dept modification of windows and its elements

'''

import PySimpleGUI as sg


def main():

	text_input_ok_window()





def text_input_ok_window():
	layout = [	[sg.Text('Enter number')],
				[sg.Input()],
				[sg.OK()]	]

	window = sg.Window('Enter a number', layout)

	event, values = window.read()

	window.close()
	#sg.Print(type(values[0]))


	# Checks if input is number or not
	try:
		if float(values[0]):
			sg.Popup('Entered: ', values[0])
	except:
		sg.Popup(values[0] + ' is not a number.')










main()