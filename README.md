# Projeto de Busca pelo Caminho Mais Curto em Roraima

## Descrição

Este projeto foi desenvolvido como parte da disciplina de Inteligência Artificial e tem como objetivo demonstrar a aplicação de algoritmos de busca pelo caminho mais curto em um cenário prático. Utilizamos uma rede de 15 municípios do estado de Roraima e representamos as conexões entre eles como arestas em um grafo ponderado. As distâncias reais (de estradas) entre os municípios são utilizadas como pesos nas arestas.

## Objetivo

O objetivo principal deste projeto é encontrar o caminho mais curto entre dois municípios dentro do estado de Roraima. Para atingir esse objetivo, o projeto segue as seguintes etapas:

1. **Construção do Grafo**: Os 15 municípios de Roraima são representados como nós em um grafo, e as distâncias reais entre eles são consideradas como pesos das arestas. Isso é feito utilizando a biblioteca NetworkX para criar e manipular a estrutura do grafo.

2. **Seleção de Algoritmo de Busca**: Implementamos um algoritmo de busca apropriado para encontrar o caminho mais curto entre dois municípios dentro do grafo. Para este projeto, utilizamos o algoritmo de A* (ou A estrela), uma escolha comum para problemas de busca pelo caminho mais curto.

4. **Visualização do Grafo**: Uma etapa inicial exibe a representação visual do grafo, mostrando os municípios e as conexões entre eles.

5. **Apresentação da Solução**: A solução do problema é exibida no console, mostrando o caminho mais curto encontrado.

## Execução

Para executar o projeto e encontrar o caminho mais curto entre dois municípios de Roraima, siga os seguintes passos:

1. Clone o repositório para o seu ambiente local:

git clone https://github.com/devmarcosantonio/buscaAstar.git

2. Execute o arquivo principal que representa o problema e inicie o algoritmo:

app.py

3. O projeto solicitará que você forneça um nó de origem e um nó de destino.

4. A solução do problema será exibida no console, mostrando o caminho mais curto encontrado e a distância total percorrida.


