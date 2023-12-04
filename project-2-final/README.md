## Motivação e contexto
A segunda versão do projeto traz uma análise que une o poder de bancos de dados relacionais aos baseados em grafos. Por meio dessa conexão e do uso de fontes com diferentes enfoques, tornamos possível uma investigação da complexidade camuflada no cotidiano alimentar. Para nos aprofundarmos nesse trabalho, arquitetamos uma rede de questionamentos que dialogam entre si, construindo passo a passo um painel que explora desde a identificação de relações não triviais entre alimentos até os efeitos que diferentes nichos de consumo posssuem sobre as pessoas. 

## Método

## Base de dados

título da base | link | breve descrição
----- | ----- | ----- 
FCID |  | 
FNDDS

## Evolução do projeto
A primeira grande dificuldade encontrada pelo grupo de trabalho foi encontrar bases que tivessem algum tipo de conexão, seja por meio de um ID comum ou por usar a mesma nomenclatura ao se referir aos alimentos. Como encontrar bancos de dado com essas caractérisitcas estava se mostrando muito difícil, começamos a considerar um pré-processamento dos dados armazenados nos arquivos csv. No caso de nomes comuns entre diferentes comidas, encontramos por exemplo um banco que tinha os nomes no plural e outros no singular. A primeira solução foi simplesmente exlcuir o "s" do final de todos os registros. Mas e quanto aos que naturalmente terminam em s? Isso poderia inutilizar grande parte dos dados e não garantiria uma comunicação confiável. Pensamos então em criar um algoritmo que verificasse similaridades entre strings e a partir de uma certa porcentagem de semelhança decidisse que se tratava da mesma comida. Mas e quanto a nomes curtos? A diferença entre "eggs" e "egg" é de apenas uma letra, mas apresenta uma porcentagem muito maior que "eggplant" e "eggplants".  A gota d'água foi quando descobrimos que um deles se referia a porco como pork e o outro como pig... 
Conclusão: fazer esse tipo de ligação seria uma solução deselegante e forçada para o nosso problema, pois seria extremamente restrita não apenas aos bancos de dados que estávamos utilizando naquele contexto como também comprometeria a escalabilidade do código. Se registros novos chegassem, o funcionamento de nossas aplicações estaria fragilizado, pois foi pensado apenas para aquele momento específico do banco


