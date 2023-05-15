letter = '''Dear <|Name|>,
you perforn very well in coding competiton so
you are selcted!
Date : <|Date|> 
'''
name = input("Enter your name\n")
date = input("Enter date\n")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date )
print(letter)

