
# Array of Scores - Main Branch

def calculate_sum(scores):
    return sum(scores)


def calculate_average(scores):
    return sum(scores) / len(scores)


def main():
    scores = list(map(float, input("Enter scores separated by spaces: ").split()))

    if not scores:
        print("Please enter at least one score.")
        return

    total = calculate_sum(scores)
    average = calculate_average(scores)

    print("Scores:", scores)
    print("Sum =", total)
    print("Average =", average)


if __name__ == "__main__":
    main()
