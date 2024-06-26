import cv2
import os
mainfolder = 'images'
myfolders = os.listdir(mainfolder)
print(myfolders)

for folder in myfolders:
    path = mainfolder+'/'+folder
    images=[]
    mylist = os.listdir(path)
    print(f'total no of images detected {len(mylist)}')
    for i in mylist:
        curimg = cv2.imread(f'{path}/{i}')
        curimg = cv2.resize(curimg, (0,0), None, 0.5, 0.5)
        images.append(curimg)
    
    stitcher = cv2.Stitcher.create()
    (status, result) = stitcher.stitch(images)
    
    if (status == cv2.STITCHER_OK):
        print('generated panorama')
        cv2.imshow(folder,result)
        
    else:
        print('not generated')

cv2.waitKey(0)