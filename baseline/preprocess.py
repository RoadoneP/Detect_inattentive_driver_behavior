import json
import cv2
from tqdm import tqdm
import os

path='/DATA/Final_DATA/task03_train'
json_name='labels'

reverse_names = { 'eye_opened':0 , 'eye_closed':1, 'mouth_opened':2,'mouth_closed' : 3, 'face' : 4, 'phone':5, 'cigar': 6}
with open(path+'/'+json_name+'.json', 'r') as f:
  json_data = json.load(f)
  dict = json_data['annotations']
print(f"number of dict: {len(dict)}")

if not os.path.isdir(path+'/labels'):
  os.mkdir(path+'/labels')

for i in tqdm(range(len(dict))):
  shape = cv2.imread(path+'/images/' + dict[i]['file_name']).shape

  with open(path+'/labels/' + dict[i]['file_name'][:-3] + 'txt', 'w') as f:

    line = '' 
    for j in range(len(dict[i]['objects'])):
      position = dict[i]['objects'][j]['position']
      class_ = reverse_names[dict[i]['objects'][j]['class']]
      x = ((position[0] + position[2]) / 2)/shape[1]
      y = ((position[1] + position[3]) / 2)/shape[0]
      w = (position[2] - position[0])/shape[1]
      h = (position[3] - position[1])/shape[0]
      line += '%d %f %f %f %f\n'%(class_, x, y, w, h)
    f.write(line)

f.close()

 
