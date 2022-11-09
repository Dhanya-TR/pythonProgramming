print("hello,I am a chatbot")
print("how may i help you\n")
print("hit 1 for cricket")
print("hit 2 for customer care")
print("hit 3 for news")
print("hit 4 for daily horoscope")
print("hit 5 for english novel")
#accepting our request
userinput=int(input("enter your choice:"))
#using nested if to process the user input
if userinput==1:
   inputneeded=input("provide country name")
if userinput==2:
    inputneeded=input("provide your query")
if userinput==3:
    inputneeded=input("provide the your interest")
if userinput==4:
    inputneeded=input("provide your zodiac")
if userinput==5:
    inputneeded = input("provide your genre")
print("thank you for using  our service,our team will get back to you soon")