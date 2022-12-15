"""Projeto 2
Este projeto tem como objetivo simular um ecossistema, criando vários
tipos abstratos de dados que auxiliem nesse propósito.
"""


"""TAD POSIÇÃO
Representação interna: tuplo -> (x, y)

cria_posicao: inteiro x inteiro -> posição
cria_copia_posicao: posição -> posição
obter_pos_x: posição -> inteiro
obter_pos_y: posição -> inteiro
eh_posicao: universal -> booleano
posicoes_iguais: posição x posição -> booleano
posicao_para_str: posição -> cad. carateres
"""
def cria_posicao(x, y):
    """ cria_posicao: inteiro x inteiro -> posição

    Esta função recebe os valores correspondentes às coordenadas de uma posição
    e devolve a posição.
    """

    if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
        raise ValueError("cria_posicao: argumentos invalidos")

    return (x, y)


def cria_copia_posicao(p):
    """ cria_copia_posicao: posição -> posição

    Esta função recebe uma posição e devolve uma cópia da mesma.
    """

    return cria_posicao(obter_pos_x(p), obter_pos_y(p))


def obter_pos_x(p):
    """ obter_pos_x: posição -> inteiro

    Esta função recebe uma função e devolve o x da mesma.
    """

    return p[0]


def obter_pos_y(p):
    """ obter_pos_y: posição -> inteiro
    
    Esta função recebe uma função e devolve o y da mesma.
    """

    return p[1]


def eh_posicao(arg):
    """ eh_posicao: universal -> booleano
    
    Esta função recebe um argumento e retorna True se o mesmo for uma posição como
    definida no TAD Posição.
    """

    return isinstance(arg, tuple) and len(arg) == 2 and isinstance(arg[0], int) \
           and isinstance(arg[1], int) and arg[0] >= 0 and arg[1] >= 0


def posicoes_iguais(p1, p2):
    """ posicoes_iguais: posição x posição -> booleano
    
    Esta função recebe duas posições e retorna True se as posições forem iguais.
    """

    return obter_pos_x(p1) == obter_pos_x(p2) and obter_pos_y(p1) == obter_pos_y(p2)


def posicao_para_str(p):
    """ posicao_para_str: posição -> cad. carateres
    
    Esta função recebe uma posição e retorna a mesma como uma cadeia de carateres.
    """

    return str(p)


# Funções de Alto Nível - TAD Posição
def obter_posicoes_adjacentes(p):
    """ obter_posicoes_adjacentes: posição -> tuplo
    
    Esta função recebe uma posição e retorna as posições a ela adjacentes.
    """

    cord = (obter_pos_x(p), obter_pos_y(p)-1), (obter_pos_x(p)+1, obter_pos_y(p)),\
        (obter_pos_x(p), obter_pos_y(p)+1), (obter_pos_x(p)-1, obter_pos_y(p)) 

    return tuple(map(lambda x: cria_posicao(x[0], x[1]), filter(lambda x: x[0] >= 0 and x[1] >= 0, cord)))


def ordenar_posicoes(t):
    """ ordenar_posicoes: tuplo -> tuplo
    
    Esta função recebe um tuplo e retorna um tuplo com os seus componentes organizados de acordo com a
    ordem de leitura do prado.
    """
    tuplo = ()
    for el in t:
        tuplo += ((obter_pos_x(el), obter_pos_y(el)), ) #transforma as posições em tuplos para depois ordena-las
    tuplo = sorted(sorted(tuplo), key=lambda x: x[1])
    return tuple([cria_posicao(x[0], x[1]) for x in tuplo])


