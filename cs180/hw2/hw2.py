import itertools


def main():
    # P1
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 30
    print(find_subset(arr, k))

    # P2
    '''
    arr = list(range(1, 9))
    arr.remove(5)
    n = len(arr)
    print(f"found missing: {find_missing_sorted(arr, n)}")
    '''


def find_subset(arr, k):
    # P1, O(n)
    if not B(arr, k):
        return None

    subset = []

    for e in arr:
        if B(arr, k-e):
            subset.append(e)
            k -= e
            if k == 0:
                break
    return subset


def find_missing_sorted(arr, n):
    # P2a, O(log n)
    print(f"inputs: arr={arr}, n={n}")

    lower = 0
    upper = n

    while upper-lower > 1:
        i = int((lower+upper)/2)
        print(f"lower={lower}, upper={upper}, i={i}, {arr[lower:upper]}")
        if arr[i] == i+1:
            lower = i
        elif arr[i] == i+2:
            upper = i
        else:
            print("INVALID INPUT")
            return None

    print(f"lower={lower}, upper={upper}, i={i}, {arr[lower:upper]}")

    if arr[lower] == lower+1:
        return arr[lower]+1
    elif arr[lower] == lower+2:
        return arr[lower]-1


def find_missing_unsorted(arr, n):
    # P2b, O(n)
    print(f"inputs: arr={arr}, n={n}")

    sum = 0

    for e in arr:
        sum += e

    return int((n+1)*(n+2)/2)-sum


def B(arr, k):
    # blackbox algorithm for P1
    for i in range(0,len(arr)):
        s = list(itertools.combinations(arr, i))
        for t in s:
            if sum(t) == k:
                return True
    return False


if __name__ == "__main__":
    main()
