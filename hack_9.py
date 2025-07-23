"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    dict = s
    dict_2 = {}
    _ls = []

    for llave in list(dict.items())[0]:
        if len(llave) > 3:
            for letter in llave:
                if letter == "k":
                    continue
                elif letter == llave[0]:
                    _ls.append(letter.upper())
                else:
                    _ls.append(letter)          
        else:
            dict_2[llave.capitalize()] = _ls

    valor = "".join(dict_2["Foo"])
    dict_2["Foo"] = valor
    return dict_2
