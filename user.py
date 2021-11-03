from PyInquirer import prompt
import csv
user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },
    {
        "type":"input",
        "name":"age",
        "message":"New User - Age: ",
    }
]

def add_user():
    infos = prompt(user_questions)
    file = open('users.csv', "a")
    field_names = ['name', 'age']
    writer = csv.DictWriter(file, fieldnames=field_names, delimiter=',')
    writer.writerow(infos)
    file.close()
    print("User Added !")
    return True