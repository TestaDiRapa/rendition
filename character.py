from sheet_parser import SpicySoup

class Character:

    def __init__(self, html):
        self.soup = SpicySoup(html)
        self.pg = dict()
        self.pg["name"] = self.soup.get_name()
        self.pg["img"] = self.soup.get_img()
        self.pg["description"] = self.soup.get_description()
        ac, ac_type = self.soup.get_ac()
        self.pg["ac"] = {"value": ac, "type": ac_type}
        hp, hd = self.soup.get_hit_points()
        self.pg["hp"] = {"value": hp, "hd": hd}
        self.pg["speed"] = self.soup.get_speed()
        self.pg["as"] = self.soup.get_ability_scores()
        self.pg["saving_throws"] = self.soup.get_saving_throw_prof()
        self.pg["skills"] = self.soup.get_skill_prof()
        self.pg["vulnerabilities"] = self.soup.get_vulnerabilitites()
        self.pg["resistances"] = self.soup.get_resistances()
        self.pg["immunities"] = self.soup.get_damage_immunities()
        self.pg["condition_immunities"] = self.soup.get_condition_immunities()
        self.pg["senses"] = self.soup.get_senses()
        self.pg["languages"] = self.soup.get_languages()
        cr, xp = self.soup.get_cr()
        self.pg["cr"] = {"value": cr, "exp": xp}
        self.pg["traits"] = self.soup.get_traits()
        self.pg["actions"] = self.soup.get_actions()
        self.pg["bonus_actions"] = self.soup.get_actions()
        self.pg["reactions"] = self.soup.get_reactions()
        self.pg["legendary_actions"] = self.soup.get_legendary_actions()
        self.pg["mythic_actions"] = self.soup.get_mythic_actions()
        self.pg["spellcasting"] = self.soup.get_spellcasting_info()


    def save_to_txt(self):
        with open(f"{self.pg['name']}.txt", 'w') as f:
            f.write(f"{self.pg['name']} - {self.pg['description']}\n")
            f.write(f"IMAGE: {self.pg['img']}\n")
            f.write("--------------------------\n")
            f.write(f"ARMOR:\t{self.pg['ac']['value']} ({self.pg['ac']['type']})\n")
            f.write(f"HIT POINTS:\t{self.pg['hp']['value']} ({self.pg['hp']['hd']})\n")
            f.write("SPEED:\n")
            for s in self.pg["speed"]:
                f.write(f"\t{s}\n")
            f.write("--------------------------\n")
            f.write("ABILITY SCORES\n")
            for score, value in self.pg["as"].items():
                f.write(f"{score}\t{value}\n")
            f.write("--------------------------\n")
            f.write("SAVING THROWS\n")
            for prof, value in self.pg["saving_throws"].items():
                if value > 0:
                    f.write(f"\t{prof}:\t{value}\n")
            f.write("SKILLS\n")
            for prof, value in self.pg["skills"].items():
                if value > 0:
                    f.write(f"\t{prof}:\t{value}\n")
            f.write("VULNERABILITIES:\n")
            for v in self.pg["vulnerabilities"]:
                f.write(f"\t{v}\n")
            f.write("RESISTANCES:\n")
            for r in self.pg["resistances"]:
                f.write(f"\t{r}\n")
            f.write("IMMUNITIES:\n")
            for i in self.pg["immunities"]:
                f.write(f"\t{i}\n")
            f.write("CONDITION IMMUNITIES:\n")
            for i in self.pg["condition_immunities"]:
                f.write(f"\t{i}\n")
            f.write("SENSES:\n")
            for s in self.pg["senses"]:
                f.write(f"\t{s}\n")
            f.write("LANGUAGES:\n")
            for l in self.pg["languages"]:
                f.write(f"\t{l}\n")
            f.write(f"CHALLENGE: {self.pg['cr']['value']} ({self.pg['cr']['exp']} XP)\n")
            f.write("--------------------------\n")
            f.write("TRAITS\n")
            for t in self.pg["traits"]:
                f.write(f"\t{t['name']}\n")
                f.write(f"\t{t['description']}\n\n")
            f.write("--------------------------\n")
            f.write("ACTIONS\n")
            for a in self.pg["actions"]:
                f.write(f"\t{a['name']}\n")
                f.write(f"\t{a['type']}, ")
                for _, v in a["mods"].items():
                    f.write(f"{v}, ")
                f.write("\n")
                if a["dmg"] is not None:
                    f.write(f"\t{a['dmg']['primary']['avg']} ({a['dmg']['primary']['die']})")
                    if a['dmg']['primary']['type'] is not None:
                        f.write(f" {a['dmg']['primary']['type']}")
                    f.write(" damage")
                    if "secondary" in a["dmg"]:
                        f.write(f" plus {a['dmg']['secondary']['avg']} ({a['dmg']['secondary']['die']})")
                        if a['dmg']['secondary']['type'] is not None:
                            f.write(f" {a['dmg']['secondary']['type']}")
                        f.write(" damage")
                    f.write("\n")
                f.write(f"\t{a['description']}\n\n")
            f.write("--------------------------\n")
            f.write("BONUS ACTIONS\n")
            for a in self.pg["bonus_actions"]:
                f.write(f"\t{a['name']}\n")
                f.write(f"\t{a['type']}, ")
                for _, v in a["mods"].items():
                    f.write(f"{v}, ")
                f.write("\n")
                if a["dmg"] is not None:
                    f.write(f"\t{a['dmg']['primary']['avg']} ({a['dmg']['primary']['die']})")
                    if a['dmg']['primary']['type'] is not None:
                        f.write(f" {a['dmg']['primary']['type']}")
                    f.write(" damage")
                    if "secondary" in a["dmg"]:
                        f.write(f" plus {a['dmg']['secondary']['avg']} ({a['dmg']['secondary']['die']})")
                        if a['dmg']['secondary']['type'] is not None:
                            f.write(f" {a['dmg']['secondary']['type']}")
                        f.write(" damage")
                    f.write("\n")
                f.write(f"\t{a['description']}\n\n")
            f.write("--------------------------\n")
            f.write("REACTIONS\n")
            for t in self.pg["reactions"]:
                f.write(f"\t{t['name']}\n")
                f.write(f"\t{t['description']}\n\n")
            f.write("--------------------------\n")
            f.write("LEGENDARY ACTIONS\n")
            f.write(f"{self.pg['name']} has {self.pg['legendary_actions']['total']} legendary actions each turn\n")
            for a in self.pg['legendary_actions']['actions']:
                f.write(f"\t{a['name']}\n")
                f.write(f"\t{a['type']}, ")
                for _, v in a["mods"].items():
                    f.write(f"{v}, ")
                f.write("\n")
                if a["dmg"] is not None:
                    f.write(f"\t{a['dmg']['primary']['avg']} ({a['dmg']['primary']['die']})")
                    if a['dmg']['primary']['type'] is not None:
                        f.write(f" {a['dmg']['primary']['type']}")
                    f.write(" damage")
                    if "secondary" in a["dmg"]:
                        f.write(f" plus {a['dmg']['secondary']['avg']} ({a['dmg']['secondary']['die']})")
                        if a['dmg']['secondary']['type'] is not None:
                            f.write(f" {a['dmg']['secondary']['type']}")
                        f.write(" damage")
                    f.write("\n")
                f.write(f"\t{a['description']}\n\n")
            f.write("--------------------------\n")
            f.write("MYTHIC ACTIONS\n")
            f.write(f"{self.pg['name']} triggers the mythic actions when {self.pg['mythic_actions']['trigger']}\n")
            for a in self.pg['mythic_actions']['actions']:
                f.write(f"\t{a['name']}\n")
                f.write(f"\t{a['type']}, ")
                for _, v in a["mods"].items():
                    f.write(f"{v}, ")
                f.write("\n")
                if a["dmg"] is not None:
                    f.write(f"\t{a['dmg']['primary']['avg']} ({a['dmg']['primary']['die']})")
                    if a['dmg']['primary']['type'] is not None:
                        f.write(f" {a['dmg']['primary']['type']}")
                    f.write(" damage")
                    if "secondary" in a["dmg"]:
                        f.write(f" plus {a['dmg']['secondary']['avg']} ({a['dmg']['secondary']['die']})")
                        if a['dmg']['secondary']['type'] is not None:
                            f.write(f" {a['dmg']['secondary']['type']}")
                        f.write(" damage")
                    f.write("\n")
                f.write(f"\t{a['description']}\n\n")
            f.write("--------------------------\n")
            f.write("SPELLCASTING\n")
            f.write(f"CD: {self.pg['spellcasting']['dc']}\n")
            f.write(f"TxC: {self.pg['spellcasting']['txc']}\n")
            f.write(f"Cantrips:\n")
            for c in self.pg['spellcasting']['cantrips']:
                f.write(f"\t{c}\n")
            for i in range(1, 10):
                f.write(f"Level {i} ({self.pg['spellcasting'][f'level-{i}']['slots']} slots):\n")
                for s in self.pg['spellcasting'][f'level-{i}']['spells']:
                    f.write(f"\t{s}\n")
            

