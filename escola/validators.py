from validate_docbr import CPF


def cpf_valido(numero_do_cpf: str):
    cpf = CPF()
    return cpf.validate(numero_do_cpf)

def nome_valido(nome: str):
    nome = nome.replace(' ', '')
    return nome.isalpha()

def celular_valido(celular: str):
    return len(celular) == 15