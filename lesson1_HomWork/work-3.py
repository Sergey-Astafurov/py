x = int(input("Введи Х :"))
y = int(input("Введи У :"))

if x > 0 :
   if y > 0 :
      print("1")
   else:
      print("4")
elif x < 0:
   if y < 0 :
      print("3")
   else:
      print("2")