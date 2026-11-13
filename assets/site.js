// Escola do Bolso · comportamento dos botões de compra enquanto o checkout não existe
  // Enquanto o checkout não estiver configurado, os botões com href="#breve" mostram um aviso.
  // Para abrir as vendas, troque o href="#breve" de cada botão pelo link do checkout (veja o README).
  document.querySelectorAll('a.comprar[href="#breve"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      e.preventDefault();
      document.getElementById('breve-produto').textContent = a.dataset.produto || 'Este material';
      var d = document.getElementById('breve');
      if (d.showModal) d.showModal(); else alert('As vendas abrem em breve.');
    });
  });
