"""003 批量新增；JSON 文件格式为 [{字段ID: 值}, ...]。"""
import argparse
from _common import make_client, parse_rows, write_flag, preview, output, result

p = argparse.ArgumentParser()
p.add_argument("worksheet")
p.add_argument("json_file")
write_flag(p)
a = p.parse_args()
rows = parse_rows(a.json_file)
if preview(a, "addRows", {"worksheet": a.worksheet, "count": len(rows)}):
    output(result(make_client(a.worksheet).batch_add(rows)))
