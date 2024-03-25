from taipy.gui import Gui, Markdown
from pages.page1 import page1_md
from pages.page2 import page2_md


nav = [
    ('/taipy', 'Taipy'),
    ('/embetter', 'Embetter'),
    ('https://stock-visualization.taipy.cloud/', 'Demo')
]

root_md = """
<|navbar|lov={nav}|>
"""


pages = {
    "/": Markdown(root_md),
    "taipy": page1_md,
    "embetter": page2_md,
}



if __name__ == "__main__":
    Gui(pages=pages, css_file='main.css').run(title="Taipy + Embetter", debug=True)