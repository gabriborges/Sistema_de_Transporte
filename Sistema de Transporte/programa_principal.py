from classes import Veiculo, Motorista, Empresa, Viagem, Manutencao, Abastecimento
import menu as menu

#   EDICAO "MOTORISTA"
def editar_motorista(empresa: Empresa) -> None:
    cpf = input("\nInforme o CPF: ")
    motorista = empresa.pesquisar_FuncionariosEditar(cpf)

    if isinstance(motorista, Motorista):
        while True:
            menu.menu_EditarMotorista()
            opcao: str = input("\nDigite a opção desejada: ")

            print("\n------Editando Motorista------")

            if opcao.lower() == "s": #  SAIR
                break
            elif opcao.lower() == "a":  #   NOME
                motorista.nome = input("\nInserir novo NOME:")
            elif opcao.lower() == "b": #    CPF
                motorista.cpf = input("\nInserir novo CPF: ")
            elif opcao.lower() == "c": #    RG
                motorista.rg = input("\nInserir novo RG: ")
            elif opcao.lower() == "d": #    CNH
                motorista.cnh = input("\nInserir novo CNH: ")
            else:
                print("\nERRO: OPÇAO INVÁLIDA!\n")
    else:
        print("\nERRO: FUNCIONÁRIO NÃO ENCONTRADO!")
       
def gerenciamento_Motorista(empresa: Empresa) -> None:
    while True:
        menu.menu_Motorista()
        opcao: str = input("\nDigite a opção: ")

        if opcao.lower() == "a": #  CADASTRAR
            print("------Cadastrando Motorista------")
            nome = str(input("Nome: "))
            cpf = int(input("CPF: "))
            rg = str(input("RG: "))
            cnh = str(input("CNH: "))

            motorista = Motorista(nome,cpf, rg, cnh)
            empresa.adicionar_Motorista(motorista)
            #break
        elif opcao.lower() == "b":  #   PESQUISAR/MOSTRAR MOTORISTA
            buscar_cpf = int(input("\nInforme o CPF: "))
            empresa.pesquisar_Funcionarios(buscar_cpf)
        
        elif opcao.lower() == "c":  #   EDITAR MOTORISTA
            editar_motorista(empresa)

        elif opcao.lower() == "d":  #   DELETAR MOTORISTA
            cpf = input("\nInforme o CPF: ")
            motorista = empresa.pesquisar_FuncionariosEditar(cpf)

            if isinstance(motorista, Motorista):
                empresa.remover_Motorista(motorista)
            else:
                print("\nERRO: MOTORISTA NÃO ENCONTRADO!\n")
        elif opcao.lower() == "s": #    SAIR
            break
        else:
            print("\nERRO: OPÇAO INVÁLIDA!\n")

#   EDICAO "VEICULO"
def editar_veiculo(empresa: Empresa) -> None:
    chassi = input("\nInforme o CHASSI: ")
    veiculo = empresa.pesquisar_VeiculosEditar(chassi)

    if isinstance (veiculo, Veiculo):
        while True:
            menu.menu_EditarVeiculo()
            opcao: str  = input("\nDigite a opção desejada: ")
            
            if opcao.lower() == "s": #  SAIR
                break

            elif opcao.lower() == "a": #    MARCA
                veiculo.marca = input("\nNova MARCA: ")
                print("\nMARCA alterada com sucesso!")

            elif opcao.lower() == "b":  #   ANO
                veiculo.ano(int(input("\nNovo ANO: ")))
                print("\nANO alterado com sucesso!")

            elif opcao.lower() == "c": #    PLACA
                veiculo.placa = input("\nNova PLACA: ")
                print("\nPLACA alterada com sucesso!")

            elif opcao.lower() == "d": #    CHASSI
                veiculo.chassi(input("\nNovo CHASSI: "))
                print("\nCHASSI alterado com sucesso!")

            elif opcao.lower() == "e":  #   COR
                veiculo.cor(input("\nNova COR: "))
                print("\nCOR alterada com sucesso!")

            elif opcao.lower() == "f": #    QUILOMETRAGEM
                veiculo.quilometragem(float(input("\nNova QUILOMETRAGEM: ")))
                print("\nQUILOMETRAGEM alterada com sucesso!")
            else:
                print("\nERRO: OPÇÃO INVÁLIDA!\n")

    else:
        print("\nERRDO: VEICULO NÃO ENCONTRADO!\n")

