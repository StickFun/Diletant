import random

def getnamebox(link):
    n = len(link)-1
    namebox = ''
    while link[n] != '/':
        namebox = link[n] + namebox
        n-=1
    namebox = '_b_' + namebox + '_join_name'
    return namebox

def saygoodbye():
    keywords = ['До свидания', 'Всего доброго', 'до свидания', 'всего доброго']
    return keywords[random.randint(0,3)]



