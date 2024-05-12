import cv2

def detect_people(image_path):
    # Wczytanie obrazu
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Utworzenie detektora ludzi
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    
    # Wykrywanie ludzi na obrazie
    (rects, weights) = hog.detectMultiScale(gray, scale=1.09, winStride=(4, 8))

    # Zaznaczanie ludzi na obrazie
    for (x, y, w, h) in rects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Zapisywanie obrazu z zaznaczonymi ludźmi
    output_image_path = "detected_people.jpg"
    cv2.imwrite(output_image_path, image)

    return len(rects), output_image_path

if __name__ == "__main__":
    image_path = "pic/sample3.jpg"  # Ścieżka do zdjęcia
    num_people, output_image_path = detect_people(image_path)
    print("Liczba wykrytych ludzi:", num_people)
    print("Zapisano obraz z zaznaczonymi ludźmi:", output_image_path)
