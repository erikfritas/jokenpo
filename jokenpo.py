from random import randint as ri
from sys import argv

MSG = {
    "vence": "Você venceu parabéns!",
    "empata": "Empate ;-;",
    "perda": "Você perdeu, ;_; que pena"
}

JOKENPO = {
    "pedra": { "vence": "tesoura" },
    "papel": { "vence": "pedra" },
    "tesoura": { "vence": "papel" }
}

GAME_KEYS = list(JOKENPO.keys())

class Jokenpo:
    def __init__(self):
        '''
        Declaração das variáveis
        '''
        self.num = 0
        self.pc = GAME_KEYS[ri(0, 2)]

    def setNum(self):
        '''
        Setando um valor à variável num
        '''
        try:
            n = int(argv[1])
        except:
            n = argv[1]
        if type(n) is int and GAME_KEYS[n] in GAME_KEYS:
            self.num = [GAME_KEYS[n], JOKENPO[GAME_KEYS[n]]]
        else:
            raise Exception("<\ERROR/> Opção inválida!")

    def start(self):
        '''
        Executando o game
        '''
        self.setNum()
        num = self.num[0]
        vence = self.num[1]["vence"]
        
        res = MSG["vence"]
        if num == self.pc:
            res = MSG["empata"]
        elif self.pc != vence:
            res = MSG["perda"]

        print(f"Você: {num}\nPC: {self.pc}\n\nResultado: {res}")


if __name__ == "__main__":
    Jokenpo().start()
