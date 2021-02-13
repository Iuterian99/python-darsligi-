                                # Dictionary(lug'at)
"""
Dictionary (lug'at) bu tartiblanmagan, o'zgartiriladigan va indexlangan to'plamdir!
ularda kalitlar va qiymatlar saqlanadi!
"""
                                # Set
"""
Set bu tartiblanmagan va takrorlanmagan elementlardan tashkil topgan to'plam!                                
"""

car ={'model': 'kaptiva', 'color ': 'white'}
# print("Moshin turi: ", car['model'], "\nMoshin rangi: ", car['color '])

a = {}
a["name"] ="Abduhalim"
a["Surname"] ="Orziqulov"
# print("Egasi: ", a['name'], a['Surname'])
# keys => Dictionaryning keylari ':' belgidan chap tomonda turadi!
b = a.keys() # keys metodi dictionaryning keylarini qaytarib beradi!
# print(b) # natija: dict_keys(['name', 'Surname'])
b = list(a.keys()) #natija: ['name', 'Surname']
# print(b)
# print(a)
# values => Dictionaryning valuelari ':' belgidan o`ng tomonda turadi!
b = list(a.values())
# print(b)
b = a.values()
# print(b)
#pop metodi name nomli elementni 'a' dictionarydan o`chirib tashidi!
a.pop("name")
# print(a)
# 'in' metodi 'name' elementi 'a'dictionaryda bormi yoki yo`q aniqlab beradi!
b = 'name' in a
# print(b)
                        # 2ta dictionaryni bir biriga qo`shish
a = {'Ism ':'Abduhalim', 'Familya ':'Orziqulov'}
b = {'Tug`ilgan Yil ': '1999'}
c = a.update(b)
# print( a)
# print(a.items()) # ".items" bu lug`atdagi barcha elementlarni chiqarib beradi!
telefonlar = {
    'ali':'iphone 12',
    'malik': 'nokia 6300',
    'sarvar': 'samsung S10e'
}
for key, value in telefonlar.items():
    print(f"{key.title()} ning telefoni {value}")



                        # Set

# 'set' => (to`plam) ni listdan farqi to`plamda duplicate(bir hil son) takroran bo`lmidi!
# 'set' ketma ketligda saqlamaydi!
# a = {'model' : 'Damas'} => Dictionary, a = {'model', 'Damas'} => Set

colors = {'yellow', 'red', 'black'}
# print(type(colors))  # natija: <class 'set'>
colors = set()
# print(type(colors))  # natija: <class 'set'>
colors = {'yellow', 'red', 'black'}
colors.add("blue")   # colors setiga blue elementini qo`shadi!
# print(colors)
colors.remove("black") # Setdan black elementini o`chirib tashidi!
# print(colors)
                    # Setning ustida amallar!

# union 'A' va 'B' setdagi bor elementlarni barchasini oladi!
A = {1, 2, 3, 4}
B = {1, 2, 4, 8}
union = A.union(B)
# print(union)

# intersection ikki listdagi umumiy elementlarni chiqarib beradi!
A = {1, 2, 3, 4}
B = {1, 2, 4, 8}
intersection = A.intersection(B)  # The same with intersection = B.intersection(A)
# print(intersection)

# A.difference(B) 'A' da bo`lgan lekin 'B' da bo`lmagan elementni chiqarib beradi!
A = {1, 2, 3, 4}
B = {1, 2, 4, 8}
difference = A.difference(B)
# print(difference)

# B.difference(A) 'B' da bo`lgan lekin 'A' da bo`lmagan elementni chiqarib beradi!
A = {1, 2, 3, 4}
B = {1, 2, 4, 8}
difference = B.difference(A)
# print(difference)

# ", ".join(Grades.keys()) makes the code more awesome!
Grades = {
'Azim ' : 35,
'Bobur' : 45,
'Alisher' : 50
}
# print("Best Students of the group are: ", ", ".join(Grades.keys()))

# "|" (= union) belgisi bir nechta setni union yani birlashtiradi!
a = {1, 2, 3, 4}
b = {1, 4, 6, 7}
c = {3, 4, 6, 9}
d = a|b|c # a, b, va c setda bo`lgan barcha elementlarni chiqarib beradi!
# print(d)

