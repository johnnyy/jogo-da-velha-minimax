import tkinter as tk

from interface import JogoDaVelha

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Jogo da Velha")

    frame_radio = tk.Frame(root)
    frame_radio.grid(sticky=tk.N, padx=10, pady=10)

    frame_tabuleiro = tk.Frame(root)
    frame_tabuleiro.grid(sticky=tk.S)

    clicked = True

    JogoDaVelha(frame_radio, frame_tabuleiro)

    root.mainloop()
