"""Gera termos.html e privacidade.html com o mesmo cabeçalho e rodapé do site.
Uso: python gerar_paginas_legais.py   (rode de novo depois de mudar os dados da empresa abaixo)"""
from pathlib import Path

EMPRESA = "IACAO TEC PORTAIS DE CONTEUDO NA INTERNET LTDA"
CNPJ = "68.297.061/0001-04"
ENDERECO = "Rua Pais Leme, 215, conj. 1713, Pinheiros, São Paulo/SP, CEP 05424-150"
EMAIL = "contato@escoladobolso.com.br"
AQUI = Path(__file__).resolve().parent

MODELO = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} · Escola do Bolso</title>
<meta name="robots" content="noindex">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>

<header>
  <div class="wrap bar">
    <a class="logo" href="index.html" aria-label="Escola do Bolso, início"><img src="assets/icone.svg" alt=""><span>Escola do <b>Bolso</b></span></a>
    <nav aria-label="Principal">
      <a class="btn btn-green" href="index.html#kit">Ver os materiais</a>
    </nav>
  </div>
</header>

<main class="wrap doc">
{corpo}
  <a class="voltar" href="index.html">&lt; Voltar ao início</a>
</main>

<footer>
  <div class="wrap">
    <a class="logo" href="index.html"><img src="assets/icone.svg" alt=""><span>Escola do <b>Bolso</b></span></a>
    <p>Material educativo. Não é recomendação de investimento, consultoria financeira nem consultoria tributária.</p>
    <p class="empresa">Escola do Bolso é uma marca de {empresa} · CNPJ {cnpj} · {endereco} ·
      <a href="mailto:{email}">{email}</a></p>
    <p class="legal"><a href="termos.html">Termos de uso</a> · <a href="privacidade.html">Política de privacidade</a></p>
    <p>© Escola do Bolso</p>
  </div>
</footer>
</body>
</html>
"""

TERMOS = """  <h1>Termos de uso</h1>
  <p>Estes termos valem para o site da Escola do Bolso e para os materiais vendidos ou oferecidos de graça nele.
  Ao comprar ou baixar um material, você concorda com eles.</p>

  <h2>1. Quem somos</h2>
  <p>A Escola do Bolso é uma marca de {empresa}, CNPJ {cnpj}, com sede na {endereco}. Fale com a gente pelo
  e-mail <a href="mailto:{email}">{email}</a>.</p>

  <h2>2. O que oferecemos</h2>
  <p>Materiais digitais de educação financeira: planilhas de Excel e guias em PDF. Cada material é entregue em
  arquivo, para uso pessoal. Não há aulas ao vivo, acompanhamento individual nem atualização automática dos
  arquivos.</p>

  <h2>3. Conteúdo educativo, não recomendação</h2>
  <p>Os materiais ensinam a entender e a fazer contas com o seu dinheiro. Eles não são recomendação de
  investimento, consultoria financeira, tributária ou jurídica, e não indicam produtos, ativos nem
  instituições. Os exemplos usam valores ilustrativos e não garantem resultados. Regras de imposto e leis mudam:
  antes de decidir, confirme as regras em vigor. As decisões tomadas com base nos materiais são de quem as toma.</p>

  <h2>4. Compra, pagamento e entrega</h2>
  <ul>
    <li>Os preços são os mostrados no site no momento da compra.</li>
    <li>O pagamento é processado pela plataforma de pagamento parceira, que segue os próprios termos. Não
    recebemos nem guardamos dados de cartão.</li>
    <li>Depois da confirmação do pagamento, você recebe por e-mail o acesso para baixar os arquivos.</li>
  </ul>

  <h2>5. Direito de arrependimento</h2>
  <p>Você pode desistir da compra em até 7 dias a partir da data da compra, sem precisar explicar o motivo,
  como garante o artigo 49 do Código de Defesa do Consumidor. Peça pelo e-mail
  <a href="mailto:{email}">{email}</a> ou pela plataforma de pagamento. O valor é devolvido integralmente, pelo
  mesmo meio usado no pagamento.</p>

  <h2>6. Material gratuito</h2>
  <p>O material 1, Renda Líquida Real, é gratuito e pode ser baixado direto no site. Ele segue as mesmas regras de
  uso dos materiais pagos.</p>

  <h2>7. Uso permitido</h2>
  <p>Cada compra dá a você uma licença pessoal e intransferível para usar os arquivos. É proibido revender,
  compartilhar, publicar ou distribuir os arquivos, inteiros ou em partes, de graça ou não. Os textos, as
  planilhas, os guias e a marca Escola do Bolso pertencem à {empresa}.</p>

  <h2>8. Mudanças nestes termos</h2>
  <p>Podemos atualizar estes termos. A versão que vale é sempre a publicada nesta página; compras já feitas
  seguem os termos da data da compra.</p>

  <h2>9. Foro</h2>
  <p>Fica eleito o foro do domicílio do consumidor, como prevê o Código de Defesa do Consumidor.</p>
