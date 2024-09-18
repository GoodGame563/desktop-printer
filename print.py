import os
import win32print
import win32api

def list_printers():
    # Получение списка всех доступных принтеров
    printers = [printer[2] for printer in win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)]
    return printers

def select_printer(printers):
    # Показ списка принтеров и выбор пользователем
    print("Доступные принтеры:")
    for idx, printer in enumerate(printers, start=1):
        print(f"{idx}. {printer}")
    
    choice = int(input("Выберите принтер по номеру: ")) - 1
    if choice < 0 or choice >= len(printers):
        print("Неправильный выбор принтера.")
        return None
    return printers[choice]

def print_pdf(file_path, printer_name):
    # Проверка существования файла
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден.")
        return

    # Печать файла через выбранный принтер
    try:
        win32print.SetDefaultPrinter(printer_name)
        win32api.ShellExecute(0, "print", file_path, None, ".", 0)
        print(f"Файл {file_path} отправлен на принтер {printer_name}.")
    except Exception as e:
        print(f"Ошибка при отправке на печать: {str(e)}")

if __name__ == "__main__":
    # Получаем список принтеров
    printers = list_printers()

    if not printers:
        print("Принтеры не найдены.")
    else:
        # Пользователь выбирает принтер
        selected_printer = select_printer(printers)
        if selected_printer:
            pdf_file_path = "1.pdf"  # Замените на путь к вашему PDF-файлу
            print_pdf(pdf_file_path, selected_printer)
