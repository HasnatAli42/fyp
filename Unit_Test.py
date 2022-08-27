
# print("Upper =",1500 * 1.005)
# print("Lower =",1500 * 0.995)
# if (1500 * 0.995) <= 1501 <= (1500 * 1.005):
#     print(True)
# else:
#     print(False)

list = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]
# pop_symbol = liat.index(6)
# print(pop_symbol)

# for x in list:
#     print(x)
#     list.remove(x)
#     print(list)
# try:
#     while list:
#         print(list[0])
#         list.remove(11)
#         print(list)
# except Exception as e:
#     print(e)

a_variable = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,10]

class checkwhatammarsaid:

    def __init__(self):
        self.a_variable = a_variable

    def emptyvariable(self):
        self.a_variable = []
    def resetvariuable(self):
        self.a_variable = a_variable

checkwhatammarsai = checkwhatammarsaid()
print(checkwhatammarsai.a_variable)
checkwhatammarsai.emptyvariable()
print(checkwhatammarsai.a_variable)
checkwhatammarsai.resetvariuable()
print(checkwhatammarsai.a_variable)
