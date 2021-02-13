import xml.etree.ElementTree
from pathlib import Path
from datetime import datetime, timezone

class Parse:
    def __init__(self) -> None:
        self.font_name = "Fira Code Script"
        self.compact_font_name = self.font_name.replace(' ', '')
        self.website = "kryptonunite.com"
        self.github_repo_owner = "DanielAtKrypton"
        self.organization_name = "Krypton Unite"
        self.timestamp = datetime.now(timezone.utc)
        self.italicStr = "Italic"
    def process_raw_font(self, file_path):
        filename = Path(file_path).stem
        typeface = filename.split('-')[1]
        # Open original file
        et = xml.etree.ElementTree.parse(file_path)
        root = et.getroot()
        namerecords = root.findall('./name/namerecord')
        project_authors_namerecords = [namerecord for namerecord in namerecords if namerecord.text.__contains__("Project Authors")]
        font_name_namerecords = [namerecord for namerecord in namerecords if namerecord.text.__contains__("Fira Code")]
        website_namerecords = [namerecord for namerecord in namerecords if namerecord.text.__contains__("https://tonsky.me")]
        fira_mono_trademark_namerecords = [namerecord for namerecord in namerecords if namerecord.text.__contains__("Fira Mono is a trademark of The Mozilla Corporation.")]
        typeface_namerecords = [namerecord for namerecord in namerecords if (namerecord.text.__contains__(typeface) or namerecord.text.__contains__("Regular")) and not namerecord.text.__contains__("Fira")]
        compact_font_name_namerecords = [namerecord for namerecord in namerecords if namerecord.text.__contains__("FiraCode") and not project_authors_namerecords.__contains__(namerecord)]
        for project_authors_namerecord in project_authors_namerecords:
            project_authors_namerecord.text = project_authors_namerecord.text.replace('tonsky/FiraCode', '{}/{}'.format(self.github_repo_owner, self.compact_font_name))
        for font_name_namerecord in font_name_namerecords:
            font_name_namerecord.text = font_name_namerecord.text.replace('Fira Code', self.font_name)
        for website_namerecord in website_namerecords:
            website_namerecord.text = website_namerecord.text.replace('tonsky.me', self.website)
        for fira_mono_trademark_namerecord in fira_mono_trademark_namerecords:
            fira_mono_trademark_namerecord.text = fira_mono_trademark_namerecord.text.replace('Fira Mono', self.font_name)
            fira_mono_trademark_namerecord.text = fira_mono_trademark_namerecord.text.replace('The Mozilla Corporation', self.organization_name)
        for compact_font_name_namerecord in compact_font_name_namerecords:
            compact_font_name_namerecord.text = compact_font_name_namerecord.text.replace('FiraCode', self.compact_font_name)
        et.write("./temporary_folder/{}-{}.ttx".format(self.compact_font_name, typeface), xml_declaration=True)
    def process_italic_font(self, file_path):
        # Open original file
        et = xml.etree.ElementTree.parse(file_path)
        root = et.getroot()
        namerecords = root.findall('./name/namerecord')
        copyright_namerecords = [namerecord for namerecord in namerecords if namerecord.text.__contains__("Copyright")]
        font_name_namerecords = [namerecord for namerecord in namerecords if namerecord.text.__contains__("Script12 BT")]
        pitched_font_name_namerecords = [namerecord for namerecord in namerecords if namerecord.text.__contains__("Script 12 Pitch BT")]
        compact_fontname_namerecords = [namerecord for namerecord in namerecords if namerecord.text.__contains__("Script12PitchBT-Roman")]
        basefont_name_namerecords = [namerecord for namerecord in namerecords if namerecord.text.__contains__("Roman") and not compact_fontname_namerecords.__contains__(namerecord)]
        fontname_description_namerecords = [namerecord for namerecord in namerecords if namerecord.text.__contains__("Script 12 Pitch, Fixed Pitch 885")]
        timestamp_namerecords = [namerecord for namerecord in namerecords if namerecord.text.__contains__("mfgpctt-v1.57 Friday, February 19, 1993 3:04:58 pm (EST)")]
        for copyright_namerecord in copyright_namerecords:
            copyright_namerecord.text = copyright_namerecord.text.replace("1990-1993 Bitstream Inc", "{} {}".format("2021-{}".format(self.timestamp.year), self.organization_name))
        for font_name_namerecord in font_name_namerecords:
            font_name_namerecord.text = font_name_namerecord.text.replace("Script12 BT", self.font_name)
        for pitched_font_name_namerecord in pitched_font_name_namerecords:
            pitched_font_name_namerecord.text = pitched_font_name_namerecord.text.replace("Script 12 Pitch BT", "{} {}".format(self.font_name, self.italicStr))
        for compact_fontname_namerecord in compact_fontname_namerecords:
            compact_fontname_namerecord.text = compact_fontname_namerecord.text.replace("Script12PitchBT-Roman", "{}-{}".format(self.compact_font_name, self.italicStr))
        for basefont_name_namerecord in basefont_name_namerecords:
            basefont_name_namerecord.text = basefont_name_namerecord.text.replace("Roman", "Italic")
        for fontname_description_namerecord in fontname_description_namerecords:
            fontname_description_namerecord.text = fontname_description_namerecord.text.replace("Script 12 Pitch, Fixed Pitch 885", "{}, based on Fira Code and Script12 BT fonts.".format(self.font_name))
        for timestamp_namerecord in timestamp_namerecords:
            timestamp_namerecord.text = timestamp_namerecord.text.replace("mfgpctt-v1.57 Friday, February 19, 1993 3:04:58 pm (EST)", "{} {}".format(self.compact_font_name, self.timestamp.strftime("%A, %d. %B %Y %I:%M%p")))
        et.write("./temporary_folder/{}-{}.ttx".format(self.compact_font_name, "Italic"), xml_declaration=True)
