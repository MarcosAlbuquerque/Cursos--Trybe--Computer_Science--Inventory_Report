import xml.etree.ElementTree as ET


class Reader:

    @staticmethod
    def read_xml(path):
        content = []
        root = ET.parse(path)
        xml_content = root.getroot()

        for record in xml_content:
            row = {}
            for record_row in record:
                row[record_row.tag] = record_row.text
                content.append(row)

        return content