"""TAD ANIMAL
Representação interna: dicionário -> {"especie": s, "repr": [0, r], "alim": [0, a]}

cria_animal: cad. carateres x inteiro x inteiro -> animal
cria_copia_animal: animal -> animal
obter_especie: animal -> cad. carateres
obter_freq_reproducao: animal -> inteiro
obter_idade: animal -> inteiro
obter_freq_alimentacao: animal -> inteiro
obter_fome: animal -> inteiro
aumenta_idade: animal -> animal
reset_idade: animal -> animal
aumenta_fome: animal -> animal
reset_fome: animal -> animal
eh_animal: argumento -> booleano
eh_predador: argumento -> booleano
eh_presa: argumento -> booleano
animais_iguais: animal x animal -> booleano
animal_para_char: animal -> cad. carateres
animal_para_str: animal -> cad. carateres
"""
def cria_animal(s, r, a):
    """ cria_animal: cad. carateres x inteiro x inteiro -> animal
    
    Esta função recebe 3 valores correspondentes à espécie, frequência de reprodução e
    frequência de alimentação de um animal e retorna o animal.
    """

    if not isinstance(s, str) or not isinstance(r, int) or not isinstance(a, int) \
            or r <= 0 or a < 0 or len(s) == 0:
        raise ValueError("cria_animal: argumentos invalidos")
    
    return {"especie": s, "repr": [0, r], "alim": [0, a]}


def cria_copia_animal(a):
    """ cria_copia_animal: animal -> animal
    
    Esta função recebe um animal e devolve uma cópia do mesmo.
    """

    return cria_animal(obter_especie(a), obter_freq_reproducao(a), obter_freq_alimentacao(a))


def obter_especie(a):
    """ obter_especie: animal -> cad. carateres
    
    Esta função recebe um animal e retorna a sua espécie sob a forma de cadeia
    de carateres.
    """

    return a["especie"]


def obter_freq_reproducao(a):
    """ obter_freq_reproducao: animal -> inteiro
    
    Esta função recebe um animal e retorna a sua frequência de reprodução sob a 
    forma de inteiro.
    """

    return a["repr"][1]


def obter_idade(a):
    """ obter_idade: animal -> inteiro
    
    Esta função recebe um animal e retorna a sua idade sob a forma de inteiro.
    """

    return a["repr"][0]


def obter_freq_alimentacao(a):
    """ obter_freq_alimentacao: animal -> inteiro
    
    Esta função recebe um animal e retorna a sua frequência de alimentação sob a 
    forma de inteiro.
    """

    return a["alim"][1]


def obter_fome(a):
    """ obter_fome: animal -> inteiro
    
    Esta função recebe um animal e retorna a sua fome sob a forma de inteiro.
    """

    return a["alim"][0]


def aumenta_idade(a):
    """ aumenta_idade: animal -> animal
    
    Esta função recebe um animal e aumenta o valor da sua idade por um, retornando o animal.
    """
    
    a["repr"][0] += 1
    return a


def reset_idade(a):
    """ reset_idade: animal -> animal
    
    Esta função recebe um animal e modifica-o, definindo o seu valor de idade como 0, 
    retornando o animal.
    """

    a["repr"][0] = 0
    return a


def aumenta_fome(a):
    """ aumenta_fome: animal -> animal
    
    Esta função recebe um animal e, caso este seja um predador, aumenta o valor da sua 
    fome por um, retornando o animal.
    """

    if eh_predador(a):
        a["alim"][0] += 1
    return a


def reset_fome(a):
    """ reset_fome: animal -> animal
    
    Esta função recebe um animal e modifica-o, definindo o seu valor de fome como 0, 
    retornando o animal.
    """

    if eh_predador(a):
        a["alim"][0] = 0
    return a


def eh_animal(arg):
    """ eh_animal: argumento -> booleano
    
    Esta função recebe um argumento e retorna True se o mesmo for um animal como definido
    no TAD Animal.
    """

    return isinstance(arg, dict) and "especie" in arg.keys() and isinstance(arg["especie"], str) and \
            "repr" in arg.keys() and isinstance(arg["repr"], list) and "alim" in arg.keys() and\
            isinstance(arg["alim"], list) and len(arg["repr"]) == 2 and len(arg["alim"]) == 2 and\
            isinstance(arg["repr"][0], int) and isinstance(arg["repr"][1], int)\
            and isinstance(arg["alim"][0], int) and isinstance(arg["alim"][1], int)\
            and arg["repr"][0] >= 0 and arg["repr"][1] > 0 and arg["alim"][0] >= 0\
            and arg["alim"][1] >= 0


def eh_predador(arg):
    """ eh_predador: argumento -> booleano
    
    Esta função recebe um argumento e retorna True se este for um animal predador, ou seja,
    a sua frequência de alimentação for maior que 0.
    """

    return eh_animal(arg) and obter_freq_alimentacao(arg) > 0


