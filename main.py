import cv2 as cv
import tello_drone as tello

host = ''
port = 9000
local_address = (host, port)
drone = tello.Tello(host, port, is_dummy=False)
manual_mode = True


def adjust_tello_position(offset_x, offset_y, offset_z):
    if not -90 <= offset_x <= 90 and offset_x != 0:
        if offset_x < 0:
            drone.rotate_ccw(20)
        elif offset_x > 0:
            drone.rotate_cw(20)

    if not -70 <= offset_y <= 70 and offset_y != -30:
        if offset_y < 0:
            drone.move_up(20)
        elif offset_y > 0:
            drone.move_down(20)

    if not 15000 <= offset_z <= 30000 and offset_z != 0:
        if offset_z < 15000:
            drone.move_forward(100)
        elif offset_z > 30000:
            drone.move_backward(100)


face_cascade = cv.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
frame_read = drone.get_frame_read()

while True:
    frame = frame_read.frame
    cap = drone.get_video_capture()

    height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
    width = cap.get(cv.CAP_PROP_FRAME_WIDTH)

    center_x = int(width / 2)
    center_y = int(height / 2)
    cv.circle(frame, (center_x, center_y), 10, (0, 255, 0))

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, minNeighbors=5)

    face_center_x = center_x
    face_center_y = center_y
    z_area = 0
    for face in faces:
        (x, y, w, h) = face
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)

        face_center_x = x + int(h / 2)
        face_center_y = y + int(w / 2)
        z_area = w * h

        cv.circle(frame, (face_center_x, face_center_y), 10, (0, 0, 255))

    offset_x = face_center_x - center_x
    offset_y = face_center_y - center_y - 30

    #battery_level = drone.query_battery()
    '''
    Battery display issues unfixable at cuurent status
    '''

    cv.putText(frame, f'[{offset_x}, {offset_y}, {z_area}]', (10, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2,
               cv.LINE_AA)
    cv.putText(frame, f'[Manual: {manual_mode}]', (10, 150), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 2,
               cv.LINE_AA)
    #cv.putText(frame, f'Battery: {battery_level}%', (10, 250), cv.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)

    if manual_mode:
        key = cv.waitKey(1) & 0xFF
        if key == ord('q'):
            drone.rotate_ccw(25)
        elif key == ord('e'):
            drone.rotate_cw(25)
        elif key == ord('w'):
            drone.move_forward(50)
        elif key == ord('s'):
            drone.move_backward(50)
        elif key == ord('a'):
            drone.move_left(50)
        elif key == ord('d'):
            drone.move_right(50)
        elif key == ord('r'):
            drone.move_up(50)
        elif key == ord('f'):
            drone.move_down(50)
        elif key == ord(' '):
            manual_mode = False
    else:
        adjust_tello_position(offset_x, offset_y, z_area)

        key = cv.waitKey(1) & 0xFF
        if key == ord(' '):
            manual_mode = True

    cv.imshow('Tello controller by TT', frame)

    if cv.waitKey(1) == ord('l'):
        break

    if cv.waitKey(1) == ord('p'):
        cv.imwrite("picture.png", frame_read.frame)

drone.end()
cv.destroyAllWindows()


