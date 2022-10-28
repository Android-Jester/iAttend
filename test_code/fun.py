from datetime import datetime as dt
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

print(dt.now().time().strftime('%H:%M:%S %p'),'\n')
print(dt.now().date().strftime('%Y-%m-%d'))

date = '2022-7-10'
date = date.split('-')

end = '2023-08-30'
end = end.split('-')

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

import winsound
winsound.PlaySound(r'test_code\\sound\\mixkit-confirmation-tone-2867.wav',winsound.SND_FILENAME)
# winsound.Beep(1000,400)

# list_months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
# print(list_months[int(end[1])],',',int(end[0]))
# print(list_months[int(date[1])])

# n =9.9
# if isinstance(n,int):
#     print(n)
# else:
#     pass

m = []
print(int())

