import json


def user_add():
    user = {
        "first_name": input("First Name"),
        "last_name": input("Last Name"),
        "Email: input("Email),
            }
        file = open ('database/user.json', 'r') as file:
        all_users_data_json = file.read()
        print(all_users_data_json)
        all_users_data=json.loads(all_users_data_json)
        print(all_users_data)
        file.close()
        all_users_data.append(user)
        print(all_users_data)
        with open('database/user.json') as file:
            file.write()
