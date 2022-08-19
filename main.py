import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
import cvzone
import os
import time
import pyautogui
import screen_brightness_control as sbc


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)
keys = [["Chrome", "Notepad", "SwApp"],
        ["?sapp", "Librewlf", "Sound+"],
        ["Bright-", "Bright+", "Sound-"]]
finalText = ""


def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        # print(x, y)
        cvzone.cornerRect(img, (button.pos[0], button.pos[1], button.size[0], button.size[1]),
                          20, rt=0)
        cv2.rectangle(img, button.pos, (x + w, y + h), (0, 100, 240), cv2.FILLED)
        cv2.putText(img, button.text, (x + 20, y + 65),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
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

while True:
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
                cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (175, 0, 175), cv2.FILLED)
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
                        sleep(3)
                        pyautogui.write('youtube.com', interval=0.05)
                        pyautogui.press('enter')
                        sleep(3)
                        time.sleep(5)
                        pyautogui.hotkey('win', 'down')

                    elif aakashkey1 == 'Notepad':
                        command = "subl"
                        os.system(command)
                        time.sleep(1)
                        pyautogui.hotkey('ctrl', 'n')

                        pyautogui.write('Hello forbes how are you , this is the Partial project of Ranjan kumar'
                                        '\nif (WantToSee == FullProject):\n\n\tPlease wait till Final Review.\n\n',
                                        interval=0.05)
                        pyautogui.press('enter')
                        pyautogui.press('backspace', presses=3)
                        pyautogui.write('\nelse:\n\n\tNo way to see,you cant find AnyWhere.', interval=0.05)
                        # pyautogui.press('volumedown')
                        time.sleep(0.1)
                        # sleep(3)
                        time.sleep(5)
                        pyautogui.hotkey('win', 'down')

                    elif aakashkey1 == 'SwApp':
                        # command = "start msedge"
                        # os.system(command)
                        # time.sleep(5)
                        # pyautogui.hotkey('win', 'down')
                        pyautogui.keyDown('alt')
                        # time.sleep(1)
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
                    #     time.sleep(5)
                    #     pyautogui.hotkey('win', 'down')

                    elif aakashkey1 == "?sapp":
                        pyautogui.hotkey('win', 'r')
                        time.sleep(0.5)
                        pyautogui.typewrite('https://web.whatsapp.com/send?phone=+9779825830731')
                        pyautogui.press('enter')
                        time.sleep(10)
                        pyautogui.press('tab', presses=10, interval=0.1)

                        pyautogui.typewrite('Hello Aakash This is Auto Typed Message', interval=0.1)
                        pyautogui.press('enter')
                        time.sleep(1)
                        pyautogui.typewrite('This is again second Auto Typed Message, dont want to Spam so,',
                                            interval=0.1)
                        pyautogui.press('enter')
                        time.sleep(1)
                        pyautogui.typewrite('BYE', interval=0.1)
                        pyautogui.press('enter')
                        time.sleep(5)
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

                    sleep(0.15)

    cv2.imshow("GESTURE SYSTEM CONTROL", img)
    cv2.waitKey(1)
