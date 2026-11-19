"""012 查询指定字段包含某文本的记录；只读。"""
import argparse
from _common import make_client, result, output

p = argparse.ArgumentParser()
p.add_argument("worksheet")
p.add_argument("field_id")
p.add_argument("text")
p.add_argument("--limit", type=int, default=10)
a = p.parse_args()
if not 1 <= a.limit <= 100:
    p.error("--limit 范围为 1~100")
sdk = make_client(a.worksheet).table(a.worksheet)
rows = result(sdk.where(a.field_id, "contains", a.text).find(pageSize=a.limit)).get("rows", [])
output({"count": len(rows), "rowids": [x.get("rowid") for x in rows]})
