list = ['this','that', ['other']]

def capitalize_nested(list):
    res = []
    for s in list:
        if type(s) == list:
            res.append(capitalize_nested(s))
        else:
            res.append(s.capitalize())
    return res


print(capitalize_nested(list))








