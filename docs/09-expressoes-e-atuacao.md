# 9. Expressões e direção de atuação

O Avatar V não inventa uma performance sozinho. Ele devolve o repertório de gestos que viu no vídeo base e obedece ao prompt de movimento de cada render. Quem dirige a atuação é você, linha por linha. Este capítulo é o método.

## A ideia: uma linha, uma intenção

Antes de gerar qualquer coisa, escreva a partitura do roteiro. Pra cada fala, uma linha de tabela com estas colunas:

| Coluna | O que vai |
|---|---|
| Texto falado | Já com a grafia de pronúncia ([capítulo 2](02-voz-elevenlabs.md)) |
| Intenção | Uma palavra: provocar, resolver, explicar, revelar, tranquilizar, convidar |
| Voz | Tag de emoção da ElevenLabs e os parâmetros do ato |
| Cadência | Onde acelera, onde cai, onde pausa |
| Rosto e olhar | Sobrancelha, sorriso, direção do olhar |
| Gesto | Mão, cabeça, postura |
| Prompt de movimento | A frase em inglês que vai pro render |

Uma intenção por render. Se a fala muda de ideia no meio, quebre em duas falas.

## Da intenção ao rosto, ao olhar e ao gesto

| Intenção | Rosto e olhar | Gesto | Prompt de movimento |
|---|---|---|---|
| Provocar | Sobrancelha arqueada, olhar cravado na lente | Leve balanço negativo de cabeça, palma aberta como pergunta | `Direct intense eye contact, skeptical eyebrow raise, slight firm head shake, open palm questioning gesture.` |
| Resolver | Meio sorriso confiante, olhar firme | Aceno positivo, mão aberta em direção ao peito | `Warm confident smile, reassuring head nod, open hand gesture toward chest.` |
| Dor, custo | Sobrancelhas contraídas, expressão séria | Gesto ritmado, corte com a mão na palavra-chave | `Serious expression, rhythmic hand gesture, subtle downward hand chop on the key phrase, cautionary nod.` |
| Explicar em itens | Rosto aceso, postura ereta | Contar nos dedos, voltar o olhar à lente a cada item | `High energy, upright posture, counting points on fingers, eyes return to the lens after each point.` |
| Segredo, vantagem | Sobrancelhas sobem, meio sorriso de cúmplice | Pequena inclinação em direção à câmera | `Eyebrows raised, conspiratorial half smile, small lean toward the camera.` |
| Autoridade | Olhar seguro | Aceno firme, mão fechada precisa na frase-chave | `Authoritative nod, precise closed-hand gesture on the key phrase, steady gaze.` |
| Simplicidade | Rosto relaxado, sorriso discreto | Mão aberta sem esforço | `Relaxed approachable expression, slight smile, effortless open hand gesture.` |
| Tranquilizar | Olhar que passa controle e segurança | Gesto de proteção na frase-chave | `Reassuring confident expression, protective hand gesture on the key phrase.` |
| Orgulho de resultado | Sorriso genuíno | Ritmo vivo ao listar itens | `Energetic pacing, proud confident smile while stating the result.` |
| Convidar, fechar | Olhar cravado, sorriso que segura contato por cerca de um segundo | Gesto em direção ao link ou botão | `Direct charismatic close-up, short pause, warm confident smile held for one second, mouth closed at the end.` |

Dica de escrita: cite no prompt a expressão que você quer na palavra que importa (`on 'the key phrase'`). Eu usei isso e o resultado acompanhou a ênfase, mas não medi quanto.

## Casar voz e movimento na mesma linha

A intenção tem que ser a mesma nas duas ferramentas, senão o rosto diz uma coisa e a voz outra.

| Intenção | Tag de emoção (ElevenLabs, em inglês) | Ajuste de voz (ato correspondente do capítulo 2) |
|---|---|---|
| Provocar | `[sarcastic]` ou `[serious]` | Gancho: estável baixo, estilo alto, mais rápido |
| Resolver, convidar | `[warm]` | Convite: estilo médio-alto, velocidade mais calma |
| Dor, urgência | `[serious]` | Dor: mais rápido, estilo menor |
| Revelar, autoridade | `[confident]` | Virada: estilo médio-alto |
| Explicar | `[excited]` | Prova: estilo médio, velocidade firme |

