from typing import Type
import pygeoip
from colorama import Fore
import os
import pathlib
import cli
gi = pygeoip.GeoIP('C:/testfolder/geo.dat')
def print_record():
    try:
        tgt = input("Please provide the ip adress:")
        rec = gi.record_by_addr(tgt)
        city = rec['city']
        country = rec['country_name']
        postal_code = rec['postal_code']
        areacode = rec['area_code']
        long = rec['longitude']
        lat = rec['latitude']
        dma_code = rec['dma_code']
        region_code = rec['region_code']
        timezone = rec['time_zone']
        print(f"[*] Target found {tgt}")
        print(Fore.RED + f"Information: \nCity: {city}\nArea code: {areacode}\nCountry: {country}\nPostal Code: {postal_code}\nLongtitude: {long}\nLatitude: {lat}\nDma code: {dma_code}\nTimezone: {timezone}\nRegion Code: {region_code} ")
    except OSError:
        print(Fore.RED + "THAT IS NOT A VALID IP ADDRESS. Please use a different one!\n")
        os.system('pause')
        cli.main()
    except TypeError:
        print(Fore.RED + "THAT IS NOT A VALID IP ADDRESS. Please use a different one!\n")
        os.system('pause')
        cli.main()