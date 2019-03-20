# For loop
# A loop statement allows us to execute a statement or group of statements multiple times. 
friends = ["Apple", "Banana", "Cherries", "Dates"]
for index in range(len(friends)):
   print(friends[index])

   # conditional statement check inside foor loop
   if index == 0:
       print("First")
   else:
       print("Not First")