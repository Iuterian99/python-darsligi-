# Kerakli malumotlar!
# Ctrl+Alt+L  kodni ko'rinishi yaxshilaydi
# Ctrl+D o'zi joylashgan qator yoki belgilangan sohadan nusxa oladi
# Alt yordamida bir paytda kursorni bir nechta joyga joylashtirish mumkin
# Alt+J orqali belgilangan qismning pastdagi ishlatilgan qismlarini belgilaydi
# Shift+F6 refactor qilish
# Ctrl+F bitta fayldan izlash
# Ctrl+Shift+F butun project yoki uning modullari bo'yicha izlash
# Ctrl+R bu replace uchun
# Ctrl + shift + J 2 ta qatorni bitta qilib, ishlatilmay qogan keraksiz qatorlarni o`chiradi!
#
# 6-dars List va Tuple

"""
List - [1, 4, 9]
List -> Hajmi dinamikli o`zgaradigan, bir nechta ma`lumotlar kolleksiyasini saqlash uchun mo`ljallangan ma`lumot turi!
Tuple -(1,4,9)
Tuple -> Hajmi o`zgarmaydigan bir nechta ma`lumotlar kolleksiyasini saqlash uchun mo`ljallangan ma`lumot turi!
"""
empty_list = [1, 3, 5, 7, 9, 11, 13, 15]
son = min(empty_list)
# print(son)
empty_tuple = (2, 4, 6, 8, 10)
son1 = min(empty_tuple)
# print(son1)
total = sum(empty_list)
# print(total)
# print(empty_tuple[-1])

# List va tuple ustida bajariladigan amallar!
# nums = [1, 3, 5, 7]
#  "length = len(nums) nums ni elementlar sonini aniqlab beradi!\n"     natija: 4
#  max = max(nums) nums ning eng katta qiymatini aniqlaydi!             natija: 7
# min = min(nums) nums ning eng kichik qiymatini aniqlaydi !            natija: 1
# total = sum(nums) nums dagi elementlar yig`indisini chiqarib beradi!  natija: 16
#

# Indexing
"""
  nums = [1, 3, 5, 7]
 index -> 0  1  2  3        
print(nums[1]) 1-index o`rindagi list elementni chiqarib beradi ! natija: 3
"""
# nums = [1, 3.5, 5, 7]
# #index->0  1  2  3
# print(nums[1:3])
# print(nums)
# Slicing (kesib olish)

"""
nums = [ 1, 3, 5, 7]
print(nums[1:3]) nums listdagi 1-indexdan to 3-endexgachon elementlarni chiqarib beradi 3-indexdagi element kirmaydi!
"""


                                #listning metotlari

# append -> oxiriga element qo`shadi!
nums = [2, 4, 6, 8]
nums.append(12)
# print(nums)
# clear ->barcha elementlarni o`chirib tashlaydi!
nums.clear()
# print(nums)
# copy -> listdan nusxa qaytaradi!
nums = [2, 4, 6, 2, 8, 2]
nums.copy()
# print(nums)
# arrayname.count(n) -> arrayname listidagi 'n' lar sonini aniqlab beradi!
nums.count(2) # nums listidagi 2 lar nechtaligini sanab beradi
# print(nums)
# extend nums listiga [11, 12, 13] elementlarini qo`shadi!
nums.extend([11, 12, 13])
# print(nums) # Natija [2, 4, 6, 2, 8, 2, 11, 12, 13]
# print(nums[1]) # 1-index o`rindagi list elementni chiqarib beradi ! natija: 3
# range -> 1 dan boshlab 10gachon sonlarni chiqarib beradi!
numbers = list(range(1, 10))
# print(numbers)
# insert -> adds an element into users array!
users = ["ali", "vali", "sobir"]
users.insert(1,"Bill") # 1-indexda Bill so`zini yozib beradi!
# print(users) # natija: [ 'ali', 'bill', 'vali', 'sobir']
# pop -> listdagi elementni o`chirish uchun ishlatiladi!
users.pop(3) # 3-indexdagi stringni o`chirib beradi!
# print(users) #natija ['ali', 'Bill', 'vali']
# remove -> [-1] yani oxxirgi elementni o`chirib beradi!
last_user = users[-1]
users.remove(last_user)
# print(users) #natija: ['ali', 'Bill']

# deleting exact element from array!
users = ["ali", "vali", "sobir"]
item = "vali"
if item in users:
    users.remove(item)
    # print(users)

# 'count' listda yani arrayda 1 xil qiymat necchi marta qatnashganini aniqlaydi!
a = [1, 2, 3, 3, 3, 1]
# print(a.count(3))

                     #listdagi eng katta va eng kichik elementni topish usuli
# long_name = max(words, key=len)   # ctrl + p => bizga funksiya qila olishi mumkin bo`lgan jadvalni chiqarib beradi!
# print(long_name)
# short_name = min(words, key=len)
# print(short_name)

                                    #Guessing game

# guess_secret = 4
# guess_number = 0
# guess_limit = 3
# while guess_number < guess_limit:
#     guess = int(input("enter: "))
#     guess_number += 1
#     if guess == guess_secret:
#         print("you won!")
#         break
# else:
#     print("Sorry, you failed!")


# salary_employees = ['O`ktam, Dilrabo, Shohruh, Abduhalim, Sardor,']
# print(salary_employees)
# print("salom "*10) # salom so`zini 10 marta chiqarib beradi
# numbers = list(range(10))
# print(numbers)

                   # checksiz list yaratish usuli
a = []
b = []
a.append(b)
# print(a)
b.append(a)
# print(b)

                    # Matrix ->Two or three dimensional array
#list ichida list(nested)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
print(matrix[0])  # nolinchi indexdagi element ya`ni listni qaytarib beradi: [1, 2, 3]

a = [1, 2, 3, 4, 5]
b = 1 in a # 'in' 1 elementi a listda bormi degani
print(b)