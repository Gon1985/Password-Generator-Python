import tkinter as tk
from tkinter import messagebox
import secrets
import string
import os


def generate_password():
    try:
        length = int(length_entry.get())

        characters = "0123456789"

       
        if special_var.get():
            characters += "!@#$%^&*()_-+={}[]|\:;'<>,.?/~`"

        
        if uppercase_var.get():
            characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        
        if lowercase_var.get():
            characters += "abcdefghijklmnopqrstuvwxyz"

        password = ''.join(secrets.choice(characters) for _ in range(length))
        password_var.set(password)

        
        password_history.append(password)
        if len(password_history) > 26:
            password_history.pop(0)  

    except ValueError:
        password_var.set("Error: Please enter a valid number")



def reset_password():
    password_var.set("")
    length_var.set("")


def confirm_close_program():
    result = messagebox.askquestion("Confirm close program", "Are you sure you want to close the program?")
    if result == 'yes':
        window.destroy()


def clear_password_history():
    password_history.clear()
    messagebox.showinfo("Password History Cleared", "Password history has been cleared.")


def show_about():
    global background_image_about
    if not is_window_open("About"):
        about_window = tk.Toplevel(window)
        about_window.title("About")
        about_window.geometry("510x100")
        about_window.resizable(False, False)

        
        background_image_about_path = os.path.join(current_dir, "images", "background4.png")
        try:
            background_image_about = tk.PhotoImage(file=background_image_about_path)
            background_label = tk.Label(about_window, image=background_image_about)
            background_label.place(relwidth=1, relheight=1)
        except tk.TclError as e:
            print(f"Error loading background image for About: {e}")

       
        icon_path = os.path.join(current_dir, "images", "icon.ico")

        
        if os.path.exists(icon_path):
            about_window.iconbitmap(icon_path)
        else:
            print(f"Icon not found at: {icon_path}")

        about_label = tk.Label(about_window, text=" PPG 1.0 \ This program was created by Gonzalo Ezequiel Temes in the year 2024\nKunker Studios RD", font=font_style, wraplength=300)
        about_label.pack(pady=20, padx=20)

#
def show_password_history():
    if not is_window_open("Password History"):
        history_window = tk.Toplevel(window)
        history_window.title("Password History")
        history_window.geometry("510x720")
        history_window.resizable(False, False)  

       
        background_image_history_path = os.path.join(current_dir, "images", "background2.png")
        try:
            background_image = tk.PhotoImage(file=background_image_history_path)
            background_label = tk.Label(history_window, image=background_image)
            background_label.place(relwidth=1, relheight=1)
        except tk.TclError as e:
            print(f"Error loading background image for Password History: {e}")

        
        icon_path = os.path.join(current_dir, "images", "icon.ico")

        
        if os.path.exists(icon_path):
            history_window.iconbitmap(icon_path)
        else:
            print(f"Icon not found at: {icon_path}")

        
        sorted_history = sorted(enumerate(password_history, start=1), key=lambda x: x[0], reverse=True)
        sorted_passwords = [f"{num}: {password}" for num, password in sorted_history]

        
        history_label = tk.Label(history_window, text="\n".join(sorted_passwords), font=font_style, fg="black")
        history_label.pack(pady=20, padx=20)

        
        clear_button = tk.Button(history_window, text="Clear History", command=clear_password_history, **button_style)
        clear_button.pack(pady=10)

        
        history_window.image = background_image


