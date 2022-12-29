import face_recognition

face = face_recognition.load_image_file('media\images\Abdulhamid.PNG')
face_encoding = face_recognition.face_encodings(face)[0]
print(face_encoding)