def eh_presa(arg):
    """ eh_presa: argumento -> booleano
    
    Esta função recebe um argumento e retorna True se este for um animal presa, ou seja,
    a sua frequência de alimentação for igual a 0.
    """

    return eh_animal(arg) and obter_freq_alimentacao(arg) == 0


def animais_iguais(a1, a2):
    """ animais_iguais: animal x animal -> booleano
    
    Esta função recebe dois animais e retorna True se estes forem iguais.
    """

    return eh_animal(a1) and eh_animal(a2) and obter_especie(a1) == obter_especie(a2)\
            and obter_idade(a1) == obter_idade(a2) and obter_fome(a1) == obter_fome(a2)\
            and obter_freq_reproducao(a1) == obter_freq_reproducao(a2)\
            and obter_freq_alimentacao(a1) == obter_freq_alimentacao(a2)


def animal_para_char(a):
    """ animal_para_char: animal -> cad. carateres
    
    Esta função recebe um animal e retorna o primeiro carater do seu espécie, em minúsculas
    se for uma presa e em maiúsculas se for um predador.
    """

    if eh_presa(a):
        return obter_especie(a)[0].lower()
    else:
        return obter_especie(a)[0].upper()


def animal_para_str(a):
    """ animal_para_str: animal -> cad. carateres
    
    Esta função recebe um animal e retorna informação sobre o mesmo no formato 
    "espécie [idade/frequência de reprodução]" se for uma presa e no formato
    "espécie [idade/frequência de reprodução;fome/frequência de alimentação]"
    se for um predador.
    """

    if eh_presa(a):
        return obter_especie(a) + " [" + str(obter_idade(a)) + "/" + str(obter_freq_reproducao(a)) + "]"

    return obter_especie(a) + " [" + str(obter_idade(a)) + "/" + str(obter_freq_reproducao(a)) + ";"\
             + str(obter_fome(a)) + "/" + str(obter_freq_alimentacao(a)) + "]"


#Funções de Alto Nível - TAD Animal
def eh_animal_fertil(a):
    """ eh_animal_fertil: animal -> booleano
    
    Esta função recebe um animal e retorna True se este estiver fértil, ou seja,
    a sua idade é igual ou superior à sua frequência de reprodução.
    """

    return obter_idade(a) >= obter_freq_reproducao(a)


def eh_animal_faminto(a):
    """ eh_animal_faminto: animal -> booleano
    
    Esta função recebe um animal e retorna True se este estiver faminto, ou seja,
    a sua fome é igual ou superior à sua frequência de alimentação.
    """

    return eh_predador(a) and obter_fome(a) >= obter_freq_alimentacao(a)


def reproduz_animal(a):
    """ eh_animal_faminto: animal -> animal
    
    Esta função recebe um animal e modifica-o, recorrendo à função reset_idade, retornando
    um segundo animal, resultante da reprodução do primeiro.
    """

    reset_idade(a)
    return cria_copia_animal(a)


"""TAD PRADO
Representação interna: lista -> [dim, roc, list(a), list(p)]

cria_prado: posição x tuplo x tuplo x tuplo -> prado
cria_copia_prado: prado -> prado
obter_tamanho_x: prado -> inteiro
obter_tamanho_y: prado -> inteiro
obter_numero_predadores: prado -> inteiro
obter_numero_presas: prado -> inteiro
obter_posicoes_animais: prado -> tuplo
obter_animal: prado x posição -> animal
eliminar_animal: prado x posição -> prado
mover_animal: prado x posição x posição -> prado
inserir_animal: prado x animal x posição -> prado
eh_prado: universal -> booleano
eh_posicao_animal: prado x posição -> booleano
eh_posicao_obstaculo: prado x posição -> booleano
eh_posicao_livre: prado x posição -> booleano
prados_iguais: prado x prado -> booleano
prado_para_str: prado -> cad. carateres
"""
def cria_prado(dim, roc, a, p):
    """ cria_prado: posição x tuplo x tuplo x tuplo -> prado

    Esta função recebe quatro parâmetros, uma posição e três tuplos, que representam respetivamente 
    a posição que ocupa o canto inferior direito do prado, a localização de rochedos no mesmo, os 
    animais nele presentes e as suas respetivas posições, retornando o prado.
    """

    if not eh_posicao(dim) or not isinstance(roc, tuple) or not isinstance(a, tuple)\
        or not isinstance(p, tuple) or len(a) != len(p) or len(a) < 1:
        raise ValueError("cria_prado: argumentos invalidos")

    for el in a:
        if not eh_animal(el):
            raise ValueError("cria_prado: argumentos invalidos")

    for el in p+roc:
        if not eh_posicao(el) or (obter_pos_x(el) >= obter_pos_x(dim) or obter_pos_y(el) >= obter_pos_y(dim) or\
             obter_pos_x(el) == 0 or obter_pos_y(el) == 0): #certifica que se encontram dentro do prado
            raise ValueError("cria_prado: argumentos invalidos")
    
    return [dim, roc, list(a), list(p)]


