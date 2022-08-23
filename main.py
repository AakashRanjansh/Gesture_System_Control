import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import os
import time
import pyautogui
import screen_brightness_control as sbc
import speech_recognition as sr
from pywhatkit.core import core
import webbrowser as web

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8,maxHands=1)
keys = [["Chrome", "Notepad", "SwApp"],
        ["?sapp", "Librewlf", "Sound+"],
        ["Bright-", "Bright+", "Sound-"]]
finalText = ""

def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0], button.size[1]),
                          20, rt=0)
        cv2.rectangle(img, button.pos, (x + w, y + h), (0, 100, 240), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
        # icon = cv2.imread('download.png')
        # size = 100
        # icon = cv2.resize(icon,(size,size))

    return img


class Button:
    def __init__(self, pos, text, size=[300, 85]):
        self.pos = pos
        self.size = size
        self.text = text


buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([450 * j + 50, 200 * i + 50], key))  # left increase Horizontal size

while cap.isOpened():
    success, in_img = cap.read()
    img = cv2.flip(in_img, 1)

    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)
    img = drawAll(img, buttonList)

    # print(detector.lmList)
    # print("\n")

    if lmList:
        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            if x < lmList[8][0] < x + w and y < lmList[8][1] < y + h:
                cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5),
                              (175, 0, 175), cv2.FILLED)
                cv2.putText(img, button.text, (x + 20, y + 65),
                            cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                l, _, _ = detector.findDistance(8, 12, img, draw=False)
                print(l)

                # when clicked
                if l < 35:
                    cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                    # print(x,y)
                    cv2.putText(img, button.text, (x + 20, y + 65),
                                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                    aakashkey1 = button.text

                    if aakashkey1 == 'Chrome':
                        command = "Start chrome"
                        os.system(command)
                        time.sleep(3)
                        pyautogui.write('youtube.com', interval=0.05)
                        pyautogui.press('enter')
                        time.sleep(3)
                        time.sleep(5)
                        pyautogui.hotkey('win', 'down')

                    elif aakashkey1 == 'Notepad':
                        command = "subl"
                        os.system(command)
                        time.sleep(1)
                        pyautogui.hotkey('ctrl', 'n')

                        pyautogui.write('Hello folks how are you, this is the Ongoing project of Ranjan kumar'
                                        '\nif (WantToSee == FullProject):\n\n\tPlease wait till completion.\n\n',
                                        interval=0.05)
                        pyautogui.press('enter')
                        pyautogui.press('backspace', presses=3)
                        pyautogui.write('\nelse:\n\n\tNo way to see,you cant find AnyWhere.', interval=0.05)
                        time.sleep(0.1)
                        time.sleep(5)
                        pyautogui.hotkey('win', 'down')

                    elif aakashkey1 == 'SwApp':
                        pyautogui.keyDown('alt')
                        pyautogui.press('tab', )
                        time.sleep(0.1)
                        pyautogui.press('tab', )
                        time.sleep(0.1)
                        pyautogui.press('tab')
                        time.sleep(1)
                        pyautogui.keyUp('alt')

                    # elif aakashkey1 == 'Librewlf':
                    #     command = "librewolf.exe"
                    #     os.system(command)

                    elif aakashkey1 == "?sapp":
                        web.open("https://web.whatsapp.com/send?phone=+9779825830731")
                        time.sleep(7)
                        pyautogui.click(core.WIDTH / 2, core.HEIGHT / 2)
                        time.sleep(3)
                        pyautogui.click()
                        time.sleep(0.5)


                        pyautogui.typewrite('Hello Aakash This is Auto Typed Message', interval=0.05)
                        pyautogui.press('enter')
                        time.sleep(1)
                        pyautogui.typewrite('Now This is Switching To Manual Voice Typing Mode',
                                            interval=0.1)
                        pyautogui.press('enter')
                        time.sleep(1)
                        r = sr.Recognizer()

                        # listening the speech and store in audio_text variable
                        while True:
                            with sr.Microphone() as source:
                                audio_text = r.listen(source)

                                try:
                                    SPtotext = r.recognize_google(audio_text)
                                except:
                                    print("Sorry, I did not get that")
                                    break

                            Aakash = str(SPtotext)
                            Ranjan = Aakash.lower()
                            print(SPtotext)
                            if Ranjan == "exit":
                                break

                            pyautogui.typewrite(SPtotext, interval=0.1)
                            pyautogui.press('enter')

                        time.sleep(1)
                        pyautogui.hotkey('win', 'down')

                    elif aakashkey1 == "Sound+":
                        pyautogui.press('volumeup')
                        time.sleep(0.05)

                    elif aakashkey1 == "Sound-":
                        pyautogui.press('volumedown')
                        time.sleep(0.05)

                    elif aakashkey1 == "Bright+":
                        sbc.set_brightness('+20')
                        time.sleep(0.15)

                    elif aakashkey1 == "Bright-":
                        sbc.set_brightness('-20')
                        time.sleep(0.15)

                    else:
                        pyautogui.alert(text='We Cant this find software on this System', title='  Alert  ',
                                        button='OK')
                        # print("No input")

                    time.sleep(0.15)

    cv2.imshow("GESTURE SYSTEM CONTROL", img)
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
