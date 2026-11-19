/**
 * Dify JavaScript Code: 001-query-rows
 * 唯一输入：params (String)，从 000-config.js 的 params 输出绑定
 * params 是 JSON 文本，字段如下：
 * - app_key (str): 应用 API Key，通常来自 Dify Secret 变量 MINGDAO_APP_KEY
 * - sign (str): 应用 Sign，通常来自 Dify Secret 变量 MINGDAO_SIGN
 * - worksheet_id (str): 工作表 ID 或 API 支持的别名，例如 shuji
 * - limit (int): 每次读取条数，1~100，默认 10
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
  const limit = data.limit === undefined ? 10 : data.limit;

  if (!Number.isInteger(Number(limit)) || limit < 1 || limit > 100) throw new Error("limit must be 1..100");
  const body = {
    appKey: app_key,
    sign: sign,
    worksheetId: worksheet_id,
    pageSize: Number(limit),
    pageIndex: 1,
    notGetTotal: 1,
  };
  return {
    url: "https://api.mingdao.com/v2/open/worksheet/getFilterRows",
    body: JSON.stringify(body)
  };
}
