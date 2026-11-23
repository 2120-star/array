
def calculate_scores(scores):
    total = sum(scores)
    average = total / len(scores)

    print("Scores:", scores)
    print("Sum of scores:", total)
    print("Average of scores:", average)


scores = input("Enter scores separated by spaces: ")
scores = list(map(int, scores.split()))

calculate_scores(scores)
