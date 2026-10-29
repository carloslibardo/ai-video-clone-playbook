# 5. Rodando tudo de dentro do Claude Code (MCP)

Eu não abro o site da HeyGen nem o da ElevenLabs. O Claude Code fala com as duas por MCP, escreve o script de montagem, roda, confere e me mostra o resultado.

## Servidores MCP que uso

| MCP | Pra quê |
|---|---|
| HeyGen | upload de áudio, render do avatar por fala, status, looks |
| ElevenLabs | geração de voz por frase, transcrição, flows |
| Contatio (o meu produto) | publicar em todas as redes, reposts, agendamento |

Instale os MCPs oficiais das ferramentas na sua conta e deixe o agente descobrir as ferramentas sozinho. Não cole chave de API em chat ou em arquivo do repositório.

## Como dividir o trabalho com o agente

1. Você escreve o roteiro e aprova.
2. O agente gera as vozes por frase e manda os takes.
3. Você escolhe os takes.
4. O agente sobe os áudios, dispara os renders, espera, monta e faz o QA (capítulo 8).
5. Você revisa o vídeo final. Só depois disso publica.

Dois pontos onde o agente sempre para e pergunta: antes de gastar crédito além do combinado, e antes de publicar ou mandar mensagem pra qualquer pessoa.

## System prompts

Prontos em [../prompts/](../prompts/):

- [system-prompt-diretor.md](../prompts/system-prompt-diretor.md): o agente que produz o vídeo de ponta a ponta.
- [system-prompt-roteirista.md](../prompts/system-prompt-roteirista.md): o agente que escreve e critica roteiros curtos.
- [motion-prompts.md](../prompts/motion-prompts.md): biblioteca de prompts de movimento por intenção.

## Lições de operar com agente

- Peça sempre "faça uma auto-revisão antes de dizer que terminou". Sem isso ele entrega a prévia acelerada achando que é o vídeo.
- Peça evidência: duração do vídeo e do áudio, LUFS, frames pretos, transcrição. "Ficou bom" não vale.
- Guarde IDs de render, de asset e de geração num arquivo. A conversa acaba, o arquivo fica.
