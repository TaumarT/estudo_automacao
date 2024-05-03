import requests
from lxml import html

# URL do resultado da Mega Sena no Google
url = 'https://www.google.com/search?q=mega+sena&sca_esv=8e68bf274b59ae51&sca_upv=1&sxsrf=ACQVn0_xany40ZNp1UeAemGLG-sRsTfj3Q%3A1714701681611&ei=cUU0Zov2JMiS5OUPsq6BsAY&udm=&ved=0ahUKEwjL8oLFsfCFAxVICbkGHTJXAGYQ4dUDCBA&uact=5&oq=mega+sena&gs_lp=Egxnd3Mtd2l6LXNlcnAiCW1lZ2Egc2VuYTIKECMYgAQYJxiKBTILEAAYgAQYsQMYgwEyChAAGIAEGEMYigUyDRAAGIAEGLEDGEMYigUyChAAGIAEGEMYigUyDhAAGIAEGLEDGIMBGIoFMgQQABgDMg4QABiABBixAxiDARiKBTIEEAAYAzIEEAAYA0iWD1AAWOUNcAB4AJABAJgBqgGgAZ4JqgEDMC45uAEDyAEA-AEBmAIJoAKSCsICERAuGIAEGLEDGNEDGIMBGMcBwgIOEC4YgAQYsQMYgwEYigXCAgQQIxgnwgIQEAAYgAQYsQMYQxiDARiKBcICCBAAGIAEGLEDwgIUEC4YgAQYsQMYgwEYxwEYjgUYrwHCAhMQLhiABBixAxjRAxhDGMcBGIoFmAMAkgcDMC45oAeXXA&sclient=gws-wiz-serp'

# Fazendo uma requisição GET para obter o conteúdo da página
response = requests.get(url)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Parseando o conteúdo HTML da página usando lxml
    tree = html.fromstring(response.content)
    
    # Encontrando o elemento usando o XPath fornecido
    resultado = tree.xpath('//*[@id="tsuid_26"]/span/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/text()')
    
    # Verificando se o resultado foi encontrado
    if resultado != ' ':
        # Convertendo a lista de resultados em uma string
        resultado_texto = ' '.join(resultado)
        print(resultado_texto)
    else:
        resultado_texto = "Resultado da Mega Sena não encontrado."
else:
    resultado_texto = "Erro ao obter o resultado da Mega Sena."

# Imprimindo o resultado ou fazendo o que desejar com ele
print(resultado_texto)
