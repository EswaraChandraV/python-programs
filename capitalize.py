def capitalize(string):
    e=string.split(" ")
    c = [j.capitalize() for j in e]       
    return " ".join(c)