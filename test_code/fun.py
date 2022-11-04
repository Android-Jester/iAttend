from datetime import datetime as dt
import json

path = (r'test_code\\data_json.json')
# with open(path,'r') as f:
#     c = json.load(f)
# print(len(c))

def country_names(path:str):
    with open(path,'r') as data:
        json_data = json.load(data)
    country_list = []
    for country_name in range(len(json_data)):
        country_list.append(json_data[country_name]['Name'])
    return country_list

d = country_names(path)
print(d)
    
# from posixpath import splitext

# def print_document(self):
#         self.printer = QPrinter(QPrinter.HighResolution)
#         self.dialog = QPrintDialog(self.printer, self)
#         if self.dialog.exec_() == QPrintDialog.Accepted:
#             self.handlePaintRequest(self.dialog.printer())

#     def print_preview_dialog(self):
#         printer = QPrinter(QPrinter.HighResolution)
#         self.dialog = QPrintPreviewDialog(printer, self)
#         self.dialog.paintRequested.connect(self.handlePaintRequest)
#         self.dialog.exec_()

#     def handlePaintRequest(self, printer):
#         document = QTextDocument()
#         doc_cursor = QTextCursor(document)
#         table = doc_cursor.insertTable(self.ui.tableWidget.rowCount(),self.ui.tableWidget.columnCount())
#         for row in range(table.rows()):
#             for col in range(table.columns()):
#                 doc_cursor.insertText(self.ui.tableWidget.item(row,col).text())
#                 doc_cursor.movePosition(QTextCursor.NextCell)
#             document.print_(printer)

# print(dt.now().date().strftime('%a-%b-%d'))
# year=int(dt.now().date().strftime('%Y'))
# month =int(dt.now().date().strftime('%m'))
# day = int(dt.now().date().strftime('%d'))
# print(day)

# print(dt.now().time().strftime('%H:%M:%S %p'),'\n')
# print(dt.now().date().strftime('%Y-%m-%d'))
# date=dt.now().date().strftime('%d-%m-%Y')
# time=dt.now().time().strftime('%I:%M:%S %p')

# # date = int('2022-7-10')

# def reconstruct_date(date:str):
#         list_months = ['January', 'Febuary', 'March',
#                 'April', 'May', 'June', 'July',
#                 'August', 'September', 'October',
#                 'November', 'December']
#         date_value=str(date).split('-')
#         year = date_value[0]
#         day = date_value[2]
#         month = date_value[1]
#         month=list_months[int(month)-1]
#         return str(day+' '+month+' '+year)
        
# d = reconstruct_date('2024-10-10')
# print(d)

# year=int(dt.now().date().strftime('%Y'))
# month =int(dt.now().date().strftime('%m'))
# day = int(dt.now().date().strftime('%d'))

# if int(end[0]) >= year :
#     print('Valid')
#     print(int(end[0])-year)
# else:
#     print('Invalid')



# b = None
# if b:
#     print(b)
# else:
#     pass
# import os
# path = 'C:\\ProgramData\\iVision\\redolf'

# if not os.path.exists(path):
#     os.makedirs(path)

# import winsound
# winsound.PlaySound(r'test_code\\sound\\mixkit-confirmation-tone-2867.wav',winsound.SND_FILENAME)
# winsound.Beep(1000,400)

# list_months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# print(list_months[int(end[1])],',',int(end[0]))
# print(list_months[int(date[1])])

# n =9.9
# if isinstance(n,int):
#     print(n)
# else:
#     pass



