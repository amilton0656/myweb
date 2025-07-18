// Espera o HTML ser totalmente carregado para executar o script
document.addEventListener('DOMContentLoaded', () => {

    const video = document.getElementById('meuVideo');
    const listaDialogo = document.getElementById('lista-dialogo');
    let pontoDeParada;
    let linhaAtiva = null;

    // Adiciona UM único 'ouvinte' de evento para toda a lista
    listaDialogo.addEventListener('click', (evento) => {
        // Verifica se o elemento clicado foi um botão
        if (evento.target.classList.contains('btn-play')) {
            const botao = evento.target;
            const inicio = parseFloat(botao.dataset.inicio);
            const fim = parseFloat(botao.dataset.fim);

            // Encontra o elemento <li> pai do botão
            const linhaAtual = botao.closest('.linha-dialogo');

            // Remove o destaque da linha anteriormente ativa
            if (linhaAtiva) {
                linhaAtiva.classList.remove('active');
            }

            // Adiciona o destaque à nova linha e a armazena
            linhaAtual.classList.add('active');
            linhaAtiva = linhaAtual;

            // Rola a página para centralizar la linha ativa
            linhaAtual.scrollIntoView({ behavior: 'smooth', block: 'center' });

            reproduzirTrecho(inicio, fim);
        }
    });

    function reproduzirTrecho(inicio, fim) {
        pontoDeParada = fim;
        video.currentTime = inicio;
        video.play();
    }

    video.addEventListener('timeupdate', () => {
        if (pontoDeParada && video.currentTime >= pontoDeParada) {
            video.pause();
            pontoDeParada = undefined;

            // Remove o destaque quando o trecho termina
            if (linhaAtiva) {
                linhaAtiva.classList.remove('active');
                linhaAtiva = null;
            }
        }
    });
});