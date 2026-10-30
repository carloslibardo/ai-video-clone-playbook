# 0. Seu primeiro vídeo, passo a passo

Este é o caminho inteiro em ordem, do zero ao vídeo publicado. Cada passo aponta pro capítulo que tem o detalhe. Os tempos e custos são só os que eu medi e já estão escritos nos outros capítulos; o que eu não medi está marcado como "não medi".

Modelos que eu uso de verdade: voz com ElevenLabs `eleven_v4` e vídeo com HeyGen Avatar V (engine `avatar_v`).

## Passo 1. Contas e ferramentas

1. Plano da HeyGen com Avatar V e avatar próprio (digital twin).
2. Plano pago da ElevenLabs com Professional Voice Clone (PVC). Pra só testar, o Instant Voice Clone serve.
3. Python 3.10+, `pip install -r requirements.txt`, ffmpeg e, pro QA, `pip install openai-whisper`.
4. Opcional: Claude Code com os MCPs da HeyGen e da ElevenLabs.

Detalhes: [README](../README.md) e [capítulo 5](05-mcp-e-agentes.md).

## Passo 2. Grave a base do vídeo (uma vez só)

Cerca de 30 segundos de vídeo seu: roupa lisa sem logo, luz a 45 graus, câmera na altura dos olhos, mãos visíveis, energia de conversa, e nos últimos 3 segundos boca fechada com meio sorriso olhando pra lente. Leia a frase de consentimento sem corte.

Detalhes: [capítulo 1](01-gravacao-base.md). Pra variar expressão, leia também o [capítulo 9](09-expressoes-e-atuacao.md) antes de gravar.

## Passo 3. Treine a voz

Junte áudio limpo seu (eu usei umas 2 horas, a maior parte de uma palestra com microfone decente) e crie o clone profissional na ElevenLabs. Prefira 30 minutos limpos a 2 horas misturadas.

Detalhes: [capítulo 2](02-voz-elevenlabs.md) e a seção de áudio do [capítulo 1](01-gravacao-base.md).

## Passo 4. Escreva o roteiro, uma linha por fala

Use o [system prompt do roteirista](../prompts/system-prompt-roteirista.md) ou escreva à mão. Conte cerca de 2,6 palavras por segundo. Pra cada fala, anote numa tabela: o texto como se fala (com o dicionário de pronúncia), a emoção, o look e o prompt de movimento. Sem número que você não mediu.

Detalhes: [capítulo 9](09-expressoes-e-atuacao.md) pra decidir emoção e movimento de cada linha.

## Passo 5. Gere a voz, fala por fala

Uma geração por fala, com `previous_text` e `next_text`, valores de `stability`, `style` e `speed` ajustados por ato, e 2 takes por frase. Escolha ouvindo. Só refaça a frase que falhou.

Detalhes: [capítulo 2](02-voz-elevenlabs.md).

## Passo 6. Renderize o avatar, fala por fala

Suba cada áudio escolhido, dispare um render por fala com o prompt de movimento daquela fala (biblioteca em [motion-prompts](../prompts/motion-prompts.md)), saída com fundo transparente, e consulte o status a cada 30 segundos. Nunca dispare de novo pra "destravar". Se há elemento gráfico ao lado do rosto, peça movimento frontal.

Custo que eu medi: 17 a 19 créditos numa fala de 20 segundos.

Detalhes: [capítulo 3](03-video-heygen.md).

## Passo 7. Monte

Script Python que desenha cada frame e manda pro ffmpeg: fundo, avatares, efeitos de [clone_fx.py](../scripts/clone_fx.py), texto e legenda palavra a palavra. Respeite a área segura (250 px no topo, 420 px embaixo), um evento visual a cada 1 a 2 segundos, áudio em -14 LUFS e último frame que funciona parado. Use a prévia só pra você.

Detalhes: [capítulo 4](04-edicao.md).

## Passo 8. QA com medição

Duração de vídeo e áudio, trechos pretos, frames congelados, loudness, transcrição comparada com o roteiro e contact sheet. Assista o arquivo final inteiro, não a prévia.

Detalhes: [capítulo 8](08-checklist-qa.md).

## Passo 9. Publique

Um 9:16 de 1080x1920 a 30 fps, capa no primeiro frame, texto dizendo que é IA e rótulo de IA da rede ligado.

Detalhes: [capítulo 7](07-publicacao.md).

## Quanto tempo e quanto custa

Tempo de gravação da base: 30 segundos de vídeo, e eu recomendo reservar uns dez minutos pra roupa, luz e enquadramento. Revisão: cada vídeo ainda pede alguns minutos. O tempo total de um vídeo completo eu não medi.

Custo: um vídeo de 30 segundos com três "clones" saiu na faixa de 40 a 60 créditos da HeyGen contando refações. Na ElevenLabs, uma frase de 3 segundos ficou em cerca de 120 créditos por geração; o caro é errar várias vezes. A edição é código local e não custa nada. As tabelas de preço mudam, confira as atuais.

## Quando algo der errado

Veja a lista de erros e correções no [capítulo 10](10-dicas-e-melhorias.md).
