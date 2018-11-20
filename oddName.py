"""Hello, my name is Myo Min Htwe"""
name = input("Enter name: ")
while len(name) <1:
    print ("Enter character: ")
    name = input("Enter name")
for i in range(0,len(name),2):
    print(name[i])
