import cv2, pytesseract, sys
from googletrans import Translator

arti = Translator()

#Change this path to your own
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def fungsi(text):
    # change src and dest to your languange
    result = arti.translate(text, src='en', dest='id')
    print(result.text)

def main ():
    data = cv2.VideoCapture(0)
    img_counter = 0
    while True:
        ret, frame = data.read()
        if not ret:
            print("gagal")
            break
        cv2.imshow("Visit >> github.com/Anasg4 ", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC for exit
            print("Close program")
            break
        elif k%256 == 32:
            # SPACE for take the photo
            try :
                img_name = "gambar_{}.png".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1
                text = pytesseract.image_to_string(img_name)
                print(text)
                fungsi(text)
            except:
                print("Cant Read your photo, NO Words or Your Camera Suck !!!\n Try to Capture Again ^^v")

if __name__ == '__main__':
    print("Photo Translate\n github.com/Anasg4")
    a = input("Type 'on' to open the camera\n >> ")
    if a == "on":
        main()
    else:
        print("U are Robot >__<")
        sys.exit()




