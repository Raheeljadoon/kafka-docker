from time import sleep
from json import dumps
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                            value_serializer=lambda x: dumps(x).encode('utf-8'))



# for i in range(1000):
#     data = {"number":i}

#     producer.send("numtest", value=data)

#     sleep(4)


def test():
    for i in range(10):
        yield i*3
        sleep(4)



for k in test():
    producer.send("numtest", value=k)