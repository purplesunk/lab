from main import *

run_cases = [
    (
        [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
        ],
        ([0, 1, 2, 3, 4, 5], [[1], [0, 2], [1, 3], [2, 4], [3, 5], [4]]),
    ),
    (
        [
            (0, 1),
            (0, 2),
            (0, 3),
            (1, 2),
            (1, 3),
        ],
        ([0, 1, 2, 3], [[1, 2, 3], [0, 2, 3], [0, 1], [0, 1]]),
    ),
]
submit_cases = run_cases + [
    (
        [
            (0, 2),
            (2, 4),
            (2, 1),
            (3, 1),
            (4, 5),
        ],
        ([0, 2, 5], [[2], [0, 1, 4], [4]]),
    ),
]


def test(edges_to_add, test_nodes):
    print("=================================")
    graph = Graph()
    for edge in edges_to_add:
        graph.add_edge(edge[0], edge[1])
        print(f"Added edge: {edge}")
    print("---------------------------------")
    try:
        actual = []
        for i, edge in enumerate(test_nodes[0]):
            adj_nodes = graph.adjacent_nodes(edge)
            actual.append(adj_nodes)
            print(f"Adjacent nodes of {edge}:")
            print(f" - Expecting: {test_nodes[1][i]}")
            print(f" - Actual: {adj_nodes}")
        if actual == test_nodes[1]:
            print("Pass \n")
            return True
        print("Fail \n")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
