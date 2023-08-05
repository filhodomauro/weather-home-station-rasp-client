import sys
import argparse
import adafruit_dht
import board

def run(args):
    temperature = 0
    humidity = 0
    try:
        temperature, humidity = check_weather(args)
    except RuntimeError as error:
        print(error.args[0])
        temperature, humidity = check_weather(args) 
    if args.runner == 'gcp':
        post_on_pubsub(args, temperature, humidity)
    else:
        print('Temperature: {:.1f} - Humidity: {:.1f}'.format(temperature, humidity))

def check_weather(args):
    dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)
    temperature = dhtDevice.temperature
    humidity = dhtDevice.humidity
    return temperature, humidity

def post_on_pubsub(args, temperature, humidity):
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--runner',
        dest='runner',
        default='local'
    )
    args = parser.parse_args()
    print(args)
    run(args)
