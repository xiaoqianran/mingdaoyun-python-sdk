/**
 * 015：Dify JavaScript HTTP 响应打包
 * 输入：params (String，000 的输出，可为空)、response_body (String，HTTP.body)、
 *       status_code (Number，HTTP.status_code)
 * 输出：params (String)，连接 014-parse-response 的唯一 params 输入。
 */
function main({params, response_body, status_code}) {
  return {params: JSON.stringify({response_body, status_code: Number(status_code)})};
}
