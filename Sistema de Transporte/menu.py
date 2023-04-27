def menu_Start():
  print("""
    1 -- Gerenciamento de Motoristas
    2 -- Gerenciamento de Veículos
    3 -- Gerenciamento de Viagens
    4 -- Registrar Abastecimento
    5 -- Registrar Manutenção
    6 -- Relatório

    0 -- SAIR
    """)
 

def menu_Motorista():
  print("""
    a -- Cadastrar Novo Motorista
    b -- Pesquisar Motorista
    c -- Editar Motorista
    d -- Deletar Motorista

    s -- Sair/Voltar
    """)


def menu_Viagem():
  print("""
    a -- Cadastrar Viagem
    b -- Editar Viagem

    s -- Sair/Voltar
    """)


def menu_EditarViagem():
  print("""
    a -- Editar Destino
    b -- Editar Origem
    c -- Editar Distancia
    d -- Editar Motorista
    e -- Editar Veiculo

    s -- Sair/Voltar
    """)


def menu_EditarVeiculo():
  print("""
    a -- Editar Marca
    b -- Editar Ano
    c -- Editar Placa
    d -- Editar Chassi
    e -- Editar Cor
    f -- Editar Quilometragem

    s -- Sair/Voltar
    """)


def menu_EditarMotorista():
  print("""
    a -- Editar Nome
    b -- Editar Cpf
    c -- Editar RG
    d -- Editar CNH

    s -- Sair/Voltar
    """)


def menu_Veiculos():
  print("""
    a -- Cadastrar Veiculos
    b -- Gerenciar Veiculos

    s -- Sair/Voltar
    """)


def menu_GerenciarVeiculos():
  print("""
    a -- Mostrar informações do Veiculo
    b -- Editar Veiculo
    c -- Deletar Veiculo
    d -- Ver Quilometragem do Veículo

    s -- Sair/Voltar
    """)
