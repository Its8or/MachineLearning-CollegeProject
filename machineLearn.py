import re
# "RE" tem funcoes proprias para reconhecimento de padroes.

data = [
    ("O atendimento na loja foi simplesmente excelente.", "Positivo"),
    ("O produto chegou quebrado e a caixa estava amassada.", "Negativo"),
    ("A cor da parede é um tom de bege claro.", "Neutro"),
    ("Estou muito feliz com os resultados do meu projeto.", "Positivo"),
    ("O filme é extremamente entediante e sem sentido.", "Negativo"),
    ("A reunião está marcada para as dez horas da manhã.", "Neutro"),
    ("Adorei a comida, o tempero estava no ponto certo.", "Positivo"),
    ("O serviço de internet caiu três vezes hoje.", "Negativo"),
    ("O carro atravessou a rua e virou à esquerda.", "Neutro"),
    ("Que dia maravilhoso para um passeio no parque!", "Positivo"),
    ("Nunca mais volto nesse restaurante, fui mal tratado.", "Negativo"),
    ("O livro possui duzentas páginas de conteúdo técnico.", "Neutro"),
    ("Ganhei um bônus inesperado e estou radiante.", "Positivo"),
    ("O preço deste computador é abusivo e injusto.", "Negativo"),
    ("A temperatura hoje deve ficar em torno de 25 graus.", "Neutro"),
    ("A viagem superou todas as minhas expectativas.", "Positivo"),
    ("Sinto um vazio enorme e muita tristeza hoje.", "Negativo"),
    ("O portão da garagem é feito de alumínio.", "Neutro"),
    ("Parabéns pelo sucesso, você merece tudo de bom!", "Positivo"),
    ("O trânsito está horrível e vou me atrasar muito.", "Negativo"),
    ("O relatório contém os dados do último trimestre.", "Neutro"),
    ("Este café é o melhor que já provei na vida.", "Positivo"),
    ("A bateria do celular não dura nem duas horas.", "Negativo"),
    ("O evento acontecerá no auditório principal do prédio.", "Neutro"),
    ("É incrível como a tecnologia facilita nossa rotina.", "Positivo"),
    ("Fiquei decepcionado com a falta de suporte técnico.", "Negativo"),
    ("As chaves estão penduradas no gancho atrás da porta.", "Neutro"),
    ("O design da nova interface ficou elegante e intuitivo.", "Positivo"),
    ("O barulho da obra ao lado é insuportável e irritante.", "Negativo"),
    ("O vôo tem uma escala prevista em Brasília.", "Neutro"),
    ("Agradeço imensamente pela ajuda e pelo carinho.", "Positivo"),
    ("O hotel era sujo e o café da manhã estava frio.", "Negativo"),
    ("O documento precisa ser assinado e digitalizado.", "Neutro"),
    ("Sinto-me renovado após essa pausa relaxante.", "Positivo"),
    ("Perdi todos os meus arquivos por causa de um vírus.", "Negativo"),
    ("A mesa da cozinha é de madeira escura.", "Neutro"),
    ("Que notícia fantástica, estou muito empolgado!", "Positivo"),
    ("O atendimento telefônico é lento e ineficiente.", "Negativo"),
    ("O ônibus passa nesta parada a cada vinte minutos.", "Neutro"),
    ("A paisagem do topo da montanha é deslumbrante.", "Positivo"),
    ("Infelizmente, o plano de saúde negou o exame.", "Negativo"),
    ("A lâmpada da sala queimou ontem à noite.", "Neutro"),
    ("É um prazer imenso conhecer alguém tão gentil.", "Positivo"),
    ("O site está cheio de erros e links quebrados.", "Negativo"),
    ("O mercado fecha às dez horas nos fins de semana.", "Neutro"),
    ("O show foi vibrante e a energia estava lá em cima.", "Positivo"),
    ("Detestei o final da série, foi uma perda de tempo.", "Negativo"),
    ("O carregador está conectado na tomada do quarto.", "Neutro"),
    ("Desejo a você um ano repleto de alegria e paz.", "Positivo"),
    ("O clima na cidade é seco durante o inverno.", "Neutro")
]

