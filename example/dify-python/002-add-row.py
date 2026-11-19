"""
Dify Python Code 节点：002-add-row。

节点输入（只需 1 个）：params，String，JSON 格式。
从 000-config.py 的 params 输出绑定；业务参数在其 options_json 中一次性传入。
params 内使用以下 JSON 键：
- app_key (str)：应用 API Key，通常来自 Dify Secret 变量 MINGDAO_APP_KEY
- sign (str)：应用 Sign，通常来自 Dify Secret 变量 MINGDAO_SIGN
- worksheet_id (str)：工作表 ID 或 API 支持的别名，例如 shuji
- controls_json (str)：字段数组的 JSON 字符串，例如 [{"controlId":"字段ID","value":"测试"}]
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
    controls_json = data["controls_json"]
    controls = json.loads(controls_json)
    if not isinstance(controls, list) or not controls:
        raise ValueError("controls_json must be a non-empty array")

    body = {
        "appKey": app_key,
        "sign": sign,
        "worksheetId": worksheet_id,
        "triggerWorkflow": False,
        "controls": controls,
    }
    return {
        "url": "https://api.mingdao.com/v2/open/worksheet/addRow",
        "body": json.dumps(body, ensure_ascii=False),
    }
