from inventory_report.importer.importer import Importer
import xml.etree.ElementTree as ET


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if path.endswith(".xml"):
            list = []
            tree = ET.parse(path)
            result = tree.getroot()

            for item in result:
                list_of_objects = {}
                for item in item:
                    list_of_objects[item.tag] = item.text
                list.append(list_of_objects)
                return list
        else:
            raise ValueError("Arquivo inválido")
