
# Working with files

twoFile_Open = open("firstText.txt", "r")
if twoFile_Open.readable():
    print("File is readable")
    print(twoFile_Open.read())
else:
    print("File is not readable")


twoFile_Open.close()
print("Entire file was read")
print()
print()
# Reading all lines in a file
twoFile_Open = open("firstText.txt", "r")
for employee in twoFile_Open.readlines():
    print(employee)
twoFile_Open.close()
print("All individual lines were read")

# Adding employees to a file through user input
twoFile_Open = open("firstText.txt", "a")
print()
userInput = input("Enter employee name: ")
twoFile_Open.write("\n" + userInput)
twoFile_Open.close()


