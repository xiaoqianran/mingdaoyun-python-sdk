"""000：Dify Python Code 节点，零输入，输出 params（String）。

部署时只需修改下方配置；不要将真实 AppKey/Sign 提交 Git。
Dify 业务节点 001-013 只接受 params 一个输入。
"""
import json

def main() -> dict:
    # 认证：把下面两项占位符替换成自己的应用凭据。
    # 警告：硬编码密钥可能暴露于 Dify 代码编辑器、执行历史与导出的 DSL。
    app_key = "REPLACE_WITH_APP_KEY"
    sign = "REPLACE_WITH_SIGN"

    # 工作表 ID 或别名：书籍表示例为 shuji。
    worksheet_id = "shuji"

    # 业务选项：只需根据要调用的 001-013 示例修改此字典。
    # limit：001 查询时单页最多返回几条，默认 10；不是工作表总条数。
    options = {
        "limit": 10,
        # "controls_json": '[{"controlId":"字段ID","value":"测试"}]',  # 002 新增
        # "row_id": "真实记录ID",                            # 004、005、008、011
        # "attachment_field_id": "附件字段ID",              # 006-008
        # "file_base64": "实际文件字节编码后的Base64",        # 006-008
        # "file_name": "example.xlsx",                      # 006-008
    }
    if not app_key or not sign or not worksheet_id:
        raise ValueError("Missing app_key, sign or worksheet_id")
    return {
        "params": json.dumps(
            {"app_key": app_key, "sign": sign, "worksheet_id": worksheet_id, **options},
            ensure_ascii=False,
        )
    }
