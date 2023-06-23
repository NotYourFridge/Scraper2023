import hdfs

client = hdfs.InsecureClient('http://localhost:9870/')

with open('C:\Users\MrFre\txt files hadoop\reviewsAdidas.txt', 'rb') as r:
    data = r.read()
    client.write("/data/AdidasRevs.txt", data)

with open('C:\Users\MrFre\txt files hadoop\reviewsNike.txt', 'rb') as r:
    data = r.read()
    client.write("/data/NikeRevs.txt", data)

with open('C:\Users\MrFre\txt files hadoop\reviewsVans.txt', 'rb') as r:
    data = r.read()
    client.write("/data/VansRevs.txt", data)
with open('C:\Users\MrFre\txt files hadoop\imagesBristol.txt', 'rb') as r:
    data = r.read()
    client.write("/data/ImagesBT.txt", data)
    