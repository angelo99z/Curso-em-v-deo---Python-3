import math
cd1 = '\033[1;35m'
cd2 = '\033[m'
angulo = float(input('{}Digite o grau do ângulo: {}'.format(cd1, cd2)))
seno = math.sin(math.radians(angulo))
# para calcular o seno é necessário converter o angulo em radianos primeiro "(math.radians(angulo))"
# após convertido é possível encontrar o seno com o comando "math.sin(x)"
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('{}O ângulo de {} tem o seno {:.2f}{}'.format(cd1, angulo, seno, cd2))
print('{}O ângulo de {} tem o seno {:.2f}{}'.format(cd1, angulo, cosseno, cd2))
print('{}O ângulo de {} tem o seno {:.2f}{}\n'.format(cd1, angulo, tangente, cd2))
