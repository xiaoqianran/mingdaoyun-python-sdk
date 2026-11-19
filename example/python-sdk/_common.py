"""V2 SDK 示例公共配置与输入校验。"""
import argparse
import base64
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT))

from dotenv import load_dotenv
from mingdaoyun_sdk.MingdaoYun import MingdaoYun

load_dotenv(ROOT / ".env")


def make_client(worksheet):
    key = os.getenv("MINGDAO_APP_KEY")
    sign = os.getenv("MINGDAO_SIGN")
    if not key or not sign:
        raise ValueError("请在根目录 .env 中配置 MINGDAO_APP_KEY 和 MINGDAO_SIGN")
    sdk = MingdaoYun(key, sign, os.getenv("MINGDAO_HOST", "https://api.mingdao.com").rstrip("/"))
    sdk.worksheetId = worksheet
    return sdk


def parse_fields(value):
    obj = json.loads(value)
    if not isinstance(obj, dict) or not obj:
        raise ValueError("字段应为非空 JSON 对象：{字段ID: 值}")
    return [{"controlId": k, "value": v} for k, v in obj.items()]


def parse_rows(path):
    values = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(values, list) or not 1 <= len(values) <= 100:
        raise ValueError("JSON 文件必须包含 1~100 条记录")
    return [parse_fields(json.dumps(item, ensure_ascii=False)) for item in values]


def file_control(path, field_id, append=False):
    file = Path(path)
    if file.suffix.lower() not in (".png", ".xlsx"):
        raise ValueError("示例只接受 PNG/XLSX")
    if not file.is_file():
        raise ValueError("文件不存在")
    if file.stat().st_size > 5 * 1024 * 1024:
        raise ValueError("示例限制 5 MiB，避免 Base64 请求过大")
    return {
        "controlId": field_id,
        "editType": 1 if append else 0,
        "valueType": 2,
        "controlFiles": [{
            "baseFile": base64.b64encode(file.read_bytes()).decode("ascii"),
            "fileName": file.name,
        }],
    }


def output(data):
    print(json.dumps(data, ensure_ascii=False, indent=2))


def result(data):
    if not data.get("success"):
        raise RuntimeError(f"明道云错误：{data.get('error_code')} {data.get('error_msg')}")
    return data.get("data")


def write_flag(parser):
    parser.add_argument("--execute", action="store_true", help="明确允许执行真实写操作")


def preview(args, action, detail):
    output({"action": action, "target": detail, "mode": "execute" if args.execute else "preview"})
    if not args.execute:
        print("只预览，未调用写入接口；添加 --execute 才会执行。")
    return args.execute
