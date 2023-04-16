class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def personal_best(self):
        return max(self.scores)

    def latest(self):
        return self.scores[-1]

    def personal_top_three(self):
        return sorted(self.scores, reverse=True)[:3]


# --------------------------------------------------------

scores1 = HighScores([30, 50, 20, 70])
print(scores1.personal_top_three())

scores2 = HighScores([10, 30, 90, 30, 100, 20, 10, 0, 30, 40, 40, 70, 70])
print(scores2.personal_top_three())
