#!/usr/bin/env python3

equivalence = {}


def start_city(graph):
    src_city = None
    for city in graph:
        if city not in [c for dsts in graph.values() for c in dsts]:
            if src_city is None:
                src_city = city
            else:
                return None
    return src_city


def check_isomorph(original, other, orig_node, othr_node):
    # If some node is None -> False
    if orig_node is None or othr_node is None:
        return False
    # Case 1: some node doesn't have any children
    if orig_node not in original and othr_node not in other:
        return True
    # Case 2: every children has an equivalent node
    #         both nodes must have the same num. of children
    if (orig_node in original and othr_node in other and
        len(original[orig_node]) == len(other[othr_node])):
        assigned = [False] * len(other[othr_node])
        for othr_child in other[othr_node]:
            match = False
            for i in range(len(original[orig_node])):
                if not assigned[i]:
                    if check_isomorph(original, other,
                                      original[orig_node][i],
                                      othr_child):
                        assigned[i] = True
                        match = True
                        break
            if not match:
                return False
        return True
    return False


def tree_levels(tree):
    levels = [[start_city(tree)]]
    while True:
        aux = [city for src in levels[-1] if src in tree for city in tree[src]]
        aux.sort()
        if len(aux) == 0:
            return levels
        levels.append(aux)


def virus(original, other):
    # Get cities by tree level
    lvls_orig = tree_levels(original)
    lvls_othr = tree_levels(other)
    cities_orig = [city for lvl in lvls_orig for city in lvl]
    cities_orig.sort()
    for city_orig in cities_orig:
        # Condition 2 (same tree level)
        lvl = 0
        for i in range(len(lvls_orig)):
            if city_orig in lvls_orig[i]:
                lvl = i
                break
        if len(lvls_othr) <= lvl:
            return "NO"
        match = False
        for city_othr in lvls_othr[lvl]:
            if city_othr not in list(equivalence.values()):
                if city_orig not in original and city_othr not in other:
                    match = True
                    equivalence[city_orig] = city_othr
                    break
                # Condition 1 (same number infected cities)
                elif (city_orig in original and city_othr in other and
                      len(original[city_orig]) == len(other[city_othr])):
                    # Condition 4 (same paths)
                    if check_isomorph(original, other, city_orig, city_othr):
                        match = True
                        equivalence[city_orig] = city_othr
                        break
        if not match:
            return "NO"
    cities = [(orig_city, equivalence[orig_city]) for orig_city in equivalence]
    cities.sort()
    return " ".join(["/".join(pair) for pair in cities])


if __name__ == "__main__":
    n = int(input())
    graph_orig = {}
    for _ in range(n-1):
        s, d = input().split()
        if s in graph_orig:
            graph_orig[s].append(d)
        else:
            graph_orig[s] = [d]
    for src in graph_orig:
        graph_orig[src].sort()
    test_cases = int(input())
    for case in range(1, test_cases+1):
        graph_othr = {}
        for _ in range(n-1):
            s, d = input().split()
            if s in graph_othr:
                graph_othr[s].append(d)
            else:
                graph_othr[s] = [d]
        for src in graph_othr:
            graph_othr[src].sort()
        equivalence = {}
        print("Case #{}: {}".format(case, virus(graph_orig, graph_othr)))
