## 000 零输入配置（当前版本）

000-config 的 main() **不声明任何输入变量**。直接在代码中填写 app_key、sign、worksheet_id 和 options 字典/对象，输出一个 params（String），随后 001-013 只需接收 params。

limit=10 表示 **001 查询的单页最多返回 10 条记录**，不是总条数；需要遍历全部记录必须分页读取。009 统计总数不需要 limit。

新增或更新操作时修改 000 中 options 的业务字段（参看下方各操作示例）。与其他选项不冲突时，limit 可以保留，但只在读取代码中生效。000 的配置由当前工作流内所有下游业务节点共享。

**安全警告：** 样例只保留 REPLACE_WITH_APP_KEY / REPLACE_WITH_SIGN 占位符；在 Dify 编辑器中填入真实值后请勿公开分享工作流 DSL 或代码截图，且需限制执行历史、调试日志的可见权限。更安全的方案仍是 Dify Secret 环境变量绑定，但那会增加输入绑定。

# Dify JavaScript V2：统一 params 接口

所有文件都是普通 .js 代码片段，复制到 Dify JavaScript Code 节点；无需 Node.js、require、fetch 或 SDK。
000-config.js 接收 app_key、sign、worksheet_id、options_json，返回 params：String。
001–013 的 function main({params}) 只从 Dify 输入对象读取 params：String，返回 url：String、body：String。
Dify HTTP Request 节点采用 POST、Content-Type=application/json，将上一节点 url 和 body 引入。
015-pack-response.js 将 HTTP 的 body/status_code 组合成一个 params 字符串；014-parse-response.js 采用 function main({params})，只接收这个 params，返回 ok、error、result。

每个文件开头都有输入字段说明。业务 options_json 的例子参见 ../dify-python/README.md。
JS 与 Python 的参数名完全相同，均使用 V2 接口的 AppKey/Sign。
任何写操作可能影响云端数据；不要将 002–008/010 直接连至生产执行链路做随意测试。

注意：params 和 body 都可能包含秘密凭据。限制节点运行日志/历史可见范围。
