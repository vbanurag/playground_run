'''
1366. Rank Teams by Votes

In a special ranking system,
each voter gives a rank from highest to lowest to all teams participating in the competition.

The ordering of teams is decided by who received the most position-one votes.
If two or more teams tie in the first position, we consider the second position to resolve the conflict,
if they tie again, we continue this process until the ties are resolved. If two or more teams are still tied after
considering all positions, we rank them alphabetically based on their team letter.

You are given an array of strings votes which is the votes of all voters
in the ranking systems. Sort all teams according to the ranking system described above.

Return a string of all teams sorted by the ranking system.

Example 1:

    Input: votes = ["ABC","ACB","ABC","ACB","ACB"]
    Output: "ACB"
    Explanation:
        Team A was ranked first place by 5 voters. No other team was voted as first place, so team A is the first team.
        Team B was ranked second by 2 voters and ranked third by 3 voters.
        Team C was ranked second by 3 voters and ranked third by 2 voters.
        As most of the voters ranked C second, team C is the second team, and team B is the third.

'''
import collections

def rankTeams(votes):
        teamVotes = collections.defaultdict(lambda: [0] * 26)

        for vote in votes:
            for pos, team in enumerate(vote):
                teamVotes[team][pos] += 1
        # print(dict(teamVotes))
        # print(sorted(teamVotes.keys(), reverse=True, key=lambda team: (teamVotes[team], -ord(team))))
        return ''.join(sorted(teamVotes.keys(), reverse=True,
                              key=lambda team: (teamVotes[team], -ord(team))))

import unittest

class TestRankTeams(unittest.TestCase):
    def test_rankTeams(self):
        self.assertEqual(rankTeams(["ABC","ACB","ABC","ACB","ACB"]), "ACB")

        # self.assertEqual(rankTeams(["WXYZ","XYZW"]), "XYZW")
        # self.assertEqual(rankTeams(["WPQR","PQRW","WPQR","PQRW","WPQR"]), "WPQR")

if __name__ == "__main__":
    unittest.main()
