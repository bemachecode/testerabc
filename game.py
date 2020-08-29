varname = "hello"

varinx = input("what is your name? " + "\n")

print("hello " + varinx)

varina = ("please choose one of the following \n(a) \n(b) \n(c) \n(d) \n => ")

varinb = input(varina)
if varinb == "a":
	print("a means odds and evens \n")
	game = "a"
elif varinb == ("b"):
	print("b")
elif varinb == ("c"):
	print("c")
elif varinb == ("d"):
	print("d")
else:
	print("not a valad answer")

if game == "a":
	varinc = input("pick a low number \n=>")
	varind = input("pick a high number \n=>")
	for x in range(int(varinc),int(varind)):
		if (int(x) % 2 == 0):
			print(str(x) + " is even")
		else: 
			print(str(x) + " is odd")

print("thank you for playing Jack \n goodbye my new friend")
