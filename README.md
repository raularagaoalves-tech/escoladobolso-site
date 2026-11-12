# Site da Escola do Bolso (repositório público)

Página única de vendas, servida pelo GitHub Pages a partir da raiz deste repositório.

- `index.html`: a página (abertura, como funciona, os oito materiais, kit, por dentro, dúvidas).
- `assets/site.css`: estilos. Cores da marca no topo do arquivo (`:root`).
- `assets/icone.svg` e `assets/favicon.svg`: logo (moeda entrando no bolso).
- `assets/img/`: capas e páginas dos guias, geradas a partir dos PDFs.
- `assets/gratis/`: o material 1 (guia + planilha em zip), que é gratuito e baixado direto do site.
- `.nojekyll`: faz o Pages servir os arquivos como estão.

Este repositório é público: não coloque aqui os arquivos dos produtos pagos (materiais 2 a 8). Só o material 1, gratuito, fica aqui. O botão de compra aponta para o
checkout externo, que cobra e entrega o arquivo.

## Abrir as vendas

Cada botão de compra está assim em `index.html`:

```html
<a class="btn btn-green comprar" href="#breve" data-produto="Renda líquida real">Comprar</a>
```

Enquanto o `href` for `#breve`, o botão mostra o aviso "As vendas abrem em breve". Para vender, troque `#breve`
pelo link de checkout do produto (Hotmart, Kiwify ou Eduzz). São oito botões: um por material pago (2 a 8) e o do kit.

O material 1 não passa pelo checkout: o botão "Baixar grátis" aponta para `assets/gratis/Renda-Liquida-Real-gratis.zip`.
Se o material 1 mudar, gere o zip de novo com o guia e a planilha atualizados.

## Trocar preços

Os preços aparecem como texto em `index.html`: `Grátis` (material 1), `R$ 15` (materiais 2, 7 e 8),
`R$ 20` (materiais 3 e 4), `R$ 25` (materiais 5 e 6), `R$ 90` (kit), `R$ 135` (soma dos avulsos) e a economia do
kit (`R$ 45`). Como há preços repetidos, troque card a card, pelo `data-produto` do botão. O preço cobrado de verdade é o do checkout.

## Ver no computador

```
python -m http.server 8765 --directory .
```

Depois abra http://localhost:8765.

## Publicar

1. Enviar este repositório para a organização da marca no GitHub.
2. Em Settings > Pages, escolher a branch `main` e a pasta `/ (root)`.
3. Depois de registrar o domínio, informá-lo em Settings > Pages > Custom domain.