def cria_copia_prado(m):
    """ cria_copia_prado: prado -> prado
    
    Esta função recebe um prado e retorna uma cópia do mesmo.
    """

    return cria_prado(m[0], m[1], tuple(m[2]), tuple(m[3]))


def obter_tamanho_x(m):
    """ obter_tamanho_x: prado -> inteiro
    
    Esta função recebe um prado e retorna o valor da dimensão Nx do prado
    """

    return obter_pos_x(m[0]) + 1


def obter_tamanho_y(m):
    """ obter_tamanho_y: prado -> inteiro
    
    Esta função recebe um prado e retorna o valor da dimensão Ny do prado
    """

    return obter_pos_y(m[0]) + 1


def obter_numero_predadores(m):
    """ obter_numero_predadores: prado -> inteiro

    Esta função recebe um prado e retorna um inteiro que corresponde à quantidade de animais
    predadores presente no mesmo.
    """

    return len(list(filter(lambda x: eh_predador(x), m[2])))


def obter_numero_presas(m):
    """ obter_numero_presas: prado -> inteiro

    Esta função recebe um prado e retorna um inteiro que corresponde à quantidade de animais
    presas presente no mesmo.
    """
    
    return len(list(filter(lambda x: eh_presa(x), m[2])))


def obter_posicao_animais(m):
    """ obter_posicoes_animais: prado -> tuplo
    
    Esta função recebe um prado e retorna as posições do mesmo ordenadas.
    """

    return ordenar_posicoes(m[3])


def obter_animal(m, p):
    """ obter_animal: prado x posição -> animal
    
    Esta função recebe um prado e uma posição e retorna o animal presente nessa posição,
    caso exista.
    """

    for i in range(len(m[3])):
        if posicoes_iguais(m[3][i], p):
            return m[2][i]


def eliminar_animal(m, p):
    """ eliminar_animal: prado x posição -> prado
    
    Esta função recebe um prado e uma posição e elimina o animal presente nessa posição
    do prado, caso exista.
    """

    for i in range(len(m[3])):
        if posicoes_iguais(m[3][i], p):
            del m[3][i]
            del m[2][i]
            return m


def mover_animal(m, p1, p2):
    """ mover_animal: prado x posição x posição -> prado
    
    Esta função recebe um prado e duas posições e move o animal presente na primeira posição
    para a segunda, retornando o prado.
    """

    for i in range(len(m[3])):
        if posicoes_iguais(m[3][i], p1):
            m[3][i] = p2
            return m


def inserir_animal(m, a, p):
    """ inserir_animal: prado x animal x posição -> prado
    
    Esta função recebe um prado, um animal e uma posição e adiciona o animal ao prado
    na posição dada, retornando o prado.
    """

    m[2] += [a]
    m[3] += [p]
    return m


def eh_prado(arg):
    """ eh_prado: universal -> booleano
    
    Esta função recebe um argumento e retorna True se este for um prado.
    """

    return isinstance(arg, list) and len(arg) == 4 and isinstance(arg[0], tuple) and\
             isinstance(arg[1], tuple) and isinstance(arg[2], list) and isinstance(arg[3], list)\
             and len(arg[2]) == len(arg[3]) and len(arg[2]) >= 1 and eh_posicao(arg[0])


def eh_posicao_animal(m, p):
    """ eh_posicao_animal: prado x posição -> booleano

    Esta função recebe um prado e uma posição e retorna True se um animal se encontrar nessa posição do prado.
    """
    
    ani = False
    for i in range(len(m[3])):
        if posicoes_iguais(m[3][i], p):
            ani = True
    return eh_prado(m) and ani


