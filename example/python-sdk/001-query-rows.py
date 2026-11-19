"""001 读取表结构和样例记录。"""
import argparse
import json
from _common import make_client, output, result

p = argparse.ArgumentParser()
p.add_argument("worksheet")
p.add_argument("--limit", type=int, default=5)
a = p.parse_args()
if not 1 <= a.limit <= 100:
    p.error("--limit 范围为 1 到 100")
sdk = make_client(a.worksheet)
schema = result(sdk.exec(sdk.WORKSHEET_MAP_URL))
fields = [{"id": f["controlId"], "name": f.get("controlName"), "type": f.get("type")} for f in schema.get("controls", [])]
output({"worksheet": a.worksheet, "fields": fields})
rows = result(sdk.find(pageSize=a.limit)).get("rows", [])
for row in rows:
    values = {}
    for f in fields:
        value = row.get(f["id"])
        if f["type"] == 14 and isinstance(value, str):
            try:
                value = [{"name": v.get("original_file_name"), "file_id": v.get("file_id")} for v in json.loads(value)]
            except (ValueError, TypeError):
                pass
        values[f["name"] or f["id"]] = value
    output({"rowid": row.get("rowid"), "values": values})
