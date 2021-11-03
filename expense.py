from PyInquirer import prompt
import csv

def get_spenders():
    filename = open('users.csv', 'r')
    file = csv.DictReader(filename)
    user = []
    for col in file:
        user.append(col['name'])
    if (len(user) == 0):
        raise ValueError('There are no current user')
    filename.close()
    return user

def get_involved():
    filename = open('users.csv', 'r')
    file = csv.DictReader(filename)
    user =  [{
            'name': n['name'],
            'checked': False
        }
        for n in file
    ]
    filename.close()
    return user

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": get_spenders(),
    },
    {
        'type': 'checkbox',
        'message': 'Select Involved',
        'name': 'involved',
        'choices': get_involved()
    }

]

def add_repartition(infos):
    amount = infos['amount']
    infos['repartition'] = []
    for i in range(len(infos['involved'])):
        infos['repartition'].append(int(amount)/len(infos['involved']))

def new_expense(*args): 
    infos = prompt(expense_questions)
    file = open('expense.csv', "a")
    field_names = ['amount', 'spender','label', 'involved', 'repartition']
    add_repartition(infos)
    writer = csv.DictWriter(file, fieldnames=field_names, delimiter=',')
    writer.writerow(infos)
    print("Expense Added !")
    return True


