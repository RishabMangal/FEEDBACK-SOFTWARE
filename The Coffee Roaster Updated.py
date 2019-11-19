from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
from tkinter import messagebox
import datetime
import os.path
import smtplib, ssl

# import cv2
# import PIL.Image, PIL.ImageTk

window = Tk()
window.title("Feedback Form For THE COFFEE ROASTER")
window.configure(background="lightblue")
# window.geometry("2000*1000")
serviceV = StringVar()
staffV = StringVar()
foodV = StringVar()
coffeeV = StringVar()
atmosV = StringVar()
valueV = StringVar()
cleanV = StringVar()
phone = IntVar()
phone = 0
# serviceV.set(3)
s = Style()
s.configure('Wild.TRadiobutton', background="lightblue")
h1 = Label(window, text="The Cof", font=("Georgia Bold", 50), foreground="blue", background="lightblue")
h1.grid(column=3, row=0, sticky=E, padx=0, pady=5)
h1 = Label(window, text="fee Roaster", font=("Georgia Bold", 50), foreground="blue", background="lightblue")
h1.grid(column=4, row=0, sticky=W, padx=0, pady=5)
h2 = Label(window, text="Start every day fresh!", font=("Courier", 20), foreground="blue",
           background="lightblue")
h2.grid(column=5, row=1, sticky=W, padx=5, pady=5)
namel = Label(window, text="Name:", font=("Comic Sans Ms Bold", 20), background="lightblue")
namel.grid(column=0, row=3, sticky=E, padx=5, pady=5)
gst = Label(window, text="GST : TIN-2018164164162303106", font=("Comic Sans Ms", 15), foreground="grey")
gst.grid(column=5, row=3, sticky=W, padx=5, pady=5)
name = Entry(window, width=40)
name.focus()
name.grid(column=1, row=3, sticky=E, padx=5, pady=5)
emaill = Label(window, text="Email:", font=("Comic Sans Ms Bold", 20))
emaill.grid(column=0, row=4, sticky=E, padx=5, pady=5)
email = Entry(window, width=40)
email.grid(column=1, row=4, sticky=E, padx=5, pady=5)
ema = Label(window, text="Email: 2018kucp****@iiitkota.ac.in", font=("Comic Sans Ms", 15),
            foreground="grey")
ema.grid(column=5, row=4, sticky=W, padx=5, pady=5)
phonel = Label(window, text="Phone no:", font=("Comic Sans Ms Bold", 20))
phonel.grid(column=0, row=5, sticky=E, padx=5, pady=5)
phone = Entry(window, width=40)
phone.grid(column=1, row=5, sticky=E, padx=5, pady=5)
tel = Label(window, text="Tel No: 9928****** | 7041*****", font=("Comic Sans Ms", 15), foreground="grey")
tel.grid(column=5, row=5, sticky=W, padx=5, pady=5)
stm = Label(window, text="Timestamp:", font=("Comic Sans Ms", 15), foreground="grey")
stm.grid(column=5, row=6, sticky=W, padx=5, pady=5)
x = datetime.datetime.now()
tim = Label(window, text=((x).strftime("%X") + "   " + (x).strftime("%x")), font=("Comic Sans Ms", 15), foreground="grey")
tim.grid(column=5, row=6, sticky=E, padx=5, pady=5)
time = (x).strftime("%X") + "   " + (x).strftime("%x")
ratel = Label(window, text="Please Rate Us Out OF 3", font=("Georgia", 15), foreground="purple")
ratel.grid(column=2, row=7, padx=5, pady=5)

servicel = Label(window, text="Services:", font=("Georgia", 20))
servicel.grid(column=0, row=9, sticky=E, padx=5, pady=5)
awe1 = Radiobutton(window, text="Awesome", value="AWESOME", variable=serviceV, style="Wild.TRadiobutton")
verg1 = Radiobutton(window, text="Good", value="GOOD", variable=serviceV, style="Wild.TRadiobutton")
goo1 = Radiobutton(window, text="Average", value="AVERAGE", variable=serviceV, style="Wild.TRadiobutton")
# bad1 = Radiobutton(window, text="Bad", value=4, variable=serviceV,style="Wild.TRadiobutton")
# verb1 = Radiobutton(window, text="Very Bad", value=5, variable=serviceV,style="Wild.TRadiobutton")
awe1.grid(column=1, row=9, sticky=E, padx=5, pady=5)
verg1.grid(column=2, row=9, padx=5, pady=5)
goo1.grid(column=3, row=9, sticky=W, padx=5, pady=5)
# bad1.grid(column=4, row=7, sticky=W,padx=5,pady=5)
# verb1.grid(column=5, row=7, sticky=W,padx=5,pady=5)


