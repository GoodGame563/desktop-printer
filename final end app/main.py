import customtkinter as ctk
from tkinter import messagebox
from PIL import Image, ImageTk

# Initialize customtkinter
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Main application class
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Авторизация")
        self.geometry("800x600")

        self.create_login_screen()

    def create_login_screen(self):
        """Create the login screen"""
        self.login_frame = ctk.CTkFrame(self)
        self.login_frame.pack(pady=100, padx=100)

        # Load and display the logo image in the top-left corner
        logo_image = Image.open("logo.png")  # Replace with your image path
        logo_image = logo_image.resize((50, 50), Image.LANCZOS)
        self.logo_photo = ImageTk.PhotoImage(logo_image)

        logo_label = ctk.CTkLabel(self.login_frame, image=self.logo_photo, text="")  # Image with no text
        logo_label.pack(anchor="nw", padx=10, pady=10, side="left")

        # "Авторизация" label (replacing the old "THE ONE MARKET")
        auth_label = ctk.CTkLabel(self.login_frame, text="Авторизация", font=ctk.CTkFont(size=20, weight="bold"))
        auth_label.pack(pady=(0, 30))

        # Username and password fields
        self.username_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Логин")
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Пароль", show="*")
        self.password_entry.pack(pady=10)

        # Login button
        login_button = ctk.CTkButton(self.login_frame, text="ВОЙТИ", command=self.login)
        login_button.pack(pady=20)

    def login(self):
        """Handles login button click and moves to main screen"""
        # In a real-world app, you'd verify login credentials here
        self.login_frame.pack_forget()
        self.create_main_screen()

    def create_main_screen(self):
        """Create the main screen with the print queue"""
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Table Header
        table_header = ["Очередь для печати", "ID", "Имя", "Маркетплейс", "Код", "Принтер", "Пример", "Пример"]
        for idx, header in enumerate(table_header):
            label = ctk.CTkLabel(self.main_frame, text=header)
            label.grid(row=0, column=idx, padx=5, pady=5)

        # Table Body (Sample Data)
        for i in range(1, 9):
            for j in range(8):
                entry = ctk.CTkLabel(self.main_frame, text=f"Пример {i}")
                entry.grid(row=i, column=j, padx=5, pady=5)

        # Buttons for "Manage Printers" and "Send to Print"
        manage_printers_button = ctk.CTkButton(self.main_frame, text="Управление принтерами", command=self.show_printer_management)
        manage_printers_button.grid(row=10, column=0, columnspan=4, pady=20)

        send_to_print_button = ctk.CTkButton(self.main_frame, text="Отправить на печать", command=self.show_confirmation_popup)
        send_to_print_button.grid(row=10, column=4, columnspan=4, pady=20)

    def show_confirmation_popup(self):
        """Show confirmation popup for sending to print"""
        confirmation = ctk.CTkToplevel(self)
        confirmation.geometry("300x150")
        confirmation.title("Подтверждение")

        label = ctk.CTkLabel(confirmation, text="Подтвердите отправку на печать")
        label.pack(pady=20)

        confirm_button = ctk.CTkButton(confirmation, text="Подтвердить", command=confirmation.destroy)
        confirm_button.pack(pady=10)

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

    def discover_printer(self):
        """Simulate printer discovery"""
        messagebox.showinfo("Обнаружение", "Новый принтер найден!")

# Create the application instance
if __name__ == "__main__":
    app = App()
    app.mainloop()
