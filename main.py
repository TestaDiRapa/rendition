import pickle
from rolldriver import Roll20Driver


if __name__ == "__main__":
    cred = pickle.load(open("credentials.pkl", "rb"))
    driver = Roll20Driver()
    driver.login(cred[0], cred[1])
    print(driver.list_games())
    driver.list_characters("11831308")
    driver.get_character("Vath")