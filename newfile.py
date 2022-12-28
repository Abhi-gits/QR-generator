#code to convert text into qr code
import qrcode
import random
import pandas as pd

df = pd.read_excel("data_file.xlsx")
# print(df)

df['Student name'] = df['Student name'].str.strip()
df.dropna(axis=0, subset=['Roll No.'], inplace=True)
# df
rol = df.iloc[:,4]
l = rol.to_list()

for i in l:
    
    # generating a QR code using the make() function  
    qr_img = qrcode.make(i)  
    count = random.randint(1, 99999999999999999999999999999999999999)
    if (count > 0):             
        name = 'qrfile/'+"qr-img"+ str(count) +".jpg"
        qr_img.save(name)   
    print("QR saved")
print("All files convertad into qr code")












# #to read QR code image
# # importing the OpenCV library  
# import cv2  
# # reading the image  
# qr_img = cv2.imread(name)  
# # using the QRCodeDetector() function  
# qr_det = cv2.QRCodeDetector()  
# # using the detectAndDecode() function  
# val, pts, st_code = qr_det.detectAndDecode(qr_img)  
# # printing the value  
# print("Information:", val)  