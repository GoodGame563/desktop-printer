from pdf2image import convert_from_path
from PIL import Image
import serial

PORT = 'COM1'  # Замените на ваш последовательный порт
BAUDRATE = 9600

def print_image(image):
    with serial.Serial(PORT, BAUDRATE, timeout=1) as ser:
        # Преобразование изображения в формат, понятный принтеру TSC
        # Настройки для печати изображения должны быть установлены согласно документации принтера
        image = image.convert('1')  # Преобразуем в черно-белое изображение
        # Отправляем изображение в принтер
        # Потребуется дополнительная обработка для корректной передачи данных
        # К примеру, можно использовать специальные команды для передачи изображения в принтер
        pass

def print_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    for image in images:
        print_image(image)

if __name__ == '__main__':
    print_pdf('1.pdf')
