import json
from pathlib import Path
from datetime import datetime


class DataManipulator:

    json_data_dict: dict = None

    def __init__(self, path: Path):  # constructor function
        print(f"Starting to parsing json {path}")
        # open file with pathlib.Path method open
        with path.open('r') as f:  # 'r' = read mode, f = file object that is created when the file is opened
            # read the json data from the file into a string called - json_data
            json_data_str: str = f.read()
            # parse the json from the string into a dictionary called - json_dict(dict is like json type in Python)
            json_data_dict: dict = json.loads(json_data_str)
            # save the data to the class
            self.load_data(json_data_dict)
            # when adding the "self." before the object - I can use this object in any func inside the class
        print(f"Finished to parse and load json {path}")

    def load_data(self, parsed_data: dict):
        print("Loading data to DataManipulator object")
        self.json_data_dict = parsed_data

    def process_data(self):
        print("Starting to process the parsed data")
        for key in self.json_data_dict:
            try:
                if isinstance(self.json_data_dict[key], str):  # check if the value of the key in the dict is a string
                    # because trying to parse a non-string value as a datetime object will raise a "TypeError"
                    # try to cast to date, if ok then its a date and change the year
                    try:
                        current_date = datetime.strptime(self.json_data_dict[key], '%Y/%m/%d %H:%M:%S')
                        # strptime - takes a string and parse it to 'datetime' object in this format
                        new_value = str(current_date.replace(year=2021))
                        # replace - takes a keyword argument (year=2021) and returns a new datetime object
                    except ValueError: # if it's a str but not a datetime, remove whitespaces
                        json_string: str = self.json_data_dict[key]
                        #splitted_str: str = str(json_string.strip())  # remove leading and trailing whitespaces
                        non_spaces_str = json_string.replace(" ", "")  # remove remaining whitespace characters within the sentence
                        new_value = non_spaces_str[::-1]  # start, stop and step = -1,starts from the end of the string
                    finally:
                        self.json_data_dict[key] = new_value

                elif isinstance(self.json_data_dict[key], list):  # if it's a list
                    new_list = list(set(self.json_data_dict[key]))  # parse to set type - automatically remove duplicates
                    self.json_data_dict[key] = new_list

            except ValueError:
                print("Bad input")

            except TypeError:
                print("Bad input")

        print("Finished processing data")

    def save_json(self, dest_path: Path):
        # if dest_path is None: # in case the user didn't enter a dest_path
        #     dest_path = Path("new_json_file.json")
        print(f"Saving data to json path: {dest_path}")
        with dest_path.open('w') as f:
            json.dump(self.json_data_dict, f)
        print(f"Saved json {dest_path}")