staffl = Label(window, text="Staff Friendliness:", font=("Georgia", 20))
staffl.grid(column=0, row=10, sticky=E, padx=5, pady=5)
awe2 = Radiobutton(window, text="Awesome", value="AWESOME", variable=staffV, style="Wild.TRadiobutton")
verg2 = Radiobutton(window, text="Good", value="GOOD", variable=staffV, style="Wild.TRadiobutton")
goo2 = Radiobutton(window, text="Average", value="AVERAGE", variable=staffV, style="Wild.TRadiobutton")
# bad2 = Radiobutton(window, text="Bad", value=4, variable=staffV,style="Wild.TRadiobutton")
# verb2 = Radiobutton(window, text="Very Bad", value=5, variable=staffV,style="Wild.TRadiobutton")
awe2.grid(column=1, row=10, sticky=E, padx=5, pady=5)
verg2.grid(column=2, row=10, padx=5, pady=5)
goo2.grid(column=3, row=10, sticky=W, padx=5, pady=5)
# bad2.grid(column=4, row=8, sticky=W,padx=5,pady=5)
# verb2.grid(column=5, row=8, sticky=W,padx=5,pady=5)


foodl = Label(window, text="Food Quality:", font=("Georgia", 20))
foodl.grid(column=0, row=11, sticky=E, padx=5, pady=5)
awe3 = Radiobutton(window, text="Awesome", value="AWESOME", variable=foodV, style="Wild.TRadiobutton")
verg3 = Radiobutton(window, text="Good", value="GOOD", variable=foodV, style="Wild.TRadiobutton")
goo3 = Radiobutton(window, text="Average", value="AVERAGE", variable=foodV, style="Wild.TRadiobutton")
# bad3 = Radiobutton(window, text="Bad", value=4, variable=foodV,style="Wild.TRadiobutton")
# verb3 = Radiobutton(window, text="Very Bad", value=5, variable=foodV,style="Wild.TRadiobutton")
awe3.grid(column=1, row=11, sticky=E, padx=5, pady=5)
verg3.grid(column=2, row=11, padx=5, pady=5)
goo3.grid(column=3, row=11, sticky=W, padx=5, pady=5)
# bad3.grid(column=4, row=9, sticky=W,padx=5,pady=5)
# verb3.grid(column=5, row=9, sticky=W,padx=5,pady=5)


coffeel = Label(window, text="Coffee Quality:", font=("Georgia", 20))
coffeel.grid(column=0, row=12, sticky=E, padx=5, pady=5)
awe4 = Radiobutton(window, text="Awesome", value="AWESOME", variable=coffeeV, style="Wild.TRadiobutton")
verg4 = Radiobutton(window, text="Good", value="GOOD", variable=coffeeV, style="Wild.TRadiobutton")
goo4 = Radiobutton(window, text="Average", value="AVERAGE", variable=coffeeV, style="Wild.TRadiobutton")
# bad4 = Radiobutton(window, text="Bad", value=4, variable=coffeeV,style="Wild.TRadiobutton")
# verb4 = Radiobutton(window, text="Very Bad", value=5, variable=coffeeV,style="Wild.TRadiobutton")
awe4.grid(column=1, row=12, sticky=E, padx=5, pady=5)
verg4.grid(column=2, row=12, padx=5, pady=5)
goo4.grid(column=3, row=12, sticky=W, padx=5, pady=5)
# bad4.grid(column=4, row=10, sticky=W,padx=5,pady=5)
# verb4.grid(column=5, row=10, sticky=W,padx=5,pady=5)


