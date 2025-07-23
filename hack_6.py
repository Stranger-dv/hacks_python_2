"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    _ls = []

    if(result == []): 
        return ["0"]
    else:
        for letter in result:
            indice = lista.index(letter)
            num_str = str(indice + 1)
            if indice % 2 != 0:
                num_str = "-"
                _ls.append(num_str)
            else:
                _ls.append(num_str)

    result = _ls
    return result

lista = ["a","b","c","d","e"]

print(fn_hack_6(lista))