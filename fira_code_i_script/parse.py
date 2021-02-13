import xml.etree.ElementTree

def parse(file_path):
    # Open original file
    et = xml.etree.ElementTree.parse(file_path)
    root = et.getroot()
    namerecords = root.findall('./name/namerecord')
    project_authors_namerecords = [namerecord for namerecord in namerecords if namerecord.text.__contains__("Project Authors")]
    font_name_namerecords = [namerecord for namerecord in namerecords if namerecord.text.__contains__("Fira Code")]
    website_namerecords = [namerecord for namerecord in namerecords if namerecord.text.__contains__("https://tonsky.me")]
    fira_mono_trademark_namerecords = [namerecord for namerecord in namerecords if namerecord.text.__contains__("Fira Mono is a trademark of The Mozilla Corporation.")]
    typeface_namerecords = [namerecord for namerecord in namerecords if (namerecord.text.__contains__("Bold") or namerecord.text.__contains__("Regular")) and not namerecord.text.__contains__("Fira")]
    compact_font_name_namerecords = [namerecord for namerecord in namerecords if namerecord.text.__contains__("FiraCode") and not project_authors_namerecords.__contains__(namerecord)]
    for namerecord in namerecords:
        print(namerecord.text)
    pass

    # # Append new tag: <a x='1' y='abc'>body text</a>
    # new_tag = xml.etree.ElementTree.SubElement(et.getroot(), 'a')
    # new_tag.text = 'body text'
    # new_tag.attrib['x'] = '1' # must be str; cannot be an int
    # new_tag.attrib['y'] = 'abc'

    # # Write back to file
    # #et.write('file.xml')
    # et.write('file_new.xml')