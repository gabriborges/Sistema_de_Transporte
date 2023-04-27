class Veiculo:
    def __init__(self, marca: str, modelo: str, ano: int, placa: str, chassi: str, cor: str, quilometragem: float = 0 ) -> None:
      self.marca = marca
      self.modelo = modelo
      self.__ano = ano
      self.placa = placa
      self.__chassi = chassi
      self.cor = cor
      self.__quilometragem = quilometragem

    #   ACESSA ATRIBUTOS PRIVADOS  
    @property
    def ano(self):
      return self.__ano
    @ano.setter
    def ano(self, ano: int):
       self.__ano = ano
    
    @property
    def chassi(self):
       return self.__chassi
    @chassi.setter
    def chassi(self, chassi:str):
       self.__chassi = chassi

    @property
    def quilometragem(self):
       return self.__quilometragem
    @quilometragem.setter
    def quilometragem(self, quilomentagem: float):
       self.__quilometragem = quilomentagem

class Motorista:
    def __init__(self, nome: str, cpf: int, rg: str, cnh: str) -> None:
      self.nome = nome
      self.cpf = cpf 
      self.rg = rg
      self.cnh = cnh
      self.quant_viagens = 0
      self.__quilometragem = 0

    @property
    def quilometragem(self):
       return self.__quilometragem
    @quilometragem.setter
    def quilometragem(self, quilomentagem: float):
       self.__quilometragem = quilomentagem

class Viagem:
    def __init__(self, codigo: int, destino: str, origem: str, distancia: float, motorista: Motorista, veiculo: Veiculo) -> None:
        self.codigo = codigo
        self.destino = destino
        self.origem = origem
        self.distancia = distancia
        self.motorista = motorista
        self.veiculo = veiculo
    
class Manutencao:
   def __init__(self, data: str, tipo: str, custo: float, veiculo: Veiculo) -> None:
      self.data = data
      self.tipo = tipo
      self.custo = custo
      self.veiculo = veiculo

class Abastecimento:
   def __init__(self, data: str, quant_combustivel: float, valor: float, veiculo: Veiculo) -> None:
      self.data = data
      self.quant_combustivel = quant_combustivel
      self.valor = valor
      self.veiculo = veiculo

class Empresa:
    def __init__(self, nome: str, cnpj: str) -> None:
      self.nome = nome
      self.cnpj = cnpj
      self.frota = list()
      self.funcionarios = list()
      self.registro_Abastecimento = list()
      self.registro_Viagens = list()
      self.registro_Manutencao = list()

      self.despesa_abastecimento = 0.0
      self.despesa_manutencao = 0.0
   
    #   ALTERAR FROTA
    def adicionar_Veiculo(self, veiculo: Veiculo):
        self.frota.append(veiculo)
    
    def remover_Veiculo(self, veiculo: Veiculo):
        self.frota.remove(veiculo)
    
    def pesquisar_Veiculos(self, chassi: str) -> None:
      contador = 0
      for veiculo in self.frota:
            contador += 1
            if chassi == veiculo.chassi:
                print(f"Marca:{veiculo.marca}\nAno: {veiculo.ano}\nPlaca: {veiculo.placa}")
                print(f"Chassi:{veiculo.chassi}\nCor: {veiculo.cor}\nQuilometragem: {veiculo.quilometragem}")
                break
      else:
        if contador == len(self.frota):
            print("Veículo não encontado")
    
    def pesquisar_VeiculosEditar(self, chassi: str) -> object:
      contador = 0
      for veiculo in self.frota:
            #contador += 1
            if chassi == veiculo.chassi:
                return veiculo
            contador += 1
      else:
        if contador == len(self.frota):
            return None

    #   ALTERAR QUADRO FUNCIONÁRIOS
    def adicionar_Motorista(self, motorista: Motorista):
        self.funcionarios.append(motorista)
    
    def remover_Motorista(self, motorista: Motorista):
        self.funcionarios.remove(motorista)

    
    def pesquisar_Funcionarios(self, cpf: int) -> None:
      contador = 0
      for funcionario in self.funcionarios:
            if cpf == funcionario.cpf:
                print(f"Nome:{funcionario.nome}\nCPF: {funcionario.cpf}\nRG: {funcionario.rg}")
                print(f"CNH:{funcionario.cnh}\nQuant. Km trabalhados: {funcionario.quilometragem}")
                break
            contador += 1
      else:
        if contador == len(self.funcionarios):
            print("\nFuncionário não encontado\n")
    
    def pesquisar_FuncionariosEditar(self, cpf: str) -> object:
      contador = 0
      for funcionario in self.funcionarios:
            #contador += 1
            if cpf == funcionario.cpf:
                return funcionario
            contador += 1
      else:
        if contador == len(self.funcionarios):
            return None

    #   CONTROLE VIAGENS
    def registrar_Viagem(self, viagem: Viagem)-> None:
         self.registro_Viagens.append(viagem)

         for motorista in self.funcionarios:
            if motorista.cpf == viagem.motorista.cpf:
               motorista.quilometragem+= viagem.distancia
               motorista.quant_viagens += 1
               
         for veiculo in self.frota:
            if veiculo.chassi == viagem.veiculo.chassi:
               veiculo.quilometragem+= viagem.distancia

    #   FALTA "EDITAR VIAGEM"
    
    def pesquisar_Viagem(self, codigo: int) -> object:
       contador = 0
       for viagem in self.registro_Viagens:
          contador += 1
          if codigo == viagem.codigo:
            return viagem  
          else:
            if contador == len(self.registro_Viagens):
               return None        
    
    #   CONTROLE MANUTENÇÃO
    def registrar_Manutencao(self, veiculo: Veiculo):
       data = input("DATA: ")
       tipo = input("TIPO DA MANUTENÇÃO: ")
       custo = float(input("VALOR: "))

       manutencao = Manutencao(data, tipo, custo, veiculo)
       self.registro_Manutencao.append(manutencao)
       self.despesa_manutencao += custo
    
    #  CONTROLE ABASTECIMENTO
    def registrar_Abastecimento(self, veiculo: Veiculo):
        data = input("DATA: ")
        quant_combustivel = float(input("QUANTIDADE DE COMBUSTIVEL: "))
        valor = float(input("CUSTO: ")) 

        abastecimento = Abastecimento(data, quant_combustivel, valor, veiculo)
        self.registro_Abastecimento.append(abastecimento)
        self.despesa_abastecimento += valor

    def gerar_Relatorio(self):...