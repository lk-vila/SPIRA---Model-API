<h1 align="center">SPIRA LABXP - WIKI</h1>

<p align="center">
  <img src="https://cdn.discordapp.com/attachments/887108943963369513/900115923795578880/68913925.png" alt="Tree" width="125" height="125">
</p>
<p align="center">
  <i>Projeto do LabXP em parceria com o SPIRA.</i>
</p>

<br>

&nbsp;&nbsp;&nbsp;&nbsp;O [SPIRA](https://spira.ime.usp.br/coleta/) (Sistema de detecção precoce de insuficiência respiratória por meio de análise de áudio) é um projeto focado em criar um método de triagem baseado em áudio e inteligência artificial para a detecção de insuficiência respitória.

O nosso grupo da matéria LabXP de 2021 está encarregado de construir a API responsável pela interação com o modelo de inteligência artificial.

<br>

## <b>Tabela de Conteúdo</b>
---
 - [Grupo](#<b>grupo</b>)
 - [Ferramentas](#ferramentas)
 - [Desenvolvimento](#desenvolvimento)
    - [Preparação e decisões iniciais](#preparação-e-decisões-iniciais)
    - [Construção da API](#construção-da-api)
 - [Futuros Passos](#futuros-passos)

<br>

## Grupo
---

- <b>João Vitor Soares</b>
- <b>Leonardo Meireles da Silva</b>
- <b>Lucas Vilela Aleixo</b>
- <b>Raul Mello Silva</b>
- <b>Vitor Daisuke Tamae</b> 
- <b>Ygor Sad Machado</b>

<br>

## Ferramentas
---

 - [Python](https://www.python.org/)
 - [PyTorch](https://pytorch.org/)
 - [Flask](https://flask.palletsprojects.com/en/2.0.x/)
 - [MongoDB](https://www.mongodb.com/)

<br>

## Desenvolvimento
---
## Preparação e decisões iniciais
&nbsp;&nbsp;&nbsp;&nbsp;Para iniciarmos o projeto tivemos que estudar a [pesquisa](https://aclanthology.org/2021.findings-acl.55.pdf) em que o SPIRA se baseia para compreender a lógica por trás do modelo com que estamos trabalhando e sobre como é feita a coleta de dados. 

&nbsp;&nbsp;&nbsp;&nbsp;O modelo de inteligência artificial foi construído em Python através da biblioteca PyTorch. Por questões de compatibilidade, optamos por também utilizar a linguagem Python para construir a API, utilizando a biblioteca Flask para o recebimento de requisições de inferência, que por sua vez são realizadas com o auxílio do próprio PyTorch. A ferramenta MongoDB é utilizada para o banco de dados de outros setores do projeto. Sendo assim, tendo em mente potenciais futuros planos de integração das aplicações, optamos por também utilizá-la para a nossa API.

&nbsp;&nbsp;&nbsp;&nbsp;Houve a necessidade de pesquisar sobre as ferramentas visto que nenhum dos membros da equipe tiveram contato prévio com elas.

##  Construção da API
&nbsp;&nbsp;&nbsp;&nbsp;Foi necessário compreender o funcionamento do código do modelo para que pudéssemos produzir uma inferência sobre os resultados obtidos, no entanto isso se mostrou um desafio muito maior do que esperado, devido à nossa falta de experiência trabalhando com modelos e a complexidade ímpar do código diversas dúvidas sobre as configurações que deveriam ser usadas e como utilizar algumas funções do PyTorch foram surgindo.

&nbsp;&nbsp;&nbsp;&nbsp;Após algumas semanas de desenvolvimento, conseguimos encapsular o modelo para que ele recebesse o áudio e realizasse as devidas predições. As primeiras inferências foram feitas com um modelo rudimentar treinado por nós mesmos. Logo após, um dos desenvolvedores do modelo, Edresson Casanova, nos forneceu um arquivo com as configurações da versão mais recente do modelo, esse que utilizamos de fato para realizar as inferências definitivas com o encapsulamento que havíamos criado.

&nbsp;&nbsp;&nbsp;&nbsp;Mesmo com o novo arquivo de configuração, os testes de inferência realizados eram em sua grande maioria inconclusivos, o que era um indicativo de que haviam partes do procedimento de inferência que precisavam ser corrigidas. Com o auxílio de um dos pesquisadores do modelo, Daniel Peixoto, encontramos os seguintes erros na primeira versão do encapsulamento:

- Strict = false: Ignora camadas que não são iguais ao modelo que estamos utilizando para classificar a entrada, levando o Pytorch à ignorar qualquer erro que acontecesse.

- Test = false: No teste era inserido um ruido diferente sobre o áudio, então é preciso que ele seja true para que o ruido adequado fosse implementado.


&nbsp;&nbsp;&nbsp;&nbsp;Após a correção dos erros encontrados, observamos que as inferências se tornaram condizentes com os resultados esperados.

 &nbsp;&nbsp;&nbsp;&nbsp;Uma vez que o encapsulamento do modelo foi corrigido, utilizamos a biblioteca Flask para construir uma API funcional que recebe o arquivo de áudio em formato ".wav" a ser analisado e retorna como resposta uma análise dizendo se o usuário possui ou não insuficiência respiratória.

&nbsp;&nbsp;&nbsp;&nbsp;

## Futuros Passos
---

- Dockerizar a aplicação
- Deploy da aplicação no Heroku
- Implementação do armazenamento de resultados no banco de dados
- Ajustes na inferência do modelo - Feito