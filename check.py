import time
import datetime
import json
import argparse
import adafruit_dht
import board
from google.cloud import pubsub_v1

def run(args):
    temperature, humidity = check_weather(args)
    if temperature:
        if args.runner == 'gcp':
            post_on_pubsub(args, temperature, humidity)
        else:
            print('Temperature: {:.1f} - Humidity: {:.1f}'.format(temperature, humidity))
    else:
        raise RuntimeError('Fail to get temperature')

def check_weather(args):
    dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)
    temperature = None
    humidity = None
    tries = 0
    while temperature == None and tries < 10:
        try:
            humidity = dhtDevice.humidity
            temperature = dhtDevice.temperature
        except RuntimeError as error:
            print(error.args[0])
            tries += 1
            time.sleep(3.0)
    return temperature, humidity

def post_on_pubsub(args, temperature, humidity):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(args.project_id, args.topic_id)
    data = json.dumps({
        'temperature': temperature,
        'humidity': humidity,
        'local_datetime': datetime.datetime.now().isoformat()
    }).encode('utf-8')
    future = publisher.publish(topic_path, data)
    print(f'published message id {future.result()}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--runner',
        dest='runner',
        default='local'
    )
    parser.add_argument(
        'project_id',
        dest='project_id',
        default=None
    )
    parser.add_argument(
        'topic_id',
        dest='topic_id',
        default=None
    )
    args = parser.parse_args()
    print(args)
    run(args)
