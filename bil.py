# Skriv ett program som låter användaren mata in en int.
# Du ska räkna och skriva ut vad talet * 2, talet * 3 och talet *4 blir.
# Ex: 
# Mata in ett tal:
# 17                        <--- Detta matar användaren in
# 17 * 2 = 34
# 17 * 3 = 51
# 17 * 4 = 68

tal = input("Mata in ett tal")
print(f"{tal} * 2 = {tal * 2}")
print(f"{tal} * 3 = {tal * 3}")
print(f"{tal} * 4 = {tal * 4}")

for tal in range(2,5):
    print(f"{tal} * 2 = {tal * 2}")





listOfPoints = []
for index in range(1,6):
    tal = float(input(f"Poäng från domare {index}:"))
    listOfPoints.append(tal)

sum = 0
biggest = listOfPoints[0]
smallest = listOfPoints[0]

for tal in listOfPoints:
    sum = sum + tal
    if tal > biggest:
        biggest = tal
    if tal < smallest:
        smallest = tal

total = sum - biggest - smallest
medel = total / 3

print(f"{round(medel,3)}")






def calcLetters(listaMedord:list)->int:
    antal = 0
    for one in listaMedord:
        antal = antal + len(one)
    return antal

cities = [ "Stockholm", "Göteborg", "Malmö", "Köpenhamn", "London"]
antal = calcLetters(cities)
print(f"Totala antalet är {antal}")













# x = input("Mata in en text")
# badWords = ["work", "job", "boss", "vegetables", "fish"]
# x = x.replace("work", "****")
# x = x.replace("job", "****")
# x = x.replace("boss", "*****")
# x = x.replace("vegetables", "*****")
# x = x.replace("fish", "*****")
# print(x)


x = input("Mata in en text")
badWords = ["work", "job", "boss", "vegetables", "fish"]
for ord in badWords:
    x = x.replace(ord, "****")
print(x)





def isValidPassword(password:str)->bool:
    if len(password) != 8:
        return False
    return True    

if isValidPassword("12345#123"):
    print("Ja")
else:    
    print("Nej")


def isValidRegno(regno:str)->bool:
    if len(regno) != 6:
        return False
    if not regno[0].isalpha():
        return False
    if not regno[1].isalpha():
        return False
    if not regno[2].isalpha():
        return False
    if not regno[3].isdigit():
        return False
    if not regno[4].isdigit():
        return False

    if  regno[5].isdigit() or regno[5].isalpha():
        return True

    return False

x = input("Mata in bilreg")
if isValidRegno(x):
    print("Ja")
else:    
    print("Nej")

    
