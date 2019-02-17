import cv2
import os



inputname='TumeBeach'
format = 'mp4'
vidcap = cv2.VideoCapture('./input/'+inputname+'.'+format)
success,image = vidcap.read()
count = 0

directory = './'+inputname

if not os.path.exists(directory):
    os.makedirs(directory)
if not os.path.exists(directory+'/people'):
    os.makedirs(directory+'/people')
if not os.path.exists(directory+'/negative'):
    os.makedirs(directory+'/negative')



while success:
  if count %125==0:
    cv2.imwrite(directory +'/'+inputname+'frame%d.jpg' % count, image)     # save frame as JPEG file
    print('Wrote a new train frame: ', count, ' ', success)
  
  success,image = vidcap.read()
  print('Read a new frame: ',count,' ', success)
  count += 1