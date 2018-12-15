
def crypto_ceasar(text: str, key: str, step: int = 3):
    hidden_text = []
    for symbol in text:
        symbol_index = key.find(symbol)
        crypto_index = symbol_index + step
        hidden_text.append(key[crypto_index])

    return ''.join(hidden_text)

def main():
    key_word = 'abcdefghijklmnopqrstuvwxyz'
    text_to_hide = input('Type a text: ').lower()
    print(crypto_ceasar(text_to_hide, key_word))


if __name__ == '__main__':
    main()