As tags de exemplo são ilustrativas. Eu só confirmei na documentação que o `eleven_v4` aceita tags de áudio entre colchetes, com exemplos em inglês. Não verifiquei quais nomes de tag existem nem se tags em português funcionam: teste com uma frase curta e ouça antes de usar no vídeo todo. Os valores numéricos por ato estão na tabela do [capítulo 2](02-voz-elevenlabs.md).

Exemplo de linha completa:

```
Fala:      [serious] Hoje você paga caro pra um time perder horas no braço.
Voz:       ato Dor (stability 0.40, style 0.38, speed 1.16)
Cadência:  acelera em "perder horas no braço", cai no fim
Movimento: Serious expression, rhythmic hand gesture, cautionary nod on the last phrase.
```

## Pausas e respiros

- Marque a pausa no roteiro, com duração aproximada. Nos meus roteiros usei de cerca de 200 a 350 milissegundos antes de uma virada ou de uma chamada, e foi isso que fez a frase "pousar". Ajuste ouvindo.
- Uma pausa antes da solução ("A [produto] resolve isso") faz a virada soar segura.
- Depois de uma frase de impacto, dê uma pausa curta antes da chamada pra ação.
- Respiro não é defeito. No experimento com modelo aberto, preencher as pausas com ruído de sala tirou todos os respiros e a fala ficou colada ([capítulo 6](06-open-source.md)). A voz real e a da ElevenLabs têm pausas de verdade.
- Frase de pergunta indignada sobe no fim; frase de solução cai no fim. Escreva isso na coluna de cadência.

## O que parece falso

- Sorriso o tempo todo. Alterne com expressão séria e neutra, senão nada tem peso.
- Gesto igual em toda fala. Varie o prompt de movimento por intenção.
- Olhar que sai da lente sem motivo. Em geral o olhar volta à lente depois de cada ponto.
- Rosto contente com voz de urgência (ou o contrário). Case a intenção nas duas ferramentas.
- Boca aberta no quadro de repouso. Por isso a base termina com a boca fechada e meio sorriso ([capítulo 1](01-gravacao-base.md)).
- Fala de pergunta sem a inflexão de pergunta, ou frase que não "fecha" no fim: soa lida, não dita.
- Ênfase em todas as palavras. Uma ou duas por frase.

## A regra frontal

Se há painel, card ou texto ao lado do rosto, não peça "olhar pro painel". Peça movimento frontal e deixe a edição criar a interação: `Stays frontal, eyes on the lens, gestures stay inside the frame, no head turn.`

O que aconteceu quando eu não segui: o avatar virou de perfil, o rosto ficou atrás do painel e o texto na tela dizia "olhando pra câmera". Detalhes no [capítulo 3](03-video-heygen.md).

## Direção na hora de gravar a base

A expressão que o clone sabe fazer vem do vídeo base. Na gravação, faça deliberadamente:

- Sobrancelhas ativas, sorriso leve nos olhos, variação de ritmo.
- Palma aberta explicando, um gesto firme pra pontuar, depois mãos relaxadas.
- Uma ou duas expressões sérias e uma de surpresa, pra existir repertório pra elas.
- Final com boca fechada e meio sorriso olhando pra lente.

Se o look novo for gravado, o resultado só reproduz o que você mostrou lá. Se faltou uma expressão, grave outro look em vez de pedir pro prompt inventar.

## Movimento por cima do rosto

Boa parte do dinamismo não vem do avatar, vem da montagem: punch-in, whip-pan, congelar em preto e branco, texto atrás da cabeça, cartões flutuantes, vídeo pequeno no canto. Fica no [capítulo 4](04-edicao.md) e em [clone_fx.py](../scripts/clone_fx.py).
