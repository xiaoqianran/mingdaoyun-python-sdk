"""009 获取记录总数。"""
import argparse
from _common import make_client, output, result

p = argparse.ArgumentParser()
p.add_argument("worksheet")
a = p.parse_args()
output({"worksheet": a.worksheet, "count": result(make_client(a.worksheet).count())})
