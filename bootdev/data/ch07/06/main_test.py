from main import HashMap
from user import User

run_cases = [
    (
        512,
        [User(1, 30, "Engineer"), User(2, 25, "Designer")],
        [
            ("Ricky#1", User(1, 30, "Engineer")),
            ("Shelley#2", User(2, 25, "Designer")),
            ("FakeyFaker#2", None),
        ],
    ),
]

submit_cases = run_cases + [
    (
        1028,
        [User(4, 36, "Clerk"), User(5, 29, "Chef"), User(6, 55, "Pilot")],
        [
            ("George#4", User(4, 36, "Clerk")),
            ("John#5", User(5, 29, "Chef")),
            ("Blake#1", None),
        ],
    ),
]


def test(size, users, expected_hashmap):
    print("---------------------------------")
    print(f"Inputs:")
    print(f" * HashMap size: {size}")
    hm = HashMap(size)
    for user in users:
        hm.insert(user.user_name, user)
        print(f"   * Inserted ({user.user_name}, {user})")

    passes = True
    for user_name, expected in expected_hashmap:
        try:
            result = hm.get(user_name)
            if result == expected:
                print(f"Get {user_name}: Pass")
            else:
                print(f"Get {user_name}: Fail")
                print(f"   * Expect: {expected}")
                print(f"   * Actual: {result}")
                passes = False
        except Exception as e:
            actualErr = str(e)
            expectedErr = "sorry, key not found"
            if actualErr == expectedErr:
                print(f"Get {user_name}: Pass")
            else:
                print(f"Get {user_name}: Fail")
                print(f"   * Expect exception: {expectedErr}")
                print(f"   * Actual exception: {actualErr}")
                passes = False

    if passes:
        print("Pass")
        return True
    print("Fail")
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
