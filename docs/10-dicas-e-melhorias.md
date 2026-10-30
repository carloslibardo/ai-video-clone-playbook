# 10. Dicas, erros e próximas melhorias

Lista consolidada do que deu errado e como eu corrigi, agrupada por etapa. Cada item aponta pro capítulo com o detalhe.

## Gravação da base

- Logo na roupa aparece em todo vídeo seguinte. Use peça lisa ([capítulo 1](01-gravacao-base.md)).
- Listra fina e tecido brilhante viram moiré no 9:16. Evite.
- Teto direto em cima da cabeça cria olheira e piora o lip-sync. Luz a 45 graus.
- Terminar a base de boca aberta deixa todo vídeo pequeno no canto e toda pausa com cara de interrompido. Termine de boca fechada com meio sorriso olhando pra lente.
- O clone só sabe os gestos e as expressões que viu. Grave variedade de propósito ([capítulo 9](09-expressoes-e-atuacao.md)).

## Voz

- Áudio de WhatsApp no treino piorou a voz do modelo aberto: compressão e sala diferente a cada gravação. Prefira poucos minutos limpos a muitas horas misturadas ([capítulo 1](01-gravacao-base.md), [capítulo 6](06-open-source.md)).
- A sigla "IA" saiu "ei-ai". Escreva como se fala e mantenha um dicionário de pronúncia aplicado antes de toda chamada ([capítulo 2](02-voz-elevenlabs.md)).
- Um bloco único de 30 segundos sai com a mesma temperatura do começo ao fim. Gere por fala ou por ato, com `previous_text` e `next_text`, e ajuste os parâmetros por ato.
- Não aperte "gerar" de novo à toa: cada geração cobra. Peça 2 takes por frase e refaça só a que falhou.
- Pra encaixar uma frase regerada, acelere levemente com ffmpeg (`atempo=1.09` passou despercebido). Acima de cerca de 1.12 soa apressado.
- Não sei se tags de emoção em português funcionam no `eleven_v4`. Teste com uma frase curta e, na dúvida, use inglês.

## Vídeo no HeyGen

- Prompt dizendo "vira pra olhar o painel" fez o avatar virar de perfil. Com elemento gráfico ao lado, peça movimento frontal ([capítulo 3](03-video-heygen.md), [capítulo 9](09-expressoes-e-atuacao.md)).
- Um render por fala: refazer custa só aquela fala, e cada uma ganha o próprio prompt.
- Nunca dispare de novo pra "ver se anda". É outro render cobrado. Consulte o status a cada 30 segundos.
- Planeje uma refação por fala no orçamento.
- Fundo transparente: confira na documentação atual como ligar, eu não consegui confirmar o parâmetro.

## Edição

- A prévia em 1 frame a cada 6 foi codificada na taxa errada e acelerou o vídeo: ficou com 5 segundos pra 32 de áudio. Encode a prévia em `fps / 6` e nunca mostre ela como se fosse o vídeo ([capítulo 4](04-edicao.md)).
- O tremor de câmera quebrou o render com "box offset can't be negative". Limite a caixa de recorte dentro do quadro.
- Deixe 250 px livres no topo e 420 px embaixo por causa da interface das redes.
- Um evento visual novo a cada 1 a 2 segundos.
- Mixe em -14 LUFS, pico abaixo de -1 dBFS.
- O último frame precisa funcionar parado: rosto de frente, boca fechada, chamada legível.

## Operando com agente

- Peça auto-revisão antes de dizer que terminou. Sem isso ele entrega a prévia achando que é o vídeo ([capítulo 5](05-mcp-e-agentes.md)).
- Peça evidência medida: duração, LUFS, frames pretos, transcrição.
- Guarde os IDs de render, de asset e de geração num arquivo.
- Aprovação sua antes de gastar além do combinado e antes de publicar ou mandar mensagem.
- Não cole chave de API em chat nem no repositório.

## Publicação

- Capa como primeiro frame por 0,1 segundo, com o áudio atrasado em 100 ms, senão a boca fica adiantada o vídeo inteiro ([capítulo 7](07-publicacao.md)).
- Diga que é IA no texto e no rótulo da rede.
- Responder comentário com mensagem automática é envio de mensagem: só com a API oficial, dentro das regras, pra quem pediu.

## Pesquisa e métricas

- "Parece melhor" me enganou uma vez: era só nitidez a mais, o movimento era idêntico. Meça sincronia, nitidez e estabilidade de identidade antes de comparar ([capítulo 6](06-open-source.md)).
- Número copiado de uma rodada anterior não é medição da rodada atual. Re-meça antes de afirmar.
- Voz: um clipe de referência fixo e parágrafos inteiros, não frases soltas, deram timbre mais estável.

## Próximas melhorias

Tudo abaixo está em andamento ou é intenção, sem resultado medido ainda.

- Open source (rodada r6): treino de voz e vídeo em GPU alugada, com comparação cega contra HeyGen e ElevenLabs. Acompanhe o [capítulo 6](06-open-source.md), que eu atualizo conforme sair resultado.
- Mais looks (roupas e cenários) a partir de novas bases curtas, com expressões variadas.
- Biblioteca de prompts de movimento maior, por intenção, com os que funcionaram marcados.
- Cenários gerados como fundos vazios e o avatar composto por cima, em vez de render com o fundo embutido.
- Versões em inglês e português com a mesma voz, gerando a de cada idioma do zero em vez de dublar a outra.
- Script de montagem genérico publicado aqui, hoje só os efeitos estão no repositório.
