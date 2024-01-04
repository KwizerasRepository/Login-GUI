#importing modules I'm going to need
import tkinter
import customtkinter
from PIL import ImageTk, Image

customtkinter.set_appearance_mode("System") #can set light or dark
customtkinter.set_default_color_theme('dark-blue') #Setting theme colour


#creation of the log in window
app = customtkinter.CTk()
app.geometry("600x440")
app.title("Login")



#loading background image
img1 = ImageTk.PhotoImage(Image.open("Desktop/pattern.png"))
label1 = customtkinter.CTkLabel(master=app, image=img1)
label1.pack()

#creating a frame to house login entries and labels
frame=customtkinter.CTkFrame(master=label1, width=320, height=360)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

#first label
label2=customtkinter.CTkLabel(master=frame, text="Log into your Account", font=('Century Gothic',20))
label2.place(x=50,y=45)

#username entry area
entry1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
entry1.place(x=50,y=110)

#password entry area
entry2=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password')
entry2.place(x=50,y=165)

#forgot password label
label2=customtkinter.CTkLabel(master=frame, text="forgot password", font=('Century Gothic', 12))
label2.place(x=155,y=195)

#login button
button1=customtkinter.CTkButton(master=frame, width=220, text='Login', corner_radius=6, fg_color='Green', hover_color='#A4A4A4')
button1.place(x=50, y=240)

#Pictures that are going to be housed within buttons
img2=ImageTk.PhotoImage(Image.open('/home/mpilo/Desktop/google.jpg').resize((20,20), Image.ANTIALIAS))
img3=ImageTk.PhotoImage(Image.open('/home/mpilo/Desktop/Facebook.png').resize((20,20), Image.ANTIALIAS))

#login with google button
button2=customtkinter.CTkButton(master=frame, width=100, image=img2,text='Google', height=20, corner_radius=6, 
                                compound='left', fg_color='White', text_color='Black', hover_color='#A4A4A4')
button2.place(x=50, y=290)

#login with Facebook button
button2=customtkinter.CTkButton(master=frame, width=100, image=img3,text='Facebook', height=20, corner_radius=6, compound='left', hover_color='#A4A4A4')
button2.place(x=170, y=290)

app.mainloop()