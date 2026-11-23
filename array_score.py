
import sys

def calculate_sum(scores):
    return sum(scores)


def calculate_average(scores):
    return sum(scores) / len(scores)


def calculate_maximum(scores):
    return max(scores)


def calculate_minimum(scores):
    return min(scores)


def main():
    if len(sys.argv) > 1:
        scores = [float(x) for x in sys.argv[1:]]
    else:
        n = int(input("Enter number of scores: "))
        scores = []

        for i in range(n):
            score = float(input("Enter score: "))
            scores.append(score)

    if len(scores) == 0:
        print("No scores entered.")
        return

    print("Scores:", scores)
    print("Sum of scores:", calculate_sum(scores))
    print("Average of scores:", calculate_average(scores))
    print("Maximum score:", calculate_maximum(scores))
    print("Minimum score:", calculate_minimum(scores))


if __name__ == "__main__":
    main()
