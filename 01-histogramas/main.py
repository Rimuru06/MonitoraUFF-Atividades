import cv2 as cv


def histogram():
    image = cv.imread("01-histogramas\10097610.jpg")
    cv.imshow("Imagem", image)
    

if __name__ == "__main__":
    histogram()