def eh_posicao_obstaculo(m, p):
    """ eh_posicao_obstaculo: prado x posição -> booleano
    
    Esta função recebe um prado e uma posição e retorna True se nessa posição se encontrar um obstáculo.
    """

    obs = False
    for i in range(len(m[1])):
        if posicoes_iguais(m[1][i], p):
            obs = True
    return obs or obter_pos_x(p)==0 or obter_pos_x(p)==obter_tamanho_x(m)-1 or\
             obter_pos_y(p)==0 or obter_pos_y(p)==obter_tamanho_y(m)-1


def eh_posicao_livre(m, p):
    """ eh_posicao_livre: prado x posição -> booleano
    
    Esta função recebe um prado e uma posição e retorna True se essa posição no prado se encontrar livre.
    """

    return not eh_posicao_animal(m, p) and not eh_posicao_obstaculo(m, p)


def prados_iguais(m1, m2):
    """ prados_iguais: prado x prado -> booleano
    
    Esta função recebe dois prados e retorna True se estes forem iguais.
    """

    obs = True
    pos = True

    for p in m1[1]+m2[1]:
        if not eh_posicao_obstaculo(m1, p) or not eh_posicao_obstaculo(m2, p):
            obs = False

    for i in range(len(obter_posicao_animais(m1))):
        if not posicoes_iguais(obter_posicao_animais(m1)[i], obter_posicao_animais(m2)[i]):
            pos = False
            
    return eh_prado(m1) and eh_prado(m2) and obter_tamanho_x(m1) == obter_tamanho_x(m2) and obter_tamanho_y(m1) == obter_tamanho_y(m2)\
             and len(m1[3])==len(m2[3]) and pos and obs and\
             obter_numero_predadores(m1) == obter_numero_predadores(m2) and obter_numero_presas(m1) == obter_numero_presas(m2)\
             and list(map(lambda x: obter_animal(m1, x), obter_posicao_animais(m1))) == list(map(lambda x: obter_animal(m1, x), obter_posicao_animais(m1)))
            

def prado_para_str(m):
    """ prado_para_str: prado -> cad. carateres
    
    Esta função recebe um prado e retorna o mesmo em forma de cadeia de carateres.
    """

    tam = obter_tamanho_x(m)-2
    prado = "+" + "-"*tam + "+\n"

    for i in range(1, obter_tamanho_y(m)-1):
        prado += "|"

        for j in range(1, obter_tamanho_x(m)-1):
            p = cria_posicao(j, i)

            if eh_posicao_livre(m, p):
                prado += "."
            elif eh_posicao_obstaculo(m, p):
                prado += "@"
            elif eh_posicao_animal(m, p):
                prado += animal_para_char(obter_animal(m, p))

        prado += "|\n"

    return prado + "+" + "-"*tam + "+"
        
    
# Funções de Alto Nível - TAD Prado
def obter_valor_numerico(m, p):
    """ obter_valor_numerico: prado x posição -> inteiro
    
    Esta função retorna o valor numérico da posição de acordo com a ordem de leitura do prado.
    """

    return obter_pos_y(p)*obter_tamanho_x(m) + obter_pos_x(p)


def obter_movimento(m, p):
    """ obter_movimento: prado x posição -> posição
    
    Esta função recebe um prado e uma posição e retorna a posição onde o animal na posição inicial
    se moverá de acordo com se esse animal é predador(ou seja, tem a opção de comer presas) ou presa.
    """

    p_adja = obter_posicoes_adjacentes(p)
    p_num = obter_valor_numerico(m, p)

    if len(p_adja) == 0:
        return p

    if eh_predador(obter_animal(m, p)):
        
        res = list(filter(lambda x: not eh_posicao_obstaculo(m, x) and not eh_predador(obter_animal(m, x)), p_adja)) #posições para onde um predador pode mover
        if res == []:
            return p

        come = list(filter(lambda x: eh_presa(obter_animal(m, x)), res)) #posições onde se encontram presas
        if come: 
            return come[p_num%len(come)] #se existirem presas, uma posição onde uma esteja é escolhida

        return res[p_num%len(res)] #caso contrário, é escolhida uma posição livre

    else:

        res = list(filter(lambda x: eh_posicao_livre(m, x), p_adja))
        if res == []:
            return p

        return res[p_num%len(res)] #as presas vão sempre para uma posição livre caso exista