def show_help():
    global background_image_help
    if not is_window_open("Help"):
        help_window = tk.Toplevel(window)
        help_window.title("Help")
        help_window.geometry("510x720")
        help_window.resizable(False, False)

        help_window.configure(bg="#757575")

         
        background_image_help_path = os.path.join(current_dir, "images", "background3.png")
        try:
            background_image_help = tk.PhotoImage(file=background_image_help_path)
            background_label = tk.Label(help_window, image=background_image_help)
            background_label.place(relwidth=1, relheight=1)
        except tk.TclError as e:
            print(f"Error loading background image for Help: {e}")

        
        icon_path = os.path.join(current_dir, "images", "icon.ico")

        
        if os.path.exists(icon_path):
            help_window.iconbitmap(icon_path)
        else:
            print(f"Icon not found at: {icon_path}")

        help_text = "Welcome! This is the help section.\n\n" \
                    "1) First, enter a number of your preference in the length box.\n\n" \
                    "2) Then, press the 'Generate Password' button.\n\n" \
                    "You can also click on special characters, uppercase, and lowercase letters to create an even stronger password.\n\n" \
                    "3) Finally, you will be able to see the generated passwords by pressing the right button and accessing the password history.\n\n" \
                    "These created passwords are not stored; they are deleted when you close the program."

        text_frame = tk.Frame(help_window, bg="#757575")
        text_frame.pack(pady=20, padx=20)

        
        text_bg_color = "#d1d1d1"
        help_text_widget = tk.Text(text_frame, wrap="word", font=font_style, width=40, height=20, bg=text_bg_color)
        help_text_widget.insert(tk.END, help_text)
        help_text_widget.config(state="disabled")
        help_text_widget.pack()


def is_window_open(window_title):
    
    open_windows = window.winfo_children()
    for child in open_windows:
        if isinstance(child, tk.Toplevel) and child.title() == window_title:
            return True
    return False


window = tk.Tk()
window.title("Portable Password Generator")
window.geometry("510x720")
window.resizable(False, False)


frame = tk.Frame(window, bg="#161717")  

current_dir = os.path.dirname(os.path.abspath(__file__))
background_image_path = os.path.join(current_dir, "images", "background1.png")


try:
    background_image = tk.PhotoImage(file=background_image_path)
    background_label = tk.Label(window, image=background_image)
    background_label.place(relwidth=1, relheight=1)  
except tk.TclError as e:
    print(f"Error loading background image: {e}")


icon_path = os.path.join(current_dir, "images", "icon.ico")


if os.path.exists(icon_path):
    window.iconbitmap(icon_path)
else:
    print(f"Icon not found at: {icon_path}")


password_var = tk.StringVar()
length_var = tk.StringVar()


special_var = tk.BooleanVar()
uppercase_var = tk.BooleanVar()
lowercase_var = tk.BooleanVar()


password_history = []


font_style = ('Helvetica', 10)


length_label = tk.Label(window, text="Length:", font=font_style)
length_entry = tk.Entry(window, textvariable=length_var, font=font_style, width=30)  
password_label = tk.Label(window, text="Password:", font=font_style)
password_entry = tk.Entry(window, textvariable=password_var, show="", font=font_style, width=30)  


special_button = tk.Checkbutton(window, text="Special Characters", variable=special_var, font=font_style)
uppercase_button = tk.Checkbutton(window, text="Uppercase Letters", variable=uppercase_var, font=font_style)
lowercase_button = tk.Checkbutton(window, text="Lowercase Letters", variable=lowercase_var, font=font_style)


button_style = {'font': font_style, 'relief': tk.RAISED, 'bg': '#d61a1a', 'fg': 'white', 'activebackground': '#dbd7d7'}


generate_button = tk.Button(window, text="Generate Password", command=generate_password, **button_style)
reset_button = tk.Button(window, text="Reset", command=reset_password, **button_style)
close_button = tk.Button(window, text="Close", command=confirm_close_program, **button_style)


context_menu = tk.Menu(window, tearoff=0)
context_menu.add_command(label="About", command=show_about)
context_menu.add_command(label="Password History", command=show_password_history)
context_menu.add_command(label="Help", command=show_help)


window.bind("<Button-3>", lambda e: context_menu.post(e.x_root, e.y_root))


icon_path = os.path.join("images", "icon.ico")


if os.path.exists(icon_path):
    window.iconbitmap(icon_path)
else:
    print(f"Icon not found at: {icon_path}")


length_label.pack(pady=5)
length_entry.pack(pady=5)
password_label.pack(pady=10)
password_entry.pack(pady=10)


special_button.pack(pady=5)
uppercase_button.pack(pady=5)
lowercase_button.pack(pady=5)

generate_button.pack(pady=10)
reset_button.pack(pady=5)
close_button.pack(pady=5)


window.mainloop()
