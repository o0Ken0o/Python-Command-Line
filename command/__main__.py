from argparse import ArgumentParser
from utils.FileManager import gen_seed_data, read_data, send_email

parser = ArgumentParser()
parser.add_argument("-id", "--user_id", type=int)
parser.add_argument("-op", "--operation", type=int)

def print_usage():
	print("Usage: python3 -id <user_id> -op <operation number from 1 to 4>")

args = parser.parse_args()
if args.user_id is None or args.operation is None:
	print_usage()
elif args.operation == 1:
	gen_seed_data()
elif args.operation == 2:
	read_data()
elif args.operation == 3:
	send_email(args.user_id)
else:
	print_usage()
















