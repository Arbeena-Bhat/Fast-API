def add(firstName:str|None,lastName:str=None):
    if(firstName!=None):
     return firstName.title()+" "+lastName.title()
firstName="bill"
lastName="gates"
name=add(firstName,lastName)
print(name)

