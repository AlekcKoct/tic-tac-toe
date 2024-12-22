import tkinter as tk
from tkinter import messagebox

# Создаём главное окно
window = tk.Tk()
window.title("Крестики-нолики")
window.geometry("315x360")

# Основные переменные
current_player = "X"
buttons = []
score_X = 0
score_O = 0

# Проверка на наличие победителя#
def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False

# Проверка на ничью
def is_draw():
    for row in buttons:
        for btn in row:
            if btn["text"] == "":
                return False
    return True

# проверка нажатия на кнопку
def on_click(row, col):
    global current_player, score_X, score_O
    if buttons[row][col]['text'] != "":
        messagebox.showwarning("Неправельный ход", "Эта клетка занята!")
        return

    buttons[row][col]['text'] = current_player

    # Проверяем, выиграл ли текущий игрок
    if check_winner():
        if current_player == "X":
            score_X += 1
        else:
            score_O += 1
        if score_X == 3:
            messagebox.showinfo("Поздравляем!", f"Игрок Николай победил!")
        elif score_O == 3:
            messagebox.showinfo("Поздравляем!", f"Игрок Петр победил!")
            return
        update_score()
        disable_buttons()


    # Проверяем, ничья или нет
    elif is_draw():
        messagebox.showinfo("Игра", "Ничья!")
        disable_buttons()
        return

    # Меняем игрока
    current_player = "O" if current_player == "X" else "X"

# Отключение всех кнопок
def disable_buttons():
    for row in buttons:
        for btn in row:
            btn.config(state="disabled")

# Сброс игрового поля для начала новой игры
def reset_game():
    global current_player
    current_player = "X"
    for row in buttons:
        for btn in row:
            btn.config(state="normal", text="")

# Функция для обновление счёта на экране
def update_score():
    score_label.config(text=f"Счёт - Николай: {score_X} | Петр: {score_O}")


# Создаём игровое поле
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(window, text="", font=("Arial", 20), width=6, height=2,
                        command=lambda r=i, c=j: on_click(r, c))
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

# Отображение счёта
score_label = tk.Label(window, text=f"Счёт - Николай: {score_X} | Петр: {score_O}", font=("Arial", 14))
score_label.grid(row=3, column=0, columnspan=3)

# Кнопка для сброса
reset_button = tk.Button(window, text="Сброс", font=("Arial", 14), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

# Запуск приложения
window.mainloop()