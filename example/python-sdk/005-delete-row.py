"""005 删除指定记录。"""
import argparse
from _common import make_client, write_flag, preview, output, result

p = argparse.ArgumentParser()
p.add_argument("worksheet")
p.add_argument("rowid")
write_flag(p)
a = p.parse_args()
if preview(a, "deleteRow", {"worksheet": a.worksheet, "rowid": a.rowid}):
    output(result(make_client(a.worksheet).delete(a.rowid)))
