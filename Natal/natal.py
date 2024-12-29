import time
from colorama import Fore, Style, init
import pygame

# Inicializar colorama
init(autoreset=True)

# Lista de cores alternadas
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA]

# Mensagem de Natal
message = (
    "🎄 Feliz Natal! 🎅 \n Que seu Natal seja muito abençoado com a paz de Cristo!"
)


# Função para exibir a mensagem de Natal com cores alternadas
def display_message():
    while True:
        for color in colors:
            print("\033c", end="")  # Limpar terminal (ANSI escape)
            print(color + Style.BRIGHT + message.center(50))
            time.sleep(0.5)


# Função principal
def new_func(__name__, display_message):
    if __name__ == "__main__":
        try:
            display_message()
        except KeyboardInterrupt:
            pygame.mixer.music.stop()


if __name__ == "__main__":
    # Inicializar o mixer do pygame
    pygame.mixer.init()

    # Carregar a música de Natal
    pygame.mixer.music.load("musicanatal.mp3")

    # Reproduzir a música em loop
    pygame.mixer.music.play(-1)

    # Exibir a mensagem de Natal
    display_message()


# Função para exibir mensagem de sucesso
def display_success_message():
    print(Fore.GREEN + Style.BRIGHT + "Mensagem de Natal exibida com sucesso!")
    time.sleep(2)
    print(Fore.RESET + Style.RESET_ALL)