def gerenciamento_Veiculo(empresa: Empresa) -> None:
    while True:
        menu.menu_Veiculos()
        opcao: str = input("\nDigite a opção desejada: ")

        if opcao.lower() == "a": #  CADASTRO VEICULO
            print("\n------Cadastrando Veículo------")
            marca = input("\nInserir MARCA: ")
            modelo = input("Inserir MODELO: ")
            ano = int(input("Inserir ANO: "))
            placa = input("Inserir PLACA: ")
            chassi = input("Inserir CHASSI: ")
            cor = input("Inserir COR: ")
            quilometragem = float(input("Inserir QUILOMETRAGEM: "))

            veiculo = Veiculo(marca, modelo, ano, placa, chassi, cor, quilometragem)

            empresa.adicionar_Veiculo(veiculo)

        elif opcao.lower() == "b": #    MOSTRAR INFORMACOES VEICULO
            chassi = input("\nInforme o CHASSI: ")
            empresa.pesquisar_Veiculos(chassi)

        elif opcao.lower() == "c":  #   EDITAR VEICULO
            editar_veiculo(empresa)

        elif opcao.lower() == "d": #    REMOVER VEICULO
            chassi = input("\nInforme o CHASSI: ")
            veiculo = empresa.pesquisar_VeiculosEditar(chassi)

            if isinstance(veiculo, Veiculo):
                empresa.remover_Veiculo(veiculo)
            else:
                print("\nERRO: VEÍCULO NÃO ENCONTRADO!\n")

        elif opcao.lower() == "e": #    VER QUILOMETRAGEM
            chassi = input("\nInforme o CHASSI: ")
            veiculo = empresa.pesquisar_VeiculosEditar(chassi)

            if isinstance(veiculo, Veiculo):
                print(f"\nCHASSI: {veiculo.chassi}\tQUILOMETRAGEM: {veiculo.quilomentagem}")
            else:
                print("\nERRO: VEÍCULO NÃO ENCONTRADO!\n")
        elif opcao.lower() == "s":  #   SAIR
            break
        else:
            print("\nERRO: OPÇÃO INVÁLIDA!\n")

