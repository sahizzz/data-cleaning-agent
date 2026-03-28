from .tasks import easy_data, medium_data, hard_data

class DataCleaningEnv:

    def __init__(self, difficulty="easy"):
        self.df = None
        self.done = False
        self.difficulty = difficulty

    def reset(self):
        if self.difficulty == "easy":
            self.df = easy_data()
        elif self.difficulty == "medium":
            self.df = medium_data()
        else:
            self.df = hard_data()

        self.done = False
        return self._get_obs()

    def step(self, action):
        if self.done:
            return self._get_obs(), 0, True, {}

        if action == "fill_mean":
            self.df = self.df.fillna(self.df.mean(numeric_only=True))

        elif action == "fill_median":
            self.df = self.df.fillna(self.df.median(numeric_only=True))

        elif action == "drop_missing":
            self.df = self.df.dropna()

        elif action == "remove_duplicates":
            self.df = self.df.drop_duplicates()

        elif action == "done":
            self.done = True

        reward = self._calculate_reward()

        return self._get_obs(), reward, self.done, {}

    def _get_obs(self):
        return {
            "data": str(self.df.head()),
            "missing": self.df.isnull().sum().to_dict(),
            "duplicates": int(self.df.duplicated().sum()),
            "difficulty": self.difficulty
        }

    def _calculate_reward(self):
        reward = 0

        missing = self.df.isnull().sum().sum()
        reward += max(0, 5 - missing)

        duplicates = self.df.duplicated().sum()
        reward += max(0, 3 - duplicates)

        return reward
