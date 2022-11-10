#creating a quiz
print("hello, welcome to quiz mania!")
name=input("provide your name : ")
one=input("who is the president of India?")
two=input("how many districts are there in karnataka?")
three=input("what is the capital of australia?")
firstanswer = "Droupadi Murmu"
secondanswer = "31"
thirdanswer = "Canberra"
print("")
if one == firstanswer:
    print("1.Correct")
else:
    print("1.Incorrect")
if two == secondanswer:
    print("2.Correct")
else:
    print("2.Incorrect")
if three == thirdanswer:
    print("3.Correct")
else:
    print("3.Incorrect")
    print("")

print("Thank you "+name+" for playing this quiz!")