# /// script
# dependencies = [
#   "pandas",
# ]
# ///
from urllib.parse import urlparse
import pandas as pd

csv = pd.read_csv("links.csv")

csv["domain"] = csv["link"].apply(lambda x: urlparse(x).hostname)

print(csv["domain"].value_counts())