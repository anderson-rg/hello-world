import os

# meus_resultados = os.listdir('C:\\Users\\AndersonGuilherme\\Desktop\\testes')


def deletar_arquivos(cep):
    meus_resultados = os.listdir('C:\\Users\\AndersonGuilherme\\Desktop\\testes')

    for resultado in meus_resultados:

        if resultado.endswith('.txt'):
            try:
                os.remove('C:\\Users\\AndersonGuilherme\\Desktop\\testes\\' +resultado)
            except OSError as e:
                print(e)
    validation_list = executar_arquivo(cep)

    return validation_list


def executar_arquivo(cep):

    os.system('call "C:\\Program Files\\SmartBear\\SoapUI-5.6.0\\bin\\testrunner.bat" -Gcep=' + cep + ' -r -a -fC:\\Users\\AndersonGuilherme\\Desktop\\testes C:\\Users\\AndersonGuilherme\\Documents\\Projeto-Cep-soapui-project.xml')
    vvv = validar_arquivos()
    return vvv

def validar_arquivos():
    meus_resultados = os.listdir('C:\\Users\\AndersonGuilherme\\Desktop\\testes')
    val_list = []

    for resultado in meus_resultados:


        if 'OK' in resultado:
             result = {
                resultado: 'Passed'
            }

        elif 'UNKNOWN' in resultado:
            result = {
                resultado: 'Missing Assertion'
            }

        else:
            result = {
                resultado: '-Failed.'
            }

        val_list.append(result)
    print(val_list)

    return val_list

# deletar_arquivos('13504056')