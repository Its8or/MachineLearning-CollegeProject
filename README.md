# MachineLearning-CollegeProject

###### Proposta: _Utilizar 50 frases como treinamento inicial e fazer com que o código determine se é uma frase positiva, negativa ou neutra._

## O método: Abordagem Baseada em Dicionário
### Pré-Processamento:
Utilizando  **_Python_**:
1. Remover conectores: a(s), o(s), de, da(s), etc.
2. Separar frase em palavras(tokens), atribuir valor a cada categoria:
    * Positiva: +1 
    * Negativa: -1 
    * Neutra:    0  
        * Definir dicionário de palavras para as três categorias
    
                EXEMPLO:
                positivo (pos_words):
                excelente, feliz, adorei, maravilhoso, radiante, superou, parabéns, etc.

4. Calcular a Pontuação(Score) da Frase:
$$Score = \sum_{i=1}^{n} Peso(token_i)$$
* Se $Score > 0$: Positivo. 
* Se $Score < 0$: Negativo.
* Se $Score = 0$: Neutro.

--- 
### Execução do código
