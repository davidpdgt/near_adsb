# Near ADSB

This repo is intended to show what the current closest aircraft to a given position is.

## Changing the Config File to Suit

Change the config_template.json file values, based on what you want. Values to change:

- latitude: The latitude of the ground location in decimal degrees
- longitude: The longitude of the ground location in decimal degrees
- distance: The distance to fetch ADS-B data within, in nautical miles. Note, this must be greater than 0.
- update_rate: The time, in seconds, to fetch updated data from the API