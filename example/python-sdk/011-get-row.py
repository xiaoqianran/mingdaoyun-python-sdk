"""011 通过记录 ID 查询单条记录；只读。"""
import argparse
import json
from _common import make_client, result, output

p = argparse.ArgumentParser()
p.add_argument("worksheet")
p.add_argument("rowid")
a = p.parse_args()
data = result(make_client(a.worksheet).find(rowid=a.rowid))
# 原始响应可能含带签名的附件链接，避免意外输出，仅保留行 ID 与字段值摘要。
if isinstance(data, dict):
    output({"rowid": data.get("rowid"), "field_ids": [k for k in data if k not in ("rowid", "_id", "ctime", "utime", "caid", "uaid", "ownerid", "autoid")]})
else:
    output({"found": bool(data), "data_type": type(data).__name__})
