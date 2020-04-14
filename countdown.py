import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--time", type=int, help="The seconds to countdown", default=10)
args = parser.parse_args()

sec = args.time

for i in range(sec, 0, -1):
    time.sleep(1)
    print(i)
