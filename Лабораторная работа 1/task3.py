list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
num_of_players = len(list_players)
half_index = int(num_of_players / 2)
team_1 = list_players[:half_index]
team_2 = list_players[half_index:]

print(team_1)
print(team_2)
