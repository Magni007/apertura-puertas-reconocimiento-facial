from deepface import DeepFace

obj = DeepFace.analyze (img_path = "/home/mhernandez/apertura-puertas-reconocimiento-facial/deepface/faces/aigeneratedface2.jpg", actions = ['age', 'gender', 'race', 'emotion'])



print ("El resultado del analisis es: ")
print (obj)
