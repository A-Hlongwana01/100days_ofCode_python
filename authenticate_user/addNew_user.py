import authenticate_user.signUp as signUp, query as q

# from openpyxl import workbook, load_workbook


# def addToData(info):
#     wb = load_workbook("example.xlsx")
#     ws = wb.active
#     ws.append(info)
#     wb.save('example.xlsx')

# info = signUp.run()
# addToData(info)
# print("Added successfully")k

def addToData(info):
    q.myQuery(info)
    


info = signUp.run()
addToData(info)
print("Added successfully")