#Funções Adicionais#
def geracao(m):
    """ geracao: prado -> prado
    
    Esta função recebe um prado e simula as ações de cada animal no mesmo de acordo com
    as suas regras de movimento, reprodução e alimentação.
    """

    pos_ani = obter_posicao_animais(m)
    mortos = ()

    for p in pos_ani:
        if p not in mortos:

            ani = obter_animal(m, p)
            aumenta_idade(ani) #aumenta a idade independentemente do tipo do animal
            mov = obter_movimento(m, p)

            if eh_presa(ani):
                mover_animal(m, p, mov)

            else:
                aumenta_fome(ani) #só aumenta fome se não for presa (ou seja, é predador)
                if obter_animal(m, mov):
                    eliminar_animal(m, mov)
                    mortos += (mov, ) #garante que, se o animal comido estiver numa posição seguinte, o predador não se move 2 vezes
                    reset_fome(ani)
                mover_animal(m, p, mov)

            if eh_animal_fertil(ani) and eh_posicao_livre(m, p):
                inserir_animal(m, reproduz_animal(ani), p)

            if eh_animal_faminto(ani):
                eliminar_animal(m, mov)

    return m


def simula_ecossistema(fich, gen, verb):
    """ simula_ecossistemas: cad. carateres x inteiro x booleano -> tuplo
    
    Esta função recebe uma cadeia de carateres que corresponde ao nome de um ficheiro, um inteiro que representa
    o número de gerações a simular e um booleano que determina se cada vez que o número de presas ou predadores muda
    mostra-se o prado ou não. Esta função retorna um tuplo com o número de predadores e de presas no prado após 
    realizar a simulação das gerações.
    """

    prado = config_prado(fich)
    n_animais = obter_numero_predadores(prado), obter_numero_presas(prado)
    print("Predadores: {} vs Presas: {} (Gen. 0)\n".format(n_animais[0], n_animais[1]) + prado_para_str(prado))

    if verb:

        for i in range(0, gen):
            geracao(prado)

            if obter_numero_predadores(prado) != n_animais[0] or obter_numero_presas(prado) != n_animais[1]:
                n_animais = obter_numero_predadores(prado), obter_numero_presas(prado)
                print("Predadores: {} vs Presas: {} (Gen. {})\n".format(n_animais[0], n_animais[1], i+1) + prado_para_str(prado))
    
    else:

        for i in range(0, gen):
            geracao(prado)

        n_animais = obter_numero_predadores(prado), obter_numero_presas(prado)
        print("Predadores: {} vs Presas: {} (Gen. {})\n".format(n_animais[0], n_animais[1], gen) + prado_para_str(prado))

    return n_animais


def config_prado(fich):
    """ config_prado: cad. carateres -> prado
    
    Esta função auxiliar recebe uma cadeia de carateres correspondente ao nome de um ficheiro e simplifica
    o conteúdo do mesmo, possibilitando o retorno de um prado.
    """

    def separa(lista):
        """ separa: lista -> lista
        
        Esta função auxiliar separa os diferentes componentes importantes do ficheiro, retornando-os em lista.
        """

        res = []

        for el in lista:
            if len(el) > 1:
                el = el.replace("\n", "").replace(" ", "").replace("(", "").replace(")", "")
                res += [el.split(",")] #na resposta ficam só os números e as cadeias de carateres relevantes

        return res

    f = open(fich, "r")
    info = separa(f.readlines())
    f.close()
    dim = cria_posicao(int(info[0][0]), int(info[0][1]))
    roc, a, p = (), (), ()

    if len(info[1]) > 1:
        for i in range(0, len(info[1]), 2):
            roc += (cria_posicao(int(info[1][i]), int(info[1][i+1])), )

    for i in range(2, len(info)):
        a += (cria_animal(info[i][0][1:-1], int(info[i][1]), int(info[i][2])), )
        p += (cria_posicao(int(info[i][3]), int(info[i][4])), )

    return cria_prado(dim, roc, a, p)