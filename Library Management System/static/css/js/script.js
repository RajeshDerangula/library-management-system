function searchBooks() {
    const input = document.getElementById('search').value.toLowerCase();
    const rows = document.querySelectorAll('#books-table tbody tr');
    rows.forEach(row => {
        const title = row.cells[1].textContent.toLowerCase();
        const author = row.cells[2].textContent.toLowerCase();
        if (title.includes(input) || author.includes(input)) {
            row.style.display = '';
        } else {
            row.style.display = 'none';
        }
    });
}

// Load dashboard data on index page
window.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('total-books')) {
        fetch('/api/books')
            .then(res => res.json())
            .then(data => {
                document.getElementById('total-books').textContent = data.length;
                document.getElementById('available-books').textContent = data.filter(b => b.available).length;
            });
    }
});
