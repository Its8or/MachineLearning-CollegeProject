import re
import json
# "RE" tem funcoes proprias para reconhecimento de padroes.

# jv: importando ojson
with open("database.json", "r", encoding="utf-8") as f:
    data_json = json.load(f)

frases = data_json["frases"]
pesos = data_json["pesos"]
conectivos = data_json["conectivos"]

def classifyPhrase(texto):
    # todo: código para predição de resposta
    texto_limpo = re.sub(r'[^\w\s]', '', texto.lower())
    
    tokens = texto_limpo.split()

    score_final = 0
    palavras_relevantes = []

    negacao_ativa = False
    i = 0

    #jv: logica pra negacao
    while i < len(tokens):
        palavra = tokens[i]

        if palavra == "não":
            negacao_ativa = True
            i += 1
            continue

        if palavra not in conectivos:
            peso = pesos.get(palavra, 0)

            if peso != 0:
                if negacao_ativa:
                    peso = -peso
                    negacao_ativa = False

                score_final += peso
                palavras_relevantes.append(f"{palavra}({peso})")

        i += 1
    
    # logica para score_final 
    if score_final > 0:
        sentimento = "Positivo"
    elif score_final < 0:
        sentimento = "Negativo"
    else:
        sentimento = "Neutro"
    
    return sentimento, score_final, palavras_relevantes

print(f"{'FRASE':<50} | {'PREDIÇÃO':<10} | {'SCORE':<5}")
print("-" * 75)

# jv: mudando o loop pra usar o json
for item in frases:
    frase = item["texto"]
    rotulo_real = item["sentimento"]

    predicao, score, detalhes = classifyPhrase(frase)
    print(f"{frase[:53]:<55} | {predicao:<10} | {score:<5}")
    #jv: se quiser deixar mais separado tem isso:
    #print("-" * 78)