def db(name, age, sex):
    hashVal = 0
    nameVal = len(name)
    sexVal = 0
    if (sex == 'F'):
        sexVal = 1
    hashVal = nameVal + age + sexVal
    return hashVal % 6

print(db('Erika', 44, 'F'))

