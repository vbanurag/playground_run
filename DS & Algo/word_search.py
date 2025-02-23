'''
79. Word Search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

'''
from collections import Counter, defaultdict


def existTest(board, word):
        ROWS, COLS = len(board), len(board[0])

        path = set()

        def dfs(r,c,i):
            if i == len(word):
                return True

            if(
                min(r,c) < 0
                or r >= ROWS
                or c >= COLS
                or word[i] != board[r][c]
                or (r,c) in path
            ):
                return False

            path.add((r,c))
            res = (
                dfs(r+1,c,i+1)
                or dfs(r-1,c,i+1)
                or dfs(r,c+1,i+1)
                or dfs(r,c-1,i+1)
            )
            path.remove((r,c))
            return res

        count = defaultdict(int, sum(map(Counter, board), Counter()))

        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False


def test_exist():
    board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word1 = "ABCCED"
    assert existTest(board1, word1) == True

    board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word2 = "SEE"
    assert existTest(board2, word2) == True

    board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word3 = "ABCCFD"
    assert existTest(board3, word3) == False

def test_exist_reversed_word():
    board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word1 = "EDCA"
    assert existTest(board1, word1) == True

test_exist()
