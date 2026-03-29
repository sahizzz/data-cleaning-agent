import gradio as gr
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath("."))

from env.environment import DataCleaningEnv

env = None
history = []


def start_env(difficulty):
    global env, history

    env = DataCleaningEnv(difficulty=difficulty)
    obs = env.reset()

    missing = sum(obs["missing"].values())
    duplicates = obs["duplicates"]

    history = [(missing, duplicates)]

    return f"🔹 Environment Started\n\n{obs}", None


def take_action(action):
    global env, history

    if env is None:
        return "⚠️ Start environment first", None

    obs, reward, done, _ = env.step(action)

    missing = sum(obs["missing"].values())
    duplicates = obs["duplicates"]
    history.append((missing, duplicates))

    steps = list(range(len(history)))
    missing_vals = [h[0] for h in history]
    duplicate_vals = [h[1] for h in history]

    plt.figure()
    plt.plot(steps, missing_vals)
    plt.plot(steps, duplicate_vals)
    plt.xlabel("Steps")
    plt.ylabel("Count")
    plt.title("Data Cleaning Progress")
    plt.legend(["Missing Values", "Duplicates"])

    output = f"⚙️ Action: {action}\n"
    output += f"🏆 Reward: {reward}\n"
    output += f"📊 State:\n{obs}\n\n"

    if done:
        output += "🏁 Cleaning Completed!"

    return output, plt


with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🤖 Advanced Data Cleaning Agent")
    gr.Markdown("Now with real-time graph visualization 📊")

    difficulty = gr.Dropdown(
        ["easy", "medium", "hard"],
        value="easy",
        label="📊 Select Difficulty"
    )

    start_btn = gr.Button("🚀 Start Environment")

    action = gr.Dropdown(
        ["fill_mean", "fill_median", "drop_missing", "remove_duplicates", "done"],
        label="Choose Action"
    )

    action_btn = gr.Button("Apply Action")

    output = gr.Textbox(label="📄 Output", lines=15)
    graph = gr.Plot(label="📈 Cleaning Progress")

    start_btn.click(start_env, inputs=difficulty, outputs=[output, graph])
    action_btn.click(take_action, inputs=action, outputs=[output, graph])


demo.launch()
