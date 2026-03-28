from env.environment import DataCleaningEnv

# Choose difficulty: easy / medium / hard
env = DataCleaningEnv(difficulty="hard")

obs = env.reset()
print("Initial State:\n", obs)

actions = ["fill_mean", "remove_duplicates", "done"]

for step, action in enumerate(actions):
    obs, reward, done, _ = env.step(action)

    print(f"\nStep {step+1}")
    print("Action:", action)
    print("Reward:", reward)
    print("State:", obs)

    if done:
        break
