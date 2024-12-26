faceLoc  = face_recognition.face_locations(imgElon)[0]
encodeElon =face_recognition.face_encodings(imgElon)[0]

cv2.rectangle(imgElon,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)


faceLocTest  = face_recognition.face_locations(imgtest)[0]
encodeTest =face_recognition.face_encodings(imgtest)[0]

cv2.rectangle(imgtest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)

results = face_recognition.compare_faces([encodeElon],encodeTest)
faceDis = face_recognition.face_distance([encodeElon],encodeTest)