from bs4 import BeautifulSoup

class SpicySoup:

    def __init__(self, html, parser='lxml'):
        self.soup = BeautifulSoup(html, 'lxml')
    
    def __get_attribute(self, selector):
        tags = self.soup.select(selector)
        if len(tags) == 0:
            return None
        else:
            return tags[0].text

    def __get_list_attribute(self, selector):
        attr = self.__get_attribute(selector)
        if attr is not None:
            return attr.split(',')
        return None    

    def get_name(self):
        '''
        Gets the name of the NPC
        '''
        return self.__get_attribute("span[name='attr_npc_name']")

    def get_description(self):
        '''
        Gets the description of the NPC
        '''
        return self.__get_attribute("span[name='attr_npc_type']")

    def get_ac(self):
        '''
        Gets AC and type of armor
        '''
        ac = self.__get_attribute("span[name='attr_npc_ac']")
        type = self.__get_attribute("span[name='attr_npc_actype']")
        return ac, type

    def get_hit_points(self):
        '''
        Gets HP and hit die
        '''
        hp = self.__get_attribute("span[name='attr_hp_max']")
        hit_die = self.__get_attribute("span[name='attr_npc_hpformula']")
        return hp, hit_die

    def get_speed(self):
        '''
        Gets the speed
        '''
        return self.__get_list_attribute("span[name='attr_npc_speed']")

    def get_ability_scores(self):
        '''
        Gets all the ability scores
        '''
        scores = dict()
        for score in ["strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma"]:
            scores[score] = self.__get_attribute(f"span[name='attr_{score}']")
        return scores

    def get_saving_throw_prof(self):
        '''
        Gets the proficiencies in saving throws
        '''
        prof = dict()
        for score in ["str", "dex", "con", "int", "wis","cha"]:
            s = self.__get_attribute(f"span[name='attr_npc_{score}_save']")
            prof[score] = 0 if s is None else int(s)
        return prof

    def get_skill_prof(self):
        '''
        Gets the proficiencies in skills
        '''
        skills = ["acrobatics", "animal_handling", "arcana", "athletics", "deception", "history", "insight", "intimidation", "investigation", "medicine", "nature",
                    "perception", "performance", "persuasion", "religion", "sleight_of_hand", "stealth", "survival"]
        prof = dict()
        for s in skills:
            s = self.__get_attribute((f"span[name='attr_npc_{s}']"))
            prof[s] = 0 if s is None or s.startswith('@') else int(s)
        return prof

    def get_vulnerabilitites(self):
        '''
        Get vulnerabilities
        '''
        return self.__get_list_attribute("span[name='attr_npc_vulnerabilities']")

    def get_resistances(self):
        '''
        Get resistances
        '''
        return self.__get_list_attribute("span[name='attr_npc_resistances']")

    def get_damage_immunities(self):
        '''
        Get damage immunities
        '''
        return self.__get_list_attribute("span[name='attr_npc_immunities']")

    def get_condition_immunities(self):
        '''
        Get condition immunities
        '''
        return self.__get_list_attribute("span[name='attr_npc_condition_immunities']")

    def get_senses(self):
        '''
        Get all the senses of the creature
        '''
        return self.__get_list_attribute("span[name='attr_npc_senses']")

    def get_languages(self):
        '''
        Get all the languages spoken by the creature
        '''
        return self.__get_list_attribute("span[name='attr_npc_languages']")

    def get_cr(self):
        '''
        Get exp and challenge rate
        '''
        cr = self.__get_attribute(f"span[name='attr_npc_challenge']")
        exp = self.__get_attribute(f"span[name='attr_npc_xp']")

    def get_traits(self):
        '''
        Gets all the trait with their description
        '''
        ret = list()
        for el in self.soup.select("div.row.traits div.trait"):
            name = el.find("span", {"name": "attr_name"}).text
            if name is not None and name != "":
                ret.append({
                    "name": name,
                    "description": el.find("span", {"name": "attr_description"}).text
                })
        return ret

if __name__ == "__main__":
    html = open("test.html", "r").read()
    soup = SpicySoup(html)
    print(soup.get_traits())