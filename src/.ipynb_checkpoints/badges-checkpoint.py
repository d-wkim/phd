
def static_badge(link, label, color, logo = "", logo_color = "", logo_size = 30):
    from IPython.display import display, HTML
    if logo == "":
        badge = f"""<div align="center">
    <a href="{link}"><img alt="{label}" src="https://img.shields.io/badge/{label.replace(" ", "_")}-{color}?style=for-the-badge"  width="{logo_size}"></a>
</div>"""
    else:
        badge = f"""<div align="center">
    <a href="{link}"><img alt="{label}" src="https://img.shields.io/badge/{label.replace(" ", "_")}-{color}?style=for-the-badge&logo={logo}&logoColor={logo_color}" width = "{logo_size}"></a>
</div>"""
    display(HTML(badge))
    print(badge)

def custom_badge(link, label, color, logo = "", logo_color = ""):
    if logo == "":
        badge = f"""<div align="center">
    <a href="{link}"><img alt="{label}" src="https://custom-icon-badges.demolab.com/badge/{label.replace(" ", "_")}-{color}?style=for-the-badge&logo={logo}&logoColor={logo_color}" width = "{logo_size}"></a>
</div>"""

    else:
        badge = f"""<div align="center">
    <a href="{link}"><img alt="{label}" src="https://custom-icon-badges.demolab.com/badge/{label.replace(" ", "_")}-{color}?style=for-the-badge&logo={logo}&logoColor={logo_color}" width = "{logo_size}"></a>
</div>"""
    display(HTML(badge))
    print(badge)