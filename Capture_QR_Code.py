import cv2
from pyzbar.pyzbar import decode
import os
from tkinter import messagebox as msgx



def QR_Code_Capturing(Condition=False):
    Captured = False
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    cv2.namedWindow("Adding New QR-Code", cv2.WINDOW_NORMAL)

    while Condition:
        ret, frame = cap.read()
        frame_W = cv2.resize(frame, (960, 540))

        if not ret:
            print("Failed to Grab Frame")
            break
        cv2.imshow("Adding New QR-Code", frame_W)
        k = cv2.waitKey(1)

        if k % 256 == 27:
            print("Window Destroyed Successfully")
            break
        elif k % 256 == 32:
            img_name = "QR-Code Captured.png"
            cv2.imwrite(img_name, frame)
            msgx.showinfo('QR-Code Captured', "QR-Code is Captured Successfully")

            Captured = True

    cap.release()
    cv2.destroyAllWindows()
    return Captured


def Decode_QR_Code():
    Code_Data = False
    Img_Taken = True
    Captured = QR_Code_Capturing(True)
    if Captured:
        img = cv2.imread('QR-Code Captured.png')
        decoded_list = decode(img)
        os.remove("QR-Code Captured.png")
        if decoded_list:
            for code in decoded_list:
                Code_Data = code.data.decode('utf-8')
                if len(Code_Data) != 16 or Code_Data[0:4] != '2166':
                    msgx.showerror("Invalid QR-Code Window","The QR-Code You Entered is Invalid!")
                    Img_Taken = False
                    return Img_Taken
                else:
                    msgx.showinfo("Decoded QR-Code Window", "QR-Code Entered, is Decoded Successfully!")
            return Code_Data
        else:
            msgx.showerror("Failed To Decode QR-Code Window", "Failed To Decode QR-Code, Please Take Picture Carefully, and Try Again.")
            Img_Taken = False
            return Img_Taken

    else:
        print("Picture Was not Taken!")
        Img_Taken = False
        return Img_Taken
