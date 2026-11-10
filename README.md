# Site da Escola do Bolso (repositório público)

Página única de vendas, servida pelo GitHub Pages a partir da raiz deste repositório.

- `index.html`: a página (abertura, como funciona, os cinco materiais, kit, por dentro, dúvidas).
- `assets/site.css`: estilos. Cores da marca no topo do arquivo (`:root`).
- `assets/icone.svg` e `assets/favicon.svg`: logo (moeda entrando no bolso).
- `assets/img/`: capas e páginas dos guias, geradas a partir dos PDFs.
- `.nojekyll`: faz o Pages servir os arquivos como estão.

Este repositório é público: não coloque aqui os arquivos dos produtos pagos. O botão de compra aponta para o
checkout externo, que cobra e entrega o arquivo.

## Abrir as vendas

Cada botão de compra está assim em `index.html`:

```html
<a class="btn btn-green comprar" href="#breve" data-produto="Renda líquida real">Comprar</a>
```

Enquanto o `href` for `#breve`, o botão mostra o aviso "As vendas abrem em breve". Para vender, troque `#breve`
pelo link de checkout do produto (Hotmart, Kiwify ou Eduzz). São seis botões: um por material e o do kit.

## Trocar preços

Os preços aparecem como texto em `index.html`: `R$ 19,90` (cada material), `R$ 67` (kit), `R$ 99,50` (soma dos
avulsos) e `R$ 32,50` (economia). Use buscar e substituir. O preço cobrado de verdade é o do checkout.

## Ver no computador

```
python -m http.server 8765 --directory .
```

Depois abra http://localhost:8765.

## Publicar

1. Enviar este repositório para a organização da marca no GitHub.
2. Em Settings > Pages, escolher a branch `main` e a pasta `/ (root)`.
3. Depois de registrar o domínio, informá-lo em Settings > Pages > Custom domain.
