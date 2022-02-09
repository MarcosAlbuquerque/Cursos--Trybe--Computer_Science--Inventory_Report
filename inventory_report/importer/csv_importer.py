# from inventory_report.importer.importer import Importer
# import csv


# class CsvImporter(Importer):
#     @classmethod
#     def import_data(cls, path):
#         if path.endswith(".csv"):
#             data = []
#             with open(path) as arquivo_csv:
#                 reader = csv.DictReader(arquivo_csv)
#                 data = []
#                 for row in reader:
#                     data.append(row)
#                 return data
#         else:
#             raise ValueError("Arquivo inválido")
