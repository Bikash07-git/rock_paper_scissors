import tkinter as tk
from PIL import Image, ImageTk
import random

# 🎮 Main window setup
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("750x650")
root.config(bg="#1e1e1e")

choices = ["rock", "paper", "scissors"]
images = {
    "rock": ImageTk.PhotoImage(Image.open("rock.png").resize((100, 100))),
    "paper": ImageTk.PhotoImage(Image.open("paper.png").resize((100, 100))),
    "scissors": ImageTk.PhotoImage(Image.open("scissors.png").resize((100, 100)))
}

player_score = 0
computer_score = 0
match_history = []

# 📦 GUI Layout
title = tk.Label(root, text="🪨 Rock ✋ Paper ✌️ Scissors", font=("Helvetica", 26, "bold"), bg="#1e1e1e", fg="#00FFAB")
title.pack(pady=10)

score_label = tk.Label(root, text="Player: 0    Computer: 0", font=("Arial", 14), bg="#1e1e1e", fg="white")
score_label.pack()

countdown_label = tk.Label(root, text="", font=("Arial", 18), bg="#1e1e1e", fg="yellow")
countdown_label.pack(pady=5)

result_text = tk.Label(root, text="", font=("Helvetica", 20), bg="#1e1e1e", fg="#00FFAB")
result_text.pack(pady=20)

image_frame = tk.Frame(root, bg="#1e1e1e")
image_frame.pack()

player_label = tk.Label(image_frame, bg="#1e1e1e")
player_label.pack(side=tk.LEFT, padx=60)

computer_label = tk.Label(image_frame, bg="#1e1e1e")
computer_label.pack(side=tk.RIGHT, padx=60)

# 🕹 Game logic
def shake(label):
    x = label.winfo_x()
    def do_shake(count):
        if count > 0:
            label.place(x=x + (-1)**count * 10)
            root.after(50, do_shake, count - 1)
        else:
            label.place(x=x)
    do_shake(6)

def fade_result():
    colors = ["#00FFAB", "#1e1e1e"] * 3
    def flicker(i):
        if i < len(colors):
            result_text.config(fg=colors[i])
            root.after(100, flicker, i+1)
        else:
            result_text.config(fg="#00FFAB")
    flicker(0)

def update_history(player_choice, computer_choice, result):
    entry = f"Player: {player_choice.capitalize()} | Computer: {computer_choice.capitalize()} → {result}"
    match_history.append(entry)
    if len(match_history) > 10:
        match_history.pop(0)  # Keep last 10 rounds
    history_list.delete(0, tk.END)
    for item in match_history:
        history_list.insert(tk.END, item)

def show_result(player_choice, computer_choice):
    global player_score, computer_score

    player_label.config(image=images[player_choice])
    computer_label.config(image=images[computer_choice])

    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        result = "You Win!"
        player_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    result_text.config(text=result)
    score_label.config(text=f"Player: {player_score}    Computer: {computer_score}")

    update_history(player_choice, computer_choice, result)
    shake(result_text)
    fade_result()

def countdown(player_choice, count=3):
    if count > 0:
        countdown_label.config(text=f"Result in {count}...")
        root.after(1000, countdown, player_choice, count - 1)
    else:
        countdown_label.config(text="")
        computer_choice = random.choice(choices)
        show_result(player_choice, computer_choice)

def play(player_choice):
    result_text.config(text="")
    player_label.config(image="")
    computer_label.config(image="")
    countdown(player_choice)

def reset_game():
    global player_score, computer_score, match_history
    player_score = 0
    computer_score = 0
    match_history.clear()
    result_text.config(text="")
    score_label.config(text="Player: 0    Computer: 0")
    countdown_label.config(text="")
    player_label.config(image="")
    computer_label.config(image="")
    history_list.delete(0, tk.END)

# 🧮 Styled buttons for enhanced user experiece
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=20)

for choice in choices:
    btn = tk.Button(
        button_frame,
        image=images[choice],
        command=lambda c=choice: play(c),
        bg="#2c2c2c",
        bd=2,
        relief=tk.RAISED,
        activebackground="#444444",
        cursor="hand2"
    )
    btn.pack(side=tk.LEFT, padx=20)

# 🔁 Reset Button
reset_btn = tk.Button(
    root,
    text="🔁 Reset Game",
    font=("Arial", 12),
    command=reset_game,
    bg="#444444",
    fg="white",
    activebackground="#666666",
    relief=tk.RIDGE,
    padx=10,
    pady=5,
    cursor="hand2"
)
reset_btn.pack(pady=10)

# 📜 Match History Box
tk.Label(root, text="Match History (Last 10)", font=("Arial", 14), bg="#1e1e1e", fg="#00FFAB").pack(pady=(10, 0))

history_list = tk.Listbox(root, width=70, height=8, bg="#2e2e2e", fg="white", font=("Courier New", 10))
history_list.pack(pady=10)

# 🚀 Run the game
root.mainloop()
# Trigger GitHub Linguist
