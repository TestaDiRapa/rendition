from character import Character

if __name__ == "__main__":
    html = open("test.html", "r").read()
    c = Character(html)
    c.save_to_txt()