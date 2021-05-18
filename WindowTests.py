'''
	Author: Stefan Popovic
	Date  : 17/05/2021

	About : More in-dept modification of windows and its elements

'''

import PySimpleGUI as sg


def main():

	# text_input_ok_window()
	# filename_browse()
	one_shot_window()



# Simple window with three elements (text, input, ok)
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

# Browsing a filename and returning string of location
def filename_browse():
	sg.theme('DarkAmber')
	layout = [	[sg.Text('Filename')],
				[sg.Input(), sg.FileBrowse()],
				[sg.OK(), sg.Cancel()]	]

	window = sg.Window('Get filename', layout)
	event, values = window.read()
	window.close()

	sg.popup('Location', values[0])

# Window is not read multiple times
def one_shot_window():
	layout = [	[sg.Text('SHA-1 and SHA-256 Hashes for the file')],
				[sg.InputText(), sg.FileBrowse()],
				[sg.Submit(), sg.Cancel()]	]

	window = sg.Window('SHA-1 & SHA-256 Hash', layout)

	event, values = window.read()
	window.close()

	source_filename = values[0]










main()