class HighScores:
    def __init__(self, scores):
        self.scores_list = scores

    def highscore(self):
        return max(self.scores_list)

    def last_score(self):
        return self.scores_list[-1]

    def podium(self):
        high_scores = []
        for score in self.scores_list:
            high_scores.append(score)
            high_scores.sort()
            if len(high_scores) > 3:
                high_scores.pop(0)
        return high_scores



# --------------------------------------------------------

scores1 = HighScores([30, 50, 20, 70])
print(scores1.scores_list)
print(scores1.highscore())
print(scores1.podium())
print(scores1.last_score())
