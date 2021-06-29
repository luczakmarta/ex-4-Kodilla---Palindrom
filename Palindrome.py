#napisanie funkcji, która sprawdza, czy dany wyraz jest palindromem. Przykłady to “kajak” i “potop”.
#Zaprogramuj funkcję, która przyjmuje jeden argument (typu string) i zwraca wartość boolean: True/False, mówiącą czy podany tekst jest palindromem.
def isPalindrome(p):
    return p == p[::-1]

p = "Marta"
word = isPalindrome(p)

if word:
    print("True")
else:
    print("False")

#ale jak to zrobić z input?