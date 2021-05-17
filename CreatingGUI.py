'''
	Author: Stefan Popovic
	Date  : 16/05/2021

	Resources: pyautogui documentation, tkinter documentation
		https://pysimplegui.readthedocs.io/en/latest/#about-the-pysimplegui-documentation-system
	
	About: Learning to create a GUI with Python libraries and possibly create
		   applications and full user interfaces for software.
		   Possible use pyautogui, tkinter or pysimplegui

	TODO: ----
'''

'''
			---- Popup window arguments ----
	
	popup(args=*<1 or N object>,
	    title = None,
	    button_color = None,
	    background_color = None,
	    text_color = None,
	    button_type = 0,
	    auto_close = False,
	    auto_close_duration = None,
	    custom_text = (None, None),
	    non_blocking = False,
	    icon = None,
	    line_width = None,
	    font = None,
	    no_titlebar = False,
	    grab_anywhere = False,
	    keep_on_top = False,
	    location = (None, None),
	    any_key_closes = False,
	    image = None,
	    modal = True
	    )
'''

'''
			---- Popup window types ----

	sg.popup('popup')  # Shows OK button
	sg.popup_ok('popup_ok')  # Shows OK button
	sg.popup_yes_no('popup_yes_no')  # Shows Yes and No buttons
	sg.popup_cancel('popup_cancel')  # Shows Cancelled button
	sg.popup_ok_cancel('popup_ok_cancel')  # Shows OK and Cancel buttons
	sg.popup_error('popup_error')  # Shows red error button
	sg.popup_timed('popup_timed')  # Automatically closes
	sg.popup_auto_close('popup_auto_close')  # Same as PopupTimed
	sg.popup_scrolled('popup_scrolled')  # Scrolling window
	sg.popup_no_wait('popup_no_wait')	# Doesn't wait for user input to close / used for debugging
	sg.popup_get_text('popup_get_text')  # Gets line of text from user
	sg.popup_get_file('popup_get_file')  # Asks user to provide file/ opens browse
	sg.popup_get_folder('sg.popup_get_folder')  # Gets folder
	sg.popup_animated('popup_animated')  # Can show an animated gif or loading for example
	sg.one_line_progress_meter('one_line_progress_meter') # Shows loading progress

'''




#import pyautogui
#import tkinter
import PySimpleGUI as sg
import base64

def main():

	# popup()
	# popup_timed()
	# popup_scrolled()
	# popup_no_wait()
	# someWindow()
	# popup_get_text()
	# popup_get_file()
	# popup_get_folder()
	# popup_animated()
	one_line_progress_meter()




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

# Automatically closes after few seconds
def popup_timed():
	sg.theme('DarkAmber')
	sg.popup_timed('Closing soon') 

# Scrolling popup window
def popup_scrolled():
	sg.theme('Black')
	sg.popup_scrolled('Romale\n', 'Romali\n', 'Romale\n', 'Romali\n', 'Romale\n', 'Romali\n')

# Popup doesnt wait for user input but immediately closes unless specified otherwise
# non_blocking argument in popup_no_wait is set to True by default
# Can be and is used for debugging
def popup_no_wait():
	sg.popup_no_wait('Wait a second')
	sg.popup_non_blocking('aa', non_blocking = False)

# Gets line of text from user which can be stored in a variable
def popup_get_text():
	name = sg.popup_get_text('Name:', default_text = 'First Name', no_titlebar = True)
	print(name)
	password = sg.popup_get_text('Password:', password_char = '*', modal = True)
	print(password)

# Asks user for file. Can ask for specific file types as well
# Can also save file/ save as
# Browse / Save as
def popup_get_file():
	text = sg.popup_get_file('File:')#, save_as = True)
	sg.popup('Results', 'The value returned from popup_get_file', text)

# Asks for folder
def popup_get_folder():
	sg.popup_get_folder('Get folder:')

# Can show an animation
# GIF stored through file or base64
# Figure out how to make it work
def popup_animated():
	with open('loading_animated.gif', 'rb') as loading:
		base64string = base64.b64encode(loading.read()).decode('ascii')

	sg.popup_animated(base64string)
	print(len(base64string))

# Loading line/ showing progress/ iteration
def one_line_progress_meter():
	for i in range(1,10000):
		sg.one_line_progress_meter('Loading', i+1, 10000, 'key', 'Optional message', orientation = 'h')





main()