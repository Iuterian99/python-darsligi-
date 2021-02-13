                        # 6-dars 1-uyga vazifa

# My_list = ['Dadam: O`ktam ', 'Onam: Dilrabo', 'Akam: Shoxrux', 'O`zim: Abduhalim', 'Ukam:  Sardor']
# for elem in My_list:
#     print(elem)

                        # 2-uyga vazifa

# Standart kiruvchi ma'lumotdagi vergul bilan ajratilgan so'zlar ketma-ketligini teskari tartibda chiqaradigan dastur tuzing
# Masalan:      Ismlar: john, alice, bob
#                         Natija: bob, alice, john


# names = input("input the names that you want to reverse: ")
# changed = names.split(", ")
# tag1 = "Entered inputs are: "
# # print(tag1, changed)
# changed.reverse() # reverse bu orqadagi elementlarni oldinga ko`chirib beradi!
# tag2 = "Reversed inputs are: "
#  print(tag2, changed)

                        # 3-uyga vazifa

# Standart kiruvchi ma'lumotdagi vergul bilan ajratilgan so'zlar ketma-ketligini alifbo tartibida chiqaradigan dastur tuzing
# Masalan:  Ismlar: john, alice, bob
#   Natija: alice, bob, john

# names = input("input the names that you want to reverse: ")
# changed = names.split(", ")
# tag1 = "Entered inputs are: "
# print(tag1, changed )
# a = input("input the element name of the list: ")
# if a == names:
#     names.count(a) # sort elementi alifbo bo`yicha saralaydi!
#     tag2 = "Alphabetical ordered inputs are: "
#     print(tag2, changed)

                    # 4-uyga vazifa

# names = input("Please input the names: ")
# changed = names.split(sep=", ")
# print(changed)
# chosen_name = input("input the name you want to find its index: ")
#
# if chosen_name in changed:
#     index = changed.index(chosen_name)
#     print(index)
# else:
#     print("not found in list")

                            # 5-uyga vazifa

names = input("Please input the names: ")
changed = names.split(sep=", ")
chosen_name = input("input the name you want to find its repitation: ")
print(changed.count(chosen_name))
