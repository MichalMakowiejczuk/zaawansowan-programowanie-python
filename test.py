import cv2


def detect_people(image_path):
    # Wczytanie obrazu
    image = cv2.imread(image_path)

    # Utworzenie detektora ludzi
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
    
    # Wykrywanie ludzi na obrazie
    (rects, weights) = hog.detectMultiScale(image, scale=1.09, winStride=(4, 4), padding=(8, 8))

    # Zaznaczanie ludzi na obrazie
    for (x, y, w, h) in rects:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Kodowanie obrazu do formatu (JPEG)
    success, encoded_image = cv2.imencode('.jpg', image)
    
    if success:
        image_bytes = encoded_image.tobytes()
    else:
        image_bytes = None

    return len(rects), image_bytes



if __name__ == "__main__":
    image_path = "pic/sample1.jpg"  # Ścieżka do jpg
    num_people, image_data = detect_people(image_path)

    if image_data:
        # Zapisanie obrazu do pliku (opcjonalnie)
        with open('detected_people_variable.jpg', 'wb') as f:
            f.write(image_data)
        print(f'Wykryto {num_people} osób.')
    else:
        print('Błąd podczas kodowania obrazu.')