# 明道云 V2 API 示例

三个对等实现：
- python-sdk/：Python 直接使用仓库内 MingdaoYun V2 SDK。
- dify-python/：Dify Python Code（无 SDK，无网络访问依赖）。
- dify-javascript/：Dify JavaScript Code（无 SDK，无 Node.js 依赖）。

两套 Dify 的 000-config **零输入**，在函数内集中填写凭据、工作表和 options，返回一个 params：String；
001–014 都只配置一个 params 输入（Python: def main(params)，JS: function main({params})），无需重复声明 AppKey、Sign、worksheetId。
015-pack-response 是 014 前的可选桥接节点，用于把 HTTP 响应打包为 params。

三套中的 001–014 功能顺序一致：
001 查询，002 新增，003 批量新增，004 修改，005 删除，
006 PNG，007 XLSX，008 更新附件，009 数量，010 批量更新，
011 根据 ID 查询，012 条件查询，013 字段结构，014 解析响应。

## Dify 使用方式

000-config -> 001–013 Code -> HTTP Request -> 015-pack-response -> 014-parse-response

每一个 Code 文件均附有注释说明输入 JSON 键、值类型、示例和输出结构。
详细 JSON options_json 示例见 dify-python/README.md。
HTTP Request 采用 POST；URL 和 JSON Body 绑定业务 Code 节点返回的 url、body。

本项目严格使用 V2 API。认证 AppKey/Sign；工作表 ID 通过参数传入，不使用 PAT。
Dify Code 节点不直接发 HTTP。真实明道云接口已在 PC1 验证，但还未在 Dify 平台内跑完整节点链路。

## 安全

000 统一透传认证方便接线，但 params、body 均包含密钥；应严格限制 Dify 运行历史和日志访问权限。
若有更强保密需求，可直接在 HTTP 节点引用 Secret 环境变量，避免在 Code 输出中传递密钥。



## 零输入配置

Python：def main() -> dict；JavaScript：function main()。
不需要在 Dify 的 000 Code 节点配置输入变量。输出统一为 params（String）。
默认 worksheet_id=shuji、options.limit=10。limit 仅控制 001 单页返回条数，不是记录总数。
两个 000 示例仅保留密钥占位符，不把真实密钥提交到仓库。
