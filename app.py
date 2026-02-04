values = [1,2.23,5,7,2,30,15]
print(values[0])
print(values[6])
for i in values:
    print(i)

number = int(input("Pick a Number"))
if number%2 == 0:
    print("even")
else:
    print("odd")

print("What is your bill")
tip = (input("How was the service?"))
if tip == "great":
    [print(number*float(1.25))]
elif tip == "good":
    [print(number*float(1.2))]
elif tip == "okay":
    [print(number*float(1.15))]
elif tip == "bad":
    [print(number)]


def discount(age,isResident,isMember):
    age = (input("What is your age?"))
    isResident = (input("Are you a resident"))
    if isResident == "yes":
        isResident == True
    else:
        isResident == False
    if discount(age >= 65 or age < 12) and discount(isResident == True or isMember == True):
        print("The person is valid for discount")
    else:
        print("The person is not valid for discount")
