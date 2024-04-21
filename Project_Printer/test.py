from datetime import date
from datetime import datetime
from classes import Order, Orders, Printers, Storage
#=====================================================================

printer=Printers("fhh",5600,"bj","jjj",5,"ggg","gh")
printer.print()
str=printer.join()
print(str)
setPrinter = Printers("",0,"","",0,"","")
setPrinter.set(str)
setPrinter.print()

print(printer.get("name"))
print(printer.get("price"))
print(printer.get("printing"))
print(printer.get("technology"))
print(printer.get("weight"))
print(printer.get("brend"))
print(printer.get("country"))

printer.edit("name", "new-name")
printer.edit("printing", "mew-printing")
printer.edit("price", 600.5)
printer.edit("technology", "new-technology")
printer.edit("weight", 8.2)
printer.edit("brend", "new-brand")
printer.edit("country", "new-country")

printer.print()

