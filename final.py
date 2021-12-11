import cv2
import mediapipe as mp
import time
import keyboard

cap = cv2.VideoCapture("hand.mp4") # or put it to "1" to use the webcam if u have

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        pos_num = [0]
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                #print(id, cx, cy)
                data = [id, cx, cy]
                print(data)
                with open('D:\programming\computer vision\listfile12.txt', 'a') as filehandle:
                    for listitem in data:
                        filehandle.write('%s\n'%listitem)
                        #filehandle.close()
                        #if keyboard.press("ctrl"):
                            #filehandle.write('%s\n' % listitem +(pos_num + 1)+"**")

                # if id == 4:
                cv2.circle(img, (cx, cy), 8, (255, 0, 255), cv2.FILLED) # circle colore and size

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 50, 255), 3)

    cv2.imshow("the vid", img)
    #cv2.waitKey(0)
    if cv2.waitKey(1) == ord('q'): # quit window
        break
cap.release()
cv2.destroyAllWindows


