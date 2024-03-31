def avaliar_risco(historico_credito, renda_mensal, dividas, valor_emprestimo):
    # Verificar regras para risco alto
    if (
        historico_credito == "ruim"
        or renda_mensal < valor_emprestimo
        or dividas > 0.5 * renda_mensal
    ):
        nivel_risco = "Alto"
        justificativa = "O risco de crédito é considerado Alto devido a:\n"
        if historico_credito == "ruim":
            justificativa += "- Histórico de crédito ruim\n"
        if renda_mensal < valor_emprestimo:
            justificativa += "- Renda mensal menor que o valor do empréstimo solicitado\n"
        if dividas > 0.5 * renda_mensal:
            justificativa += "- Dívidas existentes maiores que 50% da renda mensal\n"


    # Verificar regras para risco moderado
    elif (
        historico_credito == "regular"
        and renda_mensal >= valor_emprestimo
        and dividas <= 0.5 * renda_mensal
    ):
        nivel_risco = "Moderado"
        justificativa = "O risco de crédito é considerado Moderado porque:\n"
        justificativa += "- Histórico de crédito regular\n"
        justificativa += "- Renda mensal igual ou superior ao valor do empréstimo solicitado\n"
        justificativa += "- Dívidas existentes menores ou iguais a 50% da renda mensal\n"


    # Caso contrário, risco baixo
    else:
        nivel_risco = "Baixo"
        justificativa = "O risco de crédito é considerado Baixo porque:\n"
        justificativa += "- Bom histórico de crédito\n"
        justificativa += "- Renda mensal pelo menos duas vezes o valor do empréstimo solicitado\n"
        justificativa += "- Dívidas existentes menores ou iguais a 30% da renda mensal\n"


    return nivel_risco, justificativa


# Exemplo de uso
historico_credito = "bom"
renda_mensal = 5000
dividas = 1000
valor_emprestimo = 2000


nivel_risco, justificativa = avaliar_risco(historico_credito, renda_mensal, dividas, valor_emprestimo)
print(f"Nível de risco: {nivel_risco}")
print(justificativa)
