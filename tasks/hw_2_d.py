def reflection(r, x):
    for i in x:
        if not (i, i) in r:
            return False
    return True


def antireflection(r, x):
    for i in x:
        if (i, i) in r:
            return False
    return True


def symmetry(r, X):
    for x in X:
        for y in X:
            if (x, y) in r and not ((y, x) in r):
                return False
    return True


def antisymmetry(r, X):
    for x in X:
        for y in X:
            if (x, y) in r and (y, x) in r and x != y:
                return False
    return True


def asymmetry(r, X):
    for x in X:
        for y in X:
            if (x, y) in r and (y, x) in r:
                return False
    return True


def transitivity(r, X):
    for x in X:
        for y in X:
            for z in X:
                if (x, y) in r and (y, z) in r and not (x, z) in r:
                    return False
    return True


def antitransitivity(r, X):
    for x in X:
        for y in X:
            for z in X:
                if (x, y) in r and (y, z) in r and (x, z) in r:
                    return False
    return True


def connectivity(r, X):
    for x in X:
        for y in X:
            if x != y and not ((x, y) in r or (y, x) in r):
                return False
    return True


def equivalent(r, X):
    return reflection(r, X) and symmetry(r, X) and transitivity(r, X)


def partial_order(r, X):
    return reflection(r, X) and antisymmetry(r, X) and transitivity(r, X)


def strict_order(r, X):
    return antireflection(r, X) and antisymmetry(r, X) and transitivity(r, X)


def linear_order(r, X):
    return connectivity(r, X) and partial_order(r, X)


def domination(r, X):
    return antireflection(r, X) and antisymmetry(r, X)


x = {1, 2, 3, 4, 5}

R0={(1,1),(2,2),(3,3),(4,4),(5,5)}
R1={(1,2),(1,3),(1,5),(2,3),(2,4),(2,5),(3,4),(3,5),(4,5)}
R2={(1,2),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5),(3,4),(3,5),(4,5)}
R3={(1,1),(1,3),(1,5),(2,2),(3,1),(3,3),(3,5),(4,2),(4,4),(5,1),(5,3),(5,5)}
R4={(2,1),(3,1),(3,2),(4,1),(4,2),(4,3),(5,1),(5,2),(5,4)}
R5={(1,1),(2,1),(2,2),(3,1),(3,2),(3,3),(4,1),(4,2),(4,3),(4,4),(5,1),(5,2),(5,3),(5,4),(5,5)}
R6={(2,1),(2,2),(3,1),(3,2),(3,3),(4,2),(4,3),(4,4),(5,1),(5,2),(5,3),(5,4),(5,5)}
R7={(2,1),(3,1),(3,2),(4,1),(4,2),(4,3),(5,1),(5,2),(5,3),(5,4)}
R8={(1,2),(1,3),(1,4),(1,5),(2,1),(2,3),(2,4),(3,1),(3,2),(3,4),(4,1),(4,2),(4,3),(4,5),(5,1),(5,2),(5,3),(5,4)}
R9={(1,1),(1,2),(1,3),(1,4),(1,5),(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5),(5,5)}
R10={(1,1),(2,2),(3,3),(5,5)}
R11={(1,1),(2,2),(4,4),(5,5)}
R12={(1,2),(2,3),(3,4),(4,5)}
R13={(1,1),(1,2),(1,3),(1,4),(1,5),(2,2),(2,3),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5),(5,5)}

array_of_relations = [R0, R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13]

for i in range(len(array_of_relations)):
    if reflection(array_of_relations[i], x):
        print(f"R{i}")

print('antireflection:')
for i in range(len(array_of_relations)):
    if antireflection(array_of_relations[i], x):
        print(f"R{i}")

print('symmetry:')
for i in range(len(array_of_relations)):
    if symmetry(array_of_relations[i], x):
        print(f"R{i}")

print('antisymmetry:')
for i in range(len(array_of_relations)):
    if antisymmetry(array_of_relations[i], x):
        print(f"R{i}")

print('asymmetry:')
for i in range(len(array_of_relations)):
    if asymmetry(array_of_relations[i], x):
        print(f"R{i}")

print('transitivity:')
for i in range(len(array_of_relations)):
    if transitivity(array_of_relations[i], x):
        print(f"R{i}")

print('antitransitivity:')
for i in range(len(array_of_relations)):
    if antitransitivity(array_of_relations[i], x):
        print(f"R{i}")

print('connectivity:')
for i in range(len(array_of_relations)):
    if connectivity(array_of_relations[i], x):
        print(f"R{i}")


print('11. equivalent:')
for i in range(len(array_of_relations)):
    if equivalent(array_of_relations[i], x):
        print(f"R{i}")

print('12. partial_order:')
for i in range(len(array_of_relations)):
    if partial_order(array_of_relations[i], x):
        print(f"R{i}")

print('13. strict_order:')
for i in range(len(array_of_relations)):
    if strict_order(array_of_relations[i], x):
        print(f"R{i}")

print('14. linear_order:')
for i in range(len(array_of_relations)):
    if linear_order(array_of_relations[i], x):
        print(f"R{i}")


print('15. domination:')
for i in range(len(array_of_relations)):
    if domination(array_of_relations[i], x):
        print(f"R{i}")