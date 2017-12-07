graph = {}
graph['Prof'] = ['Amelie', 'Kaouther', 'Mostafa', 'Fabien']
graph['Amelie'] = ['Safaa', 'Mohamed']
graph['Fabien'] = ['Flore', 'Hamidou', 'Serges']
graph['Kaouther'] = []
graph['Mostafa'] = []
graph['Safaa'] = []
graph['Mohamed'] = []
graph['Flore'] = []
graph['Hamidou'] = []
graph['Serges'] = []


def as_tu_vole_ma_pomme(nom):
    if (nom == 'Safaa'):
        return True
    else:
        return False


from collections import deque


def search(nom):
    search_queue = deque()
    search_queue += graph['Prof']
    while search_queue:
        person = search_queue.popleft()
        if as_tu_vole_ma_pomme(person):
            print (person + " est le(a) voleu(r)se")
            return True
        else:
            search_queue += graph[person]
    return False

search('Prof')



