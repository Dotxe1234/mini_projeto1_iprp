# Carregar o mapa:

Então, primeiro, no ficheiro "principal_alunos.py", na função "carrega_jogo" criei um loop que lê o ficheiro e cria uma lista com o conteúdo do mesmo (no caso é um mapa) e atualizei o dicionário "estado_jogo" na key "mapa" com essa lista que criei. olakdajondahdnn

#------------------------
```
def carrega_jogo(estado_jogo, nome_ficheiro):
    # Abrir e ler o arquivo
    with open(rf"C:\\Users\\Utilizador\\Desktop\\Codigo-Alunos\\Codigo-Alunos\\{nome_ficheiro}", 'r') as file:
        data = file.read()

    data = data.replace('\n', '').replace(' ', '')

    elementos = data.split(',')
    elementos = [int(x) for x in elementos if x]

    estado_jogo['mapa'] = elementos

    return estado_jogo['mapa']
```

#------------------------

# Movimentar o Pacman

Coloquei o pacman a andar, basicamente o dicionário "estado_jogo" possui uma key "pacman" que por si contem outro dicionario "direcao_atual" na qual é atribuido o valor de um tuplo com valores entre 0,5. Sendo o tuplo (x, y) se quiser andar para cima vai ser (0, 5). Exemplo:

#-------------------------

```
def pacman_cima(estado_jogo):
    estado_jogo['pacman']['direcao_atual'] = (0, 5)
    return estado_jogo['pacman']['direcao_atual']
```

#-------------------------

Depois tem uma função chamada "movimenta_pacman" que pega nesse valor do tuplo e calcula se é um movimento válido atravéz daquilo que o stor que veio quando o stor charles faltou disse, epa tinha lá um código como comentario a dizer como se fazia e eu so tirei de comentário e deu.
