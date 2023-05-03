import csv
from typing import List

INPUT_DATA_PATH = './resources/data/rides.csv'


def read_csv(resource_path: str = INPUT_DATA_PATH) -> List[str]:
    records = []
    with open(resource_path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)  # skip the header
        for row in reader:
            records.append(', '.join(row))
        return records

def delivery_report(err, msg):
    if err is not None:
        print("Delivery failed for record {}: {}".format(msg.key(), err))
        return
    print('Record:{} successfully produced to topic:{} partition:[{}] at offset:{}'.format(
        msg.key(), msg.topic(), msg.partition(), msg.offset()))
