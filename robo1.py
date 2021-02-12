"""importando bibliotecas do selenium"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import xlrd

print("Iniciando nosso robô... \n")
dominios = []
"""escrevendo num arquivo"""
arquivo = open("resultado.txt","w")
"""lendo arquivo excell"""
workbook = xlrd.open_workbook('/Users/3AM IT/Robos/dominios.xlsx')
"""aqui nós referenciamos a planilha dentro do arquivo
caso o arquivo tiver mais que uma planilha use o index para fazer a referencia
no caso abaixo estamos referenciando a 1 planilha"""
sheet = workbook.sheet_by_index(0)

for linha in range(0,8):
    for coluna in range(0,2):
        print(sheet.cell_value(linha,coluna))
        dominios.append(sheet.cell_value(linha,coluna))

"""carregando o driver do chrome"""
driver = webdriver.Chrome('/Users/3AM IT/Robos/chromedriver.exe')
"""entrando no site"""
driver.get("https://registro.br/")

for dominio in dominios:
    pesquisa = driver.find_element_by_id("is-avail-field")
    """importante localizar o elemento pelo id
    inspecione o pagina web e localize"""
    pesquisa.clear()
    """limpa se estiver preenchido"""
    pesquisa.send_keys(dominio)
    """preenchendo o campo"""
    pesquisa.send_keys(Keys.RETURN)
    """a propriedade RETURN implica no envio do <enter> para obter uma resposta"""
    """controlando o tempo de abertura do site"""
    time.sleep(2)
    resultados = driver.find_elements_by_tag_name("strong")

    texto = ("Dominio %s %s\n" % (dominio, resultados[4].text))
    arquivo.write(texto)

arquivo.close()
driver.close()





