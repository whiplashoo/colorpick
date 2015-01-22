import re

with open("colortable.txt","r") as f:
    lines = f.read()
    m = re.findall('\#\w+',lines)
    a = []
    for word in m:
        
        #word = word.replace('#','')
        a.append(word)
    print(a)
    
