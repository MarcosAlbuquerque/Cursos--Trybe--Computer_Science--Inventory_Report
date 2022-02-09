from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import json
import xmltodict


class Inventory:
    def import_data(path, type):
        name_file = path.split('.')
        # print(name_file[1])  # extensão do arquivo

        with open(path) as file:
            if(name_file[1] == 'csv'):
                csv_file = list(csv.DictReader(file))

                if(type == 'simples'):
                    return SimpleReport.generate(csv_file)
                if(type == 'completo'):
                    return CompleteReport.generate(csv_file)

            elif(name_file[1] == 'json'):
                json_file = json.loads(file.read())

                if(type == 'simples'):
                    return SimpleReport.generate(json_file)
                if(type == 'completo'):
                    return CompleteReport.generate(json_file)

            elif(name_file[1] == 'xml'):
                xml_file = xmltodict.parse(file.read())
                # xml_file = list(dict(file.getroot()))

                if(type == 'simples'):
                    return SimpleReport.generate(xml_file)
                if(type == 'completo'):
                    return CompleteReport.generate(xml_file)
