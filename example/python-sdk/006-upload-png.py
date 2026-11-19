"""006 新增记录并通过 Base64 上传 PNG。"""
import argparse
from _common import make_client, file_control, write_flag, preview, output, result

p = argparse.ArgumentParser()
p.add_argument("worksheet")
p.add_argument("attachment_field_id")
p.add_argument("png_file")
write_flag(p)
a = p.parse_args()
if not a.png_file.lower().endswith(".png"):
    p.error("必须为 PNG 文件")
field = file_control(a.png_file, a.attachment_field_id)
if preview(a, "addRow+PNG", {"worksheet": a.worksheet, "file": a.png_file}):
    output(result(make_client(a.worksheet).add([field])))
