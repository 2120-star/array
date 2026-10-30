
def calculate_sum(scores):
    return sum(scores)


def calculate_average(scores):
    return sum(scores) / len(scores)


def find_maximum(scores):
    return max(scores)


def find_minimum(scores):
    return min(scores)


def main():
    scores = list(map(float, input("Enter scores separated by spaces: ").split()))

    if not scores:
        print("Please enter at least one score.")
        return

    print("Sum =", calculate_sum(scores))
    print("Average =", calculate_average(scores))
    print("Maximum =", find_maximum(scores))
    print("Minimum =", find_minimum(scores))


if __name__ == "__main__":
    main()
