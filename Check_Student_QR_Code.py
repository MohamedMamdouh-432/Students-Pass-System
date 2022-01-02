def Main_Check_QR_Code():
    import cv2
    import numpy as np
    from pyzbar.pyzbar import decode
    import pandas
    from tkinter import messagebox as msgx

    xls = pandas.ExcelFile('CollegeData.xlsx')
    df1 = pandas.read_excel(xls,'Students')
    df2 = pandas.read_excel(xls,'Lecturers')

    list1 = df1['College Id'].tolist()
    list2 = df2['College Id'].tolist()
    List = list1 + list2

    QR_Code_List = [str(i) for i in List]

    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

    cap.set(3,640)
    cap.set(4,480)
    Passed = False
    while True:
        success, img = cap.read()
        decoded_image = decode(img)
        if success and decoded_image is not None:
            for barcode in decode(img):
                myData = barcode.data.decode('utf-8')

                if myData in QR_Code_List:
                    myOutput = 'Authorized'
                    myColor = (0,255,0)
                    Passed = True
                else:
                    myOutput = 'Un-Authorized'
                    myColor = (0,0,255)
                    Passed = False

                pts = np.array([barcode.polygon],np.int32)
                pts = pts.reshape((-1,1,2))
                cv2.polylines(img,[pts],True,myColor,5)
                pts2 = barcode.rect

                cv2.putText(img,myOutput,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
                        0.9,myColor,3)

            cv2.imshow("QR-Code Student's ID Scanner ",img)
            k = cv2.waitKey(1)
            if k % 256 == 27:
                msgx.showinfo("QR-Code Checking Window", "QR-Code Checking Window is Destroyed Successfully")
                #print("Window Destroyed Successfully")
                break

    cap .release()
    cv2.destroyAllWindows()
    return Passed




