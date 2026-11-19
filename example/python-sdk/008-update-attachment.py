"""008 向已有记录上传 PNG/XLSX，可指定追加。"""
import argparse
from _common import make_client, file_control, write_flag, preview, output, result

p = argparse.ArgumentParser()
p.add_argument("worksheet")
p.add_argument("rowid")
p.add_argument("attachment_field_id")
p.add_argument("file")
p.add_argument("--append", action="store_true", help="追加而非覆盖")
write_flag(p)
a = p.parse_args()
field = file_control(a.file, a.attachment_field_id, append=a.append)
if preview(a, "editRow+attachment", {"worksheet": a.worksheet, "rowid": a.rowid, "file": a.file, "append": a.append}):
    output(result(make_client(a.worksheet).edit(a.rowid, [field])))
