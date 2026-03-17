import random

def gerar_novo_cpf_valido():

    cpf = ''

    # Gera 9 numeros aleatorios para o CPF
    for n in range(9):
        novo_numero = str(random.randint(0, 9))
        cpf += novo_numero

    # Gerando o primeiro digito verificador (10º numero)

    lista_de_pesos_1 = []
    soma_de_tudo_1 = 0
    primeiro_digito_verificador = 0

    for n in range(10, 1, -1):
        lista_de_pesos_1.append(n)

    for n in range(9):
        valor_do_cpf_1 = int(cpf[n])
        valor_do_peso_1 = lista_de_pesos_1[n]
        resultado_1 = valor_do_cpf_1 * valor_do_peso_1
        soma_de_tudo_1 += resultado_1

    if soma_de_tudo_1 % 11 == 0 or soma_de_tudo_1 % 11 == 1:
        primeiro_digito_verificador = 0
    else:
        primeiro_digito_verificador = 11 - (soma_de_tudo_1 % 11)

    # Transformo o primeiro digito verificador de int para str, visando adiciona-lo aos 9 numeros iniciais do CPF

    primeiro_digito_verificador = str(primeiro_digito_verificador)
    cpf = cpf + primeiro_digito_verificador

    # Gerando o segundo digito verificador (11º numero)

    lista_de_pesos_2 = []
    soma_de_tudo_2 = 0
    segundo_digito_verificador = 0

    for n in range(11, 1, -1):
        lista_de_pesos_2.append(n)

    for n in range(10):
        valor_do_cpf_2 = int(cpf[n])
        valor_do_peso_2 = lista_de_pesos_2[n]
        resultado_2 = valor_do_cpf_2 * valor_do_peso_2
        soma_de_tudo_2 += resultado_2        

    if soma_de_tudo_2 % 11 == 0 or soma_de_tudo_2 % 11 == 1:
        segundo_digito_verificador = 0
    else:
        segundo_digito_verificador = 11 - (soma_de_tudo_2 % 11)

    # Transformo o segundo digito verificador de int para str, visando adiciona-lo aos 10 numeros que temos no momento do CPF

    segundo_digito_verificador = str(segundo_digito_verificador)
    cpf = cpf + segundo_digito_verificador

    # Formato o CPF para o padrao (xxx.xxx.xxx-xx)

    cpf_formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    return cpf_formatado

def validador_de_cpf(cpf):
    cpf = str(cpf)
    validacao_do_primeiro_digito = False
    validacao_do_segundo_digito = True

    cpf_com_9_digitos = cpf[:-2]
    lista_de_pesos_3 = []

    for n in range(10, 1, -1):
        lista_de_pesos_3.append(n)

    soma_total_validador = 0

    for n in range(9):
        valor_do_cpf_3 = int(cpf_com_9_digitos[n])
        valor_do_peso_3 = lista_de_pesos_3[n]
        resultado_3 = valor_do_cpf_3 * valor_do_peso_3
        soma_total_validador += resultado_3

    if soma_total_validador % 11 == 0 or soma_total_validador % 11 == 1:
        if cpf[9] != '0':
            return 'CPF invalido!'
        else:
            validacao_do_primeiro_digito = True
    elif soma_total_validador % 11 == 2 or soma_total_validador % 11 == 3 or soma_total_validador % 11 == 4 or soma_total_validador % 11 == 5 or soma_total_validador % 11 == 6 or soma_total_validador % 11 == 7 or soma_total_validador % 11 == 8 or soma_total_validador % 11 == 9 or soma_total_validador % 11 == 10:
        if cpf[9] != str(11 - (soma_total_validador % 11)):
            return 'CPF invalido!'
        else:
            validacao_do_primeiro_digito = True
    
    cpf_com_10_digitos = cpf[:-1]
    lista_de_pesos_4 = []
    soma_total_validador_1 = 0

    for n in range(11, 1, -1):
        lista_de_pesos_4.append(n)

    for n in range(10):
        valor_do_cpf_4 = int(cpf_com_10_digitos[n])
        valor_do_peso_4 = lista_de_pesos_4[n]
        resultado_4 = valor_do_cpf_4 * valor_do_peso_4
        soma_total_validador_1 += resultado_4
    
    
    # resto_da_soma_total_1 = soma_total_validador_1 % 11
    # decimo_digito = 11 - resto_da_soma_total_1
    # print(resto_da_soma_total_1, decimo_digito)
    
    if soma_total_validador_1 % 11 == 0 or soma_total_validador_1 % 11 == 1:
        if cpf[10] != '0':
            return 'CPF invalido!'
        else:
            validacao_do_segundo_digito = True
    elif soma_total_validador_1 % 11 == 2 or soma_total_validador_1 % 11 == 3 or soma_total_validador_1 % 11 == 4 or soma_total_validador_1 % 11 == 5 or soma_total_validador_1 % 11 == 6 or soma_total_validador_1 % 11 == 7 or soma_total_validador_1 % 11 == 8 or soma_total_validador_1 % 11 == 9 or soma_total_validador_1 % 11 == 10:
        if cpf[10] != str(11 - (soma_total_validador_1 % 11)):
            return 'CPF invalido!'
        else:
            validacao_do_segundo_digito = True
    
    if validacao_do_primeiro_digito == True and validacao_do_segundo_digito == True:
        return 'CPF Valido!'

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
            print(f'CPF gerado: {gerar_novo_cpf_valido()}')
            continue
        elif resposta_do_usuario == 2:
            cpf__enviado_pelo_usuario = input('Digite o CPF que voce quer verificar, sem separacoes: ')
            if len(cpf__enviado_pelo_usuario) != 11:
                print('\nErro: Um CPF deve conter exatamente 11 numeros...')
            print()
            print(validador_de_cpf(cpf__enviado_pelo_usuario))
            continue
        else:
            print('Alternativa invalida, escolha uma das opcoes disponiveis por favor (1 ou 2)...')
    except ValueError:
        print()
        print('Erro: Voce precisa digitar numeros inteiros...')
    except KeyboardInterrupt:
        print()
        print('Programa encerrado pelo usuario...')
        break
    except IndexError:
        print('\nErro: O formato do CPF e invalido ou esta muito curto...')