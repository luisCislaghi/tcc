import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


## MUDANÇAS NOS DADOS
# removida a P1 de todos
# A1 [1] = 55 -> 35
# A1 [4] = 52 -> 40
# A3 [6] = 58 -> 20
# A5 [1] = 48 -> 25
# A5 [4] = 66 -> 36
# B4 [4] = 57 -> 17

# Amostras
amostrasA =   [
    [ 35, 28, 38, 40, 37, 22, 24, 25], #56,
    [ 24, 23, 9, 11, 13, 11, 8, 11], #39,
    [ 25, 27, 21, 22, 18, 20, 15, 19], #86,
    [ 25, 16, 30, 14, 14, 13, 12, 14], #45,
    [ 25, 27, 17, 36, 29, 14, 15, 16], #53,
]
amostrasB =   [
    [ 18, 12, 10, 10, 16, 13, 9, 14], #60,
    [ 26, 10, 14, 11, 15, 17, 19, 16], #39,
    [ 31, 13, 27, 9, 9, 18, 9, 10], #53,
    [ 28, 29, 15, 17, 34, 18, 16, 12], #84,
    [ 29, 14, 11, 17, 14, 7, 12, 8], #24,
]
amostras = np.concatenate((amostrasA,amostrasB))
mediaTotalPorAmostra = np.mean(amostras, axis=1)
mediasA = np.mean(amostrasA, axis=0)
mediasB = np.mean(amostrasB, axis=0)




########################################
########################################
########################################
### MEDIA POR GRUPO ###

def mediaPorGrupo(amostraA,amostraB):
  totalA = np.array(amostraA).flatten()
  totalB =  np.array(amostraB).flatten()
  d = [totalA, totalB]
  medias = np.mean(d, axis=1)
  for i, media in enumerate(medias):
      print("Média do item", i+1, ":", media)

# mediaPorGrupo(amostrasA,amostrasB)


########################################
########################################
########################################
### GRAFICO MÉDIA POR PERGUNTA
def plotMediaPorPergunta(amostras,mediasA, mediasB):
  mediaTotal = np.mean(amostras, axis=0)
  perguntas = ("P2","P3","P4","P5","P6","P7","P8","P9")
  medias = {
      'A': (mediasA),
      'B': (mediasB),
  }

  x = np.arange(len(perguntas))  # label locations
  width = 0.25  # bars width
  multiplier = 0

  fig, ax = plt.subplots(layout='constrained')
 
  ax.plot(mediaTotal, color="#ff99c3",linewidth=3)

  def color(g):
    if(g == "A"):
      return "#5b8ff9"
    return "#41c590"

  for attribute, measurement in medias.items():
      offset = width * multiplier
      rects = ax.bar(x + offset, measurement, width, label=attribute,color=color(attribute))
      ax.bar_label(rects, padding=2)
      multiplier += 1

  ax.set_xticks(x + width, perguntas)
  ax.legend(loc='upper left', ncols=2)
  ax.set_ylim(0, 45)
  ax.set_ylabel('Segundos')
  ax.set_xlabel('Perguntas')
  ax.set_title('Média de tempo dispensado por pergunta por grupo')

  t2 = np.arange(0.0, 2.0, 0.01)

  plt.show()


plotMediaPorPergunta(amostras,mediasA,mediasB)


########################################
########################################
########################################
### GRAFICO MEDIA TEMPO TOTAL POR AMOSTRA ###

def plotMediaTempoPorAmostra(mediaTotalPorAmostra):
  x = ['A1','A2','A3','A4','A5','B1','B2','B3','B4','B5']
  y = mediaTotalPorAmostra
  colors = ["#5b8ff9","#5b8ff9","#5b8ff9","#5b8ff9","#5b8ff9","#41c590","#41c590","#41c590","#41c590","#41c590"]

  # plot
  fig, ax = plt.subplots()

  bars = ax.bar(x, y, width=1, edgecolor="white",color=colors, linewidth=0.7, label="asdas")
  ax.bar_label(bars,padding=2)
  ax.set_ylabel('Segundos')
  ax.set_xlabel('Amostras')
  ax.set_title('Média de tempo dispensado por pergunta')
  ax.set(xlim=(-1, 10), 
        ylim=(0, 45), yticks=np.arange(0, 46,5))

  plt.show()

plotMediaTempoPorAmostra(mediaTotalPorAmostra)



########################################
########################################
########################################
### T STUDENT

def eleva2(lista):
  nova_lista = []
  for item in lista:
      resultado = item ** 2
      nova_lista.append(resultado)
  return nova_lista

def testeT(mediasA,mediasB):
  gl= 6
  t = 2.4469 ## t critico na tabela

  t_statistic, p_value = stats.ttest_ind(mediasA, mediasB)

  # Exibindo os resultados
  print("Estatística do teste t:", t_statistic)
  print("Valor p:", p_value)




testeT(mediasA,mediasB)


########################################
########################################
########################################