"""014 本地解析明道云 V2 HTTP 响应。"""
import json
import argparse

def main(response_body: str, status_code: int) -> dict:
    try:
        data = json.loads(response_body)
    except (ValueError, TypeError):
        return {"ok": False, "error": "Invalid JSON response", "result": ""}
    ok = 200 <= int(status_code) < 300 and data.get("success") is True
    return {
        "ok": ok,
        "error": "" if ok else str(data.get("error_msg") or data.get("error_code") or status_code),
        "result": json.dumps(data.get("data"), ensure_ascii=False) if ok else "",
    }

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("response_body")
    parser.add_argument("status_code", type=int)
    args = parser.parse_args()
    print(json.dumps(main(args.response_body, args.status_code), ensure_ascii=False))
