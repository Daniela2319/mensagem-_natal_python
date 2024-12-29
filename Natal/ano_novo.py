import os
import random
import tkinter as tk
from tkinter import messagebox
import pygame  # Biblioteca para tocar música
import webbrowser

# Caminho do arquivo de música
arquivo_musica = "c:/Edu.Dani/teste/mensagem_natal/Natal/ano_novo.mp3"


# Função para abrir o vídeo
def abrir_video():
    video_url = "https://www.youtube.com/watch?v=LQKeHRqOAj4&ab_channel=NaturalDeep"
    webbrowser.open(video_url)


# Função para tocar música
def tocar_musica():
    if os.path.exists(arquivo_musica):
        pygame.mixer.init()  # Inicializa o mixer do pygame
        pygame.mixer.music.load(arquivo_musica)  # Carrega o arquivo de música
        pygame.mixer.music.play()  # Toca a música
    else:
        messagebox.showerror("Erro", "Arquivo de música não encontrado!")


# Função para exibir mensagem de sucesso
def exibir_mensagem():
    messagebox.showinfo("Parabéns!", "🎉 Você acertou! Feliz Ano Novo 2025! 🎆")


# Função chamada ao clicar em uma opção
def verificar_resposta(escolha, opcao_correta):
    if escolha == opcao_correta:
        tocar_musica()
        exibir_mensagem()
        abrir_video()
        root.destroy()  # Fecha a janela após o acerto
    else:
        messagebox.showwarning(
            "Resposta Incorreta", "❌ Resposta errada. Tente novamente!"
        )


# Configuração da interface
def main():
    global root
    root = tk.Tk()
    root.title("Jogo de Ano Novo")
    root.geometry("500x400")

    # Texto inicial
    tk.Label(
        root,
        text="🌟 Bem-vindo ao Jogo de Ano Novo! 🌟",
        font=("Helvetica", 14),
        wraplength=350,
        justify="center",
    ).pack(pady=10)

    tk.Label(
        root,
        text="Escolha a resposta correta para celebrar o Ano Novo! 🎶",
        font=("Helvetica", 12),
        wraplength=350,
        justify="center",
    ).pack(pady=10)

    # Opções embaralhadas
    opcoes = [
        "Ano Novo é Amor 💕.",
        "Ano Novo é Alegria 😄.",
        "Ano Novo é Felicidade, Alegria, Amor e Saúde 😊.",
    ]
    random.shuffle(opcoes)
    opcao_correta = opcoes.index("Ano Novo é Felicidade, Alegria, Amor e Saúde 😊.")

    # Botões para as opções
    for i, opcao in enumerate(opcoes):
        tk.Button(
            root,
            text=opcao,
            font=("Roboto", 14),
            width=40,
            command=lambda escolha=i: verificar_resposta(escolha, opcao_correta),
        ).pack(pady=5)
    root.mainloop()


if __name__ == "__main__":
    main()
