def avg_user_time(stream):    
    data, views = zip(*(s.split(';') for s in stream))
    users, date = zip(*(r.split(',') for r in data))
    users_cnt = len(set(users))
    views_cnt = tuple(map(int, views))
    result = sum(views_cnt) / users_cnt
    print(f'Среднее количество просмотров на уникального пользователя: {result}')
    
stream = [
    'user4,2021-01-01;3',
    'user3,2022-01-07;4',
    'user2,2022-03-29;1',
    'user1,2020-04-04;13',
    'user2,2022-01-05;7',
    'user1,2021-06-14;4',
    'user3,2022-07-02;10',
    'user4,2021-03-21;19',
    'user4,2022-03-22;4',
    'user4,2022-04-22;8',
    'user4,2021-05-03;9',
    'user4,2022-05-11;11'
]
avg_user_time(stream)