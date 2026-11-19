"""004 更新指定记录。"""
import argparse
from _common import make_client, parse_fields, write_flag, preview, output, result

p = argparse.ArgumentParser()
p.add_argument("worksheet")
p.add_argument("rowid")
p.add_argument("fields")
write_flag(p)
a = p.parse_args()
fields = parse_fields(a.fields)
if preview(a, "editRow", {"worksheet": a.worksheet, "rowid": a.rowid, "fields": [x["controlId"] for x in fields]}):
    output(result(make_client(a.worksheet).edit(a.rowid, fields)))
