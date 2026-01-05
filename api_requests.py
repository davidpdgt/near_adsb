# Fetches data from API source

import argparse
import datetime
import json
import requests

from pathlib import Path
from zoneinfo import ZoneInfo

class adsb_api():
    def __init__(self, config_lat: float, config_lon: float, config_dist: float) -> None:
        self.config_latitude = config_lat
        self.config_longitude = config_lon
        self.config_distance = config_dist

    def get_data_from_api(self):
        construct_url = f"https://opendata.adsb.fi/api/v3/lat/{self.config_latitude}/lon/{self.config_longitude}/dist/{self.config_distance}"

        try:
            api_response = requests.get(construct_url, timeout=2.5)
        except Exception as e:
            print(f"API query failed, exception: {e}")
        api_data = api_response.json()
        aircraft_data = api_data["ac"]
        aircraft_number = api_data["total"]
        time_now = datetime.datetime.fromtimestamp(api_data["now"]/1000)

        return aircraft_data, aircraft_number, time_now

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-j', '--json', type=str)

    args = parser.parse_args()

    try:
        with open(Path(args.json)) as file:
            config_data = file.read()
        config = json.loads(config_data)
    except Exception as e:
        print(f"Exception raised: {e}")
        raise Exception

    program = adsb_api(config["latitude"], config["longitude"], config["distance"])
    program.get_data_from_api()