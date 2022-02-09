from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as xmlFile


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".xml"):
            list = []
            tree = xmlFile.parse(path)
            result = tree.getroot()

            for item in result:
                listaDeObjetos = {}
                for item in item:
                    listaDeObjetos[item.tag] = item.text
                list.append(listaDeObjetos)
                return list
        else:
            raise ValueError("Arquivo inválido")
