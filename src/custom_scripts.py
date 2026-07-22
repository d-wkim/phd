def csv(filename):
    import pandas as pd
    df = pd.read_csv(f"./data/{filename}.csv", encoding = "utf-8")
    return df

def markdown_to_html(markdown_text):
    import markdown
    from IPython.display import HTML, Markdown, display
    
    markdown_text = f"{markdown_text}"
    html = markdown.markdown(markdown_text)
    print(html)
    display(HTML(f"""<div align="center">
{html}</div>"""))

def df_to_markdown_table(df):
    from IPython.display import Markdown, display
    import markdown
    df = df
    markdown_table = df.to_markdown()
    print(markdown_table)
    display(Markdown(markdown_table))

def requirements():
    requirements = [
        "pandas",
        "biopython",
        "ipython",
        "ipywidgets",
        "tabulate",
        "jupyterlab-spreadsheet-editor"
    ]

    requirements = "\n".join(requirements)
    with open("./requirements.txt", "w") as f:
        f.write(requirements)

def mkdir(folders):
    import os
    for x, y in folders.items():
        folder = f"{y}"
        os.makedirs(folder, exist_ok = True)
        with open(f"{folder}/index.md", "w") as f:
            f.write(f"""<a id="{x}"></a>
---
title: {x.replace("_", " ").title()}
---""")

def static_badge(link, label, color, size = 30, logo = "", logo_color = "", ):
    from IPython.display import display, HTML
    if logo == "":
        badge = f"""<a href="{link}"><img alt="{label}" src="https://img.shields.io/badge/{label.replace(" ", "_")}-{color}?style=for-the-badge"  height="{size}"></a>"""
    else:
        badge = f"""<a href="{link}"><img alt="{label}" src="https://img.shields.io/badge/{label.replace(" ", "_")}-{color}?style=for-the-badge&logo={logo}&logoColor={logo_color}" height = "{size}"></a>"""
    print(badge)
    display(HTML(badge))


def icon(link, img, width = 25, height = 25):
    icon = f"""<a href="{link}"><img alt = "" src="{img}" width="{width}" height="{height}"></a>"""
    print(icon)
    import ipywidgets as widgets
    from IPython.display import display, HTML
    display(HTML(icon))
    return icon