graph = {}
graph['Prof'] = ['Amelie','Kawther','Mostafa','Fabien']
graph['Amelie'] = ['Safaa','Mohamed']
graph['Fabien'] = ['Flore','Hamido','Sierge']
graph['Safaa'] = []
graph['Mohamed'] = []
graph['Flore'] = []
graph['Hamido'] = []
graph['Sierge'] = []
graph['Mostafa'] = []
graph['Kawther'] = []

def as_tu_vole_ma_pomme(nom):
    if (nom == "Safaa"):
       return True
    else:
       return False

from collections import deque

def search(nom):
    search_deque = deque()
    search_deque += graph['Prof']
    while search_deque:
        personne = search_deque.popleft()
        if as_tu_vole_ma_pomme(personne) :
            print(personne + " est le(a) voleur(se) ")
            return True
        else:
            search_deque += graph[personne]
    return False


search('Prof')
