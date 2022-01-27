# let's build a program to measure our weight on different

#  planets and moons in our solar system
name= input("Name?\n")

print("okay " + name + ", are you planing to travel to a different planet, well you should probably know your how much you weigh there first")

weight = int(input("what is your weight in kgs?\n"))

Planets = "mercury, venus, mars, jupiter, saturn, neptune, uranus, moon "

print("Which planet or moon are you traveling to? Here are the options: \n" + Planets)

choice = input()

mercury_weight= round((weight/9.81)*3.7)

venus_weight= round((weight/9.81)*8.87)

mars_weight= round((weight/9.81)*3.711)

jupiter_weight= round((weight/9.81)*24.79)

saturn_weight= round((weight/9.81)*10.44)

neptune_weight= round((weight/9.81)*11.15)

uranus_weight= round((weight/9.81)*8.69)

moon_weight= round((weight/9.81)*1.622)



if choice == "mercury":
 
    print(f"your weight on  {choice} is {mercury_weight} kgs")

if choice == "venus":
 
    print(f"your weight on  {choice} is {venus_weight} kgs")

if choice == "mars":
 
    print(f"your weight on  {choice} is {mars_weight} kgs")

if choice == "jupiter":
 
    print(f"your weight on  {choice} is {jupiter_weight} kgs") 

if choice == "saturn":
 
    print(f"your weight on  {choice} is {saturn_weight} kgs")  

if choice == "neptune":
 
    print(f"your weight on  {choice} is {neptune_weight} kgs") 

if choice == "uranus":
 
    print(f"your weight on  {choice} is {uranus_weight} kgs")

if choice == "moon":
 
    print(f"your weight on  {choice} is {moon_weight} kgs")  

else:
    print("wrong input. Please try again.")
