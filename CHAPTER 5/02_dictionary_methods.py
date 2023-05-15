myDict = {
    "fast": "In a Quick Manner", 
    "harry": "A Coder",
    "marks": [1, 2, 3]
}

# dictionary methods
print(myDict.keys())
print(myDict.values())
print(myDict.items())
print(myDict.values())

updateDict = {
    "hanish": "a politician who belives in secularism",
    "modi": "the prime minister of india"
} 
myDict.update(updateDict)
print(myDict)

print(myDict.get("harry"))     # return none as harry2 is not presnt in the dictionary
print(myDict["harry2"])         # throws an error as harry2 is not present in the dictionary
