# from inventory_report.importer.importer import Importer
# import json


# class JsonImporter(Importer):
#     @classmethod
#     def import_data(cls, path):
#         if path.endswith(".json"):
#             with open(path) as arquivo_json:
#                 content = arquivo_json.read()
#                 result = json.loads(content)
#             return result
#         else:
#             raise ValueError("Arquivo inválido")
