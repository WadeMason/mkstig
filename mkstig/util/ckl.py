from xml.etree.ElementTree import Element, parse as parseXml

class Checklist:
    summary = {
        'not_reviewed': 0,
        'open': 0,
        'notafinding': 0,
        'not_applicable': 0,
    }
    asset = {}
    stig = {}
    vulns = []

def parse(ckl_path: str) -> Checklist:
    tree = parseXml(ckl_path)
    root = tree.getroot()

    checklist = Checklist()

    # Asset info
    for child in root[0]:
        checklist.asset[child.tag.lower()] = child.text or ''

    # STIG info
    for child in root.findall('STIGS/iSTIG/STIG_INFO/SI_DATA'):
        sid_name = child.find('SID_NAME')
        sid_data = child.find('SID_DATA')
        if type(sid_name) is Element and type(sid_data) is Element:
            checklist.stig[str(sid_name.text).lower()] = sid_data.text or ''

    # Vuln info
    for vuln in root.findall('STIGS/iSTIG/VULN'):
        vulnerability = {}
        for child in vuln:
            if child.tag == 'STIG_DATA':
                vuln_attr = child.find('VULN_ATTRIBUTE')
                attr_data = child.find('ATTRIBUTE_DATA')
                if type(vuln_attr) is Element and type(attr_data) is Element:
                    vulnerability[str(vuln_attr.text).lower()] = attr_data.text or ''
            else:
                vulnerability[child.tag.lower()] = child.text or ''
        checklist.vulns.append(vulnerability)
        checklist.summary[str(vulnerability['status']).lower()] += 1
    
    return checklist