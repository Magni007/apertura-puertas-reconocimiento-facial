from deepface import DeepFace

print ("Se han comparado 2 imagenes. Se verificara que la persona sea la misma")
print ("Cargando...")

# result = DeepFace.verify(img1_path = "img1.jpg", img2_path = "img2.jpg")
result = DeepFace.verify(img1_path = "/home/mhernandez/apertura-puertas-reconocimiento-facial/deepface/faces/aigeneratedface2.jpg", img2_path = "/home/mhernandez/apertura-puertas-reconocimiento-facial/deepface/faces/carrie2.png")
# result = DeepFace.verify(img1_path = "/home/mhernandez/apertura-puertas-reconocimiento-facial/deepface/carrie1.png", img2_path = "/home/mhernandez/apertura-puertas-reconocimiento-facial/deepface/carrie2.png")

print ("Resultados")
print (result)
