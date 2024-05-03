import flet as ft
from bs4 import BeautifulSoup as bs
import requests

url = 'https://www.loteriaseresultados.com.br/index.php/mega-sena/concurso'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

site = requests.get(url,headers=headers)
soup = bs(site.content,'html.parser')


def main(page: ft.Page):
    page.title = "Só ganha quem joga"
    def busca_web():
    
        pass
        



    txt_titulo = ft.Text('Adicione o numero do concurso: ')
    valor_concurso = ft.TextField(label="Digite o numero do concurso",text_align=ft.TextAlign.RIGHT)
    txt_numero = ft.Text('Números do seu jogo:')
    valor_jogo = ft.TextField(label="Digite o numero do seu jogo",text_align=ft.TextAlign.RIGHT)
    btn_busca = ft.ElevatedButton("Buscar Resultado",on_click=busca_web)

    page.add(
    txt_titulo,
    valor_concurso,
    txt_numero,
    valor_jogo,
    btn_busca

    )
    pass

ft.app(target=main)