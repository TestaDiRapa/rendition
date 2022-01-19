from sheet_parser import SpicySoup

if __name__ == "__main__":
    html = open("test.html", "r").read()
    soup = SpicySoup(html)
    for el in soup.get_actions():
        print(el)
        print()