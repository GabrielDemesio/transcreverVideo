import moviepy.editor as mp
import whisper
import os

def transcrever_video(caminho_video):
    print(f"Carregando vídeo: {caminho_video}")

    if not os.path.exists(caminho_video):
        print("Erro: O arquivo de vídeo não foi encontrado.")
        return

    video = mp.VideoFileClip(caminho_video)
    caminho_audio = "audio_temporario.wav"
    video.audio.write_audiofile(caminho_audio)

    print(f"Áudio extraído e salvo em: {caminho_audio}")

    print("Carregando modelo Whisper... (Isso pode levar um tempo na primeira vez)")
    model = whisper.load_model("base")

    print("Iniciando a transcrição do áudio...")
    resultado = model.transcribe(caminho_audio, language='pt')

    texto_transcrito = resultado['text']
    print("\n--- TRANSCRIÇÃO COMPLETA ---\n")
    print(texto_transcrito)

    nome_arquivo_saida = os.path.splitext(caminho_video)[0] + ".txt"
    with open(nome_arquivo_saida, "w", encoding="utf-8") as f:
        f.write(texto_transcrito)

    print(f"\nTranscrição salva em: {nome_arquivo_saida}")

    os.remove(caminho_audio)
    print(f"Arquivo de áudio temporário ({caminho_audio}) removido.")


if __name__ == "__main__":
    meu_video_mp4 = "FLUXO.mp4"
    transcrever_video(meu_video_mp4)