'''
This script demonstrates the Levenshtein algorithm (edit distance)
to measure the similarity between two strings. It quantifies the minimum number
of single-character edits (insertions, deletions, substitutions) required
to change one string into another
'''


def Levenshtein(A, B):
    # Initialise dp table
    dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

    # Base case initialisation
    for i in range(len(A) + 1):
        dp[i][0] = i
    for j in range(len(B) + 1):
        dp[0][j] = j

    # Fill the table
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],  # deletion
                                   dp[i][j - 1],  # insertion
                                   dp[i - 1][j - 1])  # subtraction

    # Return the minimum edit distance
    return dp[len(A)][len(B)]


A = input("Enter the first word: ")
B = input("Enter the second word: ")
print(f"The edit distance between {A} and {B} is", Levenshtein(A, B))