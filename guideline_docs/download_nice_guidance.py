# /// script
# dependencies = [
#   "pandas",
#   "requests",
#   "bs4",
# ]
# ///
import os
import shutil
from urllib.parse import urlparse
import pandas as pd
import requests
from bs4 import BeautifulSoup

df = pd.read_csv("links.csv")

df["domain"] = df["link"].apply(lambda x: urlparse(x).hostname)

df = df.loc[df["domain"] == "www.nice.org.uk"]

def download_file(url):
    local_filename = "docs/" + url.split('/')[-1] + ".pdf"

    if os.path.exists(local_filename):
        print(f"\tSkipping as already downloaded")
    else:
        print(f"\t{local_filename}")
        with requests.get(url, stream=True) as r:
            with open(local_filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)

for _, row in df.iterrows():
    print(row["link"])

    nice_page = requests.get(row["link"])
    nice_soup = BeautifulSoup(nice_page.content, 'html.parser')

    pdf_link = nice_soup.select_one("[data-track='guidancedownload']")

    if not pdf_link:
        print("\tSkipped - no download button")
    else:
        pdf_link = "https://www.nice.org.uk" + pdf_link['href']
        download_file(pdf_link)
