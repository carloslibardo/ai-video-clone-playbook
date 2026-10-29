# 8. Checklist antes de publicar

Tudo aqui é medido, não "achado".

```bash
# duração de vídeo e áudio batem?
ffprobe -v error -show_entries stream=codec_type,duration -of csv=p=0 video.mp4

# trechos pretos
ffmpeg -i video.mp4 -vf blackdetect=d=0.1:pix_th=0.10 -an -f null - 2>&1 | grep black_start

# frames congelados
ffmpeg -i video.mp4 -vf freezedetect=n=0.003:d=0.5 -an -f null - 2>&1 | grep freeze_start

# loudness (alvo -14 LUFS, pico < -1 dBFS)
ffmpeg -i video.mp4 -af loudnorm=print_format=summary -f null - 2>&1 | tail -12

# pronúncia: a transcrição tem que bater com o roteiro
whisper video.mp4 --model small --language pt

# contact sheet: um frame por segundo numa grade só
ffmpeg -i video.mp4 -vf "fps=1,scale=270:-1,tile=6x6" -frames:v 1 sheet.jpg
```

- [ ] Vídeo e áudio com a mesma duração
- [ ] Nenhum trecho preto ou congelado
- [ ] Loudness entre -15 e -13 LUFS
- [ ] Transcrição sem palavra trocada (sigla é onde mais erra)
- [ ] Contact sheet: rosto de frente onde tem texto do lado, nada cortado pela área segura
- [ ] Último frame funciona como imagem parada
- [ ] Capa no frame 0
- [ ] Texto do post diz que é IA
- [ ] Assistiu o arquivo final inteiro, não a prévia
