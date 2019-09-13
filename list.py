thislist = ["apple", "banana", "cherry"]
print(thislist);

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

a = "apple, banana, cherry"
thislist = a.split(",")
#thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print("string->"+ x.strip()+" ; "+"length->"+ str(len(x.strip())))  
  