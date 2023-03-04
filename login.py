from calendar import c
from logging import exception
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image  # pip install pillow
from tkinter import messagebox
import sample_generator
import model_trainer
import face_recognition


def main():
    win = Tk()
    obj = Login_Window(win)
    win.mainloop()


class Login_Window:  # creating class
    def __init__(self, root):  # calling constructor; root is the root window..base window...the first window or the home page

        def login():
            face_recognition.face_recog()

        def pics():
            try:
                sample_generator.take_samples()
                model_trainer.train_model()
                messagebox.showinfo("Success", "Photo samples taken")
            except Exception as e:
                messagebox.showerror("Issue", e)
          
        
        def signup():
            root.withdraw()
            snup = Toplevel(self.root)
            snup.title("Signup")  # giving title to root window
            # setting screen size for root window
            snup.geometry("530x190+500+300")
            snup.configure(bg="black")

            def snup_root():
                root.deiconify()
                snup.withdraw()  

            PhotoSamplesbtn = Button(snup, text="Take Photo Samples", command=pics, font=("berlin sans fb demi", 15, "bold"),
                              bg="orange", fg="black", bd=0, cursor="hand2", activebackground="black", activeforeground="orange")
            PhotoSamplesbtn.pack(pady=15)

            Backbtn = Button(snup, text="Back", command=snup_root, font=("berlin sans fb demi", 15, "bold"),
                              bg="orange", fg="black", bd=0, cursor="hand2", activebackground="black", activeforeground="orange")
            Backbtn.pack(pady=15)


        self.root = root  # initialising self
        self.root.title("Login")  # giving title to root window
        # setting screen size for root window
        self.root.geometry("530x290+500+300")
        self.root.configure(bg="black")

        loginlbl = Label(root, text="JARVIS LOGIN", font=(
            "berlin sans fb demi", 30, "bold"), fg="orange", bg="black")
        loginlbl.place(x=140, y=50)

        loginbtn = Button(root, text="Login", command=login, font=("berlin sans fb demi", 15, "bold"), bg="orange",
                          fg="black", bd=0, cursor="hand2", activebackground="black", activeforeground="orange", width=15)
        loginbtn.place(x=180, y=130)

        signupbtn = Button(root, command=signup, text="First time Sign Up", font=("berlin sans fb demi", 15, "bold"),
                           bg="orange", fg="black", bd=0, cursor="hand2", activebackground="black", activeforeground="orange", width=15)
        signupbtn.place(x=180, y=210)


if __name__ == "__main__":
    main()