#   EDICAO "VIAGENS"
def editar_viagem(empresa: Empresa)-> None:
    codigo = int(input("\nInserir CODIGO da Viagem: "))
    viagem = empresa.pesquisar_Viagem(codigo)

    if isinstance(viagem,Viagem):
        while True:
            menu.menu_EditarViagem()
            opcao: str = input("\nDigite a opção desejada: ")

            if opcao.lower() == "s": #  SAIR
                break

            elif opcao.lower() == "a": #    DESTINO
                viagem.destino = input("\nNovo DESTINO: ")
                print("\nDESTINO atualizado com sucesso!\n")

            elif opcao.lower() == "b": #    ORIGEM
                viagem.origem = input("\nNovo ORIGEM: ")
                print("\nORIGEM atualizada com sucesso!\n")

            elif opcao.lower() == "c": #    DISTANCIA
                antiga_distancia = viagem.distancia    #   COPIA DIST. ORIGINAL

                nova_distancia = float(input("\nInforme a nova DISTANCIA: "))

                if nova_distancia > antiga_distancia:
                    aux_veiculo = viagem.veiculo.quilometragem + (nova_distancia - antiga_distancia)
                    viagem.veiculo.quilometragem = aux_veiculo
                    
                    aux_motorista = viagem.motorista.quilometragem + (nova_distancia - antiga_distancia)
                    viagem.motorista.quilometragem = aux_motorista

                elif nova_distancia < antiga_distancia:
                    aux_veiculo = viagem.veiculo.quilometragem - abs(nova_distancia - antiga_distancia)
                    viagem.veiculo.quilometragem = aux_veiculo
                    
                    aux_motorista = viagem.motorista.quilometragem - abs(nova_distancia - antiga_distancia)
                    viagem.motorista.quilometragem = aux_motorista
                else:
                    pass
                    #   PODE NÃO ESTAR FUNCINANDO
            elif opcao.lower() == "d": #    EDITAR MOTORISTA
                novo_motoristaCPF = input("\nInforme o CPF do novo Motorista: ")
                novo_motorista = empresa.pesquisar_FuncionariosEditar(novo_motoristaCPF)

                if isinstance(novo_motorista, Motorista):
                    # ATUALIZA QUILOMETRAGEM NO VEICULO VELHO
                    aux_motorista_antigo = viagem.motorista.quilometragem() - viagem.distancia

                    viagem.motorista.quilometragem(aux_motorista_antigo)
                    # ATUALIZA QUILOMETRAGEM NO VEICULO NOVO
                    aux_motorista_novo = viagem.distancia + novo_motorista.quilometragem()
                    novo_motorista.quilometragem(aux_motorista_novo)

                    viagem.motorista = novo_motorista
                else:
                    print("\nERRO: FUNCIONARIO NAO ENCONTRADO!\n")
                    #   PODE NÃO ESTAR FUNCIONANDO   
            elif opcao.lower() == "e": #    EDITAR VEICULO
                novo_veiculoCHASSI = input("\nInforme o CHASSI do novo Veiculo: ")
                novo_veiculo = empresa.pesquisar_VeiculosEditar(novo_veiculoCHASSI)

                if isinstance(novo_veiculo, Veiculo):
                    # ATUALIZA DISTANCIA NO VEICULO VELHO
                    aux_veiculo_antigo = viagem.veiculo.quilometragem() - viagem.distancia

                    viagem.veiculo.quilometragem(aux_veiculo_antigo)
                    # ATUALIZA DISTANCIA NO VEICULO NOVO
                    aux_veiculo_novo = viagem.distancia + novo_veiculo.quilometragem()
                    novo_veiculo.quilometragem(aux_veiculo_novo)

                    viagem.veiculo = novo_veiculo
                else:
                    print("\nERRO: VEICULO NAO ENCONTRADO!\n")
            else:
                print("\nERRO: OPCAO INVALIDA!")
    else:
        print("\nERRO: VIAGEM NAO ENCONTRADA!\n")

def gerenciamento_Viagens(empresa: Empresa) -> None:
    while True:
        menu.menu_Viagem()
        opcao = input("\nDigite a opção desejada: ")

        if opcao.lower() == "s": #  SAIR
            break
        elif opcao.lower() == "a": #    CADASTRO VIAGEM
            chassi = input("\nInforme o CHASSI do VEICULO: ")
            veiculo: object = empresa.pesquisar_VeiculosEditar(chassi)

            cpf = input("\nInforme o CPF do MOTORISTA: ")
            motorista: object = empresa.pesquisar_FuncionariosEditar(cpf)

            if (isinstance(veiculo, Veiculo)) and (isinstance(motorista, Motorista)):

                print("\n------Cadastrando Viagem------")
                codigo = int(input("\n CODIGO: "))
                origem = input("ORIGEM: ")
                destino = input("DESTINO: ")
                distancia = float(input("DISTANCIA: "))
                

                viagem = Viagem(codigo, destino, origem, distancia, motorista, veiculo)
                empresa.registrar_Viagem(viagem, veiculo, motorista)

                distancia_Aux = veiculo.quilometragem() + distancia
                veiculo.quilometragem(distancia_Aux)
                #veiculo.quilometagem += distancia
                motorista.quilometragem += distancia
                motorista.quant_viagens += 1
            else:
                print("\nERRO: VEICULO E/OU MOTORISTA NÃO ENCONTRADOS!\n")

        elif opcao.lower() == "b": # EDITAR VIAGEM
            editar_viagem(empresa)
        else:
            print("\nERRO: OPCAO INVALIDA!\n")

def  cadastrar_Manutencao(empresa: Empresa):
    chassi = input("\nInserir CHASSI do Veiculo: ")
    veiculo = empresa.pesquisar_VeiculosEditar(chassi)

    if isinstance(veiculo, Veiculo):
        empresa.registrar_Manutencao(veiculo)
    else:
        print("\nERRO: VEICULO NAO ENCONTRADO!\n")

