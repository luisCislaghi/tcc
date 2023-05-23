import numpy as np
from scipy import stats

# Amostras
amostra1 = np.array([10, 12, 15, 13, 11])
amostra2 = np.array([8, 9, 11, 10, 12])

# Teste t de Student independente
statistic, p_value = stats.ttest_ind(amostra1, amostra2)

# Imprimindo os resultados
print("Estatística de teste:", statistic)
print("Valor p:", p_value)