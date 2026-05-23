text = input("nhap cai gi do")


def character_frequency_counter(text):
    """
    dêm tân suất xuất hien của ký tự
    :param text: srting
    :return: None
    """
    characters = []
    frequencies =[]
    for char in text:
        if char in characters:
            index = characters.index(char)
            frequencies[index] = frequencies[index] + 1
        else :
            characters.append(char)
            frequencies.append(1)

    for i in range(len(characters)):
        print(f'so la xuat hien cua {characters[i]}:{frequencies[i]}')
        # print()




character_frequency_counter(text)