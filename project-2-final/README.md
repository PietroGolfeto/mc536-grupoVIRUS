## Motivação e contexto
A segunda versão do projeto traz uma análise que une o poder de bancos de dados relacionais aos baseados em grafos. Por meio dessa conexão e do uso de fontes com diferentes enfoques, tornamos possível uma investigação da complexidade camuflada no cotidiano alimentar. Para nos aprofundarmos nesse trabalho, arquitetamos uma rede de questionamentos que dialogam entre si, construindo passo a passo um painel que explora desde a identificação de relações não triviais entre alimentos até os efeitos que diferentes nichos de consumo posssuem sobre as pessoas. 

## Slides

### Apresentação Prévia
> Coloque aqui o link para o PDF da apresentação prévia

### Apresentação Final
> Coloque aqui o link para o PDF da apresentação final

## Modelo Conceitual

![ER Taxi](images/diagrama_er.png)

## Modelos Lógicos

~~~
Recipe(_Food_Code_, Food_Desc)

Crop_Group(_CGN_, Crop_Group_Description, Is_Vegan)

Ingredient(_FCID_Code_, _Crop_Group_, FCID_Desc, Popularity)
  Crop_Group: chave estrangeira -> Crop_Group

Recipe_Composition(_Food_Code_, _FCID_Code_, Ingredient_Order)
  Food_Code: chave estrangeira -> Recipe
  FCID_Code: chave estrangeira -> Ingredient

Nutrient_Values(_Food_Code_, Main food description, Energy (kcal), Carbohydrate (g), Protein (g), Sugars total (g), Total Fat (g), Cholesterol (mg), Fiber total dietary (g), Vitamin A RAE (mcg_RAE), Vitamin B-6 (mg), Vitamin C (mg), Calcium (mg), Iron (mg), Potassium (mg), Sodium (mg), Caffeine (mg), Alcohol (g))
  Food_Code: chave estrangeira -> Recipe

Recommended_Values(Nutrient, Reference Daily Intake)
~~~

![Modelo Lógico de Grafos](images/diagrama_grafos.png)
## Base de dados

título da base | link | breve descrição
----- | ----- | ----- 
FCID | [Food Commodity Intake Database](https://fcid.foodrisk.org/) | 
FNDDS | [FNDDS Databases](https://www.ars.usda.gov/northeast-area/beltsville-md-bhnrc/beltsville-human-nutrition-research-center/food-surveys-research-group/docs/fndds-download-databases/) |

## Detalhamento do Projeto
> Apresente aqui detalhes do processo de construção do dataset e análise. Nesta seção ou na seção de Perguntas podem aparecer destaques de código como indicado a seguir. Note que foi usada uma técnica de highlight de código, que envolve colocar o nome da linguagem na abertura de um trecho com `~~~`, tal como `~~~python`.
> Os destaques de código devem ser trechos pequenos de poucas linhas, que estejam diretamente ligados a alguma explicação. Não utilize trechos extensos de código. Se algum código funcionar online (tal como um Jupyter Notebook), aqui pode haver links. No caso do Jupyter, preferencialmente para o Binder abrindo diretamente o notebook em questão.
> Aqui devem ser apresentadas as operações de construção do dataset:
> * extração de dados de fontes não estruturadas como, por exemplo, páginas Web
> * agregação de dados fragmentados obtidos a partir de API
> * integração de dados de múltiplas fontes
> * tratamento de dados
> * transformação de dados para facilitar análise e pesquisa

## Evolução do projeto
A primeira grande dificuldade encontrada pelo grupo de trabalho foi encontrar bases que tivessem algum tipo de conexão, seja por meio de um ID comum ou por usar a mesma nomenclatura ao se referir aos alimentos. Como encontrar bancos de dado com essas caractérisitcas estava se mostrando muito difícil, começamos a considerar um pré-processamento dos dados armazenados nos arquivos csv. No caso de nomes comuns entre diferentes comidas, encontramos por exemplo um banco que tinha os nomes no plural e outros no singular. A primeira solução foi simplesmente exlcuir o "s" do final de todos os registros. Mas e quanto aos que naturalmente terminam em s? Isso poderia inutilizar grande parte dos dados e não garantiria uma comunicação confiável. Pensamos então em criar um algoritmo que verificasse similaridades entre strings e a partir de uma certa porcentagem de semelhança decidisse que se tratava da mesma comida. Mas e quanto a nomes curtos? A diferença entre "eggs" e "egg" é de apenas uma letra, mas apresenta uma porcentagem muito maior que "eggplant" e "eggplants".  A gota d'água foi quando descobrimos que um deles se referia a porco como pork e o outro como pig... 

Conclusão: fazer esse tipo de ligação seria uma solução deselegante e forçada para o nosso problema, pois seria extremamente restrita não apenas aos bancos de dados que estávamos utilizando naquele contexto como também comprometeria a escalabilidade do código. Se registros novos chegassem, o funcionamento de nossas aplicações estaria fragilizado, pois foi pensado apenas para aquele momento específico do banco

## Perguntas de Pesquisa/Análise Combinadas e Respectivas Análises
### Perguntas/Análise com Resposta Implementada - SQL
#### [Notebook com resoluções](notebooks/notebook.ipynb)

#### Pergunta/Análise 1

 * Analisar o quão "diet" é uma receita baseado no percentual diario de determinados indicadores nutricionais (gordutas totais/trans, sodio, açucar). Quais as receitas mais diet baseadas nesse critério? E quais possuem maior teor de açúcar, gordura e sódio?

   
   >* Explicação sucinta da análise que será feita e conjunto de queries que responde à pergunta.

#### Pergunta/Análise 2
 * Analisar o quão balanceada é uma receita com base na quantidade de nutrientes para os quais essa receita possui valores dentro da taxa recomendada. Quais as receitas mais balanceadas de acordo com esse critério?
   
   >* Explicação sucinta da análise que será feita e conjunto de queries queresponde à pergunta.

### Perguntas/Análise com Resposta Implementada - Grafos

#### Pergunta/Análise 1
 * Que receitas possuem o maior número relativo de ingredientes compartilhados? Vamos analisar comunidades das receitas e seus nutrientes predominantes para caracterizar elas (grupo dos carbs, proteína etc.).
   
   >* Explicação sucinta da análise que será feita e conjunto de queries que responde à pergunta.

#### Pergunta/Análise 2
 * Quais os crop groups mais centrais, com base no número de receitas?
   
   >* Explicação sucinta da análise que será feita e conjunto de queries que responde à pergunta.
