/**
 * 000：Dify JavaScript Code 节点，零输入，输出 params（String）。
 *
 * 复制到 Dify 后只需修改下方配置，不需为 Code 节点设置任何输入变量。
 * 切勿将填写真实密钥的代码提交 Git、公开导出 DSL 或开放运行日志访问。
 */
function main() {
  // AppKey + Sign：将占位符替换成明道云应用的实际凭据。
  const app_key = "REPLACE_WITH_APP_KEY";
  const sign = "REPLACE_WITH_SIGN";

  // 工作表 ID/别名；书籍表示例为 shuji。
  const worksheet_id = "shuji";

  // 001 查询：limit 是单页最多返回记录数，默认 10，不是总记录数。
  // 其他示例的必需字段见各编号文件及 README。
  const options = {
    limit: 10,
    // controls_json: '[{"controlId":"字段ID","value":"测试"}]', // 002
    // row_id: "真实记录ID",                                   // 004/005/008/011
    // attachment_field_id: "附件字段ID",                      // 006-008
    // file_base64: "实际文件字节编码后的Base64",               // 006-008
    // file_name: "example.xlsx",                             // 006-008
  };

  if (!app_key || !sign || !worksheet_id) {
    throw new Error("Missing app_key, sign or worksheet_id");
  }

  return {
    params: JSON.stringify({app_key, sign, worksheet_id, ...options})
  };
}
