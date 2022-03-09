import time 
import json
from kafka import KafkaProducer
from data import get_registered_user


def json_serializer(data):
    return json.dumps(data).encode("utf-8")

def get_partitions(key,all,availaible):
    return 0                    #for sending data to only partition 1

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                            value_serializer=json_serializer,
                            # partitioner=get_partitions)
                        )

if __name__ == "__main__":
    while 1 == 1:
        registered_user = get_registered_user()
        print(registered_user)
        producer.send("test_consumer", registered_user)
        time.sleep(4)

