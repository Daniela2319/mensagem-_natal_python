# 🎄 Feliz Natal! 🎅

Este projeto é uma animação de Feliz Natal que exibe uma mensagem com cores alternadas no terminal e toca uma música de Natal em loop. É um ótimo jeito de espalhar o espírito natalino de uma forma divertida e interativa.

## Funcionalidades

- Exibe uma mensagem de Natal com cores alternadas no terminal.
- Toca uma música de Natal em loop.
- Fácil de usar e personalizar.

## Dependências

Este projeto utiliza as seguintes bibliotecas:
- `colorama` para colorir o texto no terminal.
- `pygame` para reproduzir a música.

Para instalar estas dependências, execute:
```bash
pip install colorama pygame
```

# Como Usar
Certifique-se de ter Python instalado em seu sistema.
Instale as dependências necessárias usando o comando acima.
Salve sua música de Natal favorita como musicanatal.mp3 no mesmo diretório do seu script.
Execute o script Python:
```
python seu_script.py
```

# Código

```
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
```

# Observações

* Pressione `Ctrl+C` para parar a execução do script.
* Certifique-se de que o arquivo de música `musicanatal.mp3` está no mesmo diretório do script.
<br>

Desejo a todos um Feliz Natal e um próspero Ano Novo! 🎄🎅🎁
