class Solution:
    def canAliceWin(self, n: int) -> bool:
        curr_turn=10
        turn=1
        while n>=curr_turn:
            n=n-curr_turn
            turn=1-turn
            curr_turn-=1
        return turn==0   