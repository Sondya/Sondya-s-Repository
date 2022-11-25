import statistics

mas = ['H','O','M','E','N','K','O']
x = statistics.multimode(mas)
print (x)

skaits = len(mas)
print("skaits = ", skaits)

if (skaits % 2 == 1):
    #nepara skaits
    vid = int(skaits/2)
    med = ord(mas[vid])
else:
    #ja ir para skaits
    vid = int(skaits/2)
    med = (ord(mas[vid-1]) + ord(mas[vid]))/2

print("mediana = ",med)
print(vid)

    



