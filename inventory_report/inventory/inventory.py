from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv


class Inventory:
    def import_data(path, type):
        with open(path) as file:
            csv_file = list(csv.DictReader(file))

            if(type == 'simples'):
                return SimpleReport.generate(csv_file)
            if(type == 'completo'):
                return CompleteReport.generate(csv_file)
