import os
import json
import csv

bboxes=[]
labels=[]
filenames=[]
data={}
data['files']=[]

directory = "test"
for filename in os.listdir('./'+directory+'/'):
	if filename.endswith(".json"):
	
	    jsonloaded = json.load(open('./'+directory+'/'+filename))
	    for key, value in jsonloaded.items():
	        try:
	            #test if there is a value to store
	            a=(value[0]['shape_attributes'])
	            data['files'].append({key: value})
	            # print(data['files'])
	        except:
	            pass


with open(directory+'_labels.csv', mode='w', ) as employee_file:
	for file in data['files']:
	    temp_dict=file[next(iter(file))]
	    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
	    
	    for roi in temp_dict:
	        #print(roi)
	        label = "#NA"
	        for key, value in roi['region_attributes']['label'].items():
	        	label = key
	        	
	        employee_writer.writerow([str(next(iter(file))),max(roi['shape_attributes']['all_points_x'])-min(roi['shape_attributes']['all_points_x']),max(roi['shape_attributes']['all_points_y'])-min(roi['shape_attributes']['all_points_y']),label,min(roi['shape_attributes']['all_points_x']),min(roi['shape_attributes']['all_points_y']),max(roi['shape_attributes']['all_points_x']),max(roi['shape_attributes']['all_points_y'])])
	        #print([str(next(iter(file))),label,min(roi['shape_attributes']['all_points_x']),min(roi['shape_attributes']['all_points_y']),max(roi['shape_attributes']['all_points_x']),max(roi['shape_attributes']['all_points_y'])])

