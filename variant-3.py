import os
import platform
import subprocess

def get_printers():
    current_os = platform.system()
    printers = []

    if current_os == 'Linux' or current_os == 'Darwin':
        try:
            result = subprocess.run(['lpstat', '-p'], stdout=subprocess.PIPE, text=True)
            printers = [line.split()[1] for line in result.stdout.splitlines() if line.startswith('printer')]
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при получении списка принтеров: {e}")
    
    elif current_os == 'Windows':
        try:
            result = subprocess.run(
                ['powershell', '-Command', 'Get-Printer | Select-Object Name'], 
                stdout=subprocess.PIPE, text=True)
            printers = [line.strip() for line in result.stdout.splitlines() if line.strip()]
        except Exception as e:
            print(f"Ошибка при получении списка принтеров: {e}")
    
    return printers

def select_printer(printers):
    if not printers:
        print("Нет доступных принтеров.")
        return None
    
    print("Доступные принтеры:")
    for idx, printer in enumerate(printers, start=1):
        print(f"{idx}. {printer}")
    
    choice = input("Выберите принтер по номеру: ")
    
    try:
        choice_idx = int(choice) - 1
        if 0 <= choice_idx < len(printers):
            return printers[choice_idx]
        else:
            print("Неверный выбор принтера.")
            return None
    except ValueError:
        print("Пожалуйста, введите номер принтера.")
        return None

def print_pdf(file_path, printer):
    current_os = platform.system()
    
    if not printer:
        print("Принтер не выбран. Печать отменена.")
        return

    if current_os == 'Linux' or current_os == 'Darwin':
        try:
            subprocess.run(['lp', '-d', printer, file_path], check=True)
            print(f"Печать {file_path} отправлена на принтер {printer}.")
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при отправке на печать: {e}")
    
    elif current_os == 'Windows':
        try:
            # Используем os.startfile для отправки файла на печать
            os.startfile(file_path, "print")
            print(f"Печать {file_path} отправлена на принтер {printer}.")
        except Exception as e:
            print(f"Ошибка при отправке на печать: {e}")
    
    else:
        print(f"Операционная система {current_os} не поддерживается для автоматической печати.")

# Основной код
file_path = '1.pdf'  # Укажите путь к вашему PDF файлу
printers = get_printers()

if printers:
    selected_printer = select_printer(printers)
    if selected_printer:
        print_pdf(file_path, selected_printer)
