def pangram(str):
    """
    Функція перевіряє чи є слово панграмою чи ні:
        Функція приймає слово, потім перевіряє циклом по одному символу з alphabet,
        якщо всі букви є то він повертає True,
        а якщо не відповідає то в умові він опускає букву на нижній регістр щоб повторно перевірити його,
        якщо немає потрібної букви то функція повертає Fallse

    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
    return True


if __name__ == '__main__':
    text = input("введіть панграмму ")
    if (pangram(text) == True):
        print("речення є панграмою")
    else:
        print("речення не є панграмою")

    help(pangram)
