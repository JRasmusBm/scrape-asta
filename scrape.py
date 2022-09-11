"""
Hello
"""
import logging
import requests
from bs4 import BeautifulSoup



logger = logging.getLogger(__name__)

def search_link(search_period, search_query="", search_category=""):
   return f"https://www.uhr.se/studier-och-antagning/antagningsstatistik/resultatsida/?astasearchperiod={search_period}&astasearchfor={search_query}&astasearchcategory={search_category}" 


def extract_function(source_code, name):
    return source_code

def main():
  """
  hello
  """
  response = requests.get(search_link(search_period="HT21"))
  soup = BeautifulSoup(response.text, features="html.parser")
  code = soup.select("main script")[-1]
  do_file_download_source = extract_function(source_code=code, name="doFileDownload")
  print(do_file_download_source)
  
  

if __name__ == "__main__":
    main()
