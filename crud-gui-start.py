import tkinter
import tkinter.messagebox
import pickle

# This is the main class, where the menu is formulated (radio buttons)


class CrudGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Welcome Menu')
        self.radio_var = 0
        
        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)
        
        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)
        
        # create the radio buttons
        self.look = tkinter.Radiobutton(self.top_frame, text='Look up customer',
                                        variable=self.radio_var, value=1)
        self.add = tkinter.Radiobutton(self.top_frame, text='Add Customer',
                                       variable=self.radio_var, value=2)
        self.change = tkinter.Radiobutton(self.top_frame, text='Change customer email',
                                          variable=self.radio_var, value=3)
        self.delete = tkinter.Radiobutton(self.top_frame, text='Delete customer',
                                          variable=self.radio_var, value=4)
        
        # pack the radio buttons
        self.look.pack(anchor='w', padx=20)
        self.add.pack(anchor='w', padx=20)
        self.change.pack(anchor='w', padx=20)
        self.delete.pack(anchor='w', padx=20)
        
        # create ok and quit buttons
        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.master.destroy)
        
        # pack the buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()
    # These if statements direct the user to each respective menu, which is created by each respective class.

    def open_menu(self):
        if self.radio_var.get() == 1:
            search = LookGUI(self.master)
        elif self.radio_var.get() == 2:
            search = Add(self.master)
        elif self.radio_var.get() == 3:
            search = Change(self.master)
        elif self.radio_var.get() == 4:
            search = Delete(self.master)
        else:
            tkinter.messagebox.showinfo('Function', 'still under construction')

# This class is responsible for checking whether the input is already saved in customer_file.dat


class LookGUI:
    def __init__(self, master):
        
        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}
        
        self.master = master
        self.look = tkinter.Toplevel(master)
        self.look.title('Search for customer')
        
        # self.look_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)
        
        # widgets for top frame
        self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to look for: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)
        
        # pack top frame
        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')
        
        # middle frame
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Email: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)
        
        # pack Middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')
        
        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)
        
        # pack bottom frame
        self.search_button.pack(side='left')
        self.back_button.pack(side='left')
        
        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    # This is called when the "Search" button is pressed.

    def search(self):
        name = self.search_entry.get()
        if name.upper() in self.customers:  # If name(everything is uppercase) is stored, then display this email.
            result = self.customers.get(name.capitalize())
            self.value.set(result)
        else:  # If it's not, then show "Not Found"
            self.value.set('Not Found')

    def back(self):
        self.look.destroy()


# This class is called when the user wants to add a customer

class Add:
    #  open the file, load to customers, close file. Do in each class
    def __init__(self, master):
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        self.master = master
        self.look = tkinter.Toplevel(master)
        self.look.title('Add Customer')

        #  Setting up the frames
        self.top_frame = tkinter.Frame(self.look)
        self.second_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame
        self.add_customer_label = tkinter.Label(self.top_frame, text='Customer Name: ')
        self.add_customer_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.add_customer_label.pack(side='left')
        self.add_customer_entry.pack(side='left')

        # second frame widgets
        self.add_email_label = tkinter.Label(self.second_frame, text='Customer Email: ')
        self.add_email_entry = tkinter.Entry(self.second_frame, width=15)

        # second frame pack
        self.add_email_label.pack(side='left')
        self.add_email_entry.pack(side='left')

        # middle frame
        self.add_alert = tkinter.StringVar()
        self.add_alert_label = tkinter.Label(self.middle_frame, textvariable=self.add_alert)

        # pack Middle frame
        self.add_alert_label.pack(side='left')

        # buttons for bottom frame
        self.add_button = tkinter.Button(self.bottom_frame, text='Add Customer', command=self.add)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.add_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.second_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def add(self):  # This is called when the user presses "add"
        name = self.add_customer_entry.get()  # Sets the name variable equal to the user input in the name gui
        email = self.add_email_entry.get()  # Sets the email variable equal to the user input in the email gui
        if name.upper() in self.customers:  # If the entered name is in the file, then state this.
            self.add_alert.set("This customer already exists")
        else:
            self.customers[name.upper()] = email.upper()  # Adds the dictionary value of "name" with item "email"
            self.add_alert.set("Customer added: " + str(name.capitalize()))

    def back(self):  # This saves, pickles, and closes the menu.
        save_file = open('customer_file.dat', 'wb')
        pickle.dump(self.customers, save_file)
        save_file.close()
        self.look.destroy()


# This class is called if the use wants to change a customer email

class Change:
    def __init__(self, master):

        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        self.master = master
        self.look = tkinter.Toplevel(master)
        self.look.title('Change Email')

        # self.look_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.look)
        self.second_frame = tkinter.Frame(self.look)
        self.third_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame
        self.search_label = tkinter.Label(self.top_frame, text='Customer Name: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        # Pack top frame
        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        # Widgets second frame
        self.add_email_label = tkinter.Label(self.second_frame, text='New Email: ')
        self.add_email_entry = tkinter.Entry(self.second_frame, width=15)

        # Pack second frame
        self.add_email_label.pack(side='left')
        self.add_email_entry.pack(side='left')

        # Third frame widgets
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.third_frame, text='Results: ')
        self.result_label = tkinter.Label(self.third_frame, textvariable=self.value)

        # Pack third frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')

        # Buttons for bottom frame
        self.change_button = tkinter.Button(self.bottom_frame, text='Change Email', command=self.change)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # Pack bottom frame
        self.change_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.second_frame.pack()
        self.third_frame.pack()
        self.bottom_frame.pack()

    # This is called if the user selects the "change email" button.
    def change(self):
        name = self.search_entry.get()
        name = name.upper()  # Converts name to upper so that caps don't matter.
        if name in self.customers:  # If the name is in the file, then set the value of this dictionary item to the entered email.
            email = self.add_email_entry.get()
            self.customers[name] = email
            self.value.set("Email Updated")
        else:  # Else, the customer doesn't exist, so state that.
            self.value.set("That customer does not exist")

    def back(self):  # This pickles the file, closes the file, and closes the menu.
        save_file = open('customer_file.dat', 'wb')
        pickle.dump(self.customers, save_file)
        save_file.close()
        self.look.destroy()

# This is the delete class, called if the user wants to delete a customer.


class Delete:
    def __init__(self, master):

        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        self.master = master
        self.look = tkinter.Toplevel(master)
        self.look.title('Delete Customer')

        # self.look_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame
        self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to look for: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        # middle frame
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        # pack Middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Delete', command=self.delete)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    # Called if the user selects "delete"
    def delete(self):
        name = self.search_entry.get()
        if name.upper() in self.customers:  # If the entered name is in the file, then delete this dictionary item.
            del self.customers[name.upper()]
            self.value.set("Customer Deleted")
        else:       # Else, state this customer doesn't exist
            self.value.set("That customer does not exist")

    def back(self):  # Pickle the file, close the file, and close this menu.
        save_file = open('customer_file.dat', 'wb')
        pickle.dump(self.customers, save_file)
        save_file.close()
        self.look.destroy()


def main():
    # create a window
    root = tkinter.Tk()
    # call the GUI and send it the root menu
    menu_gui = CrudGUI(root)
    # control the mainloop from main instead of the class
    root.mainloop()


main()