atmosl = Label(window, text="Atmosphere:", font=("Georgia", 20))
atmosl.grid(column=0, row=13, sticky=E, padx=5, pady=5)
awe5 = Radiobutton(window, text="Awesome", value="AWESOME", variable=atmosV, style="Wild.TRadiobutton")
verg5 = Radiobutton(window, text="Good", value="GOOD", variable=atmosV, style="Wild.TRadiobutton")
goo5 = Radiobutton(window, text="Average", value="AVERAGE", variable=atmosV, style="Wild.TRadiobutton")
# bad5 = Radiobutton(window, text="Bad", value=4, variable=atmosV,style="Wild.TRadiobutton")
# verb5 = Radiobutton(window, text="Very Bad", value=5, variable=atmosV,style="Wild.TRadiobutton")
awe5.grid(column=1, row=13, sticky=E, padx=5, pady=5)
verg5.grid(column=2, row=13, padx=5, pady=5)
goo5.grid(column=3, row=13, sticky=W, padx=5, pady=5)
# bad5.grid(column=4, row=11, sticky=W,padx=5,pady=5)
# verb5.grid(column=5, row=11, sticky=W,padx=5,pady=5)


valuel = Label(window, text="Value of Money:", font=("Georgia", 20))
valuel.grid(column=0, row=14, sticky=E, padx=5, pady=5)
awe6 = Radiobutton(window, text="Awesome", value="AWESOME", variable=valueV, style="Wild.TRadiobutton")
verg6 = Radiobutton(window, text="Good", value="GOOD", variable=valueV, style="Wild.TRadiobutton")
goo6 = Radiobutton(window, text="Average", value="AVERAGE", variable=valueV, style="Wild.TRadiobutton")
# bad6 = Radiobutton(window, text="Bad", value=4, variable=valueV,style="Wild.TRadiobutton")
# verb6 = Radiobutton(window, text="Very Bad", value=5, variable=valueV,style="Wild.TRadiobutton")
awe6.grid(column=1, row=14, sticky=E, padx=5, pady=5)
verg6.grid(column=2, row=14, padx=5, pady=5)
goo6.grid(column=3, row=14, sticky=W, padx=5, pady=5)
# bad6.grid(column=4, row=12, sticky=W,padx=5,pady=5)
# verb6.grid(column=5, row=12, sticky=W,padx=5,pady=5)


cleanl = Label(window, text="Cleanliness:", font=("Georgia", 20))
cleanl.grid(column=0, row=15, sticky=E, padx=5, pady=5)
awe7 = Radiobutton(window, text="Awesome", value="AWESOME", variable=cleanV, style="Wild.TRadiobutton")
verg7 = Radiobutton(window, text="Good", value="GOOD", variable=cleanV, style="Wild.TRadiobutton")
goo7 = Radiobutton(window, text="Average", value="AVERAGE", variable=cleanV, style="Wild.TRadiobutton")
# bad7 = Radiobutton(window, text="Bad", value=4, variable=cleanV,style="Wild.TRadiobutton")
# verb7 = Radiobutton(window, text="Very Bad", value=5, variable=cleanV,style="Wild.TRadiobutton")
awe7.grid(column=1, row=15, sticky=E, padx=5, pady=5)
verg7.grid(column=2, row=15, padx=5, pady=5)
goo7.grid(column=3, row=15, sticky=W, padx=5, pady=5)
# bad7.grid(column=4, row=13, sticky=W,padx=5,pady=5)
# verb7.grid(column=5, row=13, sticky=W,padx=5,pady=5)

likel = Label(window, text="What Did You Like About Us:", font=("Georgia", 14))
likel.grid(column=0, row=17, sticky=W, padx=5, pady=5)
like = Entry(window, width=40)
like.grid(column=1, row=17, sticky=E, padx=5, pady=5)

visitl = Label(window, text="How Often Do You Visit Us:", font=("Georgia", 14))
visitl.grid(column=0, row=19, sticky=W, padx=5, pady=5)
visit = Combobox(window, width=37)
visit['values'] = ("Daily", "Frequently", "Occasionlly", "Rarely")
visit.current(0)
visit.grid(column=1, row=19, sticky=E, padx=5, pady=5)

hearl = Label(window, text="How Did You Hear About Us:", font=("Georgia", 14))
hearl.grid(column=0, row=21, sticky=W, padx=5, pady=5)
# hear=Entry(window,width=40)
hear = Combobox(window, width=37)
hear['values'] = ("Facebook", "Instagram", "Friends and Relatives", "Food Blogs", "Other")
hear.current(1)
hear.grid(column=1, row=21, sticky=E, padx=5, pady=5)

