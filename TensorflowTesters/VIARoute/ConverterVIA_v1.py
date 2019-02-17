import json
directory = 'Beach_40'

jsonloaded=json.load(open('./'+directory+'/via_region_data.json'))
for key, value in jsonloaded.items():
    data = {}
    data[value['filename']] = value['regions']


    with open('./'+directory+'/'+value['filename'][:-4]+'.json', 'w') as outfile:
        json.dump(data, outfile)

