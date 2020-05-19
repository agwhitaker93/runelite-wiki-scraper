from src.api import get_wiki_api


# We want to get all of the items listed as materials for each of the craftables pulled earlier
def run():
    print("To be implemented")
    get_wiki_api({"action": "query",
                  "titles": "Coal",
                  "prop": "templates",
                  "format": "json"}, "cmcontinue")
