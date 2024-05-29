# Importar Bibliotecas
from deepface import DeepFace
import pandas as pd
import paho.mqtt.client as mqtt_client
import random
import time
import argparse

# Parser
parser = argparse.ArgumentParser()
parser.add_argument("img_src", help="Imagen a buscar en la DB de caras")
parser.add_argument("db_path", help="Ruta de la base de datos de caras")
args = parser.parse_args()

# Variables y constantes
broker = 'broker.hivemq.com'
port = 1883
topic = "codigoIoT/mqtt/python"
topic2 = "codigoIoT/mqtt/index"
client_id = "007"  # Cliente fijo para identificar la conexión

# Conexión al broker MQTT
def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    # Especificar el callback_api_version
    client = mqtt_client.Client(client_id=client_id, protocol=mqtt_client.MQTTv311)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client, mensaje):
    time.sleep(1)
    msg = mensaje
    result = client.publish(topic, msg)
    time.sleep(1)
    print(result)
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

### Inicio del programa
# Buscar Rostro
print("Buscando rostro")

# models = [
#   "VGG-Face", 
#   "Facenet", 
#   "Facenet512", 
#   "OpenFace", 
#   "DeepFace", 
#   "DeepID", 
#   "ArcFace", 
#   "Dlib", 
#   "SFace",
#   "GhostFaceNet",
# ]

# metrics = ["cosine", "euclidean", "euclidean_l2"]

df = DeepFace.find(img_path=args.img_src, db_path=args.db_path,enforce_detection=False)
print("Resultado ")
print(df)

# Convertir el DataFrame a JSON
df = pd.concat(df, ignore_index=True)
json_view = df.to_json()
print("La expresion en JSON de los resultados es: ")
print(df)

# Enviar mensaje MQTT
client = connect_mqtt()
client.loop_start()
publish(client, json_view)




#client = connect_mqtt()
#print(type(client))  # Debería imprimir <class 'paho.mqtt.client.Client'>
#client.loop_start()



