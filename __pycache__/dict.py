person = {'name':'smjeon', 'address':'Cheonan', 'email':'b612jsm@hanmail.net'
}
print(person)
print(person['name'])
print(person['email'])
print(person.items())
for key, value in person.items():
    print("\nKey : " + key)
    print("Value : " + value)