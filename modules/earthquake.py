from flask import request
from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime


def deprem_latest():
    print(f"Son Deprem - Son Yenileme: {datetime.utcnow()}")
    URL = "http://www.koeri.boun.edu.tr/scripts/lst7.asp"
    try:
        response = requests.get(URL)
    except requests.exceptions.ConnectionError:
        print(f"Connection Error - We're trying to reconnect: {requests.exceptions.ConnectionError}")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        list = soup.find("pre")
        splitted = re.split('\n', str(list))
        son_deprem = splitted[7].split()
        tarih = son_deprem[0]
        saat = son_deprem[1]
        enlem = son_deprem[2]
        boylam = son_deprem[3]
        derinlik = son_deprem[4]
        buyukluk_md = son_deprem[5]
        buyukluk_ml = son_deprem[6]
        buyukluk_mw = son_deprem[7]
        lokasyon = ' '.join(son_deprem[8:-1])
        cozum = son_deprem[-1]
        if cozum == "Ýlksel":
            cozum = "Ilksel"
        if buyukluk_md == "-.-":
            buyukluk_md = None
        if buyukluk_mw == "-.-":
            buyukluk_mw = None
        if buyukluk_ml == "-.-":
            buyukluk_md = None
        google_maps = f"https://www.google.com/maps/search/?api=1&query={enlem},{boylam}"

        data = {"date": tarih, "time": saat,
                "latitude": enlem, "longitude": boylam,
                "depth": derinlik, "magnitude_md": buyukluk_md,
                "magnitude_ml": buyukluk_ml, "magnitude_mw": buyukluk_mw,
                "location": lokasyon, "state": cozum,
                "google_maps": google_maps}
    return data



def deprem_all():
    json_data = []
    print(f"Tüm Depremler - Son Yenileme: {datetime.utcnow()}")
    URL = "http://www.koeri.boun.edu.tr/scripts/lst7.asp"
    try:
        response = requests.get(URL)
    except requests.exceptions.ConnectionError:
        print(f"Connection Error - We're trying to reconnect: {requests.exceptions.ConnectionError}")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        list = soup.find("pre")
        splitted = re.split('\n', str(list))
        for line in splitted[7:-2]:
            deprem = line.split()
            tarih = deprem[0]
            saat = deprem[1]
            enlem = deprem[2]
            boylam = deprem[3]
            derinlik = deprem[4]
            buyukluk_md = deprem[5]
            buyukluk_ml = deprem[6]
            buyukluk_mw = deprem[7]
            lokasyon = ' '.join(deprem[8:-1])
            cozum = deprem[-1]
            if cozum == "Ýlksel":
                cozum = "Ilksel"
            if buyukluk_md == "-.-":
                buyukluk_md = None
            if buyukluk_mw == "-.-":
                buyukluk_mw = None
            if buyukluk_ml == "-.-":
                buyukluk_md = None
            google_maps = f"https://www.google.com/maps/search/?api=1&query={enlem},{boylam}"
            data = {"date": tarih, "time": saat,
                    "latitude": enlem, "longitude": boylam,
                    "depth": derinlik, "magnitude_md": buyukluk_md,
                    "magnitude_ml": buyukluk_ml, "magnitude_mw": buyukluk_mw,
                    "location": lokasyon, "state": cozum,
                    "google_maps": google_maps}
            json_data.append(data)

    return json_data


def deprem_query():
    json_data = []
    print(f"Tüm Depremler - Son Yenileme: {datetime.utcnow()}")
    URL = "http://www.koeri.boun.edu.tr/scripts/lst7.asp"
    try:
        response = requests.get(URL)
    except requests.exceptions.ConnectionError:
        print(f"Connection Error - We're trying to reconnect: {requests.exceptions.ConnectionError}")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        list = soup.find("pre")
        splitted = re.split('\n', str(list))
        for line in splitted[7:-2]:
            deprem = line.split()
            tarih = deprem[0]
            saat = deprem[1]
            enlem = deprem[2]
            boylam = deprem[3]
            derinlik = deprem[4]
            buyukluk_md = deprem[5]
            buyukluk_ml = deprem[6]
            buyukluk_mw = deprem[7]
            lokasyon = ' '.join(deprem[8:-1])
            cozum = deprem[-1]
            if cozum == "Ýlksel":
                cozum = "Ilksel"
            if buyukluk_md == "-.-":
                buyukluk_md = None
            if buyukluk_mw == "-.-":
                buyukluk_mw = None
            if buyukluk_ml == "-.-":
                buyukluk_md = None
            google_maps = f"https://www.google.com/maps/search/?api=1&query={enlem},{boylam}"
            data = {"date": tarih, "time": saat,
                    "latitude": enlem, "longitude": boylam,
                    "depth": derinlik, "magnitude_md": buyukluk_md,
                    "magnitude_ml": buyukluk_ml, "magnitude_mw": buyukluk_mw,
                    "location": lokasyon, "state": cozum,
                    "google_maps": google_maps}
            json_data.append(data)

    if "magnitude_ml" in request.args:
        magnitude = str(request.args["magnitude_ml"])
        results = []
        for d in json_data:
            if d["magnitude_ml"] == magnitude:
                results.append(d)
        return results


    if "magnitude_mw" in request.args:
        magnitudew = str(request.args["magnitude_mw"])
        results = []
        for d in json_data:
            if d["magnitude_mw"] == magnitudew:
                results.append(d)
        return results


    if "magnitude_md" in request.args:
        magnituded = str(request.args["magnitude_md"])
        results = []
        for d in json_data:
            if d["magnitude_md"] == magnituded:
                results.append(d)
        return results

    if "depth" in request.args:
        depth = str(request.args["depth"])
        results = []
        for d in json_data:
            if d["depth"] == depth:
                results.append(d)

        return results

    if "date" in request.args:
        date = str(request.args["date"])
        results = []
        for d in json_data:
            if d["date"] == date:
                results.append(d)

        return results

    if "time" in request.args:
        time = str(request.args["time"])
        results = []
        for d in json_data:
            if d["time"] == time:
                results.append(d)

        return results


    if "location" in request.args:
        location = str(request.args["location"]).upper()
        results = []
        for d in json_data:
            if location in d["location"]:
                results.append(d)

        return results


    if "state" in request.args:
        state = str(request.args["state"])
        results = []
        for d in json_data:
            if d["state"] == state:
                results.append(d)

        return results

    if "latitude" in request.args:
        lat = str(request.args["latitude"])
        results = []
        for d in json_data:
            if d["latitude"] == lat:
                results.append(d)

        return results

    if "longitude" in request.args:
        long = str(request.args["longitude"])
        results = []
        for d in json_data:
            if d["longitude"] == long:
                results.append(d)

        return results

