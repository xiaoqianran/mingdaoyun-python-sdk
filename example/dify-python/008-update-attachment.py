"""
Dify Python Code 节点：008-update-attachment。

节点输入（只需 1 个）：params，String，JSON 格式。
从 000-config.py 的 params 输出绑定；业务参数在其 options_json 中一次性传入。
params 内使用以下 JSON 键：
- app_key (str)：应用 API Key，通常来自 Dify Secret 变量 MINGDAO_APP_KEY
- sign (str)：应用 Sign，通常来自 Dify Secret 变量 MINGDAO_SIGN
- worksheet_id (str)：工作表 ID 或 API 支持的别名，例如 shuji
- row_id (str)：需操作的真实记录 rowId，删除操作不可撤销
- attachment_field_id (str)：附件字段 controlId，shuji 的附件字段 ID 可通过 013 查询
- file_base64 (str)：真实文件字节转换而来的纯 Base64 字符串；不是 URL 或 Dify File 对象
- file_name (str)：附件文件名，包含 .png 或 .xlsx 后缀
- append (bool)：更新附件时 true 为追加，false 为覆盖，默认 false
返回：001-013 为 url(String)、body(String)；014 为 ok(Boolean)、error(String)、result(String)。
"""
import base64
import json

def main(params: str) -> dict:
    """Dify Code 节点唯一输入：params（JSON 字符串）。"""
    data = json.loads(params) if isinstance(params, str) else params
    if not isinstance(data, dict):
        raise ValueError("params must be a JSON object")
    app_key = data["app_key"]
    sign = data["sign"]
    worksheet_id = data["worksheet_id"]
    row_id = data["row_id"]
    attachment_field_id = data["attachment_field_id"]
    file_base64 = data["file_base64"]
    file_name = data["file_name"]
    append = data.get("append", False)
    if not row_id or not attachment_field_id or not file_name:
        raise ValueError("row_id, attachment_field_id and file_name are required")
    try:
        decoded = base64.b64decode(file_base64, validate=True)
        if not decoded or len(decoded) > 7 * 1024 * 1024:
            raise ValueError("File must be between 1 byte and 7 MiB")
    except Exception as exc:
        raise ValueError("file_base64 must be valid base64 content") from exc
    body = {
        "appKey": app_key,
        "sign": sign,
        "worksheetId": worksheet_id,
        "rowId": row_id,
        "triggerWorkflow": False,
        "controls": [{
            "controlId": attachment_field_id,
            "editType": 1 if append else 0,
            "valueType": 2,
            "controlFiles": [{"baseFile": file_base64, "fileName": file_name}]
        }]
    }
    return {"url": "https://api.mingdao.com/v2/open/worksheet/editRow", "body": json.dumps(body, ensure_ascii=False)}
