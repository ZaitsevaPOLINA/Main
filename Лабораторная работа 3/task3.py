# TODO  Напишите функцию count_letters
def count_letters(str_):

    str_=str_.lower()

    dict_letters_={}

    for letter in str_:
        if letter.isalpha():
            if letter not in dict_letters_:
                dict_letters_[letter]=0

            if letter in dict_letters_:
                dict_letters_[letter]+=1

    return dict_letters_

# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict_):

    total=0

    for letter in dict_:
        total+=dict_[letter]

    for letter in dict_:
        dict_[letter]=format(dict_[letter]/total, ".2f")

    return dict_


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

calculate_frequency(count_letters(main_str))

for letter, value in calculate_frequency(count_letters(main_str)).items():
    print(f"{letter}: {value}")
