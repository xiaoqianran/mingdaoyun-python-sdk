/**
 * Dify JavaScript Code: 006-upload-png
 * 唯一输入：params (String)，从 000-config.js 的 params 输出绑定
 * params 是 JSON 文本，字段如下：
 * - app_key (str): 应用 API Key，通常来自 Dify Secret 变量 MINGDAO_APP_KEY
 * - sign (str): 应用 Sign，通常来自 Dify Secret 变量 MINGDAO_SIGN
 * - worksheet_id (str): 工作表 ID 或 API 支持的别名，例如 shuji
 * - attachment_field_id (str): 附件字段 controlId，shuji 的附件字段 ID 可通过 013 查询
 * - file_base64 (str): 真实文件字节转换而来的纯 Base64 字符串；不是 URL 或 Dify File 对象
 * - file_name (str): 附件文件名，包含 .png 或 .xlsx 后缀
 * 返回：001-013 -> {url: String, body: String}; 014 -> {ok: Boolean, error: String, result: String}。
 */
function main({params}) {
  // Dify 唯一输入变量：params（JSON 字符串）。
  const data = typeof params === "string" ? JSON.parse(params) : params;
  if (!data || typeof data !== "object" || Array.isArray(data)) throw new Error("params must be a JSON object");
  if (!Object.prototype.hasOwnProperty.call(data, "app_key")) throw new Error("Missing app_key");
  const app_key = data.app_key;
  if (!Object.prototype.hasOwnProperty.call(data, "sign")) throw new Error("Missing sign");
  const sign = data.sign;
  if (!Object.prototype.hasOwnProperty.call(data, "worksheet_id")) throw new Error("Missing worksheet_id");
  const worksheet_id = data.worksheet_id;
  if (!Object.prototype.hasOwnProperty.call(data, "attachment_field_id")) throw new Error("Missing attachment_field_id");
  const attachment_field_id = data.attachment_field_id;
  if (!Object.prototype.hasOwnProperty.call(data, "file_base64")) throw new Error("Missing file_base64");
  const file_base64 = data.file_base64;
  if (!Object.prototype.hasOwnProperty.call(data, "file_name")) throw new Error("Missing file_name");
  const file_name = data.file_name;

  if (!attachment_field_id || !file_name.toLowerCase().endsWith(".png"))
    throw new Error("attachment field and .png file name required");
  if (typeof file_base64 !== "string" || !/^[A-Za-z0-9+/]+={0,2}$/.test(file_base64) || file_base64.length > 10 * 1024 * 1024)
    throw new Error("invalid or oversized Base64 string");
  const body = {
    appKey: app_key,
    sign: sign,
    worksheetId: worksheet_id,
    triggerWorkflow: false,
    controls: [{controlId: attachment_field_id, valueType: 2, controlFiles: [{baseFile: file_base64, fileName: file_name}]}],
  };
  return {
    url: "https://api.mingdao.com/v2/open/worksheet/addRow",
    body: JSON.stringify(body)
  };
}
