from datetime import datetime


current_datetime = datetime.now()
print(current_datetime)

curr_now_1 = (current_datetime.day, current_datetime.month)
curr_now_2 = (current_datetime.day+1, current_datetime.month)
curr_now_3 = (current_datetime.day+2, current_datetime.month)
curr_now_4 = (current_datetime.day+3, current_datetime.month)
curr_now_5 = (current_datetime.day+4, current_datetime.month)
curr_now_6 = (current_datetime.day+5, current_datetime.month)
curr_now_7 = (current_datetime.day+6, current_datetime.month)


d1 = datetime(year=2022, month=5, day=27)
curr_b1 = (d1.day, d1.month)

d2 = datetime(year=2002, month=5, day=27)
curr_b2 = (d2.day, d2.month)

d3 = datetime(year=2001, month=5, day=28)
curr_b3 = (d3.day, d3.month)

d4 = datetime(year=2000, month=5, day=29)
curr_b4 = (d4.day, d4.month)

d5 = datetime(year=2001, month=5, day=30)
curr_b5 = (d5.day, d5.month)

d6 = datetime(year=2001, month=5, day=31)
curr_b6 = (d6.day, d6.month)

d7 = datetime(year=1991, month=4, day=30)
curr_b7 = (d7.day, d7.month)

users = [{'name': 'Vasya', 'birthday': curr_b1},
         {'name': 'Kolya', 'birthday': curr_b2}, {'name': 'Dasha', 'birthday': curr_b3}, {'name': 'Pasha', 'birthday': curr_b4}, {'name': 'Vitya', 'birthday': curr_b5}, {'name': 'Polya', 'birthday': curr_b6}, {'name': 'Dima', 'birthday': curr_b7}]


def get_birthdays_per_week(users):

    users_birthdays1 = ['Monday', ]
    users_birthdays2 = ['Tuesday', ]
    users_birthdays3 = ['Wednesday']
    users_birthdays4 = ['Thursday', ]
    users_birthdays5 = ['Friday', ]
    users_birthdays6 = ['Saturday', ]
    users_birthdays7 = ['Sunday (Greetings on Monday)']
    for user in users:
        for _, value in user.items():
            if curr_now_1 == user.get('birthday'):
                users_birthdays1.append(value)
            if curr_now_2 == user.get('birthday'):
                users_birthdays2.append(value)
            if curr_now_3 == user.get('birthday'):
                users_birthdays3.append(value)
            if curr_now_4 == user.get('birthday'):
                users_birthdays4.append(value)
            if curr_now_5 == user.get('birthday'):
                users_birthdays5.append(value)
            if curr_now_6 == user.get('birthday'):
                users_birthdays6.append(value)
            if curr_now_7 == user.get('birthday'):
                users_birthdays7.append(value)

    return [users_birthdays1, users_birthdays2, users_birthdays3, users_birthdays4, users_birthdays5, users_birthdays6, users_birthdays7]


print(get_birthdays_per_week(users))
