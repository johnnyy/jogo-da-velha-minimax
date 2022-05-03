import tkinter as tk
from tkinter.messagebox import showinfo

import numpy as np

from logica_jogo_da_velha import IA_play, create_board, game_over, wins


class JogoDaVelha:
    labels = ["X", "O"]
    ia_player = 1
    human_player = -1
    label = 0
    list_button = []

    def __init__(self, frame, frame2):
        self.var_label = tk.IntVar()
        self.var_order = tk.IntVar()

        self.text_label = tk.Label(frame, text="Escolha:")
        self.radio1 = tk.Radiobutton(frame, text="X", value=0, variable=self.var_label)
        self.radio2 = tk.Radiobutton(frame, text="O", value=1, variable=self.var_label)

        self.text_label_order = tk.Label(frame, text="Ordem:")
        self.radio1_order = tk.Radiobutton(
            frame, text="Primeiro", value=0, variable=self.var_order
        )
        self.radio2_order = tk.Radiobutton(
            frame, text="Segundo", value=1, variable=self.var_order
        )
        self.text_label.grid(row=0, column=0, pady=5)
        self.text_label_order.grid(row=1, column=0, pady=5)

        self.radio1.grid(row=0, column=1, pady=5)
        self.radio2.grid(row=0, column=2, pady=5)

        self.radio1_order.grid(row=1, column=1, pady=5)
        self.radio2_order.grid(row=1, column=2, pady=5)

        self.button_play = tk.Button(
            frame2,
            text="Jogar",
            bg="#567",
            height=4,
            width=10,
            fg="white",
            command=self.button_play_start,
        )
        self.button_play.grid(row=0, column=1, padx=1, pady=1)

        self.pos_1 = tk.Button(
            frame2,
            text="",
            bg="#706c61",
            height=4,
            width=10,
            fg="white",
            command=lambda: self.button_clicked(0, self.label, self.human_player),
        )
        self.pos_1.grid(row=1, column=0, padx=1, pady=1)
        self.pos_2 = tk.Button(
            frame2,
            text="",
            bg="#706c61",
            height=4,
            width=10,
            fg="white",
            command=lambda: self.button_clicked(1, self.label, self.human_player),
        )
        self.pos_2.grid(row=1, column=1, padx=1, pady=1)
        self.pos_3 = tk.Button(
            frame2,
            text="",
            bg="#706c61",
            height=4,
            width=10,
            fg="white",
            command=lambda: self.button_clicked(2, self.label, self.human_player),
        )
        self.pos_3.grid(row=1, column=2, padx=1, pady=1)
        self.pos_4 = tk.Button(
            frame2,
            text="",
            bg="#706c61",
            height=4,
            width=10,
            fg="white",
            command=lambda: self.button_clicked(3, self.label, self.human_player),
        )
        self.pos_4.grid(row=2, column=0, padx=1, pady=1)
        self.pos_5 = tk.Button(
            frame2,
            text="",
            bg="#706c61",
            height=4,
            width=10,
            fg="white",
            command=lambda: self.button_clicked(4, self.label, self.human_player),
        )
        self.pos_5.grid(row=2, column=1, padx=1, pady=1)
        self.pos_6 = tk.Button(
            frame2,
            text="",
            bg="#706c61",
            height=4,
            width=10,
            fg="white",
            command=lambda: self.button_clicked(5, self.label, self.human_player),
        )
        self.pos_6.grid(row=2, column=2, padx=1, pady=1)
        self.pos_7 = tk.Button(
            frame2,
            text="",
            bg="#706c61",
            height=4,
            width=10,
            fg="white",
            command=lambda: self.button_clicked(6, self.label, self.human_player),
        )
        self.pos_7.grid(row=3, column=0, padx=1, pady=1)
        self.pos_8 = tk.Button(
            frame2,
            text="",
            bg="#706c61",
            height=4,
            width=10,
            fg="white",
            command=lambda: self.button_clicked(7, self.label, self.human_player),
        )
        self.pos_8.grid(row=3, column=1, padx=1, pady=1)
        self.pos_9 = tk.Button(
            frame2,
            text="",
            bg="#706c61",
            height=4,
            width=10,
            fg="white",
            command=lambda: self.button_clicked(8, self.label, self.human_player),
        )
        self.pos_9.grid(row=3, column=2, padx=1, pady=1)

        self.list_button = [
            self.pos_1,
            self.pos_2,
            self.pos_3,
            self.pos_4,
            self.pos_5,
            self.pos_6,
            self.pos_7,
            self.pos_8,
            self.pos_9,
        ]

        for button in self.list_button:
            button.config(state="disable")

    def set_state_button(self):
        for button in self.list_button:
            button.config(state="normal", text="")

    def button_play_start(self):
        self.button_play.config(state="disable")

        self.set_state_button()

        self.label = self.var_label.get()
        self.order = self.var_order.get()
        if self.label == 0:
            self.ia_label = 1
        else:
            self.ia_label = 0

        self.board = create_board()

        if self.order == 1:
            self.IA()

    def IA(self):
        position = IA_play(self.board)
        cord = self.position2cord(position)
        self.button_clicked(cord, self.ia_label, self.ia_player)

    def set_position(self, position, player):
        self.board[position[0], position[1]] = player

    def position2cord(self, position):
        cord = position[0] * 3 + position[1]
        return cord

    def cord2position(self, cord):
        x = int(np.floor(cord / 3))
        y = int(cord - 3 * x)
        return x, y

    def over(self):
        if wins(self.board, self.ia_player):
            showinfo("", "A IA venceu!!")
        elif wins(self.board, self.human_player):
            showinfo("", "A humanidade venceu!!")
        else:
            showinfo("", "Empate!!")
        self.button_play.config(state="normal")

    def button_clicked(self, button, label, player):
        if self.list_button[button]["text"] == "":
            position = self.cord2position(button)
            self.set_position(position, player)
            self.list_button[button]["text"] = self.labels[label]
            self.list_button[button].config(state="disable")

            if game_over(self.board):
                self.over()
            if player == -1:
                self.IA()
