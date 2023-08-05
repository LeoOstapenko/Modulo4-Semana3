from requests_html import HTMLSession

sessao = HTMLSession()
url = 'https://www.olx.com.br/eletronicos-e-celulares/estado-sp?q=iphone'
resposta = sessao.get(url)

anuncios = []

links = resposta.html.find('#ad-list li a')

for link in links:
    url_iphone = link.attrs['href']
    resposta_iphone = sessao.get(url_iphone)
    
    titulo = resposta_iphone.html.find('h1', first = True).text
    preco = resposta_iphone.html.find('h2')[-1].text
    
    anuncios.append({
        'URL': url_iphone,
        'TÍTULO': titulo,
        'PREÇO': preco
    })

print(anuncios)