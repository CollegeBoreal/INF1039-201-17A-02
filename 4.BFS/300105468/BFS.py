graph = {}
graph['Teacher'] = ['Amelie','Kaouther','Mostapha','Fabien']
graph['Amelie'] = ['Safaa','Mohamed']
graph['Fabien'] = ['Flore','Hamidou','Serges']
graph['Kaouther'] = []
graph['Mostapha'] = []
graph['Safaa'] = []
graph['Mohamed'] = []
graph['Flore'] = []
graph['Hamidou'] = []
graph['Serges'] = []

def as_tu_vole_ma_pomme(nom):

from collections import deque


def search(nom):
    Search_queue = deque()
    Search_queue  += graph['Prof']
    while Search_queue:
     personne = Search_queue.popleft{}
        if as_tu_vole_ma_pomme(personne):
            print(personne + " est le(a) voleu(r)se" )
            return True
        else:



