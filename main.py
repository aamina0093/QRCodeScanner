import cv2
QrScan = cv2.QRCodeDetector()
ScanValue = QrScan.detectAndDecode(cv2.imread("qrtest.png"))
print(ScanValue)
