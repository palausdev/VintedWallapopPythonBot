import customtkinter
from tkinter import Tk, PhotoImage
from PIL import Image
from wallapop import addProductSM
from config import wallapopData, wallapopCategorySwitch, wallapopSubcategorySwitch, wallapopSpecifySwitch, wallapopConditionSwitch

customtkinter.set_appearance_mode("dark")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1550x825")
        self.title("SnapSell")
        self.iconbitmap(r'LogoSnapSellExe.ico')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame = customtkinter.CTkFrame(self)
        self.frame.grid(row=0, column=0, padx=0, pady=(0, 0), sticky="nsw")

        # Images
        self.home = customtkinter.CTkImage(dark_image=Image.open("icons/home.png"),
                                           size=(32, 32))
        self.logo = customtkinter.CTkImage(dark_image=Image.open("icons/logo.png"),
                                           size=(32, 32))
        self.config = customtkinter.CTkImage(dark_image=Image.open("icons/config.png"),
                                           size=(32, 32))

        # add widgets to app
        #self.label = customtkinter.CTkLabel(self.frame, image=self.logo, text="", width=1)
        #self.label.grid(row=1, column=0, padx=1, pady=(1, 0), sticky="w")

        self.button = customtkinter.CTkButton(self.frame, image=self.home, text="", width=1, hover=True, hover_color="#27bed5", fg_color="transparent", command=self.button_click)
        self.button.grid(row=2, column=0, padx=1, pady=(1, 0), sticky="w")

        self.configbtn = customtkinter.CTkButton(self.frame, image=self.config, text="", width=1, hover=True,
                                              hover_color="#27bed5", fg_color="transparent", command=self.button_click)
        self.configbtn.grid(row=10, column=0, padx=1, pady=(1, 2), sticky="w")

    # add methods to app
    def button_click(self):
        addProductSM(wallapopData(1)[1], wallapopData(1)[2], wallapopData(1)[3],
                     wallapopData(1)[4], wallapopData(1)[5],
                     wallapopCategorySwitch(wallapopData(1)[6]),
                     wallapopSubcategorySwitch(wallapopData(1)[6], wallapopData(1)[7]),
                     wallapopSpecifySwitch(wallapopData(1)[6], wallapopData(1)[7],
                                           wallapopData(1)[8]),
                     wallapopConditionSwitch(wallapopData(1)[9]),
                     wallapopData(1)[10], wallapopData(1)[11], wallapopData(1)[12],
                     wallapopData(1)[13], wallapopData(1)[14], "https://discord.com/api/webhooks/1119628512597377024/KCYXUjQ3oR_vuxEt65qJd3_iMPA6_sNGTg-4mCbIvrktwEkUjSl8xGh3xCksOvllUGAs")
        print("button click")

app = App()
app.mainloop()