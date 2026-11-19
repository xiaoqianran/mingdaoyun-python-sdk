"""010 批量更新：对多个 rowid 的同一字段赋值。"""
import argparse
import json
from _common import make_client, write_flag, preview, output, result

p = argparse.ArgumentParser()
p.add_argument("worksheet")
p.add_argument("rowids", help="逗号分隔的记录 ID")
p.add_argument("field_id")
p.add_argument("value")
write_flag(p)
a = p.parse_args()
rowids = [x.strip() for x in a.rowids.split(",") if x.strip()]
if not 1 <= len(rowids) <= 100:
    p.error("请输入 1~100 个 rowid")
control = {"controlId": a.field_id, "value": a.value}
if preview(a, "editRows", {"worksheet": a.worksheet, "count": len(rowids), "field_id": a.field_id}):
    output(result(make_client(a.worksheet).batch_edit(rowids, control)))
