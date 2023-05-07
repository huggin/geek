# User function Template for python3


class Solution:
    def diagonalSort(self, matrix, n, m):
        # code here
        dict = {}
        for i in range(n):
            for j in range(m):
                if not i - j in dict:
                    dict[i - j] = [matrix[i][j]]
                else:
                    dict[i - j].append(matrix[i][j])

        for k, v in dict.items():
            if k > 0:
                v.sort(reverse=True)
            elif k < 0:
                v.sort()
            else:
                v[:] = v[::-1]

        for i in range(n):
            for j in range(m):
                matrix[i][j] = dict[i - j].pop()


# {
# Driver Code Starts
# Initial Template for Python 3


if __name__ == "__main__":
    tc = int(input())
    while tc > 0:
        n, m = map(int, input().strip().split())
        inputLine = list(map(int, input().strip().split()))
        matrix = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                matrix[i][j] = inputLine[i * m + j]
        ob = Solution()
        ob.diagonalSort(matrix, n, m)
        for i in range(n):
            for j in range(m):
                print(matrix[i][j], end=" ")
            print()
        tc -= 1

# } Driver Code Ends
