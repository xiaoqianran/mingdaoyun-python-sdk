## 000 零输入配置（当前版本）

000-config 的 main() **不声明任何输入变量**。直接在代码中填写 app_key、sign、worksheet_id 和 options 字典/对象，输出一个 params（String），随后 001-013 只需接收 params。

limit=10 表示 **001 查询的单页最多返回 10 条记录**，不是总条数；需要遍历全部记录必须分页读取。009 统计总数不需要 limit。

新增或更新操作时修改 000 中 options 的业务字段（参看下方各操作示例）。与其他选项不冲突时，limit 可以保留，但只在读取代码中生效。000 的配置由当前工作流内所有下游业务节点共享。

**安全警告：** 样例只保留 REPLACE_WITH_APP_KEY / REPLACE_WITH_SIGN 占位符；在 Dify 编辑器中填入真实值后请勿公开分享工作流 DSL 或代码截图，且需限制执行历史、调试日志的可见权限。更安全的方案仍是 Dify Secret 环境变量绑定，但那会增加输入绑定。

# Dify Python V2：统一 params 接口

## 工作流节点

1. 000-config.py（Python Code）输入 app_key、sign、worksheet_id、options_json（可设为 {}）。
2. 000 的输出只声明 params：String。
3. 001–013 任意一个业务节点（Python Code）仅声明输入 params：String，绑定 000.params。
4. 业务 Code 节点输出 url：String、body：String；HTTP Request 节点 POST，URL 引用 url，Header Content-Type=application/json，Body 原样引用 body。
5. 若要解析响应，015-pack-response.py 输入 params（可取 000.params）、response_body（HTTP.body）、status_code（HTTP.status_code），输出 params：String；014-parse-response.py 仅输入 015.params，输出 ok：Boolean、error：String、result：String。

## 参数如何填写

000-config 接收：
- app_key：Dify 中绑定 Secret MINGDAO_APP_KEY。
- sign：Dify 中绑定 Secret MINGDAO_SIGN。
- worksheet_id：例如 shuji。
- options_json：JSON 字符串，放本次操作特有的参数，示例见下。

不同操作的 options_json 举例（每个示例单独运行）：
- 001 查询：{"limit":5}
- 002 新增：{"controls_json":"[{\"controlId\":\"6afc35a9fc2de46a704c900c\",\"value\":\"API示例\"}]"}
- 003 批量新增：{"rows_json":"[[{\"controlId\":\"字段ID\",\"value\":\"A\"}]]"}
- 004 编辑：{"row_id":"真实记录ID","controls_json":"[{\"controlId\":\"字段ID\",\"value\":\"新内容\"}]"}
- 005 删除：{"row_id":"真实记录ID"}
- 006 PNG：{"attachment_field_id":"附件字段ID","file_base64":"文件真实字节的Base64","file_name":"image.png"}
- 007 XLSX：{"attachment_field_id":"附件字段ID","file_base64":"文件真实字节的Base64","file_name":"table.xlsx"}
- 008 更新附件：{"row_id":"真实记录ID","attachment_field_id":"附件字段ID","file_base64":"文件真实字节的Base64","file_name":"table.xlsx","append":true}
- 009 数量：{}
- 010 批量更新：{"row_ids_json":"[\"记录ID1\",\"记录ID2\"]","field_id":"字段ID","value":"新内容"}
- 011 单行：{"row_id":"真实记录ID"}
- 012 筛选：{"filters_json":"[{\"controlId\":\"字段ID\",\"dataType\":2,\"spliceType\":1,\"filterType\":1,\"value\":\"艺术\"}]","limit":10}
- 013 工作表字段：{}

Dify 的 options_json 必须是合法 JSON；内层 JSON 字符串必须正确转义。不要把 file 对象、URL 当作 file_base64。

## 安全提示

000 的 params 包含 AppKey/Sign，因此 Dify 中间节点输出、执行历史可能显示机密。
建议将认证字段直接在 HTTP Request 节点引用 Secret 环境变量，以避免流转明文；
若按本例使用 params 传密钥，务必限制工作流日志、执行历史与权限。
不使用 PAT，不使用 V3；Code 节点只构造请求，HTTP Request 节点负责联网。
