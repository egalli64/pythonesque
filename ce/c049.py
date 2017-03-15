"""
CodeEval Peak Traffic
author: Manny egalli64@gmail.com
info: http://thisthread.blogspot.com/
      https://www.codeeval.com/open_challenges/49/
"""
import sys
from functools import reduce

interactions = [(set(), set())]
cliques = {}


class Clique:
    def __init__(self, cliques):
        self.cliques = [x for x in map(set, cliques)]
        self.reduced = reduce(set.union, self.cliques, set())


def find_cliques(cli, first_call=True):
    found = []
    for c_id, others in cli.items():
        if len(others) == 1:
            if not first_call:
                c = [c_id, next(iter(others))]
                found.append(c)
        elif len(others) > 1:
            if not first_call:
                found.extend([c_id, v] for v in others)
            sub = dict(
                (j, [x for x in filter(lambda v2: v2 in others, cli[j])])
                for j in others)
            c_sub = find_cliques(sub, False)
            for c in c_sub:
                c.insert(0, c_id)
            found.extend(c_sub)

            if first_call:
                cliques[c_id] = Clique(c_sub)
    return found


def graph_filter():
    for value in cliques.values():
        others = value.reduced
        for other in others:
            a_clique = cliques.get(other)
            if not a_clique or (not a_clique.cliques):
                continue

            some_cliques = [c for c in value.cliques if other in c]
            filtered = []
            for c in a_clique.cliques:
                if not (c <= others):
                    filtered.append(c)
                elif not any(c <= c1 for c1 in some_cliques if c is not c1):
                    filtered.append(c)

            if len(filtered) < len(a_clique.cliques):
                a_clique.cliques = filtered
                a_clique.reduced = reduce(set.union, filtered, set())


def get_id(name):
    if not users.get(name):
        users[name] = len(id_users)
        id_users.append(name)
        interactions.append((set(), set()))
    return users[name]


if __name__ == '__main__':
    with open(sys.argv[1], 'r') as file:
        id_users = [None]
        users = {}

        for line in file:
            line = line.strip()
            _, *addresses = line.split('\t')

            id_a = get_id(addresses[0])
            id_b = get_id(addresses[1])

            interactions[id_a][0].add(id_b)
            interactions[id_b][1].add(id_a)

    edges = {}
    for i, (left, right) in enumerate(interactions):
        edges[i] = (sorted(idx for idx in left & right if idx > i))

    find_cliques(edges)
    graph_filter()

    clique_list = []
    for value in cliques.values():
        if value.cliques and len(value.cliques):
            clique_list.append(*value.cliques)

    results = []
    for clique in clique_list:
        names = [id_users[i] for i in clique]
        results.append(', '.join(sorted(names)))

    for result in sorted(results):
        print(result)

