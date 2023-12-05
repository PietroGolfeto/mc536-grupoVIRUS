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

   
   * Primeiro, foi criada uma view estendendo a tabela receitas, adicionando uma nota para essa receita. Essa nota é calculada pela média dos três níveis (nível de gordura, sódio e açúcar), por meio da fórmula:
   **Nivel = (Quantidade do nutriente presente em 100 g da receita)/(Valor recomendado para 100g)**

   ~~~
   CREATE VIEW Receitas_Diet AS
               SELECT R.Food_Code, R.Food_Desc, 
               N.Total_Fat/6 AS Nivel_Gordura, N.Sugars_total/15 AS Nivel_Acucar, N.Sodium/600 AS Nivel_Sodio, (N.Total_Fat/6 + N.Sugars_total/15 + N.Sodium/600)/3 AS Nota
               FROM FCID_Food_Code_Description R, FNDDS_Nutrient_Values N
               WHERE R.Food_Code = N.Food_code AND N.Sugars_total/15 > 0.05 AND N.Sodium/600 > 0.05 AND N.Total_Fat/6 > 0.05 AND N.Caffeine = 0 AND N.Alcohol = 0        
               
   ~~~
   Foram desconsideradas receitas contendo cafeína e álcool, bem como as com valores muito insignificantes dos nutrientes usados para essa análise.
   Para calcular a nota, foi tirada uma média entre os indicadores dos três nutrientes, sendo as receitas *diet* aquelas com as menores notas.

   ~~~
   SELECT * FROM Receitas_Diet ORDER BY Nota LIMIT 10;

   SELECT Food_Code, Food_Desc, Nivel_Gordura FROM Receitas_Diet ORDER BY Nivel_Gordura DESC LIMIT 10;

   SELECT Food_Code, Food_Desc, Nivel_Acucar FROM Receitas_Diet ORDER BY Nivel_Acucar DESC LIMIT 10;

   SELECT Food_Code, Food_Desc, Nivel_Sodio FROM Receitas_Diet ORDER BY Nivel_Sodio DESC LIMIT 10;
   ~~~
   Os resultados ordenados podem ser observados nas tabelas processadas:
     * [Receitas *diet* ](../data/processed/Pergunta1SQL_Receitas_Diet_Top10.csv)
     * [Receitas com alta gordura](../data/processed/Pergunta1SQL_Receitas_Gordurosas_Top10.csv)
     * [Receitas com alto teor de açúcar](../data/processed/Pergunta1SQL_Receitas_Alto_Acucar_Top10.csv)
     * [Receitas com alto teor de sódio](../data/processed/Pergunta1SQL_Receitas_Alto_Sodio_Top10.csv)

#### Pergunta/Análise 2
 * Analisar o quão balanceada é uma receita com base na quantidade de nutrientes para os quais essa receita possui valores dentro da taxa recomendada, considerando todos os nutrientes do banco (proteínas, carboidratos, vitaminas, etc). Quais as receitas mais balanceadas de acordo com esse critério?
   
   * Foi criada uma view estendendo as receitas, contendo uma coluna para cada um dos nutrientes. Essas colunas possuem valores booleanos (1 caso a receita possua uma quantidade considerada aceitável para aquele nutriente, i.e., entre 5% e 15% do valor diário, e 0 do contrário). Em outras palavras, atribuimos 1 se 
   **(quantidade do nutriente) < 0.15 * (valor diário) AND (quantidade do nutriente)  > 0.05 * (valor diário)**.
   Obs.: a query pra essa view era muito grande então não foi inclusa aqui, mas está presente no notebook.

   Em seguida, criamos outra view contendo agora um atributo nota, dado pela soma das colunas individuais de cada ingrediente. Essa nota define o quão balanceada cada receita é.
   ~~~
   CREATE VIEW Receitas_Balanceadas AS
               SELECT R.Food_Code, R.Food_Desc, RG.Energy_level + RG.Protein_level + RG.Carbohydrate_level + RG.Sugars_total_level + RG.Fiber_total_dietary_level + RG.Total_Fat_level + RG.Cholesterol_level + RG.Vitamin_A_RAE_level + RG.Vitamin_B6_level + RG.Vitamin_C_level + RG.Calcium_level + RG.Iron_level + RG.Potassium_level + RG.Sodium_level AS Nota
               FROM FCID_Food_Code_Description R, FNDDS_Nutrient_Values N, Receitas_Grau RG
               WHERE R.Food_Code = N.Food_code AND R.Food_Code = RG.Food_Code;

   SELECT * FROM Receitas_Balanceadas ORDER BY Nota DESC LIMIT 10;
   ~~~
   Os resultados podem ser observados em:
     * [Receitas mais balanceadas](../data/processed/Pergunta2SQL_Receitas_Balanceadas_Top10.csv)


### Perguntas/Análise com Resposta Implementada - Grafos

#### Pergunta/Análise 1
 * Que receitas possuem o maior número relativo de ingredientes compartilhados? Vamos analisar comunidades das receitas e seus nutrientes predominantes para caracterizar elas (grupo dos carbs, proteína etc.).
   
   >* Explicação sucinta da análise que será feita e conjunto de queries que responde à pergunta.

#### Pergunta/Análise 2
 * Quais os crop groups mais centrais, com base no número de receitas?
   
   * Foi necessário criar um atributo "Centrality" nos nós que representam os Crop Groups. Assim, sempre que encontrarmos uma Receita que possui um ingrediente de um determinado Crop Group, esse atributo é incrementado. Em seguida, podemos selecionar apenas os nós de Crop Group com uma "Centrality" alta. No exemplo, estão apenas os nós onde a centralidade é maior que 1000.
   ~~~
    MATCH(g:Crop_Group)
    SET g.Centrality = 0

    MATCH(r:Recipe)-[:Recipe_Of_Ingredient]->(i:Ingredient)-[:Food_Group]->(g:Crop_Group)
    MERGE(r)-[x:Has_Group]->(g)
    ON CREATE SET g.Centrality=g.Centrality+1
    ON MATCH SET g.Centrality=g.Centrality+1

    MATCH(g:Crop_Group)
    WHERE g.Centrality>1000
    RETURN g
   ~~~
   Abaixo, estão fotos dos Crop Groups e suas centralidades:
   ![Crop Groups mais centrais](images/cropgroup.png)
   ![Centralidades](images/centralidades.png)

