const themeToggleElement = document.getElementsByClassName('theme-toggle')[0]

if (!localStorage.getItem('theme')) {
    const theme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
    localStorage.setItem('theme', theme)
}

if (localStorage.getItem('theme') == 'dark') {
    themeToggleElement.children[0].classList.add('hide')
    themeToggleElement.children[1].classList.remove('hide')

    document.documentElement.setAttribute('data-theme', 'dark')
}

const toggleTheme = () => {
    for (let i = 0; i < themeToggleElement.childElementCount; i++) {
        // Change icon
        if (themeToggleElement.children[i].classList.contains('hide')) {
            themeToggleElement.children[i].classList.remove('hide')
        } else {
            themeToggleElement.children[i].classList.add('hide')
        }
    }
    const theme = localStorage.getItem('theme') == 'light' ? 'dark' : 'light'
    document.documentElement.setAttribute('data-theme', theme)
    localStorage.setItem('theme', theme)
}

const toggleVuln = (element) => {
    element.getElementsByClassName('vuln-content')[0].classList.toggle('hide-row');
}

const sortTable = (n) => {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("table-body");
    switching = true;
    dir = "asc";
    while (switching) {
        switching = false;
        rows = table.rows;
        for (i = 0; i < (rows.length - 1); i++) {
            shouldSwitch = false;
            x = rows[i].getElementsByTagName("TD")[n];
            y = rows[i + 1].getElementsByTagName("TD")[n];
            if (dir == "asc") {
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            } else if (dir == "desc") {
                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            switchcount ++;
        } else {
            if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
            }
        }
    }
}