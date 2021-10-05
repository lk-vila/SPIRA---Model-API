<h1 align="center">SPIRA LABXP - WIKI</h1>
<br>

&nbsp;&nbsp;&nbsp;&nbsp;O [SPIRA](https://spira.ime.usp.br/coleta/) (Sistema de detecção precoce de insuficiência respiratória por meio de análise de áudio) é um projeto focado em criar um método de triagem baseado em áudio e inteligência artificial para a detecção de insuficiência respitória.

O nosso grupo da matéria LabXP de 2021 está encarregado de construir a API responsável pela interação com o modelo de inteligência artificial.

<br>

## <b>Tabela de Conteudo</b>
---
 - [Grupo](#grupo)
 - [Ferramentas](#ferramentas)
 - [Desenvolvimento](#desenvolvimento)
    - [Preparação e decisões iniciais](#preparação-e-decisões-iniciais)

<br>

## <b>Grupo</b>
---

- <b>João Vitor Soares</b>
- <b>Leonardo Meireles da Silva</b>
- <b>Lucas Vilela Aleixo</b>
- <b>Raul Mello Silva</b>
- <b>Vitor Daisuke Tamae</b> 
- <b>Ygor Sad Machado</b>

<br>

## <b>Ferramentas</b>
---

 - [Python](https://www.python.org/)
 - [PyTorch](https://pytorch.org/)
 - [Flask](https://flask.palletsprojects.com/en/2.0.x/)
 - [MongoDB](https://www.mongodb.com/)

<br>

## <b>Desenvolvimento</b>
---
## Preparação e decisões iniciais
&nbsp;&nbsp;&nbsp;&nbsp;Para iniciarmos o projeto tivemos que estudar a [pesquisa](https://aclanthology.org/2021.findings-acl.55.pdf) em que o SPIRA se baseia para compreender a lógica por trás do modelo com que estamos trabalhando e sobre como é feita a coleta de dados. 

&nbsp;&nbsp;&nbsp;&nbsp;O modelo de inteligência artificial foi construído em Python através da biblioteca PyTorch. Por questões de compatibilidade, optamos por também utilizar a linguagem Python para construir a API, utilizando a biblioteca Flask para o recebimento de requisições de inferência, que por sua vez são realizadas com o auxílio do próprio PyTorch. A ferramenta MongoDB é utilizada para o banco de dados de outros setores do projeto. Sendo assim, tendo em mente potenciais futuros planos de integração das aplicações, optamos por também utilizá-la para a nossa API.

&nbsp;&nbsp;&nbsp;&nbsp;Houve a necessidade de pesquisar sobre as ferramentas visto que nenhum dos membros da equipe tiveram contato prévio com elas.

##  Construção da API
&nbsp;&nbsp;&nbsp;&nbsp;Foi necessário compreender o funcionamento do código do modelo para que pudéssemos produzir uma inferência sobre os resultados obtidos, no entanto isso se mostrou um desafio muito maior do que esperado, devido à nossa falta de experiência trabalhando com modelos e a complexidade ímpar do código, causando diversas dúvidas sobre as configurações que deveriam ser usadas e como utilizar algumas funções do PyTorch.
&nbsp;&nbsp;&nbsp;&nbsp;


## <b>Futuros Passos</b>
---

- Dockerizar a aplicação
- Implementação do armazenamento de resultados no banco de dados
- Ajustes na inferência do modelo
- 