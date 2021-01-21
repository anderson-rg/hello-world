import os

meus_resultados = os.listdir('C:\\Users\\AndersonGuilherme\\Desktop\\testes')


validation_list = []

def deletar_arquivos():
    meus_resultados = os.listdir('C:\\Users\\AndersonGuilherme\\Desktop\\testes')

    for resultado in meus_resultados:


        if resultado.endswith('.txt'):
            try:
                os.remove("C:\\Users\\AndersonGuilherme\\Desktop\\testes\\" + resultado)
            except OSError as e:
                print(e)


deletar_arquivos()
