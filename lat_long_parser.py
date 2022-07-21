import pandas as pd


# https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400


class LatLongParser:
    """
    For importing csv data.

    The Pandas Library is used to convert the dataframe into dictionaries based on
    the State name and State id (Nebraska, NE), etc...
    This is an example of using the Google Docstring (Kahn Academy) style.

    Class Attributes
    ----------------
    df : Dataframe
        The Basic Dataframe that will extract info.
    state_id_dictionary : dict of {str : float}
        Dictionary to get lat, long using state ID (NE, WY, CO, ect..) as a key.
    state_name_dictionary : dict
        Dictionary to get lat, long using state Name (Nebraska, Wyoming, etc...) as a key.

    Class Methods
    -------------
    frmt_lat_long : meth
        Gets lat / long from either state id or state name
    """
    DEFAULT_STATE = "Nebraska"

    df = pd.read_csv("state_lat_long.csv")
    state_id_dictionary = {row["id"]: {"lat": row["lat"], "long": row["long"]} for index, row in df.iterrows()}
    state_name_dictionary = {row["state"]: {"lat": row["lat"], "long": row["long"]} for index, row in df.iterrows()}

    @classmethod
    def frmt_state_lat_long(cls, name_or_id: str = DEFAULT_STATE) -> str:
        if len(name_or_id) == 2:
            state_id = name_or_id.upper().strip()
            if state_id not in LatLongParser.state_id_dictionary.keys():
                raise IndexError
            else:
                return f'lat={LatLongParser.state_id_dictionary[state_id]["lat"]}' \
                       f'&lng={LatLongParser.state_id_dictionary[state_id]["long"]}'
        else:
            state_name = name_or_id.title().strip()
            if state_name not in LatLongParser.state_name_dictionary.keys():
                raise IndexError
            else:
                return f'lat={LatLongParser.state_name_dictionary[state_name]["lat"]}' \
                       f'&lng={LatLongParser.state_name_dictionary[state_name]["long"]}'

    @classmethod
    def frmt_lat_long(cls, lat, long):
        return f'lat={lat}' \
               f'&lng={long}'


if __name__ == "__main__":
    print(LatLongParser.frmt_state_lat_long("ne"))
