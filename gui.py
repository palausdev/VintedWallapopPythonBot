import customtkinter
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
        # add widgets to app
        self.button = customtkinter.CTkButton(self.frame, text="Tus muertos",width=5 ,command=self.button_click)
        self.button.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

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