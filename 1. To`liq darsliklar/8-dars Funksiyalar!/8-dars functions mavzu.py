                        # Funksiya bu nima?
# def greet("parameter" is used for receiving info inside function):
# greet("argument" is actual information that we supply to these functions)
# interprator o`zi tushunadigan va bilgan funksiyalar "built in funksiyalar" deyiladi!
"""
Funksiya bu- dasturdagi block ichiga olingan va nomlangan amallar ketma-ketligi!
funksiyani xohlagan payt istagancha chaqirish mumkin! 
"None" is an object that returns absence of a value!
biz bunksiyalada "from" reserved keywordini ishlata olmaymiz!
"""
                    # Arbitrary funksiyalar!
"""
Agar funksiyaga nechta argument berishi kerakligini bilmasak, u holda kiruvchi parameter oldida "*" belgisini qo`yamiz!
shu holda siz funksiyani chaqirganda kiruvchi parametrga bir nechta argument (to`plam) berishingiz mumkin!
"""
# def max_numbers(*nums):
   # print("max numbers are ", max(nums))

# max_numbers(1, 2, 3, 5, 4, 4, 3, 4,2)

# def average(*nums): # "*" belgisi istalgancha argument berishga ruxsat beradi!
#     print(type(nums), nums)
#     return sum(nums) / (len(nums))
# a = average(1, 2, 3, 4, 5, 6)
# print(a)

                            # Keyword argument!

"""
Biz har bir argumentni nomi bilan berib qo`ya olamiz
"""
def greeting(name, from_):
    print(f"Hello {name} from {from_}!")

# greeting(name= "Abduhalim", from_= "Inha rector") # keyword belgilashda order(tartib) ni ahamiyati yo`q!

# def sending_email(to, text):
#     print("To:", to)
#     print("Text:", text)
# sending_email(to="Abduhalim.orziqulov@bk.ru", text="Siz in shaa Alloh O`zbekistondagi eng kuchli dasturchi bo`lasiz!")

                    # Arbitrary keyword Arguments, **kwargs

"""
Agar funksiya argumentlari uchun nechta nom keragligini bilmasangiz 
unga funksiya elon qilinayotganda parametr nomi oldidan "**" belgisini qo`yish kifoya!
"""

def default_value(lang = "Python"):
    print(f"I am learning {lang}!")
# default_value() # argument kiritmasak default value yani "python" ni qabul qiladi!
# default_value("Java")  # argument kiritsak default valueni o`rnini egallaydi!
# default_value(input("Enter the language! ")) # default_value funksiyasi uchun input so`rayopmiz!

def dockstring_yozish(n):
    """Dockstring 3ta qo`shtirnoq ichiga yoziladi! va unda biz funksiya haqida malumot berishimiz mumkin!
    bu funksiya 'n' argument qabul qilib uni kvadratini qaytaradi"""
    return n*n
# print(dockstring_yozish(3))
# help(dockstring_yozish(3))

                                # TRY and except!

"""
"try" and "except" blocks are used for avoiding crushes of a program!
"""
try:
    age =int(input("input your age: "))
    print(age)
    income = 2000
    print(income/age)
except ZeroDivisionError:
    print("age cannot be zero!")
except ValueError:
    print("Wrong input") # if we input string not integer program does not crushes instead it shows "Wrong input"


