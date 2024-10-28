import pandas as pd
import numpy as np
from math import floor

netflix_titles = pd.read_csv("netflix_titles.tsv", sep="\t")

netflix_titles = netflix_titles[
    ["PRIMARYTITLE", "DIRECTOR", "CAST", "GENRES", "STARTYEAR"]
]

netflix_titles["DIRECTOR"] = netflix_titles["DIRECTOR"].str.split(", ")
netflix_titles["CAST"] = netflix_titles["CAST"].str.split(", ")
netflix_titles["GENRES"] = netflix_titles["GENRES"].str.split(", ")
netflix_titles = netflix_titles.rename(
    columns={
        "PRIMARYTITLE": "title",
        "DIRECTOR": "directors",
        "CAST": "cast",
        "GENRES": "genres",
        "STARTYEAR": "decade",
    }
)

netflix_titles["directors"] = netflix_titles["directors"].apply(
    lambda y: [] if y is np.nan else y
)

netflix_titles["cast"] = netflix_titles["cast"].apply(
    lambda y: [] if y is np.nan else y
)

netflix_titles["decade"] = netflix_titles["decade"].apply(
    lambda y: floor(y/10) * 10
)

with open("hw02_output.json", mode="w", encoding="utf-8") as netflix_file:
    netflix_titles.to_json(netflix_file, orient="records", indent=4)
