import ide_header
from ide_header import jprint, gs
from src.categories import  Category

c = Category()
list_parent_categories_from_prestashop = c.get_list_parent_categories_from_prestashop(11036)

categories_from_template_files: dict = c.categories_tree_from_template_files
pass