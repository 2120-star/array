
def calculate_sum(scores):
    return sum(scores)


def calculate_average(scores):
    return sum(scores) / len(scores)


def main():
    scores = list(map(float, input("Enter scores separated by spaces: ").split()))

    if not scores:
        print("Please enter at least one score.")
        return

    print("Sum =", calculate_sum(scores))
    print("Average =", calculate_average(scores))


if __name__ == "__main__":
    main()
