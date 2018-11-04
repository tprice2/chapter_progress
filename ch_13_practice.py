"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""
import tkinter
import tkinter.messagebox  # For 13.5
# TODO 13.2 Using the tkinter Module

# Write the code from program 13-2 to display an empty window, no need
# to re-import tkinter


def main():
    #  Create the main window widget
    main_window = tkinter.Tk()
    # Enter the tkinter main loop.
    tkinter.mainloop()
# Call the main function


main()
# create the class MyGUI2


class MyGUI2:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Create a Label Widget containing the text 'hello world'
        self.label = tkinter.Label(self.main_window, text='Hello World!')
        self.label2 = tkinter.Label(self.main_window, text='Trevor Price')
        # Call the label widget's pack method. (shows how the widget is displayed)
        self.label.pack()
        self.label2.pack()

        # Enter the tkinter main loop
        tkinter.mainloop()


my_gui2 = MyGUI2()
# TODO 13.3 Adding a label widget
# add a label that prints your first and last name

# pack the label

# enter the main loop

# create an instance of MyGUI2

# TODO 13.4 Organizing Widgets with Frames
# Create a window in the MyGUI3 class that has two frames
# In the top Frame add a labels with your name and major
# In the bottom frame add labels with the classes you are taking this semester


class MyGUI3:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()
        # Create a Label Widget containing the text 'hello world'
        self.label3 = tkinter.Label(self.main_window, text='Trevor Price: Systems Engineering and Design')
        self.label4 = tkinter.Label(self.main_window, text='PRG 105(Python) and Web 175(Wordpress)')
        # Call the label widget's pack method. (shows how the widget is displayed)
        self.label3.pack(side='top')
        self.label4.pack(side='bottom')
        tkinter.mainloop()


my_gui3 = MyGUI3()
# TODO 13.5 Button Widgets and info Dialog Boxes
# Tell a joke with a button to show the punch line, which should appear in a dialog box
# This program demonstrates a Button widget.
# When the user clicks the Button, an info dialog box is displayed.


class MyGUI4:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()
        # Create a Button widget. The text 'Click Me!' should appear on the face of the Button. The do_something method should be executed when the user clicks the Button.
        self.label = tkinter.Label(self.main_window, text='What kind of bagel can fly?')
        self.my_button = tkinter.Button(self.main_window, text='Punchline', command=self.do_something)
        # Pack the Button/label.
        self.label.pack()
        self.my_button.pack()
        # Enter the tkinter main loop.
        tkinter.mainloop()
        # The do_something method is a callback function
        # for the Button widget.

    def do_something(self):
        # Display an info dialog box.
        tkinter.messagebox.showinfo('Punchline', 'A plane bagel!')


# Create an instance of the MyGUI class.
my_gui4 = MyGUI4()

# TODO 13.6 getting input / 13.7 Using Labels as output fields
# Using the program in 13.10 kilo converter as a sample, create a program
# to convert inches to centimeters


class MetricConverterGUI:
    def __init__(self):

        # Main Window
        self.main_window = tkinter. Tk()

        # Creating two frames
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Widget for the top frame:
        self.prompt_label = tkinter.Label(self.top_frame, text='Enter a distance in inches:')
        self.inch_entry = tkinter.Entry(self.top_frame, width=10)

        # Pack the top frame:
        self.prompt_label.pack(side='left')
        self.inch_entry.pack(side='left')

        # Widgets for the bottom frame:
        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.main_window.destroy)

        # Pack the bottom frame:
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames:
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Enter the tkinter main loop()
        tkinter.mainloop()

    def convert(self):
        # Gets the value enter by the user in the inch_entry widget
        inch = float(self.inch_entry.get())
        # Convert to cm's
        cm = inch*2.54
        # Display the results in a dialog box
        tkinter.messagebox.showinfo('Results', str(inch) + ' inches is equal to ' + str(cm) + " cm's.")


metric_convert = MetricConverterGUI()
