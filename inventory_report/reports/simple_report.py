from datetime import date


class SimpleReport:
    def generate(list):
        current_date = date.today()

        older = min([data["data_de_fabricacao"] for data in list])

        nearest = min(
            [
                data["data_de_validade"]
                for data in list
                if data["data_de_validade"] > str(current_date)
            ]
        )

        greatest_stock = max([empresa["nome_da_empresa"] for empresa in list])

        return (
            f"Data de fabricação mais antiga: {older}\n"
            f"Data de validade mais próxima: {nearest}\n"
            "Empresa com maior quantidade de produtos "
            f"estocados: {greatest_stock}\n"
        )
