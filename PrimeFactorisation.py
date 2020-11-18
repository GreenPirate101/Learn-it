print("Hi guys! The integer should be between 1-30 both inclusive")
x0=int(input("Enter the Integer "))
if x0==0:
  print("there are no prime factors for '0'")
elif x0>30:
  print("this integer is greater than '30', Sorry :(")
elif x0<0:
  print("hey no negative numbers :(")
else:
#2
   if x0%2==0:
      a1=1
      x1=x0/2
      if x1%2==0:
       a1=a1+1
       x2=x1/2
       if x2%2==0:
        a1=a1+1
        x11=x2/2
        if x11%2==0:
         a1=a1+1
   else:
      a1=0
#3
   if x0%3==0:
      a2=1
      x3=x0/3
      if x3%3==0:
       a2=a2+1
       x4=x3/3
       if x4%3==0:
        a2=a2+1
   else:
      a2=0
#5
   if x0%5==0:
      a3=1
      x5=x0/5
      if x5%5==0:
       a3=a3+1
       x6=x5/5
       if x6%5==0:
        a3=a3+1
   else:
      a3=0
#7
   if x0%7==0:
      a4=1
      x7=x0/7
      if x7%7==0:
       a4=a4+1
       x8=x7/7
       if x8%7==0:
        a4=a4+1
   else:
      a4=0
#11
   if x0%11==0:
      a5=1
      x9=x0/7
      if x9%11==0:
       a5=a5+1
       x10=x7/7
       if x10%7==0:
        a5=a5+1
   else:
      a5=0
#13
   if x0%13==0:
      a6=1
      x11=x0/7
      if x11%13==0:
       a6=a6+1
       x12=x11/13
       if x12%13==0:
        a6=a6+1
   else:
      a6=0
#17
   if x0%17==0:
      a7=1
      x13=x0/7
      if x13%17==0:
       a7=a7+1
       x14=x13/17
       if x14%17==0:
        a7=a7+1
   else:
      a7=0
#19
   if x0%19==0:
      a8=1
      x15=x0/19
      if x15%19==0:
       a8=a8+1
       x16=x15/17
       if x16%17==0:
        a8=a8+1
   else:
      a8=0
#23
   if x0%23==0:
      a9=1
      x17=x0/23
      if x17%23==0:
       a9=a9+1
       x18=x17/23
       if x18%23==0:
        a9=a9+1
   else:
      a9=0
#29
   if x0%29==0:
      a10=1
      x19=x0/29
      if x19%29==0:
       a10=a10+1
       x20=x19/29
       if x20%29==0:
        a10=a10+1
   else:
      a10=0

   print("Prime Factors:- ","2^",a1," 3^",a2," 5^",a3," 7^",a4," 11^",a5," 13^",a6," 17^",a7," 19^",a8," 23^",a9," 29^",a10)
