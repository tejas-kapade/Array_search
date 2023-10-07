print("Make array and search its elements")

#this function for returning index value or -1 to make sure value not found
#i used VS code to push changes...

def main(array , index):
    length = len(array)

    for a in range(length):
        if(array[a] == index):
           return a
        else:
           return -1

array = []
       
while True:
  volume = int(input("How Much  length  Of Your Array? \n "))
  for i in range(volume):
     values = int(input("Enter Number of index__"))
     array.append(values)
  print(array)
  search = int(input("Which num you want to find? __"))
  result = main(array , search)
  if(result == -1):
     print("Value Does Not Found")
  else:
     print("Index of value is _",result)
  restart = input("Wanna continue to search ? y/n __")
  if(restart == "n"):
      print("Programme stopped")
      break
