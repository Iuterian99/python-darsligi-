 # Salom deydigan greeting nomli funksiya tuzing va unga docstring yozing!
def greeting(name):
    print(f"Assalomu aleykum {name}!")
    """Foydalanuvchi ismini qabul qilib unga salom beruvchi Funksiya"""
salom = input("Ismingiz nima ? ")
greeting(salom.title())


