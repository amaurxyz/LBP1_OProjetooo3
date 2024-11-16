document.addEventListener('DOMContentLoaded', () => {
    const openModalBtns = document.querySelectorAll('.open-modal-btn');
    const closeModalBtn = document.querySelector('#closeModal');
    const modal = document.querySelector('#myModal');
    const modalNome = document.querySelector('#modal-nome');
    const modalDescricao = document.querySelector('#modal-descricao');

    // Adicionar evento para abrir o modal e exibir informações do produto
    openModalBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const nome = btn.getAttribute('data-nome');
            const descricao = btn.getAttribute('data-descricao');

            modalNome.textContent = nome;
            modalDescricao.textContent = descricao;
            modal.style.display = 'flex';
        });
    });

    // Fechar modal ao clicar no botão de fechar
    closeModalBtn.addEventListener('click', () => {
        modal.style.display = 'none';
    });

    // Fechar modal ao clicar fora do conteúdo
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.style.display = 'none';
        }
    });
});