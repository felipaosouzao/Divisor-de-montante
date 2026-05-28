# Divisor de Montante (euros)


Programa simples para dividir um montante em euros entre categorias — por porcentagens ou subtrair valores. 

Pré-requisitos
- Python 3.8+ instalado.

Como rodar

python pdp.py

1. Pressione Enter para iniciar.
2. Informe o montante total (aceita vírgula ou ponto como separador decimal).
3. Escolha o modo: `p` para porcentagens ou `v` para valores.
4. Informe os nomes das categorias (deixe o nome vazio e pressione Enter para finalizar a lista).
5. Informe a porcentagem ou o valor para cada categoria, conforme o modo.
6. O programa mostrará total alocado e restante.
7. Ao final, escolha uma das opções:
   - `1` — Finalizar
   - `2` — Refazer tudo (montante e categorias)
   - `3` — Refazer apenas valores/porcentagens (mantém montante e nomes)

Observações importantes
- Para finalizar a lista de nomes deixe o campo vazio e pressione Enter. (Pode ser necessário pressionar Enter uma vez para avançar e outra para confirmar.)
- Se a soma das porcentagens > 100% ou a soma dos valores > montante, o programa avisa. Você pode:
  - continuar (o restante ficará negativo), ou
  - corrigir e inserir novamente os valores/porcentagens.
- Entradas inválidas (texto onde se espera número, números negativos) são rejeitadas e solicitam reentrada.
- Ao escolher a opção `3`, o montante e os nomes das categorias ficam preservados; apenas as porcentagens/valores são solicitados novamente.
