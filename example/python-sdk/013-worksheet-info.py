"""013 获取工作表结构。"""
import argparse
from _common import make_client, output, result

parser = argparse.ArgumentParser()
parser.add_argument("worksheet")
args = parser.parse_args()
sdk = make_client(args.worksheet)
output(result(sdk.exec(sdk.WORKSHEET_MAP_URL)))
