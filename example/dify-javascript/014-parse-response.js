/**
 * Dify JavaScript Code: 014-parse-response
 * 唯一输入：params (String)，从 000-config.js 的 params 输出绑定
 * params 是 JSON 文本，字段如下：
 * - response_body (str): 上游 HTTP 节点输出的 body JSON 文本
 * - status_code (int): 上游 HTTP 节点的 status_code
 * 返回：001-013 -> {url: String, body: String}; 014 -> {ok: Boolean, error: String, result: String}。
 */
function main({params}) {
  // Dify 唯一输入变量：params（JSON 字符串）。
  const input = typeof params === "string" ? JSON.parse(params) : params;
  if (!input || typeof input !== "object" || Array.isArray(input)) throw new Error("params must be a JSON object");
  if (!Object.prototype.hasOwnProperty.call(input, "response_body")) throw new Error("Missing response_body");
  const response_body = input.response_body;
  if (!Object.prototype.hasOwnProperty.call(input, "status_code")) throw new Error("Missing status_code");
  const status_code = input.status_code;

  let data;
  try {
    data = JSON.parse(response_body);
  } catch (_) {
    return {ok: false, error: "Invalid JSON response", result: ""};
  }
  const ok = Number(status_code) >= 200 && Number(status_code) < 300 && data.success === true;
  return {
    ok,
    error: ok ? "" : String(data.error_msg || data.error_code || status_code),
    result: ok ? JSON.stringify(data.data === undefined ? null : data.data) : ""
  };
}
