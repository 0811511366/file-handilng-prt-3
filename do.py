# write in file using with()funtion
with open('this.txt','w') as file:
    file.write("Hi! how is science.")
file.close()

# split file into words
with open('this.txt','r') as file:
    data = file.readlines()
    print("Words in this file are....")
    for line in data:
        word = line.split()
        print (word)
file.close()