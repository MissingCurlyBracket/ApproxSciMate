from src.approxscimate.perm import perm


def compare_perm(n, k, levels):
    results = {}
    for level in levels:
        results[level] = perm(n, k, level)
    return results


def main():
    levels = [0, 1, 2, 3, 4, 5]
    print("n\tk\tLevel 0\tLevel 1\tLevel 2\tLevel 3\tLevel 4\tLevel 5")
    for n in range(10, 11):
        for k in range(1, n + 1):
            results = compare_perm(n, k, levels)
            print(f"{n}\t{k}\t{results[0]}\t{results[1]}\t{results[2]}\t{results[3]}\t{results[4]}\t{results[5]}")


if __name__ == "__main__":
    main()
