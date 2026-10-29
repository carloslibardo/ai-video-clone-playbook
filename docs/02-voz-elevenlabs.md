# 2. Voz com ElevenLabs

## Clone

- Professional Voice Clone (PVC) treinado com ~2 horas do meu áudio. Instant clone com 1 minuto funciona pra teste, mas o timbre varia mais entre frases.
- Modelo de geração: `eleven_v4`. Aceita tags de emoção entre colchetes no próprio texto, por exemplo `[calmo, debochado] Relaxa.`.

## Gere por frase, com contexto

Um bloco único de 30 segundos sai com a mesma temperatura do começo ao fim. O que funciona:

- Uma geração por fala (ou por ato do roteiro).
- Passe `previous_text` e `next_text` da API, pra entonação continuar de uma frase pra outra.
- Ajuste por ato. Os valores que usei num vídeo de 58s:

| Ato | stability | similarity_boost | style | speed |
|---|---|---|---|---|
| Gancho (provocação) | 0.34 | 0.88 | 0.52 | 1.12 |
| Dor (urgência) | 0.40 | 0.86 | 0.38 | 1.16 |
| Virada (autoridade) | 0.36 | 0.88 | 0.48 | 1.13 |
| Prova (clareza) | 0.42 | 0.86 | 0.40 | 1.14 |
| CTA (convite) | 0.35 | 0.90 | 0.50 | 1.10 |

- Peça 2 takes por frase e escolha ouvindo. Não aperte "gerar" de novo à toa: cada geração cobra.

## Pronúncia: escreva como se fala

O modelo lê sigla em inglês. "Agentes de IA" saiu "agentes de ei-ai". A correção foi escrever como se fala:

| Escrito | Mande pro TTS |
|---|---|
| IA | í-á |
| SDR | ésse-dê-érre |
| ICP | i-cê-pê |
| contatio.ai | contátio ponto A-I |
| SaaS | sás |
| LinkedIn | linquedin |

Mantenha esse dicionário num arquivo e aplique antes de toda chamada. Depois confira com transcrição automática (capítulo 8).

## Trocar uma frase sem refazer tudo

Quando só uma frase sai errada:

1. Gere só ela de novo.
2. Se ficou um pouco mais longa que o buraco, acelere levemente com ffmpeg: `atempo=1.09` passou despercebido. Acima de ~1.12 começa a soar apressado.
3. Cole no ponto exato da trilha e re-renderize só o trecho de vídeo daquela fala (o lip-sync é feito a partir do áudio).
