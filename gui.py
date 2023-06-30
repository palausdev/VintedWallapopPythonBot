import customtkinter
import customtkinter as ctk

customtkinter.set_appearance_mode("dark")


def button_function():
    print('Button pressed')

def gui():
    root = ctk.CTk()
    root.geometry("750x450")
    root.title("SnapSell")
    root.iconbitmap(r'LogoSnapSellExe.ico')
    button = customtkinter.CTkButton(master=root, text="Button", command=button_function)
    button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

    return root.mainloop()