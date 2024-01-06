# TODO  Напишите функцию count_letters
def count_letters(text):
    union_text = "".join(text.lower().split())
    counted_symbols = {}

    for symbol in union_text:
        if symbol.isalpha() and symbol in counted_symbols:
            counted_symbols[symbol] += 1
        elif symbol.isalpha() and symbol not in counted_symbols:
            counted_symbols[symbol] = 1

    return counted_symbols


# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict_of_symbols):
    sum_of_values = sum(dict_of_symbols.values())
    symbols_with_frequency = {}

    for symbol, value in dict_of_symbols.items():
        frequency = value / sum_of_values
        symbols_with_frequency[symbol] = frequency

    return symbols_with_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
first_dict = count_letters(main_str)
total_dict = calculate_frequency(first_dict)

for sym, freq in total_dict.items():
    print(f"{sym}: {freq:.2f}")
