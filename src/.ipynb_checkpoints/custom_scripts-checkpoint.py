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
    display(Markdown(markdown_table))
    