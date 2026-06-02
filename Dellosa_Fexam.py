import openpyxl as op

wbk = op.Workbook()
sheet = wbk.active 

sheet["A1"] = "Order ID"
sheet["B1"] = "Customer name"
sheet["C1"] = "Product"
sheet["D1"] = "Quantity"
sheet["E1"] = "Price"
sheet["F1"] = "Total"

sheet["A2"] = "1"
sheet["B2"] = "Juan Dela Cruz"
sheet["C2"] = "Burger"
sheet["D2"] = "2"
sheet["E2"] = "75"
sheet["F2"] = "150"

sheet["A3"] = "2"
sheet["B3"] = "Maria Santos"
sheet["C3"] = "Fries"
sheet["D3"] = "3"
sheet["E3"] = "50"
sheet["F3"] = "150"

sheet["A4"] = "3"
sheet["B4"] = "Carlo Reyes"
sheet["C4"] = "Pizza"
sheet["D4"] = "1"
sheet["E4"] = "350"
sheet["F4"] = "350"

sheet["A5"] = "4"
sheet["B5"] = "Angela Lopez"
sheet["C5"] = "Milktea"
sheet["D5"] = "4"
sheet["E5"] = "120"
sheet["F5"] = "480"

sheet["A6"] = "5"
sheet["B6"] = "Kevin Ramos"
sheet["C6"] = "Spaghetti"
sheet["D6"] = "2"
sheet["E6"] = "95"
sheet["F6"] = "190"

wbk.save("ordersDB.xlsx")