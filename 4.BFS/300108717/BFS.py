print 'Flore'
graph = {}
graph ['Teacher'] = ['Amelie','Kaouther','Mustapha','Fabien']
graph ['Amelie'] = ['Safaa', 'Mohamed']
graph ['Fabien'] = ['Hamidou' , 'Flore' , 'Serges']
graph ['kaouther']= []
graph ['Mustapha'] = []
graph ['Safaa'] =[]
graph ['Mohamed'] = []
graph ['Hamidou']= []
graph ['Flore'] = []
graph  ['Serges'] = []

def as_tu_voler_ma_pomme(nom):
    return True

from _collections import deque

def search(nom):
    search_queue = deque()
    search_queue += graph['Teacher']

    while search_queue:
        personne = search_queue.popleft()
        if as_tu_voler_ma_pomme(personne):
            print(personne + " est le(a) voleu(r)se")
            return True
        else:
            search_queue +=graph[personne]
    return False

search('Teacher')
