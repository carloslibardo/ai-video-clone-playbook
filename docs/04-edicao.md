# 4. Edição por código

Não uso editor de vídeo. A montagem é um script Python que desenha cada frame e manda pro ffmpeg. Isso deixa tudo repetível: mudou uma fala, roda de novo.

## Padrão do script de montagem

O script de montagem completo não está neste repositório, porque ele é amarrado ao meu projeto. O que está aqui são os efeitos, em [../scripts/clone_fx.py](../scripts/clone_fx.py). Este é o padrão que eu sigo, e o esqueleto abaixo é o mínimo pra você montar o seu:

- Entrada: os WebM com alfa de cada fala, a trilha de diálogo mixada e um arquivo de marcações (por exemplo `cues.json`, formato à sua escolha) com início e fim de cada fala.
- Para cada frame (30 fps): fundo, avatares nas posições da cena, efeitos, texto, legenda.
- Saída: frames crus pro `ffmpeg` via pipe, codificados em H.264 1080x1920.
- Uma prévia que renderiza 1 frame a cada 6 pra revisar rápido.

```python
import subprocess
import numpy as np
from clone_fx import W, H, shake_frame, flash_frame

FPS, DURACAO = 30, 10.0
ff = subprocess.Popen(
    ["ffmpeg", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
     "-i", "-", "-i", "dialogo.wav", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-shortest", "out.mp4"],
    stdin=subprocess.PIPE,
)
for n in range(int(FPS * DURACAO)):
    t = n / FPS
    frame = np.zeros((H, W, 3), np.float32)  # aqui entram fundo, avatares, texto e legenda
    frame = shake_frame(frame, t - 2.0)       # tremor a partir de 2,0 s
    frame = flash_frame(frame, t - 2.0)
    ff.stdin.write(np.clip(frame, 0, 255).astype(np.uint8).tobytes())
ff.stdin.close()
ff.wait()
```

Atenção: na prévia, encode na taxa certa (`fps / 6`). Eu esqueci, a prévia ficou com 5s de vídeo pra 32s de áudio, o vídeo acelerou e terminou preto. Nunca mostre a prévia pra alguém como se fosse o vídeo.

## Efeitos

Os efeitos estão em [../scripts/clone_fx.py](../scripts/clone_fx.py), em numpy/scipy, sem plugin:

- `shockwave_frame`: anel de refração que expande do ponto de impacto.
- `shake_frame`: tremor de câmera com zoom leve. Limite a caixa de recorte dentro do quadro; sem isso o render quebra com "box offset can't be negative" quando o tremor é forte.
- `flash_frame`, `chroma_frame`: flash branco e separação RGB curta, pra vender impacto.
- `orb`, `ring`: bola de luz voando entre dois pontos e anel no destino.
- `Flames`: fogo procedural subindo do contorno de um texto.

Regra de ritmo que peguei de reels que performam: um evento visual novo a cada 1 a 2 segundos.

## Legenda e área segura no 9:16

- Deixe ~250 px livres no topo e ~420 px embaixo. É onde a interface das redes cobre o vídeo.
- Legenda palavra a palavra, logo abaixo do queixo.

## Áudio

- Diálogo + trilha + efeitos sonoros mixados em `-14 LUFS` integrado (LUFS é a medida de volume percebido), pico abaixo de `-1 dBFS`. É o alvo das redes sociais; mais alto elas abaixam o volume (normalizam).

## Último frame

Termine num frame que funcione parado: rosto de frente, boca fechada, texto da chamada legível. Muita gente vê o último frame como capa quando o vídeo dá loop.
