import random

def getnamebox(link):
    namebox = '_b_' + link[-15:] + '_join_name'
    return namebox

def saygoodbye():
    keywords = ['До свидания', 'Всего доброго', 'до свидания', 'всего доброго']
    return keywords[random.randint(0,3)]



