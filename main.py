from sheet_parser import SpicySoup

if __name__ == "__main__":
    html = open("test.html", "r").read()
    soup = SpicySoup(html)
    print(soup.get_spellcasting_info())