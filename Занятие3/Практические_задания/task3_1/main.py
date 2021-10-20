def remove_whitespace(str_):
    list_words = str_.split(" ")
    print(list_words)# TODO с помощью методов строки join и split очистить строку от лишних пробелов
    result = " ".join(list_words)
    return result

if __name__ == "__main__":
    str_with_space = "    123.    test   print test11    "  # исходная строка
    print(str_with_space)

#     list_words = str_.split(" ")
#     result = str_with_space.(" ", "")
#     result =
#     return result
#
# if __name__ == "__main__":
#     str_with_space = "    123.    test   print test11    "  # исходная строка
#     print(remove_whitespace(str_with_space))