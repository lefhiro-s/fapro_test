from bs4 import BeautifulSoup

class UFParser:
    def parse_uf(self, html, date):
        soup = BeautifulSoup(html, 'html.parser')
        div_mes_all = soup.find('div', {'id': 'mes_all'})
        table = div_mes_all.find('table', {'id': 'table_export'})
        if not table:
            return None

        day = date.day
        month = date.month

        for row in table.find_all('tr')[1:]:  # Ignora el encabezado de la tabla
            day_cell, *month_cells = row.find_all(['th', 'td'])

            try:
                current_day = int(day_cell.get_text(strip=True))
            except ValueError:
                # Ignora las filas que no contienen un número de día válido
                continue

            if current_day == day:
                uf_value = month_cells[month - 1].get_text(strip=True)
                uf_value = uf_value.replace('.', '').replace(',', '.')
                return float(uf_value)

        return None
