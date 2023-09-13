import pandas as pd
import argparse
import requests


def write_html(df, filename, css=None):
    books_as_html = df[["Titel ", "Autor*in", "Sprache", "Kategorie"]].to_html()
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines('<!DOCTYPE html>\n')
        file.writelines('<head>\n')
        file.writelines('<meta charset="UTF-8">\n')
        if css:
            file.writelines(f'<link rel="stylesheet" href="{css}">\n')
        file.writelines('</head>\n')
        file.writelines('<body>\n')
        file.write(books_as_html)
        file.writelines('</body>\n')


def cli():
    parser = argparse.ArgumentParser(description='Convert an odt document to a book')
    parser.add_argument('-i', '--input-file', help="The input file (odf format)")
    parser.add_argument('-o', '--output', help="Filename where to export the html table to")
    parser.add_argument('--healthcheck', help="[Optional] Healthcheck URL")
    parser.add_argument('--css', help="[Optional] relative css file location")
    args = parser.parse_args()

    book_df = pd.read_excel(args.input, engine="odf")

    write_html(book_df, args.output, args.css)

    if args.healthcheck:
        requests.post(args.healthcheck, data=f"num_books={len(book_df)}")


if __name__ == "__main__":
    cli()
