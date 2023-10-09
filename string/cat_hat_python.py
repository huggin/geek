# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3


def cat_hat(s):
    ##your code here##
    ##You need to write complete code this time
    cat, hat = 0, 0
    n = len(s)
    for i in range(n - 2):
        if s[i : i + 3] == "cat":
            cat += 1
        elif s[i : i + 3] == "hat":
            hat += 1
    return hat == cat


# {
# Driver Code Starts.


def main():
    testcases = int(input())  # testcases
    while testcases > 0:
        str = input()
        print(cat_hat(str))
        testcases -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends
