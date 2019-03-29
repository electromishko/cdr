# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
class pars:

    def parseXML(self, xml_file, version):
        newver = version
        tree = ET.parse(xml_file)
        root = tree.getroot()
        root.set('version', str(newver))
        tree.write('up.xml', encoding="UTF-8")

    #
    # if __name__ == "__main__":
    #     parseXML("SSW4config/482-nover.xml")