commentl = Label(window, text="Comments:", font=("Georgia Bold", 20))
commentl.grid(column=0, row=23)
comment = Text(window, width="80", height="10", padx=5, pady=5)
comment.grid(column=1, row=23, sticky=W, columnspan=4)


def onSubmit():
    h = name.get() + ".txt"
    f = open(h, "a+")
    f.write(
        "\n------------------------------------------------------------------------------------------------------------------------\n")
    f.write("                                                                                 TimeStamp:  %s \n" % time)
    f.write("\nName: %s \n" % name.get())
    f.write("\nEmail: %s \n" % email.get())
    f.write("\nPhone: %s \n" % phone.get())
    f.write("\nOur Services are  %s \n" % serviceV.get())
    f.write("\nFriendliness of staff is  %s \n" % staffV.get())
    f.write("\nOur Food is  %s \n" % foodV.get())
    f.write("\nOur Coffee is  %s \n" % coffeeV.get())
    f.write("\nAtmosphere Here is  %s \n" % atmosV.get())
    f.write("\nValue of Money is  %s \n" % valueV.get())
    f.write("\nCleanliness is  %s \n" % cleanV.get())
    f.write("\nYou Like About US   %s \n" % like.get())
    f.write("\nYou visit US    %s \n" % visit.get())
    f.write("\nYou Heard About Us Through  %s \n" % hear.get())
    f.write("\nComments:\n        %s \n" % comment.get(1.0, END))
    f.write("\n                                                 **********************                                                                           \n")
    f.close()
    f=open(h,"r")
    messtext=f.read()
    f.close()
    f = open("feedbacks.txt", "a+")
    f.write("\n------------------------------------------------------------------------------------------------------------------------\n")
    f.write("                                                                                 TimeStamp:  %s \n" % time)
    f.write("\nName: %s \n" % name.get())
    f.write("\nEmail: %s \n" % email.get())
    f.write("\nPhone: %s \n" % phone.get())
    f.write("\nOur Services are  %s \n" % serviceV.get())
    f.write("\nFriendliness of staff is  %s \n" % staffV.get())
    f.write("\nOur Food is  %s \n" % foodV.get())
    f.write("\nOur Coffee is  %s \n" % coffeeV.get())
    f.write("\nAtmosphere Here is  %s \n" % atmosV.get())
    f.write("\nValue of Money is  %s \n" % valueV.get())
    f.write("\nCleanliness is  %s \n" % cleanV.get())
    f.write("\nYou Like About US   %s \n" % like.get())
    f.write("\nYou visit US    %s \n" % visit.get())
    f.write("\nYou Heard About Us Through  %s \n" % hear.get())
    f.write("\nComments:\n        %s \n" % comment.get(1.0, END))
    f.write(
        "\n                                                 **********************                                                                           \n")
    f.close()

    messagebox.showinfo(" Submitted Successfully", "Thank You " + name.get() + " For Your Valuable FeedBack.Please Do "
                                                                               "Visit Again")
    # -----------------------Send Email--------------------------------------------------------------------------------

    smtp_server = "smtp.gmail.com"
    port = 587  # For starttls
    sender_email = "mangal******@gmail.com"
    reciever_email =email.get()
    # password = input("Type your password and press enter: ")
    password = "************"
    # message = """\
    # Subject: The Coffee Roaster Feedback Form.
    #
    #
    #
    # """
    sub="The Coffee Roaster Feedback Form"
    message = f"Subject : {sub}\n\n{messtext}"
    # message = """\
    # Subject: Fist Try From Python
    #
    #
    # This is mail from Python."""
    # Create a secure SSL context
    context = ssl.create_default_context()

    # Try to log in to server and send email
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls(context=context)  # Secure the connection
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        # TODO: Send email here
        server.sendmail(sender_email, reciever_email, message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit()



    onClear()


def onClear():
    name.configure(background="lightblue")
    name.delete(0, END)
    email.delete(0, END)
    phone.delete(0, END)
    comment.delete(1.0, END)
    like.delete(0, END)
    hear.current(1)
    visit.current(0)
    serviceV.set(None)
    staffV.set(None)
    foodV.set(None)
    coffeeV.set(None)
    valueV.set(None)
    cleanV.set(None)
    atmosV.set(None)


def onView():
    newwindow = Toplevel()
    newwindow.title("View Feedback")
    newwindow.configure(background="lightblue")

    h1 = Label(newwindow, text="The Cof", font=("Georgia Bold", 50), foreground="blue", background="lightblue")
    h1.grid(column=3, row=0, sticky=E, padx=0, pady=5)
    h1 = Label(newwindow, text="fee Roaster", font=("Georgia Bold", 50), foreground="blue", background="lightblue")
    h1.grid(column=4, row=0, sticky=W, padx=0, pady=5)
    h2 = Label(newwindow, text="Start every day fresh!", font=("Courier", 20), foreground="blue",
               background="lightblue")
    h2.grid(column=5, row=1, sticky=W, padx=5, pady=5)
    namel = Label(newwindow, text="Name:", font=("Comic Sans Ms Bold", 20), background="lightblue")
    namel.grid(column=0, row=3, sticky=E, padx=5, pady=5)
    gst = Label(newwindow, text="GST : TIN-2018164164162303106", font=("Comic Sans Ms", 15), foreground="grey")
    gst.grid(column=5, row=3, sticky=W, padx=5, pady=5)
    name = Entry(newwindow, width=40)
    name.focus()
    name.grid(column=1, row=3, sticky=E, padx=5, pady=5)

    def show():
        h = (name.get() + ".txt")
        if os.path.exists(h):
            f = open(h, "r")
            contents = f.read()
            contentl = Label(newwindow, text=contents, width=120, font=("Comic Sans Ms", 11))
            contentl.grid(column=0, row=7, columnspan=5, rowspan=10, padx=5, pady=10, sticky=NW)
            # print(contents)
        else:
            messagebox.showerror("Error", "User Not Found.Please Give Us Feedback First.")


    go = Button(newwindow, text="Go", command=show)
    go.grid(column=2, row=3)
    ema = Label(newwindow, text="Email: 2018kucp****@iiitkota.ac.in", font=("Comic Sans Ms", 15), foreground="grey")
    ema.grid(column=5, row=4, sticky=W, padx=5, pady=5)
    tel = Label(newwindow, text="Tel No: 9928****** | 7041******", font=("Comic Sans Ms", 15), foreground="grey")
    tel.grid(column=5, row=5, sticky=W, padx=5, pady=5)
    stm = Label(newwindow, text="Timestamp:", font=("Comic Sans Ms", 15), foreground="grey")
    stm.grid(column=5, row=6, sticky=W, padx=5, pady=5)
    x = datetime.datetime.now()
    tim = Label(newwindow, text=((x).strftime("%X") + "   " + (x).strftime("%x")), font=("Comic Sans Ms", 15),
                foreground="grey")
    tim.grid(column=5, row=6, sticky=E, padx=5, pady=5)
    widgets2 = [gst, ema, tel, stm, tim]
    for wid in widgets2:
        wid.configure(background="lightblue")

    canvas1 = Canvas(newwindow, height=415, width=739, background="lightblue")
    canvas1.grid(column=5, row=7, columnspan=7, rowspan=20, padx=5, pady=5,sticky=NW)
    photo1 = ImageTk.PhotoImage(Image.open("hotcoffee.gif"))
    canvas1.create_image(0, 0, image=photo1, anchor=NW)

    newwindow.mainloop()


submit = Button(window, text="Submit", command=onSubmit)
clear = Button(window, text="Clear", command=onClear)
view = Button(window, text="View", command=onView)
submit.grid(column=2, row=25)
clear.grid(column=2, row=25, sticky=E)
view.grid(column=3, row=25, sticky=W)


widgets = [namel, emaill, phonel, gst, ema, tel, stm, tim, ratel, servicel, staffl, foodl, coffeel, atmosl, valuel,
           cleanl, likel, visitl, hearl, commentl]
for wid in widgets:
    wid.configure(background="lightblue")

canvas = Canvas(window, height=600, width=900, background="lightblue")
canvas.grid(column=4, row=7, columnspan=6, rowspan=20, sticky=W, padx=5, pady=5)
photo = ImageTk.PhotoImage(Image.open("3cups.gif"))
canvas.create_image(0, 0, image=photo, anchor=NW)

window.mainloop()



