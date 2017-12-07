graph = {}
graph['Prof'] = ['Amelie', 'Kaouther', 'Mustapha', 'Fabien']
graph['Amelie'] = ['Safaa', 'Mohamed']
graph['Fabien'] = ['Flore', 'Hamidou', 'Serge']
graph['Kaouther'] = []
graph['Mustapha'] = []
graph['Safaa'] = []
graph['Mohamed'] = []
graph['Flore'] = []
graph['Hamidou'] = []
graph['Serge'] = []
graph['Serge'] = []

def as_tu_vole_ma_pomme(nom):
    if (nom == "Safaa"):
        return True
    else:
        return False

from collections import deque

def search(nom):
    search_queue = deque()
    search_queue += graph['Prof']
    while search_queue:
        personne = search_queue.popleft()
        if as_tu_vole_ma_pomme (personne):
            print(personne+ ' est le(a) voleur(se)')
            return True
        else:
            search_queue += graph[personne]
    return False

search('Prof')