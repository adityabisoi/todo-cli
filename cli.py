import argparse
from priorityQueue import addToHeap, removeFromHeap

parser=argparse.ArgumentParser()

parser.add_argument('task',type=str,help='Name of the task')
parser.add_argument('--p',type=int,choices=[1,2,3],help='Priority Level')

args=parser.parse_args()

if args.task=='pop':
    print(removeFromHeap())
else:
    addToHeap(args.task, args.p)