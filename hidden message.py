# #sending a hidden message
# encrypt="dhanya"
# #reverse the string
# num=encrypt[::-1]
# vow="aeiou"
# x=''
# #replace the vowels using loops
# for i in num:
#     if(i in vow):
#         x+=str(vow.index(i))
#     else:
#         x+=i
# print(x+'aca')
#sending a hidden message
value=(input("enter a message"))
for i in value :
 print(chr(ord(i)+1))

