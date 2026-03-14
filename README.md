# Chatbot Llama3.2:3b - O Conversador Inteligente

Ah, o chatbot! Esse pequeno projeto é como um papagaio digital que aprendeu a pensar – ou pelo menos, a fingir muito bem. Usando o modelo Llama3.2:3b via Ollama, ele responde às suas perguntas de forma concisa, em português brasileiro, e com um toque de streaming que faz parecer que está digitando em tempo real. Nada de esperar uma eternidade; as respostas chegam aos pedaços, como um quebra-cabeça se montando diante dos seus olhos!

## Funcionalidades Principais

- **Respostas em português brasileiro**: Porque quem quer conversar em inglês quando pode ser em português? (E sem erros de tradução, esperamos!)
- **Streaming de chunks**: As respostas aparecem aos poucos, como se o chatbot estivesse digitando freneticamente. É divertido assistir!
- **Prompt de sistema personalizável**: Uma linha mágica no código onde você pode transformar o chatbot em um especialista em culinária, um filósofo ou até um comediante. (Ou o que sua imaginação permitir.)
- **Interação simples**: Digite sua pergunta, pressione Enter, e veja a magia acontecer. Para sair, apenas pressione Enter sem nada escrever.

## Requisitos

Antes de começar a conversa, certifique-se de que:
- Você tem Python 3.8+ instalado (porque o futuro é agora, ou pelo menos o Python moderno).
- O Ollama está rodando: Instale o CLI do Ollama e execute `ollama serve` em um terminal. (Ou deixe o daemon fazer o trabalho pesado.)
- O modelo `llama3.2:3b` está baixado: Rode `ollama pull llama3.2:3b` para garantir que o cérebro do chatbot esteja no lugar.

## Instalação e Configuração

1. **Clone ou baixe o projeto**: Coloque os arquivos em uma pasta que você goste. (Dica: Evite pastas com nomes engraçados, como "Projetos Estranhos".)
2. **Instale as dependências**: No terminal, navegue até a pasta do projeto e execute:
   ```
   pip install -r requirements.txt
   ```
   (Ou use o `pyproject.toml` se preferir ferramentas modernas como Poetry.)
3. **Verifique o Ollama**: Certifique-se de que o servidor está rodando. Se não, o chatbot ficará mudo como uma pedra.

## Como Usar

1. Abra um terminal na pasta do projeto.
2. Execute o script:
   ```
   python chatbot.py
   ```
3. Digite sua pergunta quando solicitado (ex.: "Qual é a capital do Brasil?").
4. Assista às respostas chegarem em chunks – é como ver um filme em streaming, mas com palavras!
5. Para sair, pressione Enter sem digitar nada.

Exemplo de interação:
```
Using model: llama3.2:3b
Type something and press ENTER. (Empty input to exit.)

You: Qual é a melhor pizza do mundo?
Assistant: Ah, a pizza! Uma questão filosófica profunda. Eu diria que a melhor pizza é aquela feita com amor, mas se insistir em uma resposta técnica, a Margherita italiana sempre ganha pontos. E você, o que acha?
```

## Personalização

Quer mudar o comportamento do chatbot? Abra o arquivo `chatbot.py` e edite esta linha:
```python
SYSTEM_PROMPT = "Você é um assistente útil que fornece respostas concisas e precisas às perguntas do usuário. Sempre responda em português brasileiro. Se não souber a resposta, diga que não sabe em vez de inventar algo."
```
Transforme-o em um poeta, um contador de piadas ou um especialista em memes. A criatividade é sua!

## Contribuições e Licença

Este projeto é simples como um "olá mundo", mas se quiser contribuir com melhorias (como adicionar histórico de conversa ou emojis animados), sinta-se à vontade! Licença: MIT, porque compartilhamento é amor. (Mas não culpe o autor se o chatbot contar uma piada ruim.)

Divirta-se conversando com sua nova criação digital. Quem sabe, talvez ela se torne sua melhor amiga virtual? 😄