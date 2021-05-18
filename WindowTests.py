'''
	Author: Stefan Popovic
	Date  : 17/05/2021

	About : More in-dept modification of windows and its elements

'''

import PySimpleGUI as sg


def main():

	# text_input_ok_window()
	# filename_browse()
	# one_shot_window()
	# one_show_window_compact()
	persistent_window()



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

# Window is not read multiple times compact version
def one_show_window_compact():
	event, values = sg.Window('SHA-1 & SHA-256 Hash', [	[sg.Text('SHA-1 and SHA-256 Hashes for the file')],
														[sg.InputText(), sg.FileBrowse()],
														[sg.Submit(), sg.Cancel()]	]).read(close=True)

	source_filename = values[0]

# Multiple reads using an event loop
def persistent_window():
	layout = [	[sg.Text('Persistent window')],
				[sg.Input()],
				[sg.Button('Read'), sg.Exit()]	]

	window = sg.Window('Window that stays open', layout)

	while True:
		event, values = window.read()
		if event == sg.WIN_CLOSED or event == 'Exit':
			break
		print(event + ' -', values[0])

	window.close()









main()