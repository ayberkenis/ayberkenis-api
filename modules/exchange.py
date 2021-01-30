from flask import request
from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime


def exchange_all():
    URL = "https://kur.doviz.com"
    data = {}
    try:
        response = requests.get(URL)
    except requests.exceptions.ConnectionError:
        print(f"Connection Error - We're trying to reconnect: {requests.exceptions.ConnectionError}")
    else:

        print("We're parsing the currencies!")
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find('table')
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')

        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]

            if cols[0]:
                data[cols[0][:3]] = {"currency_name": cols[0][6:],"currency_code": cols[0][:3], "currency_buy": cols[1], "currency_sell": cols[2], "currency_high": cols[3], "currency_low": cols[4],
                         "currency_change": cols[5], "time": cols[6]}
    return data



def exchange_query():
    URL = "https://kur.doviz.com"
    data = {}
    try:
        response = requests.get(URL)
    except requests.exceptions.ConnectionError:
        print(f"Connection Error - We're trying to reconnect: {requests.exceptions.ConnectionError}")
    else:

        print("We're parsing the currencies!")
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find('table')
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')

        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            if cols[0]:
                data[cols[0][:3]] = {"currency_name": cols[0][6:], "currency_code": cols[0][:3], "currency_buy": cols[1], "currency_sell": cols[2], "currency_high": cols[3], "currency_low": cols[4],
                         "currency_change": cols[5], "time": cols[6]}



    if "currency_code" in request.args:
        code = str(request.args["currency_code"])
        results = []
        for d in data:
            if code.lower() in data[d]["currency_code"].lower():
                results.append(data[d])
        return results

    if "currency_name" in request.args:
        code = str(request.args["currency_name"])
        results = []
        for d in data:
            if code.lower() in data[d]["currency_name"].lower():
                results.append(data[d])
        return results

    if "currency_buy" in request.args:
        code = str(request.args["currency_buy"])
        results = []
        for d in data:
            if code.lower() in data[d]["currency_buy"].lower():
                results.append(data[d])
        return results

    if "currency_sell" in request.args:
        code = str(request.args["currency_sell"])
        results = []
        for d in data:
            if code.lower() in data[d]["currency_sell"].lower():
                results.append(data[d])
        return results

    if "currency_high" in request.args:
        code = str(request.args["currency_high"])
        results = []
        for d in data:
            if code.lower() in data[d]["currency_high"].lower():
                results.append(data[d])
        return results

    if "currency_low" in request.args:
        code = str(request.args["currency_low"])
        results = []
        for d in data:
            if code.lower() in data[d]["currency_low"].lower():
                results.append(data[d])
        return results

    if "currency_change" in request.args:
        code = str(request.args["currency_change"])
        results = []
        for d in data:
            if code.lower() in data[d]["currency_change"].lower():
                results.append(data[d])
        return results

    if "time" in request.args:
        code = str(request.args["time"])
        results = []
        for d in data:
            if code.lower() in data[d]["time"].lower():
                results.append(data[d])
        return results
