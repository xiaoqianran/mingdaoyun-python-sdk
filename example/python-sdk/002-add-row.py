"""002 新建一条记录；字段参数是 JSON 对象。"""
import argparse
from _common import make_client, parse_fields, write_flag, preview, output, result

p = argparse.ArgumentParser()
p.add_argument("worksheet")
p.add_argument("fields", help='例如 {"字段ID":"内容"}')
write_flag(p)
a = p.parse_args()
fields = parse_fields(a.fields)
if preview(a, "addRow", {"worksheet": a.worksheet, "field_ids": [x["controlId"] for x in fields]}):
    output(result(make_client(a.worksheet).add(fields)))
