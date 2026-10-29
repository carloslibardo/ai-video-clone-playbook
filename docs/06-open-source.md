# 6. Open source: dá pra fazer mais barato?

Em paralelo ao HeyGen + ElevenLabs, estou testando um clone 100% com modelos abertos rodando em GPU alugada (A100 no Google Cloud). O objetivo é custo por vídeo perto de zero depois do treino. Resultado honesto até aqui: **ainda não chega no nível das ferramentas pagas**, mas o caminho ficou claro. Atualizo aqui conforme avança.

## Voz

Modelos testados:

| Modelo | Como usamos | Nota |
|---|---|---|
| Qwen3-TTS 1.7B | fine-tune com um falante só | Apache-2.0, pt-BR nativo, receita oficial de fine-tune. Melhor aposta aberta pra pt-BR até agora |
| VoxCPM2 | zero-shot + camada de validação | Sem treino; compete com o fine-tune quando você filtra os takes |
| F5-TTS | fine-tune | Funcionou, mas o timbre variou mais |

O que aprendemos medindo (timbre entre frases, faixa de pitch, queda no fim da frase, pausas):

1. **O problema era o processo, não o modelo.** Gerar frase por frase, cada uma clonando de um clipe de referência diferente, deixou o timbre 1,8x mais instável que a voz real. A ElevenLabs usa um modelo treinado, então o timbre é fixo.
2. **Uma referência fixa.** Use sempre o mesmo clipe limpo como referência.
3. **Gere parágrafos, não frases soltas.** Frase isolada sai com entonação "neutra-meio", sem cair no fim.
4. **Dados limpos ganham de dados muitos.** Treinar com 1h30 de áudio de WhatsApp (compressão, salas diferentes) piorou. A palestra gravada com microfone é o material certo.
5. **Gere N takes e escolha por métrica.** 8 takes por parágrafo, transcrição automática (faster-whisper), aceita só quem tem erro de palavra até 3%, e ranqueia por similaridade de voz contra a média dos seus melhores clipes.
6. **Não "preencha" as pausas.** Colocar ruído de sala contínuo tirou todos os respiros e a fala ficou colada.

## Vídeo

| Modelo | Tipo | Nota |
|---|---|---|
| LatentSync | lip-sync só da boca | Boca sincroniza, mas cabeça e sobrancelhas continuam do vídeo original |
| Wan2.2-S2V | vídeo a partir de imagem + áudio | Mexe cabeça e corpo junto com a fala; caro de rodar |
| InfiniteTalk, LTX-2.3 Dub-It | vídeo-pra-vídeo guiado por áudio | Candidatos pra re-dirigir o corpo inteiro |
| LongCat-Video-Avatar 1.5, LiveAvatar | imagem-pra-vídeo | Os mais próximos do Avatar V segundo relatos de 2026, sem prova cega |

Lições:

1. **Lip-sync só de boca não salva gesto errado.** Se o rosto foi gravado falando outra coisa, a sobrancelha não acompanha a fala (correlação de 0,17 medida). Ou você grava a base falando o mesmo roteiro, ou usa um modelo que move a cabeça inteira.
2. **Precisão numérica importa.** Em A100, rodar em fp8 foi muito mais lento (166 s por passo) porque a placa não tem núcleo fp8. Use bf16.
3. **Meça antes de comparar.** Sincronia boca-áudio, nitidez, estabilidade de identidade. "Parece melhor" enganou a gente uma vez: era só nitidez a mais, o movimento era idêntico.

## Custo do experimento

Orçamento de até ~800 USD de GPU pra rodada inteira (treino de voz, LoRA de vídeo, comparações). Depois de treinado, cada vídeo custa minutos de GPU. Compensa se você produz muito; pra poucos vídeos por mês, HeyGen + ElevenLabs ainda saem mais baratos que o seu tempo.

## Atalho que bate qualquer TTS

Grave você mesmo o roteiro uma vez, com o celular num cômodo sem eco. Prosódia real ganha de qualquer modelo. Use o clone de voz só quando não der pra gravar.
