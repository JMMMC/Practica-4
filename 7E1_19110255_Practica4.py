import numpy as np
import cv2 #OpenCV
import imutils
import ctypes

user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

h = 600

img = cv2.imread('Troya.PNG',1)
rimg = imutils.resize(img,height = h)

fil = rimg.shape[0] #Filas
col = rimg.shape[1] #Columnas
dim = rimg.shape[2] #Dimencion

oscura = np.zeros((fil, col, dim))

cv2.line(oscura,(0,0),(col,fil),(255,0,0),round(fil/12))
cv2.line(oscura,(0,fil),(col,0),(255,0,0),round(fil/12))

cv2.circle(oscura,(round(col/2),round((fil/6)*5)), round(fil/12), (0,165,255), round(fil/60))
cv2.circle(oscura,(round(col/2),round(fil/6)), round(fil/12), (0,165,255), round(fil/60))

cv2.putText(oscura,'Princesa Azteca',(round(col/9),round((fil/20)*11)), cv2.FONT_HERSHEY_COMPLEX, fil/200, (93,193,0), round(fil/50), cv2.LINE_AA)

cv2.rectangle(oscura,(round(col/12),round(fil/3)),(round((col/12)*11),round((fil/3)*2)),(192,149,182),round(fil/30))

winname = "Oscura"
cv2.namedWindow(winname)
cv2.moveWindow(winname, round((ancho/2)-(col/2)),round((alto/2)-(fil/2)))
cv2.imshow(winname, oscura)
cv2.waitKey(0)
#cv2.destroyAllWindows()
cv2.destroyWindow(winname)

#select ROI function
roi = cv2.selectROI("select the area",rimg)

#print rectangle points of selected roi
print(roi)

#Crop selected roi from raw image
roi_cropped = rimg[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

#Nombre
name = input('¿Con que nombre quieres guardar a ROI? (Solo en nombre sin formato): ')
bild = name+'.PNG'
print("Guardada como:",bild)

#show cropped image
cv2.imshow("ROI", roi_cropped)
cv2.imwrite(bild,roi_cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
