"""
Dify Python Code 节点：014-parse-response。

节点输入（只需 1 个）：params，String，JSON 格式。
从 000-config.py 的 params 输出绑定；业务参数在其 options_json 中一次性传入。
params 内使用以下 JSON 键：
- response_body (str)：上游 HTTP 节点输出的 body JSON 文本
- status_code (int)：上游 HTTP 节点的 status_code
返回：001-013 为 url(String)、body(String)；014 为 ok(Boolean)、error(String)、result(String)。
"""

# 014 的输入由 HTTP 后的 015-pack-response.py 打包。
import json

def main(params: str) -> dict:
    """Dify Code 节点唯一输入：params（JSON 字符串）。"""
    data = json.loads(params) if isinstance(params, str) else params
    if not isinstance(data, dict):
        raise ValueError("params must be a JSON object")
    response_body = data["response_body"]
    status_code = data["status_code"]
    try:
        data = json.loads(response_body)
    except (ValueError, TypeError):
        return {"ok": False, "error": "Invalid JSON response", "result": ""}
    ok = 200 <= int(status_code) < 300 and data.get("success") is True
    if not ok:
        return {
            "ok": False,
            "error": str(data.get("error_msg") or data.get("error_code") or status_code),
            "result": "",
        }
    # Dify Code output: string avoids object schema mismatch across versions.
    return {"ok": True, "error": "", "result": json.dumps(data.get("data"), ensure_ascii=False)}
