from tkinter import *


def save_info():
    fn_info = fn.get()
    ln_info = ln.get()
    age_info = age.get()
    age_info = str(age.get)
    print(fn_info, ln_info, age_info)

    file = open("user", "w")
    file.write(fn_info)
    file.write(ln_info)
    file.write(age_info)
    file.close()
    print("User", fn_info, " Has been registered sucessfully")

    fn_entry.delete(0, END)
    ln_entry.delete(0, END)
    age_entry.delete(0, END)


screen = Tk()
screen.geometry("500x500")
screen.title("Form")
heading = Label(text="Form", bg="grey", fg="black", width="500", height="3")
heading.pack()

fn_text = Label(
    text="First Name * ",
)
ln_text = Label(
    text="Last Name * ",
)
age_text = Label(
    text="Age * ",
)
fn_text.place(x=15, y=70)
ln_text.place(x=15, y=140)
age_text.place(x=15, y=210)

fn = StringVar()
ln = StringVar()
age = IntVar()

fn_entry = Entry(textvariable=fn, width="30")
ln_entry = Entry(textvariable=ln, width="30")
age_entry = Entry(textvariable=age, width="30")

fn_entry.place(x=15, y=100)
ln_entry.place(x=15, y=180)
age_entry.place(x=15, y=240)

register = Button(
    screen, text="Register", width="30", height="2", command=save_info, bg="grey"
)
register.place(x=15, y=290)

mainloop()
