class controle_remoto:
    def __init__(self,cor,altura,profundidade,largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

controle1 = controle_remoto("preto","10",'2','2')
controle2 = controle_remoto("azul","15",'3','1')

print(controle1.cor)

