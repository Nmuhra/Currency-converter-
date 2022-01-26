# let's convert some currencies 

print("Hi, wanna convert some currencies?")

standard = "USD"

amount = int(input("Amount of USD?\n"))

currencies = "EUR, JPY, GBP, CAD, ZAR "

print("Which currency do you wanna convert your USD to? Here are the options: \n" + currencies)

choice = input()

EUR= round((amount*0.89))

JPY= round((amount*114.32))

GBP= round((amount*0.74))

CAD= round((amount*1.26))

ZAR= round((amount*15.2))

if currencies == "EUR":

    print(f"you will have{EUR} {choice}")

if currencies == "JPY":

    print(f"you will have{JPY} {choice}")

if currencies == "GBP":
    print(f"you will have{GBP} {choice}")

if currencies == "CAD":
    print(f"you will have{CAD} {choice}")

if currencies == "ZAR":
    print(f"you will have{ZAR} {choice}")
