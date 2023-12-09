users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
log_user = {
    "Общее количество": 0,
    "Уникальные посещения": 0
}

log_user["Общее количество"] = len(users)
log_user["Уникальные посещения"] = len(set(users))

print(log_user)
