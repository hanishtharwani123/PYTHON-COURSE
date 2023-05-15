# Use open function to rsed the content of a file
f = open('sample.txt', 'r')   # By default the mode is r
data = f.read("r")
print(data)
f.close()