"""

PRIVACIDADE = """  <h1>Política de privacidade</h1>
  <p>Esta política explica quais dados pessoais a Escola do Bolso trata, para quê e quais são os seus direitos,
  de acordo com a Lei Geral de Proteção de Dados (Lei 13.709).</p>

  <h2>1. Quem cuida dos seus dados</h2>
  <p>O controlador dos dados é {empresa}, CNPJ {cnpj}, com sede na {endereco}, dona da marca Escola do Bolso.
  Para qualquer assunto sobre os seus dados, escreva para <a href="mailto:{email}">{email}</a>.</p>

  <h2>2. Que dados tratamos</h2>
  <ul>
    <li><b>Ao comprar:</b> nome, e-mail, CPF e dados do pedido, informados na plataforma de pagamento. Os dados de
    cartão ficam só com a plataforma; não os recebemos.</li>
    <li><b>Ao se inscrever para receber dicas:</b> o seu e-mail.</li>
    <li><b>Ao falar com a gente:</b> o que você escrever no e-mail.</li>
    <li><b>Ao navegar no site:</b> dados de acesso, como páginas visitadas, de onde veio a visita e tipo de
    aparelho, usados de forma agregada para medir o alcance do site.</li>
  </ul>
  <p>O download do material gratuito não exige cadastro.</p>

  <h2>3. Para que usamos e com qual base legal</h2>
  <ul>
    <li><b>Entregar o que você comprou e dar suporte:</b> execução do contrato.</li>
    <li><b>Emitir nota fiscal e cumprir obrigações fiscais:</b> cumprimento de obrigação legal.</li>
    <li><b>Enviar dicas e novidades por e-mail:</b> o seu consentimento, que você pode retirar a qualquer
    momento pelo link de descadastro em cada e-mail.</li>
    <li><b>Medir e melhorar o site:</b> legítimo interesse, com dados agregados.</li>
  </ul>

  <h2>4. Com quem compartilhamos</h2>
  <p>Só com quem precisa dos dados para o serviço funcionar: a plataforma de pagamento, a ferramenta de envio
  de e-mail, a hospedagem do site, a ferramenta de medição de acessos e a contabilidade. Não vendemos dados
  pessoais.</p>

  <h2>5. Por quanto tempo guardamos</h2>
  <p>Dados de compra, pelo prazo exigido pela lei fiscal. O e-mail da lista de dicas, até você se descadastrar.
  Mensagens de suporte, enquanto forem necessárias para atender você.</p>

  <h2>6. Seus direitos</h2>
  <p>Você pode pedir, a qualquer momento: confirmação de que tratamos os seus dados, acesso a eles, correção,
  anonimização, portabilidade, eliminação dos dados tratados com base no consentimento, informação sobre com
  quem compartilhamos e a retirada do consentimento. Peça pelo e-mail <a href="mailto:{email}">{email}</a>.
  Você também pode reclamar à Autoridade Nacional de Proteção de Dados (ANPD).</p>

  <h2>7. Segurança</h2>
  <p>Usamos fornecedores reconhecidos, acesso restrito às contas e verificação em duas etapas para proteger os
  dados.</p>

  <h2>8. Público</h2>
  <p>Os materiais são feitos para estudantes e recém-formados. Compras devem ser feitas por maiores de 18 anos ou
  com a autorização de um responsável.</p>

  <h2>9. Mudanças nesta política</h2>
  <p>Podemos atualizar esta política. A versão que vale é sempre a publicada nesta página.</p>
"""

dados = dict(empresa=EMPRESA, cnpj=CNPJ, endereco=ENDERECO, email=EMAIL)
for nome, titulo, corpo in (("termos.html", "Termos de uso", TERMOS), ("privacidade.html", "Política de privacidade",
                                                                     PRIVACIDADE)):
    (AQUI / nome).write_text(MODELO.format(titulo=titulo, corpo=corpo.format(**dados), **dados), encoding="utf-8")
    print("salvo:", nome)
