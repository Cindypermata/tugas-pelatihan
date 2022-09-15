#Menghitung luas permukaan dan volumme kubus
print("Menghitung luas permukaan dan volume kubus")

s = int(input("Panjang rusuk = "))

luas = 6*s*s
volume = s*s*s 

print("Luas permukaan kubus =", luas)
print("Volume kubus =", volume)


#Menghitung luas permukaan dan volume balok
print("Menghitung luas permukaan dan volume balok")

p = int(input("Masukkan panjang = "))
l = int(input("Masukkan lebar = "))
t = int(input("Masukkan tinggi = "))

luas = 2*((p*l)+(p*t)+(l*t))
volume = p*l*t

print("Luas permukaan balok =", luas)
print("Volume balok =",volume)