import sys
from datetime import datetime

from enfuserpointservice.get_data import EnfuserAPI
from enfuserpointservice import parsing


"""
Add Test Script:

# Fetch list of regions
python enfuserpointservice/main.py --regions
-> 
[{'region': 'Finland', 'areas': [
{'area': 'Tampere', 'coordinates': [[61.39344495747374, 23.501005884425652], [61.57314495747374, 24.03520588442565]]},
{'area': 'pks', 'coordinates': [[60.11905840960239, 24.593882376237627], [60.35405840960239, 25.187882376237624]]},
{'area': 'tku', 'coordinates': [[60.37804498518611, 22.043908814589667], [60.52304498518611, 22.463908814589665]]}]}]


# Fetch one point
python -m enfuserpointservice.main


TODO: parameterize

"""

def main():
    api = EnfuserAPI()

    if '--regions' in sys.argv:
        data = api.get_regions()
        print(data)
        return

    lat = 61.43
    lon = 23.86
    start = datetime.fromisoformat('2025-03-03T00:00:00.000Z')
    end = datetime.fromisoformat('2025-03-03T03:00:00.00Z')
    data = api.acquire(lat, lon, start, end)

    if '--json' in sys.argv:
        print(data)
    else:
        print(parsing.transform_to_xarray(data))

if __name__ == '__main__':
    main()
