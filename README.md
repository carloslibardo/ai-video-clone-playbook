# Playbook do clone de vídeo com IA (AI video clone playbook)

Como eu faço vídeos com o meu rosto e a minha voz sem gravar de novo. Gravei 30 segundos de vídeo uma vez e usei umas 2 horas de áudio que eu já tinha. Daí pra frente eu escrevo o roteiro e a IA grava. Mas "sem gravar de novo" tem um custo: cada vídeo ainda pede alguns minutos de revisão, e cada refação gasta crédito.

Este repositório é o passo a passo completo, pra quem chegou pelo meu reel ou direto pelo GitHub. Está aqui tudo o que eu uso de verdade, inclusive o que deu errado. O primeiro clone de voz usou palestra mais áudios de WhatsApp; depois aprendi, treinando um modelo aberto, que o áudio de WhatsApp piorou a voz (capítulo 6).

## O que tem aqui

| Arquivo | Assunto |
|---|---|
| [docs/00-guia-pratico.md](docs/00-guia-pratico.md) | Comece por aqui: seu primeiro vídeo, passo a passo |
| [docs/01-gravacao-base.md](docs/01-gravacao-base.md) | Como gravar os 30 segundos que treinam o seu clone |
| [docs/02-voz-elevenlabs.md](docs/02-voz-elevenlabs.md) | Clone de voz, pronúncia, emoção por frase |
| [docs/03-video-heygen.md](docs/03-video-heygen.md) | Avatar, looks (roupas), prompts de movimento, fundo transparente |
| [docs/04-edicao.md](docs/04-edicao.md) | Padrão de montagem em Python + ffmpeg, efeitos, legenda, áudio |
| [docs/05-mcp-e-agentes.md](docs/05-mcp-e-agentes.md) | Rodando tudo de dentro do Claude Code via MCP, system prompts |
| [docs/06-open-source.md](docs/06-open-source.md) | Modelos abertos pra ficar mais barato: o que testamos e o que aprendemos |
| [docs/07-publicacao.md](docs/07-publicacao.md) | Postar em todas as redes, capa, rótulo de IA |
| [docs/08-checklist-qa.md](docs/08-checklist-qa.md) | O que conferir antes de publicar |
| [docs/09-expressoes-e-atuacao.md](docs/09-expressoes-e-atuacao.md) | Direção de atuação: expressão, olhar, gesto, voz e movimento por linha |
| [docs/10-dicas-e-melhorias.md](docs/10-dicas-e-melhorias.md) | O que deu errado e como corrigi, mais as próximas melhorias |
| [prompts/](prompts/) | System prompts e prompts de movimento prontos pra copiar |
| [scripts/clone_fx.py](scripts/clone_fx.py) | Efeitos (onda de choque, tremor, flash, fogo no texto) usados no vídeo. Dependências em `requirements.txt` |

## Antes de começar

- Conta na [HeyGen](https://www.heygen.com) num plano que tenha o Avatar V e a criação de avatar próprio (digital twin).
- Conta na [ElevenLabs](https://elevenlabs.io) num plano pago que libere o Professional Voice Clone (PVC). Pra testar, o Instant Voice Clone serve.
- Python 3.10 ou mais novo, com `pip install -r requirements.txt` (numpy, scipy, pillow). Pra conferir a pronúncia no capítulo 8: `pip install openai-whisper`.
- ffmpeg instalado (`brew install ffmpeg` no Mac, `apt install ffmpeg` no Linux).
- Opcional: [Claude Code](https://claude.com/claude-code) com os servidores MCP da HeyGen e da ElevenLabs (capítulo 5).

## O fluxo em uma tela

```
guia prático (docs/00) -> base gravada (30s, docs/01)
roteiro (texto, com direção de atuação, docs/09)
  -> voz: ElevenLabs eleven_v4, clone profissional treinado com ~2h de áudio seu
  -> vídeo: HeyGen Avatar V (engine avatar_v), treinado com ~30s de vídeo seu, um render por fala
  -> montagem: Python (PIL/numpy) + ffmpeg, efeitos e legenda por código
  -> QA: whisper confere a pronúncia, contact sheet confere os frames
  -> publicação: uma versão 9:16 com a capa no primeiro frame
  (deu errado? docs/10)
```

## Quanto custa

- HeyGen: medi 17 a 19 créditos numa fala de 20s com o Avatar V. Um vídeo de 30s com três "clones" saiu na faixa de 40 a 60 créditos contando refações. Confira a tabela atual da HeyGen, ela muda.
- ElevenLabs: cada fala regenerada custa pouco (uma frase de 3s ficou em ~120 créditos), o caro é errar várias vezes. Gere por frase e só refaça a que falhou.
- Edição: zero, é código rodando local.

## Regras que eu sigo

1. Todo vídeo diz que foi feito com IA, no texto e no rótulo da rede quando ela tem um.
2. Nenhum número inventado no roteiro. Se eu não medi, não falo.
3. Só clono a mim mesmo, com o consentimento que as próprias ferramentas pedem.

Rosto e voz são dados biométricos, que a LGPD trata como dado pessoal sensível: saiba onde cada ferramenta guarda o seu material e como apagar o avatar e a voz. Nunca clone outra pessoa sem autorização por escrito. Não use clone em conteúdo político ou eleitoral: a Justiça Eleitoral proíbe deepfake e exige rótulo de IA em conteúdo sintético (confira a resolução do TSE vigente).

## Licença

Texto e scripts sob MIT. Use, adapte, mande de volta o que melhorar.
