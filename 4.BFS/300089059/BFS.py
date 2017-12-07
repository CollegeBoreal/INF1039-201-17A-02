graph ={}
graph['prof'] = ['amelie','kaouter','mustapha','fabien']
graph['amelie'] = ['safaa','mohamed']
graph['fabien'] =['flore','hamidou','serges']
graph['kaouter'] = []
graph['mustapha'] = []
graph['safaa'] = []
graph['mohamed'] = []
graph['flore'] = []
graph['hamidou'] = []
graph['serges'] = []

def as_tu_voler_ma_pomme(nom):
    if (nom == 'safaa'):
        return True
    else:
        return False


from collections import deque


def search(nom):
    search_queue = deque()
    search_queue += graph['prof']
    while search_queue:
        personne = search_queue.popleft()
        if as_tu_voler_ma_pomme(personne):
            print(personne+ ' est le(a) voleu(r)se')
            return True
        else:
            search_queue +=graph[personne]
    return False

search('Prof')



