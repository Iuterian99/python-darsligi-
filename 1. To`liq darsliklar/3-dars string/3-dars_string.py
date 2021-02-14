                                # string to`liq
"""
biz stringni ' '(bittalik qo`shtirnoq),
 " "(ikkitalik qo`shtirnoq), yoki """ """(3talik qo`shtirnoq ko`p qatorli matn yozishda ) 
  amallari ostida yozishimiz mumkin!
"""
ism = 'Abduhalim'
print(ism)
ism = "Abduhalim Orziqulov"
print(ism)
ism = """Mening ismim Abduhalim
familyam esa Orziqulov
"""
print(ism)
# stringni uzunligini aniqlash
length = len("Abduhalim")
print(length)
# string indexing
name = "Sardor"
     #  012345
print(name[-1]) # [-son] so`zni orqadan sanab boshlidi
print(name[:3]) # output is "Sar" as index starts from zero and ":3" is from zero index to second index
print(name[4:7])
# concatenation(ulash)
name = "Asila"
about = "Mening ismim "+name
print(about)
# lower() barcha harflarni kichigiga almashtiradi
a="HELLO WORLD"
print(a.lower())
# upper() barcha harflarni kattasiga o`tkazib beradi
b="malika"
print(b.upper())
# title() barcha so`zlarning birinchi harfini katta qiladi
c="toshkent shahridagi inha universiteti"
print(c.title())
# strip string boshidagi va oxiridagi bo`sh kataklarni yo`qotib beradi
d="   men zo`r pragramist bo`laman    "
print(d.strip())
# dir- string malumot turi metodlarini ko`rish,
# help- string malumot turi dokumentatsiyasi orqali metodlarni aniqlash va o`rganish
print(dir(name))
print(help(name))
# string formatting
name = "Abduhalim"
age = "21"
about = "mening ismim {}, yoshim {} da"
print(about.format(name, age))
about = f"mening ismim {name}, yoshim {age} da"
print(about)
# escape characters
"""
"\" escape character
"\\" backslash
"\n" new line
"\r" carriage return
"\t" tab
"\b" backspace
"\f" form Feed
"\ooo" Octal value
"\Xhh" hex value
"""