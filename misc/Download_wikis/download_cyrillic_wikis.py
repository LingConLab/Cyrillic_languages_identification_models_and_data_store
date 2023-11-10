from bs4 import BeautifulSoup
import re
import requests
import json
from pathlib import Path
import datetime

# Collect language names and tags used on different Wikipedias
# parse the table with meta information
URL = "https://meta.wikimedia.org/wiki/List_of_Wikipedias"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# find the table
result = soup.find("table", class_ = "list-of-wikipedias-table wikitable sortable")
# make a list of interesting html parts
regex_result = re.findall(pattern=r'title="en:.+ language">.+<\/a><\/td>\n<td>.+<\/td>\n<td><a.+\n',
                          string=str(result))
# filter the strings with the Cyrillic symbols

cyrillic_htmls = [string for string in regex_result if re.search(string=string, pattern="[А-я]") is not None ]
# extract English titles and wiki codes
language_code_map = {}
for chunk in cyrillic_htmls:
    language = re.search('(?<=language">).+?(?=</a></td>\n)', chunk)
    code = re.search('(?<=title=").+(?=:">)', chunk)
    language_code_map[language.group(0)] = code.group(0)

# save language-code map
with open( Path.joinpath(Path(__file__).parent.resolve(),
                         "language_code_map.json"), "w") as file:
    json.dump(language_code_map, file, indent=3)

### download all languages' dumps
print(f"Started downloading at {datetime.datetime.now()}")
i = 0
for tag in language_code_map.values():
    if str(tag) not in ['ru','uk','be-tarask','be','cu']: #'cu' - Church Slavonic # Belarusian has two Wikipedias
        i +=1
        try:
            url = 'https://dumps.wikimedia.org/'+str(tag)+'wiki/20231001/'+str(tag)+'wiki-20231001-pages-articles-multistream.xml.bz2'
            response = requests.get(url)
            path_for_dump = Path.joinpath(Path(__file__).parent.resolve(),
                                    str(tag)+'wiki-20231001-pages-articles-multistream.xml.bz2')
            with open(path_for_dump,"wb") as f:
                f.write(response.content)
            print(f"{tag} ({i}) downloaded at {path_for_dump}")
        except:
            print(f"{tag} failed to download!")

print(f"Finished downloading at {datetime.datetime.now()}")

