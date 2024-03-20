from typing import Dict, List, Optional, Literal

import requests
import json
import csv

InstrumentType = Optional[Literal["ETC", "ETF", "ETN"]]

URL = "https://www.justetf.com/servlet/etfs-table"

BASE_PARAMS = {
    "draw": 1,
    "start": 0,
    "length": -1,
    "lang": "en",
    "country": "DE",
    "universeType": "private",
}

def make_request()-> List[Dict[str, str]]:

    query = build_query()

    print("Query: " + str(query))


    response = requests.post(
        URL,
        {
            **BASE_PARAMS,
            "etfsParams": query,
        },
    )


    assert response.status_code == requests.codes.ok
    data = response.json()["data"]
    return data

def build_query() -> str:
    params = "groupField=none&ls=any"
    return params

def write_csv(data: List[Dict[str,str]], file_path: str):
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

    print("Wrote data to csv: " + file_path)