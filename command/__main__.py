from argparse import ArgumentParser
from utils.FileManager import gen_seed_data, read_data

parser = ArgumentParser()
parser.add_argument("-id", "--user_id", type=int)
parser.add_argument("-op", "--operation", type=int)

def get_operation(x):
	return {
		1: gen_seed_data,
		2: read_data
	}.get(x, not_a_valid_operation)

def not_a_valid_operation():
	print_usage()

def print_usage():
	print("Usage: python3 -id <user_id> -op <operation number from 1 to 4>")

args = parser.parse_args()
if args.user_id is None or args.operation is None:
	print_usage()
else:
	get_operation(args.operation)()