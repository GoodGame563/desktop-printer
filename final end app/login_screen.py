import customtkinter as ctk
import asyncio 
from tkinter import messagebox
from PIL import Image, ImageTk
from connection_server import enter
from CTkTable import *



ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Авторизация")
        self.geometry("1000x680")
        self.minsize(1000,600)
        self.configure(fg_color="white")

        self.create_login_screen()

    def show_confirmation_popup(self):
        confirmation = ctk.CTkToplevel(self)
        confirmation.geometry("300x150")
        confirmation.title("Подтверждение")

        label = ctk.CTkLabel(confirmation, text="Подтвердите отправку на печать")
        label.pack(pady=20)

        confirm_button = ctk.CTkButton(confirmation, text="Подтвердить", command=confirmation.destroy)
        confirm_button.pack(pady=10)

    def clear_window(self):
        for widget in self.slaves():
            widget.destroy()

    def create_main_screen(self):
        """Create the main screen with the print queue"""
        self.main_frame = ctk.CTkScrollableFrame(self)
        self.main_frame.grid(row = 1, column = 0, padx = 20, pady=20, columnspan=2,sticky="NSEW")
        self.grid_columnconfigure(1, weight=1)
        

        
        table_header = [["Очередь для печати", "USB", "Имя", "Маркетплейс", "Код", "Принтер", "Пример", "Пример"]]
        table = CTkTable(master=self.main_frame, row=5, column=5, values=table_header)
        table.grid(row=0, column=0,pady=10, sticky="NSEW")

        # Buttons for "Manage Printers" and "Send to Print"
        #manage_printers_button = ctk.CTkButton(self.main_frame, text="Управление принтерами", command=self.show_printer_management)
        #manage_printers_button.grid(row=10, column=0, columnspan=4, pady=20)

        #send_to_print_button = ctk.CTkButton(self.main_frame, text="Отправить на печать", command=self.show_confirmation_popup)
        #send_to_print_button.grid(row=10, column=4, columnspan=4, pady=20)


    def show_printer_management(self):
        """Show a list of printers in a popup"""
        printer_management = ctk.CTkToplevel(self)
        printer_management.geometry("400x300")
        printer_management.title("Управление принтерами")

        label = ctk.CTkLabel(printer_management, text="Принтеры подключенные к компьютеру")
        label.pack(pady=10)

        printers = [("01213123113", "Проводное", "Подключен"), ("01213163113", "Беспроводное", "Подключен")]

        for idx, (mac, connection_type, status) in enumerate(printers):
            row_text = f"MAC: {mac} | Тип подключения: {connection_type} | Статус: {status}"
            printer_label = ctk.CTkLabel(printer_management, text=row_text)
            printer_label.pack(pady=5)

        # Button for discovering new devices
        discover_button = ctk.CTkButton(printer_management, text="Обнаружение нового устройства", command=self.discover_printer)
        discover_button.pack(pady=20)
    
    def create_login_screen(self):
        logo_image = ctk.CTkImage(light_image=Image.open("logo.png"), dark_image=Image.open("logo.png"), size=(150,50))

        image_label = ctk.CTkLabel(master=self, image=logo_image, text="")
        image_label.grid(row = 0, column = 0, padx = 20, pady=20,sticky="NSEW" )

        self.login_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.login_frame.grid(row = 1, column = 0, padx = 20, pady=20, columnspan=2,sticky="NSEW")
        self.grid_columnconfigure(1, weight=1)

        auth_label = ctk.CTkLabel(self.login_frame, text="Авторизация", font=ctk.CTkFont(size=48))
        auth_label.pack(pady=(30, 60))

        self.username_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Логин", width=564, height=85, font=('normal', 24))
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Пароль", show="*", width=564, height=85, font=('normal', 24))
        self.password_entry.pack(pady=10)

        login_button = ctk.CTkButton(self.login_frame, text="ВОЙТИ", fg_color="#6C75FE", text_color="#FFFFFF", corner_radius=12, font=('normal', 24), width=291, height=65, command=self.login)
        login_button.pack(pady=20)

    def show_confirmation_popup(self, message):
        confirmation = ctk.CTkToplevel(self)
        confirmation.geometry("300x150")
        confirmation.title("Подтверждение")

        label = ctk.CTkLabel(confirmation, text=message)
        label.pack(pady=20)

        confirm_button = ctk.CTkButton(confirmation, text="Ok", command=confirmation.destroy)
        confirm_button.pack(pady=10)

    def login(self):
        
        
        status, final_str = asyncio.run(enter(self.username_entry.get(), self.password_entry.get()))
        if status != 1:
            self.show_confirmation_popup(final_str)
        else:
            with open("token.txt", "w") as file:
                file.write(final_str)
            self.login_frame.pack_forget()
            self.clear_window()
            self.create_main_screen()
            
        
        
        #self.create_main_screen()

if __name__ == "__main__":
    app = App()
    app.mainloop()