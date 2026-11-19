"""
Dify Python Code 节点：010-batch-update-rows。

节点输入（只需 1 个）：params，String，JSON 格式。
从 000-config.py 的 params 输出绑定；业务参数在其 options_json 中一次性传入。
params 内使用以下 JSON 键：
- app_key (str)：应用 API Key，通常来自 Dify Secret 变量 MINGDAO_APP_KEY
- sign (str)：应用 Sign，通常来自 Dify Secret 变量 MINGDAO_SIGN
- worksheet_id (str)：工作表 ID 或 API 支持的别名，例如 shuji
- row_ids_json (str)：记录 ID 数组的 JSON 字符串，例如 ["ID1","ID2"]
- field_id (str)：需要更新的字段 controlId
- value (str)：准备批量更新的字段值
返回：001-013 为 url(String)、body(String)；014 为 ok(Boolean)、error(String)、result(String)。
"""
import json

def main(params: str) -> dict:
    """Dify Code 节点唯一输入：params（JSON 字符串）。"""
    data = json.loads(params) if isinstance(params, str) else params
    if not isinstance(data, dict):
        raise ValueError("params must be a JSON object")
    app_key = data["app_key"]
    sign = data["sign"]
    worksheet_id = data["worksheet_id"]
    row_ids_json = data["row_ids_json"]
    field_id = data["field_id"]
    value = data["value"]
    row_ids = json.loads(row_ids_json)
    if not isinstance(row_ids, list) or not 1 <= len(row_ids) <= 100:
        raise ValueError("row_ids_json must be a list of 1..100 ids")

    body = {
        "appKey": app_key,
        "sign": sign,
        "worksheetId": worksheet_id,
        "triggerWorkflow": False,
        "rowIds": row_ids,
        "control": {"controlId": field_id, "value": value},
    }
    return {
        "url": "https://api.mingdao.com/v2/open/worksheet/editRows",
        "body": json.dumps(body, ensure_ascii=False),
    }
