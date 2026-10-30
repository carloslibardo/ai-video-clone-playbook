# 7. Publicação

## Uma versão, todas as redes

Exporte um 9:16 1080x1920 a 30 fps e use em Instagram Reels, TikTok, YouTube Shorts, LinkedIn e X.

## Capa

Nem toda rede deixa definir a capa por API hoje. O truque que funciona em quase todas: **coloque a capa como o primeiro frame do vídeo, por 0,1 segundo**.

```bash
ffmpeg -loop 1 -framerate 30 -t 0.1 -i capa.jpg -i video.mp4 \
  -filter_complex "[0:v]scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:color=black,setsar=1,fps=30[c];[1:v]setsar=1,fps=30[v];[c][v]concat=n=2:v=1:a=0,format=yuv420p[out];[1:a]adelay=100:all=1[a]" \
  -map "[out]" -map "[a]" -c:v libx264 -crf 18 -c:a aac -b:a 192k -movflags +faststart video-com-capa.mp4
```

A capa dura 3 quadros a 30 fps (0,1 s), por causa do `-framerate 30`. Uma capa que não é 9:16 ganha barras pretas em vez de ficar esticada. O `adelay=100` atrasa o áudio nos mesmos 0,1s da capa. Sem ele a boca fica 100 ms adiantada em relação à voz o vídeo inteiro.

- Instagram, TikTok e LinkedIn pegam o primeiro frame como capa padrão.
- YouTube Shorts escolhe sozinho. Troque no YouTube Studio depois de publicar.
- Para miniatura horizontal (16:9), centralize a capa vertical sobre uma versão desfocada dela mesma.

## Texto

- Curto. Uma frase de gancho, uma de contexto, a chamada.
- Diga que é IA: "(Vídeo gerado com IA.)" no texto, e ative o rótulo de conteúdo de IA onde existe (Instagram, TikTok, YouTube).
- Em inglês num perfil e português no outro, publique o inglês primeiro e reposte cruzado.

## Instagram: teste antes

O Reels de teste (trial reel) mostra o vídeo só pra quem não te segue. Se performar, ele vai pro perfil. Bom pra testar gancho sem queimar o feed.

## Chamada "comenta VÍDEO"

Responder cada comentário com o link por DM é uma automação de mensagem. Faça só com a API oficial da Meta (resposta privada ao comentário), dentro das regras dela, e mande só pra quem pediu.