peso = {
    # --- CATEGORIA POSITIVA ---
    "excelente": 1, "feliz": 1, "adorei": 1, "maravilhoso": 1, "radiante": 1, 
    "superou": 1, "parabéns": 1, "melhor": 1, "incrível": 1, "elegante": 1, 
    "intuitivo": 1, "agradeço": 1, "imensamente": 1, "carinho": 1, "renovado": 1, 
    "relaxante": 1, "fantástica": 1, "empolgado": 1, "deslumbrante": 1, "prazer": 1, 
    "gentil": 1, "vibrante": 1, "alegria": 1, "paz": 1, "sucesso": 1, "bom": 1, "ótimo": 1,

    # --- CATEGORIA NEGATIVA ---
    "quebrado": -1, "amassada": -1, "entediante": -1, "ruim": -1, "péssimo": -1, 
    "horrível": -1, "atrasar": -1, "vazio": -1, "tristeza": -1, "injusto": -1, 
    "abusivo": -1, "decepcionado": -1, "falta": -1, "insuportável": -1, "irritante": -1, 
    "sujo": -1, "frio": -1, "perdi": -1, "vírus": -1, "lento": -1, "ineficiente": -1, 
    "infelizmente": -1, "negou": -1, "erros": -1, "detestei": -1, "perda": -1, "caiu": -1,

    # --- CATEGORIA NEUTRA ---
    "tom": 0, "bege": 0, "reunião": 0, "marcada": 0, "dez": 0, "manhã": 0, 
    "carro": 0, "atravessou": 0, "esquerda": 0, "livro": 0, "páginas": 0, 
    "técnico": 0, "temperatura": 0, "graus": 0, "alumínio": 0, "relatório": 0, 
    "dados": 0, "trimestre": 0, "auditório": 0, "prédio": 0, "chaves": 0, 
    "porta": 0, "escala": 0, "documento": 0, "assinado": 0, "madeira": 0, 
    "ônibus": 0, "parada": 0, "lâmpada": 0, "mercado": 0, "tomada": 0, "seco": 0, "inverno": 0
}

conectivos = [
    "a", "agora", "algum", "alguma", "aquele", "aqueles", "ao", "aos", "as", "através", 
    "com", "como", "da", "das", "de", "dela", "delas", "dele", "deles", "depois", "do", 
    "dos", "dum", "duma", "e", "em", "entre", "era", "eram", "é", "essa", "essas", 
    "esse", "esses", "esta", "estamos", "estas", "estava", "estavam", "este", "esteja", 
    "estejam", "estejamos", "estes", "esteve", "estive", "estivemos", "estiver", 
    "estivera", "estiveram", "estiverem", "estivermos", "estivesse", "estivessem", 
    "estivéramos", "estivéssemos", "estou", "eu", "foi", "fomos", "for", "fora", 
    "foram", "forem", "formos", "fosse", "fossem", "fôramos", "fôssemos", "fui", 
    "há", "haja", "hajam", "hajamos", "hão", "haver", "haverá", "haverão", "haveria", 
    "haveriam", "haveríamos", "havia", "haviam", "havíamos", "houve", "houvemos", 
    "houvera", "houveram", "houvéramos", "isso", "isto", "já", "lhe", "lhes", "mais", 
    "mas", "me", "mesmo", "meu", "meus", "minha", "minhas", "muito", "na", "nas", 
    "não", "nem", "no", "nos", "nossa", "nossas", "nosso", "nossos", "num", "numa", 
    "o", "os", "ou", "outra", "outras", "outro", "outros", "para", "pela", "pelas", 
    "pelo", "pelos", "pela", "pois", "por", "qual", "quando", "que", "quem", "são", 
    "se", "seja", "sejam", "sejamos", "sem", "ser", "será", "serão", "seria", "seriam", 
    "seríamos", "seu", "seus", "só", "somos", "sou", "sua", "suas", "também", "te", 
    "tem", "temos", "tenha", "tenham", "tenhamos", "tenho", "terá", "terão", "teria", 
    "teriam", "teríamos", "teu", "teus", "teve", "tinha", "tinham", "tínhamos", "tive", 
    "tivemos", "tivera", "tiveram", "tivéramos", "tivesse", "tivessem", "tivéssemos", 
    "toda", "todas", "todo", "todos", "tu", "tua", "tuas", "um", "uma", "você", "vocês", "vos"
]

def classifyPhrase(texto):
    # todo: código para predição de resposta
    pass

print("Hello World!")