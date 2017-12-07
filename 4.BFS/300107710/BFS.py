print("bonjour")
graph = {}
graph["Prof"] = ["Amelie", "Kawtar", "Mostafa", "Fabien"]
graph["Amelie"] = ["Safaa", "Mohamed"]
graph["Fabien"] = ["Flore", "Hamidou", "Serge"]
graph["Kawtar"] = []
graph["Mostafa"] = []
graph["Safaa"] = []
graph["Mohammed"] = []
graph["Flore"] = []
graph["Hamidou"] = []
graph["Serge"] = []

def as_tu_vole_ma_pomme(nom):
    if (nom == "Safaa"):
        return True

from _collections import deque

def search(nom):
    search_queue = deque()
    search_queue += graph["Prof"]
    while search_queue:
        personne = search_queue.popleft()
        if as_tu_vole_ma_pomme(personne):
            print(personne + "  est l(e)a voleu(r)se")
            return True
        else:
            search_queue += graph[personne]
    return False

search('Prof')


