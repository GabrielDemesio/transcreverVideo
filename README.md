# 🎧 Transcrição de Vídeo com Whisper

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![OpenAI](https://img.shields.io/badge/Made%20with-Whisper-orange)

*A Python script to transcribe audio from video files using OpenAI's Whisper.*

---

## 📝 Sobre o Projeto

Este projeto contém um script Python (`transcrever_video.py`) que automatiza o processo de extração de áudio de um arquivo de vídeo (MP4) e realiza a sua transcrição para um arquivo de texto (.txt).

---

## 📖 Índice

- [Funcionalidades](#-funcionalidades)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Como Usar](#-como-usar)
- [Considerações Importantes](#-considerações-importantes)
- [Licença](#-licença)

---

## ✨ Funcionalidades

-   Extrai a faixa de áudio de arquivos de vídeo no formato MP4.
-   Utiliza a biblioteca `openai-whisper` para uma transcrição de alta precisão em português.
-   Salva a transcrição final em um arquivo de texto (`.txt`) com o mesmo nome do vídeo de origem.
-   Limpa automaticamente os arquivos de áudio temporários após a conclusão.

---

## 🛠️ Pré-requisitos

Antes de rodar o projeto, garanta que você tenha os seguintes softwares instalados no seu sistema:

1.  **Python 3.8 ou superior:**
    -   Você pode baixar em [python.org](https://www.python.org/downloads/).

2.  **FFmpeg:**
    -   É uma dependência externa essencial que o `moviepy` e o `whisper` usam para processar arquivos de áudio e vídeo.

    -   **No Linux (Ubuntu/Debian):**
        ```bash
        sudo apt update && sudo apt install ffmpeg
        ```
    -   **No macOS (usando Homebrew):**
        ```bash
        brew install ffmpeg
        ```
    -   **No Windows:**
        -   Baixe o FFmpeg em [ffmpeg.org](https://ffmpeg.org/download.html) e adicione a pasta `bin` ao PATH do seu sistema.

---

## 🚀 Instalação

Siga os passos abaixo para configurar o ambiente do projeto:

1.  **Clone o Repositório**
    ```bash
    git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
    cd seu-repositorio
    ```

2.  **Crie e Ative um Ambiente Virtual**
    -   É uma boa prática isolar as dependências do projeto.

    ```bash
    # Crie o ambiente virtual
    python3 -m venv .venv

    # Ative o ambiente
    # No Linux ou macOS:
    source .venv/bin/activate
    # No Windows:
    # .venv\Scripts\activate
    ```

3.  **Instale as Bibliotecas Python**
    -   Com o ambiente virtual ativado, instale as dependências. Usaremos uma versão específica do `moviepy` que se provou estável para este caso de uso.

    ```bash
    pip install openai-whisper moviepy==1.0.3
    ```

---

## ▶️ Como Usar

1.  **Adicione seu Vídeo**
    -   Coloque o seu arquivo de vídeo (ex: `meu_video.mp4`) na pasta principal do projeto.

2.  **Configure o Script**
    -   Abra o arquivo `transcrever_video.py` e edite a linha 40 para que ela contenha o nome exato do seu arquivo de vídeo.

    ```python
    # Linha 40 do script
    meu_video_mp4 = "seu_video.mp4" # <-- Troque este nome pelo nome do seu vídeo
    ```

3.  **Execute a Transcrição**
    -   Certifique-se de que seu ambiente virtual esteja ativado e execute o script no terminal:

    ```bash
    python transcrever_video.py
    ```

4.  **Aguarde o Resultado**
    -   O script irá extrair o áudio, carregar o modelo do Whisper (pode demorar na primeira vez) e iniciar a transcrição. Ao final, um arquivo `.txt` com o mesmo nome do seu vídeo aparecerá na pasta.

---

## ⚠️ Considerações Importantes

-   **Memória RAM e Vídeos Longos:** A transcrição de vídeos muito longos pode consumir uma quantidade significativa de memória RAM. Se o processo for interrompido com a mensagem **"Morto"** (`Killed`), significa que a memória do seu computador esgotou. Para resolver isso, você pode:
    -   **Usar um modelo menor do Whisper:** No script, troque a linha `model = whisper.load_model("base")` por `model = whisper.load_model("tiny")` para um consumo de memória muito menor.
    -   **Fechar outros aplicativos** para liberar mais RAM antes de executar o script.

-   **Primeira Execução:** A primeira vez que você rodar o script, ele precisará baixar o modelo do Whisper da internet, o que pode levar alguns minutos dependendo da sua conexão. Nas execuções seguintes, o processo será mais rápido.

---

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
