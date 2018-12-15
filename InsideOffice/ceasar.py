
def crypto_ceasar(text: str, key: str, step: int = 3):
    hidden_text, hidden_word = ([], [])
    text = text.split(' ')
    key = key + key[:step]
    for word in text:
        for symbol in word:
            symbol_index = key.find(symbol)
            crypto_index = symbol_index + step
            hidden_word.append(key[crypto_index])
        hidden_text.append(''.join(hidden_word))
        hidden_word = []

    return ' '.join(hidden_text)


def crypto_test():
    key_word = 'abcdefghijklmnopqrstuvwxyz'
    input_param = 'help me zzz'
    expected_output = 'khos ph ccc'
    test_1 = crypto_ceasar(input_param, key_word, step=3)

    if test_1 == expected_output:
        print('test 1: Passed')
    else:
        print('test 1: Failed')
        print(test_1)


def main():
    crypto_test()
    key_word = 'abcdefghijklmnopqrstuvwxyz'
    text_to_hide = input('Type a text: ').lower()
    print(crypto_ceasar(text_to_hide, key_word))


if __name__ == '__main__':
    main()
