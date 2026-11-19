/**
 * Dify JavaScript Code: 002-add-row
 * 唯一输入：params (String)，从 000-config.js 的 params 输出绑定
 * params 是 JSON 文本，字段如下：
 * - app_key (str): 应用 API Key，通常来自 Dify Secret 变量 MINGDAO_APP_KEY
 * - sign (str): 应用 Sign，通常来自 Dify Secret 变量 MINGDAO_SIGN
 * - worksheet_id (str): 工作表 ID 或 API 支持的别名，例如 shuji
 * - controls_json (str): 字段数组的 JSON 字符串，例如 [{"controlId":"字段ID","value":"测试"}]
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
  if (!Object.prototype.hasOwnProperty.call(data, "controls_json")) throw new Error("Missing controls_json");
  const controls_json = data.controls_json;

  const controls = JSON.parse(controls_json);
  if (!(Array.isArray(controls) && controls.length > 0)) throw new Error("controls must be a nonempty array");
  const body = {
    appKey: app_key,
    sign: sign,
    worksheetId: worksheet_id,
    triggerWorkflow: false,
    controls,
  };
  return {
    url: "https://api.mingdao.com/v2/open/worksheet/addRow",
    body: JSON.stringify(body)
  };
}
