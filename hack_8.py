"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    longitud = len(result)
    _ls = []
    if(longitud % 2 == 0):
        for letter in result:
            indice = result.index(letter) + 1
            indice_str = str(indice)
            _ls.append(indice_str)
        _ls.reverse()
    else:
        for letter in result:
            indice = result.index(letter) + 1
            message = f'{letter}-{indice}'
            _ls.append(message)

        _ls.reverse()

    return _ls
