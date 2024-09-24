from PIL import Image
import win32print
import win32ui
from win32con import DM_COPY

def print_image(image_path, printer_name, print_area_width_mm, print_area_height_mm):
    # Конвертируем мм в пиксели
    dpi = 203  # Принтеры TSC часто используют 203 dpi
    width_px = int(print_area_width_mm / 25.4 * dpi)
    height_px = int(print_area_height_mm / 25.4 * dpi)

    # Открываем изображение
    image = Image.open(image_path)
    image = image.resize((width_px, height_px), Image.LANCZOS)

    # Сохраняем изображение в формате, подходящем для печати
    temp_file = "temp_print_image.bmp"
    image.save(temp_file, "BMP")

    # Открываем принтер
    hPrinter = win32print.OpenPrinter(printer_name)
    try:
        # Получаем информацию о принтере
        pDevMode = win32print.GetPrinter(hPrinter, 2)["pDevMode"]
        pDocInfo = ("Print Job", None, "RAW")

        # Начинаем документ
        win32print.StartDocPrinter(hPrinter, 1, pDocInfo)
        win32print.StartPagePrinter(hPrinter)

        # Настраиваем контекст устройства
        hDC = win32ui.CreateDC()
        hDC.CreatePrinterDC(printer_name)
        hDC.StartDoc("Print Job")
        hDC.StartPage()
        
        # Загружаем изображение для печати
        bmp = win32ui.CreateBitmap()
        f = open(temp_file, 'rb')
        bmp.LoadBitmapFile(f)
        hDC.DrawBitmap(bmp.GetHandle(), (0, 0, width_px, height_px))
        hDC.EndPage()
        hDC.EndDoc()
        hDC.DeleteDC()

        win32print.EndPagePrinter(hPrinter)
        win32print.EndDocPrinter(hPrinter)
    finally:
        win32print.ClosePrinter(hPrinter)

if __name__ == "__main__":
    print_image("testBitmap.bmp", "TSC TE300", 58, 40)
