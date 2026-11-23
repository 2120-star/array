
import sys


def calculate_scores(scores):
    total = sum(scores)
    average = total / len(scores)
    maximum = max(scores)
    minimum = min(scores)

    print("Scores:", scores)
    print("Sum of scores:", total)
    print("Average of scores:", average)
    print("Maximum score:", maximum)
    print("Minimum score:", minimum)


if len(sys.argv) > 1:
    scores = list(map(int, sys.argv[1:]))
else:
    scores = list(map(int, input(
        "Enter scores separated by spaces: "
    ).split()))

if len(scores) > 0:
    calculate_scores(scores)
else:
    print("Please enter at least one score.")
