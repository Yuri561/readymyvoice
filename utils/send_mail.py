import customtkinter
from customtkinter import CTkInputDialog
import smtplib, ssl

port = 465
smtp_server = "smtp.gmail.com"
sender_email = "cloudflow34@gmail.com"
password = input("Please enter a password: ")

def send_email():
    input_box = customtkinter.CTkInputDialog(title='Enter Email to Share',text='Enter email:')
    receiver_email = input_box.get_input()

