from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-id", "--user_id", type=int)
parser.add_argument("-op", "--operation", type=int)

args = parser.parse_args()
if args.user_id is None or args.operation is None:
	print("Usage: python3 -id <user_id> -op <operation number>")
else:
	print("id:", args.user_id, ", operation:", args.operation)