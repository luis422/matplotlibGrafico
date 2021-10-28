#python -m pip install -U pip
#python -m pip install -U matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

#valores da linha 1
x1 = np.array([0,1,2,3])
y1 = np.array([3,8,1,10])

#valores da linha 2
x2 = np.array([0,1,2,3])
y2 = np.array([6,2,7,11])

#adiciona as linhas e tambem as legenda das linhas
plt.plot(x1, y1,label='Linha 1')
plt.plot(x2, y2,label='Linha 2')

#textos dos eixos
plt.ylabel('Eixo Y')
plt.xlabel('Eixo X')

#plt.axis( (xmenor,xmaior,ymenor,ymaior) )
plt.axis((-1,4,1,12))

#mostra uma grade
plt.grid(True)

#mostra a legenda
plt.legend()

#título e estilo do título
plt.title('Gráfico de Linhas', color='gray', fontsize='x-large', style='italic')

#mostra o gráfico
plt.show()