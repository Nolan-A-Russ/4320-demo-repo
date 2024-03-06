
for i in range (1,100+1):
   if i%3==0 and i%5==0:
       print("FizzBuzz")
       i+=1
       continue
   elif i%3==0:
       print ("Fizz")
       i+=1
       continue
   elif i%5==0:
       print ("Buzz")
       i=+1
       continue
   else:
       print (i)
       i+=1
