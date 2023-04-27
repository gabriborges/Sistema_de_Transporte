###########################################
# DUPLA:
# -- GABRIEL BORGES CARVALHO
# -- JOÃO MARCELO DINZ MENDES DA SILVA
###########################################

import os
import programa_principal as principal
from classes import Empresa, Veiculo, Motorista, Viagem
os.system('cls')

tx_Carrara = Empresa("Carrara Taxi", "098654345")

tx_Carrara = Empresa("Carrara Taxi", "098654345")
fiat_UNO = Veiculo("FIAT UNO","1999", 1999, "IFM-4C08", "001", "Branco")
gol_BOLA = Veiculo("GOL", '2000', 2000, "BRA-0E21", "002", "Vermelho")
brasilia = Veiculo("BRASILIA",'1990', 1990, "DTF-1E45", "003", "Amarela")

agostinho = Motorista("Agostinho Carrara", "0001", "09876544-1", "15263748028")

tx_Carrara.adicionar_Motorista(agostinho)
tx_Carrara.adicionar_Veiculo(fiat_UNO)
tx_Carrara.adicionar_Veiculo(gol_BOLA)
tx_Carrara.adicionar_Veiculo(brasilia)

viagem = Viagem(1, "caxias", "caxias", 200.0, agostinho, fiat_UNO )
viagem2 = Viagem(2, "caxias", "caxias", 1.0, agostinho, fiat_UNO )

tx_Carrara.registrar_Viagem(viagem)
tx_Carrara.registrar_Viagem(viagem2)

principal.programa_principal(tx_Carrara)