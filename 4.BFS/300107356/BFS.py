graph = {}
graph["Teacher"] = ["Amelie", "Kaouther","Moustapha","Fabien"]
graph["Fabien"] = ["Flore", "Hamidou", "Serges"]
graph["Amelie"] = ["Safaa", "Mohamed"]
graph["Moustapha"] = []
graph["Mohamed"] = []
graph["Kaouther"] = []
graph["Safaa"] = []
graph["Flor"] = []
graph["Hamidou"] = []
graph["Serges"] = []

def as_tu_voler_ma_pomme(nom):
    if (nom == "Safaa"):
        return True
    else :
        return False

from collections import deque

def search(nom):
    search_queue = deque()
    search_queue += graph["Teacher"]
    while search_queue:
        personne = search_queue.popleft()
        if as_tu_voler_ma_pomme(personne):
            print(personne + " est le(a) voleu(r)se!")
            return True
        else:
            search_queue += graph[personne]
    return False

search("Teacher")
