"""015：Dify Python HTTP 响应打包。

输入：params (String，000-config 的输出)、response_body (String，HTTP.body)、
     status_code (Number，HTTP.status_code)。
输出：params (String)；连接 014-parse-response 的 params 输入。
"""
import json

def main(params: str, response_body: str, status_code: int) -> dict:
    obj = json.loads(params) if isinstance(params, str) else params
    if not isinstance(obj, dict):
        raise ValueError("params must be a JSON object")
    # 解析响应不需要凭据，避免把密钥再次放进 014 的输入。
    return {"params": json.dumps({"response_body": response_body, "status_code": int(status_code)}, ensure_ascii=False)}
