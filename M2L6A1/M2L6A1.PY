class Cricket:
    def _init_(self, player, score):
        self._player = player
        self._score = score

    def into(self):
        print(f"Cricket -Player: {self._player}, Score: {self._score}")

    def play(self):
        print(f"{self._player} hits a six!")

    def get_score(self):
        return self._score
    
    def set_score(self, new_score):
        if new_score >= 0:
            self._score = new_score
            print(f"score updated to {self._score}")
        else:
            print("score can not be negative")

class Football:
    def _init_(self, player, score):
        self._player = player
        self._score = score

    def into(self):
        print(f"Football -Player: {self._player}, Score: {self._score}")

    def play(self):
        print(f"{self._player} scores a goal!")

    def get_score(self):
        return self._score
    
    def set_score(self, new_score):
        if new_score >= 0:
            self._score = new_score
            print(f"score updated to {self._score}")
        else:
            print("score can not be negative")