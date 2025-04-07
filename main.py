logs = [] 

def liitumine(a,b):
    logs.append('liitumine') 
    if isinstance(a,str) or isinstance(b,str):
        print("vale andmed")
        return ""
    return a + b

def korutamine(a,b):
    logs.append('korutamine') 
    if isinstance(a,str) or isinstance(b,str):
        print("vale andmed")
        return ""
    return a - b

def lahutamine(a,b):
    logs.append('lahutamine')  
    if isinstance(a,str) or isinstance(b,str):
        print("vale andmed")
        return ""
    return a * b

def jaganamine(a,b):
    try:
        logs.append('jaganamine') 
        if isinstance(a,str) or isinstance(b,str):
            print("vale andmed")
            return ""
        return a / b
    except ZeroDivisionError:
        print("ei saa jagada nullile")

def LogsKuvamine(logs):
    jag = 0
    kor = 0
    liit = 0
    lahut = 0
    for elem in logs:
        if elem == 'korutamine':
            kor += 1
        elif elem == 'jaganamine':
            jag += 1
        elif elem == 'liitumine':
            liit += 1
        elif elem == 'lahutamine':
            lahut += 1
    return [jag, kor, liit, lahut]


print(liitumine(5, 5))
print(korutamine(5, 5))
print(lahutamine(5, 5))
print(jaganamine(5, 0))
print(LogsKuvamine(logs))
