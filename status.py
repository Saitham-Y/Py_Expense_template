

def get_infos():
    filename = open('expense.csv', 'r')
    file = csv.DictReader(filename)
    spender = []
    involved = []
    for col in file:
        spender.append(col['spender'])
        involved.append(col['involved'])
    print(user)
    filename.close()
    return spender, involved

def get_user():
    filename = open('users.csv', 'r')
    file = csv.DictReader(filename)
    user = []
    for col in file:
        user.append(col['name'])
    print(user)
    if (len(user) == 0):
        raise ValueError('There are no current user')
    filename.close()
    return user

def status():
    user = get_user()
    spender, involved = get_infos()
    l = []
    for i in range(len(user)):
        l.append([])
        for j in range(len(involved)):
            if (user[i] in involved[j] and !(user[i] != spender[j]):
                return