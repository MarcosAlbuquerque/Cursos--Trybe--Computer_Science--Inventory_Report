from inventory_report.reports.simple_report import SimpleReport


class CompleteReport:
    def generate(list):
        return list_report(list)


def products_count(list):
    companies = [company["nome_da_empresa"] for company in list]
    filter_by_companies = {count: 0 for count in companies}
    for company in list:
        count = company["nome_da_empresa"]
        filter_by_companies[count] += 1
    return filter_by_companies


def list_report(list):
    simple_report = SimpleReport.generate(list)
    count_products = products_count(list)
    output = f"{simple_report}\nProdutos estocados por empresa: \n"
    for company in count_products:
        output += f"- {company}: {count_products[company]}\n"
    return output
