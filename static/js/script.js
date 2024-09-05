document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.clickable-row').forEach(row => {
        row.addEventListener('click', () => {
            const nextRow = row.nextElementSibling;
            if (nextRow && nextRow.classList.contains('extra-options')) {
                nextRow.style.display = nextRow.style.display === 'none' ? 'table-row' : 'none';
            }
        });
    });
});
