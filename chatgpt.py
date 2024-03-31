class Cliente:
    def __init__(self, historico_credito, renda_mensal):
        self.historico_credito = historico_credito
        self.renda_mensal = renda_mensal


class SistemaBaseadoEmConhecimento:
    def __init__(self):
        self.regras = [
            {"historico_credito": "ruim", "risco": "alto"},
            {"historico_credito": "medio", "renda_mensal": "baixa", "risco": "moderado"},
            {"historico_credito": "bom", "renda_mensal": "alta", "risco": "baixo"}
        ]


    def decidir_risco_emprestimo(self, cliente):
        for regra in self.regras:
            if all(getattr(cliente, chave, None) == valor for chave, valor in regra.items() if chave != "risco"):
                return regra["risco"]


        # Se nenhuma regra corresponder, o risco é desconhecido
        return "desconhecido"


    def justificar_decisao(self, cliente):
        risco = self.decidir_risco_emprestimo(cliente)
        if risco == "alto":
            return "Cliente possui histórico de crédito ruim."
        elif risco == "moderado":
            return "Cliente possui histórico de crédito médio e renda mensal baixa."
        elif risco == "baixo":
            return "Cliente possui histórico de crédito bom e renda mensal alta."
        else:
            return "Não é possível determinar o risco de empréstimo para este cliente."


# Exemplo de uso
sistema = SistemaBaseadoEmConhecimento()
cliente1 = Cliente("ruim", 2000)
cliente2 = Cliente("bom", 5000)
cliente3 = Cliente("medio", "baixa")


print(sistema.justificar_decisao(cliente1))  # Saída: Cliente possui histórico de crédito ruim.
print(sistema.justificar_decisao(cliente2))  # Saída: Cliente possui histórico de crédito bom e renda mensal alta.
print(sistema.justificar_decisao(cliente3))  # Saída: Cliente possui histórico de crédito médio e renda mensal baixa.


