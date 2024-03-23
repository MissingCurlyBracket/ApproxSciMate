from src.approxscimate.cbrt import cbrt


def compare_cbrt(n, levels):
    results = {}
    for level in levels:
        results[level] = cbrt(n, level)
    return results


def main():
    levels = [0, 1, 2]
    print("n\tLevel 0\tLevel 1\tLevel 2")
    for n in range(1, 100):
        results = compare_cbrt(n, levels)
        print(f"{n}\t{results[0]}\t{results[1]}\t{results[2]}")


if __name__ == "__main__":
    main()
