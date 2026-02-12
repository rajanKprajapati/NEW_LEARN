"""Hard 2:
Create FileReader base class with read()
Subclasses:

PDFReader

ExcelReader

CSVReader
Call all using one loop."""



class FileReader:
    def read(self):
        print("Main file reader")

class PDFReader(FileReader):
    def read(self):
        print("pdf reader")

class ExcelReader(FileReader):
    def read(self):
        print("Excel reader")

class CSVReader(FileReader):
    def read(self):
        print("CSV reader")

obj_list=[PDFReader(),ExcelReader(),CSVReader()]

for obj in obj_list:
    obj.read()
