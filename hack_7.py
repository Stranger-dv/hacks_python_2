"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = s
    _ls = []
    if result == [0]: 
        return result
    else:
        for letter in result:
            indice = result.index(letter) + 1
            if indice % 2 != 0:
                indice_str = str(indice)
                _ls.append(indice_str)
            else:
                _ls.append(indice)

    result = _ls
    return result
