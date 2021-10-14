sir='A B C D E F G H I J K L M N O P Q R S T U V W X Y'
s1=' '
s2=' '
s3=' '
for i in sir:
    if (ord(i)>=65)and(ord(i)<=89):
        s1+=chr(ord(i)+1)
    else:
        s1+=i
print("Inlocuieste litele de la 'A' pana la 'Y' prin urmatoarea litera din alfabet: \n",s1)
for i in s1:
    if i=='Z':
        s2+="A"
    else:
        s2+=i
print("Inlocuieste fiecare litera Z cu A: \n",s2)
for i in sir:
    if i==' ':
        s3+='-'
    else:
        s3+=i
print("Fiecare spatiu se inlocuieste prin '-': \n",s3)