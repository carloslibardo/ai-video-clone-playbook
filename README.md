# AI video clone playbook

Como eu faço vídeos com o meu rosto e a minha voz sem gravar de novo. Gravei 30 segundos de vídeo uma vez e usei umas 2 horas de áudio que eu já tinha. Daí pra frente eu escrevo o roteiro e a IA grava.

Esse repositório é o passo a passo de quem comentou VÍDEO. Está aqui tudo o que eu uso de verdade, inclusive o que deu errado.

## O que tem aqui

| Arquivo | Assunto |
|---|---|
| [docs/01-gravacao-base.md](docs/01-gravacao-base.md) | Como gravar os 30 segundos que treinam o seu clone |
| [docs/02-voz-elevenlabs.md](docs/02-voz-elevenlabs.md) | Clone de voz, pronúncia, emoção por frase |
| [docs/03-video-heygen.md](docs/03-video-heygen.md) | Avatar, looks (roupas), prompts de movimento, fundo transparente |
| [docs/04-edicao.md](docs/04-edicao.md) | Montagem em Python + ffmpeg, efeitos, legenda, capa |
| [docs/05-mcp-e-agentes.md](docs/05-mcp-e-agentes.md) | Rodando tudo de dentro do Claude Code via MCP, system prompts |
| [docs/06-open-source.md](docs/06-open-source.md) | Modelos abertos pra ficar mais barato: o que testamos e o que aprendemos |
| [docs/07-publicacao.md](docs/07-publicacao.md) | Postar em todas as redes, capa, rótulo de IA |
| [docs/08-checklist-qa.md](docs/08-checklist-qa.md) | O que conferir antes de publicar |
| [prompts/](prompts/) | System prompts e prompts de movimento prontos pra copiar |
| [scripts/clone_fx.py](scripts/clone_fx.py) | Efeitos (onda de choque, tremor, flash, fogo no texto) usados no vídeo |

## O fluxo em uma tela

```
roteiro (texto)
  -> voz: ElevenLabs, clone profissional treinado com ~2h de áudio seu
  -> vídeo: HeyGen Avatar V, treinado com ~30s de vídeo seu, um render por fala
  -> montagem: Python (PIL/numpy) + ffmpeg, efeitos e legenda por código
  -> QA: whisper confere a pronúncia, contact sheet confere os frames
  -> publicação: uma versão 9:16 com a capa no primeiro frame
```

## Quanto custa

- HeyGen: o Avatar V gasta por volta de 20 créditos por minuto renderizado (tabela de preço da HeyGen). Um vídeo de 30s com três "clones" saiu na faixa de 40 a 60 créditos contando refações.
- ElevenLabs: cada fala regenerada custa pouco (uma frase de 3s ficou em ~120 créditos), o caro é errar várias vezes. Gere por frase e só refaça a que falhou.
- Edição: zero, é código rodando local.

## Regras que eu sigo

1. Todo vídeo diz que foi feito com IA, no texto e no rótulo da rede quando ela tem um.
2. Nenhum número inventado no roteiro. Se eu não medi, não falo.
3. Só clono a mim mesmo, com o consentimento que as próprias ferramentas pedem.

## Licença

Texto e scripts sob MIT. Use, adapte, mande de volta o que melhorar.
