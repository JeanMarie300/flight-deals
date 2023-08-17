import os
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import requests
class CustomerAcquisition:

    def __init__ (self):

        self.window = Tk()
        self.window.title("Customer acquisition page")
        self.window.config(padx=50, pady=50)
        self.sheet_endpoint = os.getenv('EMAIL_SHEET_ENDPOINT')
        self.bearer_token = os.getenv('EMAIL_BEARER_TOKEN')

        self.createImageCanvas()

        self.addFirstName()

        self.addLastName()

        self.addEmail()

        self.addVerifyEmail()

        self.addButton()

        self.window.mainloop()
    def createImageCanvas(self):

        self.canvas = Canvas(width=200, height=200, highlightthickness=0)
        self.photo_img = ImageTk.PhotoImage(Image.open("J-M.png"))
        self.canvas.create_image(100, 100, image=self.photo_img)
        self.canvas.grid(row=0, column=1)

    def addFirstName(self):
        # First Name label
        self.FirstNamelabel = Label(text="First Name")
        self.FirstNamelabel.grid(row=2, column=0)

        # First Name input box
        self.FirstNameInputBox = Entry(width=35)
        self.FirstNameInputBox.grid(row=2, column=1)
        self.FirstNameInputBox.focus()

    def addLastName(self):
        # Last Name label
        self.LastNamelabel = Label(text="Last Name")
        self.LastNamelabel.grid(row=3, column=0, pady=10)

        # Last Name input box
        self.LastNameInputBox = Entry(width=35)
        self.LastNameInputBox.grid(row=3, column=1)

    def addEmail(self):
        # Email label
        self.Emaillabel = Label(text="Email")
        self.Emaillabel.grid(row=4, column=0, pady=10)

        # Email input box
        self.EmailInputBox = Entry(width=35)
        self.EmailInputBox.grid(row=4, column=1)

    def addVerifyEmail(self):
        # Email label
        self.verifyEmaillabel = Label(text="Verify Email")
        self.verifyEmaillabel.grid(row=5, column=0, pady=10)

        # Email input box
        self.verifyEmailInputBox = Entry(width=35)
        self.verifyEmailInputBox.grid(row=5, column=1)

    def addButton(self):

        addButton = Button(text="Submit information",command=self.verifyFields, width=35)
        addButton.grid(row=6, column=1)

    def verifyFields(self):

        first_name_value = self.FirstNameInputBox.get()
        last_name_value = self.LastNameInputBox.get()
        email_value = self.EmailInputBox.get()
        verify_email_value = self.verifyEmailInputBox.get()

        error = False

        if first_name_value == '':
            messagebox.showerror(title="Empty First name", message="There is no value entered for the first name")
            error = True
        if last_name_value == '':
            messagebox.showerror(title="Empty Last name", message="There is no value entered for the last name")
            error = True
        if email_value == '':
            messagebox.showerror(title="Empty Email value", message="There is no value entered for the Email")
            error = True
        if verify_email_value != email_value :
            messagebox.showerror(title="Mismatching email", message="Email address mismatch")
            error = True

        if not error :
            messagebox.showinfo(title="Information Submitted", message="Your email was successfully added to the mail list")
            self.postCustomerData()
            self.FirstNameInputBox.delete(0, END)
            self.LastNameInputBox.delete(0, END)
            self.EmailInputBox.delete(0, END)
            self.verifyEmailInputBox.delete(0, END)
            self.window.destroy()

    def postCustomerData(self):

        first_name_value = self.FirstNameInputBox.get()
        last_name_value = self.LastNameInputBox.get()
        email_value = self.EmailInputBox.get()


        header = {
            'Authorization': 'Bearer ' + self.bearer_token
        }
        body = {
            'sheet1':{
                'firstName': first_name_value,
                'lastName' : last_name_value,
                'email': email_value
            }
        }

        response = requests.post(url= self.sheet_endpoint, headers=header,json=body)

        return response.status_code

