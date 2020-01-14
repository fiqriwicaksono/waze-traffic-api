import urllib.request, json

# This script extract the waze-traffic api data into json files
# By: Fiqri Wicaksono
def cleanline(data):
    # Cleaning the line data in jams category to make it query-able
    for i in range(len(data['jams'])):
        data['jams'][i]['jams_line'] = []
        for a in data['jams'][i]['line']:
            element = dict(lat=a[1], long=a[0])
            data['jams'][i]['jams_line'].append(element)
        data['jams'][i].pop('line')
        data['jams'][i]['line'] = data['jams'][i].pop('jams_line')

def getdata(url):
    with urllib.request.urlopen(url) as link:
        data = json.loads(link.read().decode())
        cleanline(data)
        return data['alerts'], data['irregularities'], data['jams']

def getjson(url):
    # There are 3 categories in waze-traffic api (alerts, irregularities, jams)
    # You can customize based on your needs
    alerts, irregularities, jams = getdata(url)
    json_list = [alerts, irregularities, jams]
    json_name = ['alerts', 'irregularities', 'jams']
    for i in range(len(json_name)):
        with open(f'{json_name[i]}.json','w') as f:
            json.dump(json_list[i], f)
    print(f'Total record is: {len(jams)}')

def main():
    # Filter by date/time
    datetime_filter = "%Y-%m-%dT%H:%M:%S" # It has to follow this format
    # Enter your waze-traffic api url
    url = f'<your-waze-traffic-api-url>/$start_time={datetime_filter}'
    getjson(url)

if __name__ == '__main__':
    main()
