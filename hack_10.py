"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    _ls = []
    for dict in result:
        for tupla in dict.items():
            lista = list(tupla)
            for value in lista:
                _ls.append(value)

    longitud = len(_ls) + 1

    new_list = [i for i in range(1, longitud)]
    impares = [str(i) for i in new_list if i % 2 != 0]
    pares = [str(i) for i in new_list if i % 2 == 0]


    result = []

    i = 0
    while(i < len(pares)):
        dict = {}
        dict[impares[i]] = pares[i]
        result.append(dict)
        i += 1
    return result

_list = [{"a":"b"},{"c":"d"},{"e":"f"}]

print(fn_hack_10(_list))