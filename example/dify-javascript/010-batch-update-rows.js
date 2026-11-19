/**
 * Dify JavaScript Code: 010-batch-update-rows
 * 唯一输入：params (String)，从 000-config.js 的 params 输出绑定
 * params 是 JSON 文本，字段如下：
 * - app_key (str): 应用 API Key，通常来自 Dify Secret 变量 MINGDAO_APP_KEY
 * - sign (str): 应用 Sign，通常来自 Dify Secret 变量 MINGDAO_SIGN
 * - worksheet_id (str): 工作表 ID 或 API 支持的别名，例如 shuji
 * - row_ids_json (str): 记录 ID 数组的 JSON 字符串，例如 ["ID1","ID2"]
 * - field_id (str): 需要更新的字段 controlId
 * - value (str): 准备批量更新的字段值
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
  if (!Object.prototype.hasOwnProperty.call(data, "row_ids_json")) throw new Error("Missing row_ids_json");
  const row_ids_json = data.row_ids_json;
  if (!Object.prototype.hasOwnProperty.call(data, "field_id")) throw new Error("Missing field_id");
  const field_id = data.field_id;
  if (!Object.prototype.hasOwnProperty.call(data, "value")) throw new Error("Missing value");
  const value = data.value;

  const row_ids = JSON.parse(row_ids_json);
  if (!(Array.isArray(row_ids) && row_ids.length >= 1 && row_ids.length <= 100)) throw new Error("row ids must be 1..100 array");
  const body = {
    appKey: app_key,
    sign: sign,
    worksheetId: worksheet_id,
    triggerWorkflow: false,
    rowIds: row_ids,
    control: {controlId: field_id, value},
  };
  return {
    url: "https://api.mingdao.com/v2/open/worksheet/editRows",
    body: JSON.stringify(body)
  };
}
