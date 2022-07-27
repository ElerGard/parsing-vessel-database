import time
from requests_html import HTMLSession
import pandas as pd
import os
import re

def get_vessel_data(link) -> list:
    session = HTMLSession()
    r = session.get(link)
    ships = r.html.find('table > tbody > tr')
    if (len(ships) == 1):
        name_type = ships[0].find('.sli')[0].text.split('\n')

        ship_link = ships[0].find('.ship-link')[0].attrs['href']
        imo = int(re.search("IMO-(\d+)", ship_link).group(1))
        mmsi = int(re.search("MMSI-(\d+)", ship_link).group(1))
        
        return [name_type[0], name_type[1], imo, mmsi]
    else:
        return ["", "", "", ""]

def get_data() -> list:
    result = [[],[],[],[]]
    xls = pd.ExcelFile("Links.xlsx")
    sheetX = xls.parse(0) 
    for link in sheetX['Ссылка']:
        tmp = get_vessel_data(link)
        for i in range(len(tmp)):
            result[i].append(tmp[i])
        print(result[0][-1], result[2][-1], result[3][-1], result[1][-1])
        
        time.sleep(2)
    return result

def write_to_excel(excel_name, data) -> None:
    df = pd.DataFrame({"Name": data[0],
                   "IMO": data[2],
                   "MMSI": data[3],
                   "Type": data[1]})

    if os.path.exists(excel_name):
        print("File exist")
    else:
        writer = pd.ExcelWriter(excel_name, engine="openpyxl")
        df.to_excel(writer, index=False)
        writer.save()

def main():
    filename = "result.xlsx"
    data = get_data()
    write_to_excel(filename, data)

main()