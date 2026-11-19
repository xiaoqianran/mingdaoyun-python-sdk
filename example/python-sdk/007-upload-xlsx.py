"""007 新增记录并通过 Base64 上传 XLSX。"""
import argparse
from _common import make_client, file_control, write_flag, preview, output, result

p = argparse.ArgumentParser()
p.add_argument("worksheet")
p.add_argument("attachment_field_id")
p.add_argument("xlsx_file")
write_flag(p)
a = p.parse_args()
if not a.xlsx_file.lower().endswith(".xlsx"):
    p.error("必须为 XLSX 文件")
field = file_control(a.xlsx_file, a.attachment_field_id)
if preview(a, "addRow+XLSX", {"worksheet": a.worksheet, "file": a.xlsx_file}):
    output(result(make_client(a.worksheet).add([field])))
