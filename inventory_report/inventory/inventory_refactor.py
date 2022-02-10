from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, type):
        Reportdata = self.importer.import_data(path)

        self.data.extend(Reportdata)

        if type == "simples":
            return SimpleReport.generate(Reportdata)
        elif type == "completo":
            return CompleteReport.generate(Reportdata)

    def __iter__(self):
        iterador = InventoryIterator(self.lista)
        return iterador
        return InventoryIterator(self.data)
