import random

def gerar_novo_cpf_valido():
    cpf = ''

    # Gera 9 numeros aleatorios iniciais para o CPF
    for n in range(9):
        novo_numero = str(random.randint(0, 9))
        cpf += novo_numero

    # --- Gerando o primeiro digito verificador (10º numero) ---

    lista_de_pesos_1 = []
    soma_de_tudo_1 = 0
    primeiro_digito_verificador = 0

    # Cria a lista de pesos decrescentes de 10 ate 2
    for n in range(10, 1, -1):
        lista_de_pesos_1.append(n)

    # Multiplica cada um dos 9 digitos pelo seu peso correspondente e soma os resultados
    for n in range(9):
        valor_do_cpf_1 = int(cpf[n])
        valor_do_peso_1 = lista_de_pesos_1[n]
        resultado_1 = valor_do_cpf_1 * valor_do_peso_1
        soma_de_tudo_1 += resultado_1

    # Regra do CPF: Se o resto da divisao por 11 for 0 ou 1, o digito e 0. 
    # Caso contrario, subtrai o resto de 11.
    if soma_de_tudo_1 % 11 == 0 or soma_de_tudo_1 % 11 == 1:
        primeiro_digito_verificador = 0
    else:
        primeiro_digito_verificador = 11 - (soma_de_tudo_1 % 11)

    # Concatena o primeiro digito calculado aos 9 numeros iniciais
    primeiro_digito_verificador = str(primeiro_digito_verificador)
    cpf = cpf + primeiro_digito_verificador

    # --- Gerando o segundo digito verificador (11º numero) ---

    lista_de_pesos_2 = []
    soma_de_tudo_2 = 0
    segundo_digito_verificador = 0

    # Para o segundo digito, a contagem de pesos começa em 11 ate 2
    for n in range(11, 1, -1):
        lista_de_pesos_2.append(n)

    # Multiplica os 10 digitos atuais (9 originais + 1º verificador) pelos pesos
    for n in range(10):
        valor_do_cpf_2 = int(cpf[n])
        valor_do_peso_2 = lista_de_pesos_2[n]
        resultado_2 = valor_do_cpf_2 * valor_do_peso_2
        soma_de_tudo_2 += resultado_2        

    # Aplica a mesma regra de calculo do resto para o segundo digito
    if soma_de_tudo_2 % 11 == 0 or soma_de_tudo_2 % 11 == 1:
        segundo_digito_verificador = 0
    else:
        segundo_digito_verificador = 11 - (soma_de_tudo_2 % 11)

    # Adiciona o segundo digito ao final para completar os 11 numeros
    segundo_digito_verificador = str(segundo_digito_verificador)
    cpf = cpf + segundo_digito_verificador

    # Formata a string final para o padrao visual brasileiro (000.000.000-00)
    cpf_formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    return cpf_formatado

def validador_de_cpf(cpf):
    # Garante que a entrada seja tratada como string
    cpf = str(cpf)
    validacao_do_primeiro_digito = False
    validacao_do_segundo_digito = True # Inicializado como True para controle de fluxo

    # --- Validacao do Primeiro Digito ---
    cpf_com_9_digitos = cpf[:-2] # Pega apenas a base do CPF enviada pelo usuario
    lista_de_pesos_3 = []

    # Define pesos para o calculo de validacao (10 a 2)
    for n in range(10, 1, -1):
        lista_de_pesos_3.append(n)

    soma_total_validador = 0

    # Realiza a soma ponderada dos 9 primeiros digitos
    for n in range(9):
        valor_do_cpf_3 = int(cpf_com_9_digitos[n])
        valor_do_peso_3 = lista_de_pesos_3[n]
        resultado_3 = valor_do_cpf_3 * valor_do_peso_3
        soma_total_validador += resultado_3

    # Verifica se o 10º digito informado pelo usuario bate com o calculo matematico
    if soma_total_validador % 11 == 0 or soma_total_validador % 11 == 1:
        if cpf[9] != '0':
            return 'CPF invalido!'
        else:
            validacao_do_primeiro_digito = True
    elif soma_total_validador % 11 >= 2 and soma_total_validador % 11 <= 10:
        if cpf[9] != str(11 - (soma_total_validador % 11)):
            return 'CPF invalido!'
        else:
            validacao_do_primeiro_digito = True
    
    # --- Validacao do Segundo Digito ---
    cpf_com_10_digitos = cpf[:-1] # Inclui o primeiro digito ja verificado
    lista_de_pesos_4 = []
    soma_total_validador_1 = 0

    # Define pesos para o calculo do segundo digito (11 a 2)
    for n in range(11, 1, -1):
        lista_de_pesos_4.append(n)

    # Soma ponderada dos 10 digitos
    for n in range(10):
        valor_do_cpf_4 = int(cpf_com_10_digitos[n])
        valor_do_peso_4 = lista_de_pesos_4[n]
        resultado_4 = valor_do_cpf_4 * valor_do_peso_4
        soma_total_validador_1 += resultado_4
    
    # Verifica se o 11º digito informado pelo usuario bate com o calculo
    if soma_total_validador_1 % 11 == 0 or soma_total_validador_1 % 11 == 1:
        if cpf[10] != '0':
            return 'CPF invalido!'
        else:
            validacao_do_segundo_digito = True
    elif soma_total_validador_1 % 11 >= 2 and soma_total_validador_1 % 11 <= 10:
        if cpf[10] != str(11 - (soma_total_validador_1 % 11)):
            return 'CPF invalido!'
        else:
            validacao_do_segundo_digito = True
    
    # Se ambos os calculos baterem com os digitos informados, o CPF e considerado valido
    if validacao_do_primeiro_digito == True and validacao_do_segundo_digito == True:
        return 'CPF Valido!'

# --- Menu de Interação Principal ---
while True:
    print()
    print('Gerador e Validador de CPF:')
    print()
    print('1. Gerar CPF aleatorio')
    print('2. Validar CPF')
    print()

    try:
        resposta_do_usuario = int(input('Qual opcao voce escolhe? '))
        print()

        if resposta_do_usuario == 1:
            # Chama a funcao de geracao e exibe o CPF ja formatado
            print(f'CPF gerado: {gerar_novo_cpf_valido()}')
            continue
        elif resposta_do_usuario == 2:
            # Solicita a entrada do usuario para validacao
            cpf__enviado_pelo_usuario = input('Digite o CPF que voce quer verificar, sem separacoes: ')
            
            # Verifica se a string possui o tamanho correto antes de processar
            if len(cpf__enviado_pelo_usuario) != 11:
                print('\nErro: Um CPF deve conter exatamente 11 numeros...')
                continue
            
            print()
            print(validador_de_cpf(cpf__enviado_pelo_usuario))
            continue
        else:
            print('Alternativa invalida, escolha uma das opcoes disponiveis por favor (1 ou 2)...')
    
    # Tratamento de erros para entradas nao numericas ou interrupcoes
    except ValueError:
        print()
        print('Erro: Voce precisa digitar numeros inteiros...')
    except KeyboardInterrupt:
        print()
        print('Programa encerrado pelo usuario...')
        break
    except IndexError:
        print('\nErro: O formato do CPF e invalido ou esta muito curto...')