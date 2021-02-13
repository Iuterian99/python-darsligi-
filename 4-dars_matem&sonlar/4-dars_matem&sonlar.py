import math
x = 0.112861
print(type(x)) # float
# complex son deb kvadrat ildiz ostidagi -1 son olinadi
# complex sonlar "j" bilan yoziladi
y = 10+5j
print(type(y))
print(y)

                            # type conversion (data typni o`zgartirish)

# convert from int to float
a = 10; # x is integer
b = float(a) # we are converting from float into integer
print(b)

# convert from float to int
pi = 3.14 # floating point number
c = int(pi) # we are converting
print(c) # output is 3 because it removes decimal numbers
# convert from int to complex
d = complex(a) # we can convert from int to complex but we can`t convert from complex to int!
print(d)

                                    # converting from string to int
num = "15" # data type is string
print(type(num))
num = int(num) # We are converting from string to int
print(type(num)) # data type is int>

                                    # Arithmetic operators
"""
+ (qo`shish) x+y
- (Ayrish) x-y
* (ko`paytirish) x*y
/ (bo`lish) x/y bo`lganda kasr qismi bilan chiqarib beradi
% (modulus) ikki sonni bo`lganda qoldiqni topish x%y
// (qoldiqsiz bo`lish) faqat butun qismini chiqarib beradi x//y
** (Darajaga oshirish) x**y
"""
x = 12
y = 7
print(x/y)
print(x//y)
print(x%y)
print(x**y)

                                # built-in funksiyalar

# round(x, y) 'x' ning verguldan keyingi 'y' xonasigacha yaxlitlaydi
num = 3.1415973123
print(round(num, 2)) # natija 3.14 chunki verguldan keyin 2tasini qoldirib qoganini tashab yuboradi
num = 136.213
print(round(num, -2)) # natija 100 chunki '-2' verguldan oldingi 2ta sonni yaxlitlashni boshlaydi 3<5 va 100

# abs(x) 'x' ning musbat qiymatini qaytaradi
son = -13
print(abs(son)) # natija 13

# max(x,y) 'x' va 'y' ning eng kattasini qaytaradi
x = 24.5
y = 13.7
print(max(x,y)) # natija 24.5

# min(x,y) 'x' va 'y' ning eng kichigini qaytaradi
print(min(x,y)) # natija 13.7

# pow(x, y) 'x' ning 'y' darajasini chiqarib beradi
x = 3
y = 4
print(pow(x,y)) # natija '81' chunki 3*3*3*3=81

                                    # Math library

"""
Biz math libraryni pycharmga qo`shish uchun "import math" ni kiritishimiz kk!
ceil(x) 'x'ning tepadan eng yaqin qiymatini qaytaradi!
 floor(x) 'x' ning pastdan eng kichik qiymatini qaytaradi!
 gcd(x,y) 'x' va 'y'ning EKUBini qaytarib beradi!
 exp(x) Yevklit sonininig x-darajasini qaytaradi!
 prod(x,y) x va y ning ko`paytmasini qaytaradi!
 remainder(x,y) 'x' ni 'y' ga bo`lganda qoldig`ini qaytaradi!
 pow(x,y) 'x' ning 'y'-darajasini qaytaradi
 sqrt(x) 'x' ninig kvadrat ildizini qaytaradi
 log(x[,base]) x ning natural logarifmni qaytaradi, base orqali asosini o`zgartirish mumkin
 log2(x) 'x' ning 2 asosli logarifmini hisoblaydi
 log10(x) 'x' ning 10- asosli logarifmini  hisoblaydi
"""
print(math.sqrt(16))
print(math.log(27,3)) # '27' '3' ning nechinchi darajasi
print(math.floor(14.99999))
print(math.gcd(15,31))
print(math.e**2)
print(math.exp(2))
                        # Trigonometrik funksiyalar
"""
sin(x) 'x' ning radian qiymatidagi sinusini aniqlaydi
cos(x) 'x' ning radian qiymatidagi kosinusini aniqlaydi
tan(x) 'x' ning radian qiymatidagi taginusini aniqlaydi
asin(x) 'x' ning radian qiymatidagi arksinusini aniqlaydi
degrees(x) "x"ni radiandan gradusga o`tkazadi
radians(x) "x" gradusdan radianga o`tkazadi
"""




