from collections import deque

graph = {}
graph["you"] = ["alice", "bоb", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []


def person_is_seller(name):
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        print(person)
        if not person in searched:
            if person_is_seller(person):
                print(person + " is а mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


print(search("you"))

