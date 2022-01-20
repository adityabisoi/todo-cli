import argparse
from test import func

parser=argparse.ArgumentParser()

parser.add_argument('name',type=str)

args=parser.parse_args()

print(args.name)
