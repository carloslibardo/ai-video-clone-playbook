# 4. Edição por código

Não uso editor de vídeo. A montagem é um script Python que desenha cada frame e manda pro ffmpeg. Isso deixa tudo repetível: mudou uma fala, roda de novo.

## Estrutura do script de montagem

- Entrada: os WebM com alfa de cada fala, a trilha de diálogo mixada e um `cues.json` com início e fim de cada fala.
- Para cada frame (30 fps): fundo, avatares nas posições da cena, efeitos, texto, legenda.
- Saída: frames crus pro `ffmpeg` via pipe, codificados em H.264 1080x1920.
- Uma flag `--preview` renderiza 1 frame a cada 6 pra revisar rápido.

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

- Diálogo + trilha + efeitos sonoros mixados em `-14 LUFS` integrado, pico abaixo de `-1 dBFS`. É o alvo das redes sociais; mais alto elas abaixam e distorcem.

## Último frame

Termine num frame que funcione parado: rosto de frente, boca fechada, texto da chamada legível. Muita gente vê o último frame como capa quando o vídeo dá loop.
