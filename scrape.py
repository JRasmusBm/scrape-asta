import logging
import requests
from bs4 import BeautifulSoup


logger = logging.getLogger(__name__)


def search_link(search_period, search_query="", search_category=""):
    return f"https://www.uhr.se/studier-och-antagning/antagningsstatistik/resultatsida/?astasearchperiod={search_period}&astasearchfor={search_query}&astasearchcategory={search_category}"


def extract_function(source_code, name):
    result = []
    is_in_function = False
    indentation = ""

    for line in source_code.split("\n"):
        if f"function {name}" in line:
            is_in_function = True
            indentation = len(line) - len(line.lstrip())

        if not is_in_function:
            continue

        line_without_indentation = line[indentation:]
        result.append(line_without_indentation)

        if (line_without_indentation or [" "])[0] == "}":
            break

    return "\n".join(result)


def main():
    response = requests.get(search_link(search_period="HT21"))
    soup = BeautifulSoup(response.text, features="html.parser")
    code = soup.select("main script")[-1].contents[0]

    print(extract_function(source_code=code, name="doFileDownload"))


if __name__ == "__main__":
    main()
