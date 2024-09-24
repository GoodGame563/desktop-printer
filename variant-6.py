# В этом примере кода показано, как распечатать диапазон страниц из файла PDF в Python.
import aspose.pdf as ap

# Создать объект PDFViewer
viewer = ap.facades.PdfViewer();

# Открыть входной PDF-файл
viewer.bind_pdf("1.pdf");

# Установить атрибуты для печати
viewer.auto_resize = True
viewer.auto_rotate = True
viewer.print_page_dialog = False

# Создайте объекты для настроек принтера и страницы и PrintDocument.
pgs = ap.printing.PageSettings();
ps = ap.printing.PrinterSettings();

# Установить имя принтера
ps.printer_name = "TSC TE300";

#ps.print_range = ap.printing.PrintRange.SOME_PAGES;
#ps.from_page = 1;
#ps.to_page = 2;

# Установите размер страницы (если требуется)
pgs.paper_size = ap.printing.PaperSize("A8", 234, 160);

# Установите PageMargins (если требуется)
pgs.margins = ap.devices.Margins(0, 0, 0, 0);

# Распечатайте документ, используя настройки принтера и страницы.
for i in range(0,5):
    viewer.print_document_with_settings(pgs, ps);



# Закрыть PDF-файл
viewer.close();
