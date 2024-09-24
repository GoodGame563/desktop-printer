from pdf2image import convert_from_path
import os
from PIL import Image
import win32print
import win32api
import win32net
import psutil
import socket
import win32com.client


def convert_from_pdf_to_image(pdf_path):
    images = convert_from_path(pdf_path)
    os.makedirs("image", exist_ok=True)
    for i in range(len(images)):
        images[i].save('image\\page'+ str(i) +'.png', 'PNG')
        
    return len(images)

def rotate_image(image_path, angle = 90):
    image = Image.open(image_path)
    rotated_image = image.rotate(angle, expand=True)
    rotated_image.save(image_path)

def get_mac_address(ip):
    try:
        pid = socket.gethostbyname(ip)
        arp = psutil.net_if_addrs()
        for iface_name, iface_addresses in arp.items():
            for address in iface_addresses:
                if address.family == socket.AF_INET and address.address == pid:
                    mac = address.mac
                    return mac
    except Exception as e:
        return None

def get_printers():
    printers = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)
    for printer in printers:
        printer_name = printer[2]
        print(printer)
        print(f"Printer Name: {printer_name}")
        
        try:
            hprinter = win32print.OpenPrinter(printer_name)
            printer_info = win32print.GetPrinter(hprinter, 2)
            port_name = printer_info['pPortName']
            print(f"Port: {port_name}")
        
            status = printer_info['Status']
            attributes = printer_info["Attributes"]
            if status == 0 and (attributes & win32print.PRINTER_ATTRIBUTE_WORK_OFFLINE) == 0:
                print("Printer is available")
            else:
                print(f"Printer status code: {status}")
            
            # Получение MAC-адреса, если принтер сетевой
            if '://' in port_name:  # Указывает, что принтер сетевой (например, подключен по IP)
                ip_address = port_name.split('://')[-1].split(':')[0]
                mac_address = get_mac_address(ip_address)
                if mac_address:
                    print(f"MAC Address: {mac_address}")
                else:
                    print(f"Failed to get MAC Address for {ip_address}")
            else:
                print("Printer is local, MAC address not applicable.")
            
            win32print.ClosePrinter(hprinter)
        except Exception as e:
            print(f"Error retrieving info for printer {printer_name}: {e}")
        print()

def print_pdf(file_path, printer_name):
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден.")
        return

    try:
        win32print.SetDefaultPrinter(printer_name)
        win32api.ShellExecute(0, "print", file_path, None, ".", 0)
        print(f"Файл {file_path} отправлен на принтер {printer_name}.")
    except Exception as e:
        print(f"Ошибка при отправке на печать: {str(e)}")


get_printers()