def  cadastrar_Abastecimento(empresa: Empresa):
    chassi = input("\nInserir CHASSI do Veiculo: ")
    veiculo = empresa.pesquisar_VeiculosEditar(chassi)

    if isinstance(veiculo, Veiculo):
        empresa.registrar_Abastecimento(veiculo)
    else:
        print("\nERRO: VEICULO NAO ENCONTRADO!\n")


def gerar_relatorio(empresa: Empresa):
    print("\n---------------------RELATÓRIO---------------------")

    #Quantidade de Motorista
    def quantidade_motoristas():
        print(f'\nQuantidade de Motoristas: {len(empresa.funcionarios)}')

    #Quantidade de Veículos
    def quantidade_veiculos():
        print(f'\nQuantidade de Veículos: {len(empresa.frota)}')

    #Motorista que mais realizou viagens
    def motorista_mais_viagens():
        if len(empresa.registro_Viagens) == 0:
            print('\nMotorista(s) com maior quantidade de viagens: Nenhuma viagem foi realizada ainda.')
        else:
            viagens_maior = 0
            for motorista in empresa.funcionarios:
                if motorista.quant_viagens > viagens_maior:
                    viagens_maior = motorista.quant_viagens

            print('\nMotorista(s) com maior quantidade de viagens: ')
            for motorista in empresa.funcionarios:
                if motorista.quant_viagens == viagens_maior:
                    print(f'{motorista.nome}, cpf: {motorista.cpf}, qtd viagens: {motorista.quant_viagens}')

    #Motorista que mais km percorreu
    def motorista_maior_quilometragem():
        if len(empresa.funcionarios) == 0:
            print('\nMotorista(s) com maior quantidade de viagens: Não há motoristas cadastrados.')
        else:
            quilometragem_maior = 0
            for motorista in empresa.funcionarios:
                if motorista.quilometragem > quilometragem_maior:
                    quilometragem_maior = motorista.quilometragem

            print('\nMotorista(s) com maior quilometragem: ')
            for motorista in empresa.funcionarios:
                if motorista.quilometragem == quilometragem_maior:
                    print(f'{motorista.nome}, cpf: {motorista.cpf}, quilometragem: {motorista.quilometragem} km')

    #Veículo com maior km
    def veiculo_maior_quilometragem():
        if len(empresa.frota) == 0:
            print('\nMotorista(s) com maior quantidade de viagens: Não há veículos cadastrados.')
        else:
            quilometragem_maior = 0
            for veiculo in empresa.frota:
                if veiculo.quilometragem > quilometragem_maior:
                    quilometragem_maior = veiculo.quilometragem

            print('\nVeiculo(s) com maior quilometragem: ')
            for veiculo in empresa.frota:
                if veiculo.quilometragem == quilometragem_maior:
                    print(f'{veiculo.marca} {veiculo.modelo}, chassi: {veiculo.chassi}, quilometragem: {veiculo.quilometragem} km')

    #Total de despesas com abastecimento
    def despesas_abastecimento():
        print(f'\nTotal de despesas com abastecimento: {empresa.despesa_abastecimento}')

    #Total de despesas de Manutenção
    def despesas_manutencao():
        print(f'\nTotal de despesas com manutenção: {empresa.despesa_manutencao}')
    

    quantidade_motoristas()
    quantidade_veiculos()
    motorista_mais_viagens()
    motorista_maior_quilometragem()
    veiculo_maior_quilometragem()
    despesas_abastecimento()
    despesas_manutencao()
    print("\n---------------------------------------------------")


#   FUNCAO "PRINCIPAL"
def programa_principal(empresa: Empresa) -> None:
    while True:
        menu.menu_Start()
        opcao = int(input("\nDigite a opção desejada: "))

        if opcao == 0:
            break
        if opcao == 1: #    MOTORISTA
            gerenciamento_Motorista(empresa)
        elif opcao == 2: #  VEICULO
            gerenciamento_Veiculo(empresa)
        elif opcao == 3: #  VIAGEM
            gerenciamento_Viagens(empresa)
        elif opcao == 4: # ABASTECIMENTO
            cadastrar_Abastecimento(empresa)
        elif opcao == 5: #  MANUTENCAO
            cadastrar_Manutencao(empresa)
        elif opcao == 6: #  RELATORIO
            gerar_relatorio(empresa)
        else:
            print("\nERRO: OPCAO INVALIDA!\n")
