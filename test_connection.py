from pymongo import MongoClient

client = MongoClient("mongodb+srv://myAtlasDBUser:Vpr6rUqfaZFrN5MQ@myatlasclusteredu.ngzslnw.mongodb.net/avicola?retryWrites=true&w=majority&appName=myAtlasClusterEDU")
db = client["avicola"]

try:
    print("Conexión exitosa. Bases de datos disponibles:", client.list_database_names())
except Exception as e:
    print("Error en la conexión:", str(e))