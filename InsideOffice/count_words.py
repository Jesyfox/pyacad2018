some_text = """
За столом сидели мужики и ели.
Мясом конюх угощал своих гостей.
Все расхватывали ужин и хозяин весел был
О жене своей все время говорил.

Ели мясо мужики, пивом запивали,
О чем конюх говорил, они не понимали.

Я узнал недавно: все вы, как ни странно, -
Конюх хриплым голосом проговорил,-
С моей бабою встречались втайне от меня
И поэтому всех вас собрал сегодня я.

Ели мясо мужики, пивом запивали,
О чем конюх говорил, они не понимали.

Я за ней не уследил - в том моя вина,
Но скажите, правда вкусная она?

Ели мясо мужики, пивом запивали,
О чем конюх говорил, они не понимали.
Ели мясо мужики, пивом запивали,
О чем конюх говорил, они не понимали.
"""


def text_to_list(text):
    symbols = [',', '.', '-', '?']
    for symb in symbols:
        text = text.replace(symb, '')
    words = text.replace('\n', ' ').lower().split(' ')
    return words


def count_words(word_list):
    counted = {}
    for word in word_list:
        if word:
            counted[word] = counted.get(word, 0) + 1
        else:
            pass
    return counted


list_of_words = text_to_list(some_text)
words = count_words(list_of_words)
words = sorted(words.items(), key=lambda x: x[1], reverse=True)
print(words)
