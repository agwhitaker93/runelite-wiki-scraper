import traceback
import mwparserfromhell as mw
from src import api
from src.craftable import Craftable
from src.util import filter_templates, template_params_to_dict
import edn_format


def run():
    item_pages = api.query_category("Items")
    for name, page in item_pages.items():
        try:
            code = mw.parse(page, skip_style_tags=True)
            has_recipes = False
            craftable = Craftable(name)

            for recipe in filter_templates(code, "Recipe"):
                has_recipes = True
                craftable.add_recipe(template_params_to_dict(recipe))

            if not has_recipes:
                continue

            has_price = False
            for infobox_item in filter_templates(code, "Infobox Item"):
                has_price = True
                craftable.add_infobox(template_params_to_dict(infobox_item))

            if not has_price:
                continue

            with open(f"resources/generated/craftable/{name}.edn", "w") as f:
                f.write(edn_format.dumps(craftable.to_dict()))

        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            print("Craftable {} failed:".format(name))
            traceback.print_exc()
