# 3. Vídeo com HeyGen Avatar V

## Um render por fala, não um render do vídeo inteiro

Cada fala vira um render separado do avatar a partir do áudio dela. Vantagens:

- Refazer uma fala custa só aquela fala.
- Cada render recebe o próprio prompt de movimento.
- Dá pra usar um look (roupa) diferente por personagem. No vídeo dos clones, camiseta, blazer e moletom são três renders do mesmo avatar.

## Fundo transparente

Peça a saída em WebM com canal alfa. Assim você coloca o avatar em qualquer fundo, sobrepõe texto atrás da cabeça e põe dois clones no mesmo quadro sem recorte manual.

## Fluxo de upload do áudio

1. `create_asset_upload` com nome do arquivo, content type e tamanho em bytes.
2. PUT dos bytes na URL devolvida (com o content-type explícito e o header de criptografia que ela pedir).
3. `complete_asset_upload`.
4. `create_video_from_avatar` com o look, o asset de áudio e o prompt de movimento.
5. Consulte o status a cada 30s até terminar. Nunca dispare de novo pra "ver se anda": é outro render cobrado.

## Prompts de movimento

O prompt muda muito o resultado. Escreva a intenção da frase, o olhar e o gesto. Exemplos que usei:

- `"Direct intense eye contact, empathetic skeptical eyebrow raise, slight firm head shake, open palm questioning gesture."`
- `"Warm confident founder smile, reassuring head nod and open hand gesture toward chest."`
- `"Deadpan, unimpressed, arms relaxed, tiny shrug, looks straight at the lens."`

Mais em [../prompts/motion-prompts.md](../prompts/motion-prompts.md).

## O erro que mais me custou

Num trecho com um painel de interface na tela, o prompt dizia algo como "vira pra olhar o painel". O avatar girou de perfil, o rosto ficou atrás do painel e o texto na tela dizia "olhando pra câmera". Ficou confuso. Regra: se tem elemento gráfico do lado, peça movimento frontal (`"stays frontal, eyes on the lens, gestures stay inside the frame"`) e deixe a edição criar a interação.

## Custo

Avatar V fica na faixa de 20 créditos por minuto. Uma fala de 20s custou entre 17 e 19 créditos. Planeje uma refação por fala no orçamento.
