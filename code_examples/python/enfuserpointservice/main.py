from datetime import datetime

from enfuserpointservice.get_data import EnfuserAPI
from enfuserpointservice import parsing


"""
Add Test Script:
run with python -m enfuserpointservice.main
TODO: parameterize

"""

def main():
    api = EnfuserAPI()
    lat = 61.43
    lon = 23.86
    start = datetime.fromisoformat('2025-03-03T00:00:00.000Z')
    end = datetime.fromisoformat('2025-03-05T00:00:00.00Z')
    data = api.acquire(lat, lon, start, end)

    print(data)

    print(parsing.transform_to_xarray(data))

if __name__ == '__main__':
    main()
