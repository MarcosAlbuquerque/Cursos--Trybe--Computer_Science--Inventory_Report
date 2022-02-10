from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.xml_reader import Reader
import csv
import json


class Inventory:
    def import_data(path, type):
        name_file = path.split('.')

        with open(path, 'r') as file:
            if(name_file[1] == 'csv'):
                return csv_file(file, type)

            elif(name_file[1] == 'json'):
                return json_file(file, type)

            elif(name_file[1] == 'xml'):
                return xml_file(file, type)


def csv_file(file, type):
    csv_file = list(csv.DictReader(file))

    if(type == 'simples'):
        return SimpleReport.generate(csv_file)
    if(type == 'completo'):
        return CompleteReport.generate(csv_file)


def json_file(file, type):
    json_file = json.loads(file.read())

    if(type == 'simples'):
        return SimpleReport.generate(json_file)
    if(type == 'completo'):
        return CompleteReport.generate(json_file)


def xml_file(file, type):
    xml_file = Reader.read_xml(file)
    if(type == 'simples'):
        return SimpleReport.generate(xml_file)
    if(type == 'completo'):
        return CompleteReport.generate(xml_file)


# def xml_file(file, type):
#     xml_file = xmltodict.parse(file.read())
#     if(type == 'simples'):
#         return SimpleReport.generate(xml_file)
#     if(type == 'completo'):
#         return CompleteReport.generate(xml_file)
