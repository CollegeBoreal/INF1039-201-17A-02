graph = {}
graph['teacher'] = ['amelie', 'kaouther', 'mustapha', 'fabien']
graph['amelie'] = ['safaa', 'Mohamed']
graph['Fabien'] = ['Flore','Hamidou','serges']
graph['Kaouther'] = []
graph['Mustapha'] = []
graph['safaa'] = []
graph['Mohamed'] = []
graph['Flore'] = []
graph['Hamidou'] = []
graph['serges'] = []
def as_tu_vole_ma_pomme(non)

from collections import deque

search_queue = deque ()
search_queue += graph['prof']

    while search_queue
        personne=search_queue.popleft






