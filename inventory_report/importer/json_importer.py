from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".json"):
            with open(path) as arquivo_json:
                conteudo = arquivo_json.read()
                resultado = json.loads(conteudo)
            return resultado
        else:
            raise ValueError("Arquivo inválido")
