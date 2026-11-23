
# Array Score Program

def calculate_sum(scores):
    return sum(scores)


def calculate_average(scores):
    return sum(scores) / len(scores)


def main():
    n = int(input("Enter number of scores: "))

    scores = []

    for i in range(n):
        score = float(input("Enter score: "))
        scores.append(score)

    print("Scores:", scores)
    print("Sum of scores:", calculate_sum(scores))
    print("Average of scores:", calculate_average(scores))


if __name__ == "__main__":
    main()
