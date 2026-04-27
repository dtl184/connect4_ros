import cv2

points = []

def click_event(event, x, y, flags, param):
    global points, img
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print(f"Clicked: ({x}, {y})")
        cv2.circle(img, (x, y), 6, (0, 0, 255), -1)
        cv2.putText(img, str(len(points)), (x + 8, y - 8),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        cv2.imshow("image", img)

img = cv2.imread("paper_frame.jpg")
cv2.imshow("image", img)
cv2.setMouseCallback("image", click_event)

print("Click the 4 paper corners in this order:")
print("1. top-left")
print("2. top-right")
print("3. bottom-right")
print("4. bottom-left")

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Final points:")
print(points)