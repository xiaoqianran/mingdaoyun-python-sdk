"""Dify Python Code 节点：零输入，明道云 shuji 工作表 V2 API JSON 风格示例集。

每个示例的 JSON 参数独立展示；只需修改 api 选择要调用的示例。
HTTP Request: POST / URL={{Python.url}} / JSON Body={{Python.body}}
注意：部分场景需要填写真实 rowId、关联字段 ID 或附件 Base64。
"""
import json


def main() -> dict:
    # 1. API 选项枚举：取消某行前的 #，并保证只有一行 api 生效
    # ===== 工作表结构 =====
    api = "getWorksheetInfo"  # 获取书籍工作表的字段结构
    # ===== 查询与分页 =====
    #api = "getFilterRows"  # 查询第一页记录
    #api = "getFilterRows__page2"  # 查询第二页记录
    #api = "getFilterRows__sort_name_asc"  # 按名称升序查询
    #api = "getFilterRows__sort_name_desc"  # 按名称降序查询
    #api = "getFilterRows__name_contains"  # 筛选名称包含 Python 的记录
    #api = "getFilterRows__name_equals"  # 筛选名称等于指定值的记录
    #api = "getFilterRows__dec_not_empty"  # 筛选描述不为空的记录
    #api = "getFilterRows__name_and_dec"  # 名称和描述组合筛选
    #api = "getRowByIdPost"  # 根据记录 ID 查询单条记录
    # ===== 数量统计 =====
    #api = "getFilterRowsTotalNum"  # 统计全部记录数量
    #api = "getFilterRowsTotalNum__name_contains"  # 统计名称包含 Python 的记录数
    # ===== 关联记录 =====
    #api = "getRowRelations"  # 读取关联记录（本表暂无关联字段）
    # ===== 新增记录 =====
    #api = "addRow"  # 新增一条书籍记录
    #api = "addRow__name_only"  # 仅填写书名新增
    #api = "addRow__with_xlsx"  # 新增记录并上传 Excel 附件
    #api = "addRow__with_two_files"  # 新增记录并上传两个附件
    #api = "addRows"  # 批量新增两条记录
    #api = "addRows__name_only"  # 批量新增只有名称的记录
    # ===== 修改记录 =====
    #api = "editRow"  # 同时修改名称、描述和附件
    #api = "editRow__dec_only"  # 只修改描述
    #api = "editRow__replace_xlsx"  # 覆盖现有 Excel 附件
    #api = "editRow__append_xlsx"  # 保留旧附件并追加 Excel
    #api = "editRow__name_and_xlsx"  # 同时修改名称和 Excel 附件
    #api = "editRows"  # 批量修改描述
    #api = "editRows__rename"  # 批量修改名称
    # ===== 删除记录 =====
    #api = "deleteRow"  # 删除一条记录
    #api = "deleteRow__multiple"  # 删除多条记录
    host = "https://api.mingdao.com"           # 主域名
    prefix = "/v2/open/worksheet/"              # V2 工作表 API 路径

    # 2. 公共 JSON（请替换密钥；生产环境建议使用 Dify Secret）
    common = {
        "appKey": "替换为你的AppKey",
        "sign": "替换为你的Sign",
        "worksheetId": "shuji",             # 工作表别名
        "triggerWorkflow": False               # 修改数据时不触发自动化
    }

    # ============================================================
    # 数字参数枚举说明
    # ============================================================

    # 1. dataType：控件类型（对应 getWorksheetInfo 的 type）
    # ------------------------------------------------------------
    #  0 = 未定义
    #  1 = 单行文本
    #  2 = 多行文本
    #  3 = 手机
    #  4 = 座机
    #  5 = 邮箱
    #  6 = 数值
    #  7 = 证件
    #  8 = 金额
    #  9 = 单选平铺
    # 10 = 多选
    # 11 = 单选下拉
    # 14 = 附件
    # 15 = 日期
    # 16 = 日期时间
    # 26 = 成员
    # 27 = 部门
    # 29 = 关联记录
    # shuji：name = 2，dec = 2，fujian = 14

    # 2. spliceType：筛选条件关系
    # ------------------------------------------------------------
    # 0 = 未定义
    # 1 = AND（且）
    # 2 = OR（或）

    # 3. filterType：筛选方式
    # ------------------------------------------------------------
    #  0 = 默认
    #  1 = 包含
    #  2 = 等于
    #  3 = 开头为
    #  4 = 结尾为
    #  5 = 不包含
    #  6 = 不等于
    #  7 = 为空
    #  8 = 不为空
    # 11 = 范围内
    # 12 = 范围外
    # 13 = 大于
    # 14 = 大于等于
    # 15 = 小于
    # 16 = 小于等于
    # 17 = 日期是
    # 18 = 日期不是
    # 24 = 关联是
    # 25 = 关联不是
    # 31 = 日期范围内
    # 32 = 日期范围外
    # 33 = 日期大于
    # 34 = 日期大于等于
    # 35 = 日期小于
    # 36 = 日期小于等于

    # 4. valueType：附件来源
    # ------------------------------------------------------------
    # 0 = 未定义
    # 1 = URL
    # 2 = Base64

    # 5. editType：附件更新方式
    # ------------------------------------------------------------
    # 0 = 覆盖原附件
    # 1 = 追加新附件
    # 2 = 未定义

    # 6. notGetTotal：是否跳过记录总数统计
    # ------------------------------------------------------------
    # 0 = 不跳过（计算总数）
    # 1 = 跳过（提高查询效率）

    # 7. isAsc：排序方向
    # ------------------------------------------------------------
    # True  = 升序
    # False = 降序

    # 8. triggerWorkflow：是否触发明道云自动化
    # ------------------------------------------------------------
    # True  = 触发
    # False = 不触发

    # 3. 每个示例的业务 JSON：name / dec / fujian 都是字段别名
    # 以下示例中的记录 ID 是占位符，不能直接拿来操作真实记录。
    apis = {
        # ===== A. 获取结构 =====
        "getWorksheetInfo": {},

        # 筛选参数速查：dataType=2 文本；spliceType=1 且(AND)；filterType=1 包含、2 等于、8 非空
    # ===== B. 读取与分页 =====
        "getFilterRows": {
            "pageSize": 10,
            "pageIndex": 1,
            "notGetTotal": 1,
            "filters": []
        },
        "getFilterRows__page2": {
            "pageSize": 10,
            "pageIndex": 2,
            "notGetTotal": 1,
            "filters": []
        },
        "getFilterRows__sort_name_asc": {
            "pageSize": 10,
            "pageIndex": 1,
            "sortId": "name",                   # 按书名排序
            "isAsc": True,
            "filters": []
        },
        "getFilterRows__sort_name_desc": {
            "pageSize": 10,
            "pageIndex": 1,
            "sortId": "name",
            "isAsc": False,
            "filters": []
        },
        "getFilterRows__name_contains": {
            "pageSize": 10,
            "pageIndex": 1,
            "filters": [{
                "controlId": "name",
                "dataType": 2,                  # 文本字段
                "spliceType": 1,  # 且（AND）
                "filterType": 1,                # contains（包含）
                "value": "Python"
            }]
        },
        "getFilterRows__name_equals": {
            "pageSize": 10,
            "pageIndex": 1,
            "filters": [{
                "controlId": "name",
                "dataType": 2,  # 文本字段
                "spliceType": 1,  # 且（AND）
                "filterType": 2,                # 等于
                "value": "机器学习"
            }]
        },
        "getFilterRows__dec_not_empty": {
            "pageSize": 10,
            "pageIndex": 1,
            "filters": [{
                "controlId": "dec",
                "dataType": 2,  # 文本字段
                "spliceType": 1,  # 且（AND）
                "filterType": 8,                # 非空
                "value": ""
            }]
        },
        "getFilterRows__name_and_dec": {
            "pageSize": 10,
            "pageIndex": 1,
            "filters": [
                {"controlId": "name", "dataType": 2, "spliceType": 1,
                 "filterType": 1, "value": "Python"},  # 包含
                {"controlId": "dec", "dataType": 2, "spliceType": 1,
                 "filterType": 1, "value": "测试"}  # 包含
            ]
        },
        "getRowByIdPost": {
            "rowId": "填写真实rowId"
        },

        # ===== C. 数量统计 =====
        "getFilterRowsTotalNum": {
            "filters": []
        },
        "getFilterRowsTotalNum__name_contains": {
            "filters": [{
                "controlId": "name", "dataType": 2,
                "spliceType": 1, "filterType": 1,  # 且（AND）
                "value": "Python"
            }]
        },

        # ===== D. 关联记录（shuji 当前没有关联字段，此项为通用模板） =====
        "getRowRelations": {
            "rowId": "填写真实rowId",
            "controlId": "填写真实关联字段ID",
            "pageSize": 10,
            "pageIndex": 1
        },

        # ===== E. 新增记录 =====
        "addRow": {
            "controls": [
                {"controlId": "name", "value": "Python 数据分析"},
                {"controlId": "dec", "value": "Dify 新增的书籍"}
            ]
        },
        "addRow__name_only": {
            "controls": [
                {"controlId": "name", "value": "只有书名的新记录"}
            ]
        },
        "addRow__with_xlsx": {
            "controls": [
                {"controlId": "name", "value": "Excel 报告"},
                {"controlId": "dec", "value": "新增时上传 XLSX"},
                {"controlId": "fujian", "valueType": 2,
                 "controlFiles": [{
                     "baseFile": "填写真实XLSX的Base64",
                     "fileName": "report.xlsx"
                 }]}
            ]
        },
        "addRow__with_two_files": {
            "controls": [
                {"controlId": "name", "value": "带两个附件的记录"},
                {"controlId": "fujian", "valueType": 2,
                 "controlFiles": [
                     {"baseFile": "填写第一个文件Base64", "fileName": "report.xlsx"},
                     {"baseFile": "填写第二个文件Base64", "fileName": "notes.xlsx"}
                 ]}
            ]
        },
        "addRows": {
            "rows": [
                [{"controlId": "name", "value": "书籍 A"},
                 {"controlId": "dec", "value": "批量新增第一条"}],
                [{"controlId": "name", "value": "书籍 B"},
                 {"controlId": "dec", "value": "批量新增第二条"}]
            ]
        },
        "addRows__name_only": {
            "rows": [
                [{"controlId": "name", "value": "批量书籍 1"}],
                [{"controlId": "name", "value": "批量书籍 2"}],
                [{"controlId": "name", "value": "批量书籍 3"}]
            ]
        },

        # ===== F. 修改记录 =====
        "editRow": {
            "rowId": "填写真实rowId",
            "controls": [
                {"controlId": "name", "value": "更新后的名称"},
                {"controlId": "dec", "value": "更新后的描述"},
                {
                    "controlId": "fujian",
                    "editType": 0,  # 0：覆盖附件；1：追加附件
                    "valueType": 2, # 使用 Base64 上传
                    "controlFiles": [
                        {
                            "baseFile": "",  # 填写 Excel 的完整 Base64
                            "fileName": "report.xlsx"
                        }
                    ]
                }
            ]
        },
        "editRow__dec_only": {
            "rowId": "填写真实rowId",
            "controls": [
                {"controlId": "dec", "value": "仅更新描述"}
            ]
        },
        "editRow__replace_xlsx": {
            "rowId": "填写真实rowId",
            "controls": [
                {"controlId": "fujian", "editType": 0,  # 覆盖已有附件
                 "valueType": 2,
                 "controlFiles": [{
                     "baseFile": "填写真实XLSX的Base64",
                     "fileName": "updated_report.xlsx"
                 }]}
            ]
        },
        "editRow__append_xlsx": {
            "rowId": "填写真实rowId",
            "controls": [
                {"controlId": "fujian", "editType": 1,  # 保留旧附件并追加
                 "valueType": 2,
                 "controlFiles": [{
                     "baseFile": "填写真实XLSX的Base64",
                     "fileName": "extra_report.xlsx"
                 }]}
            ]
        },
        "editRow__name_and_xlsx": {
            "rowId": "填写真实rowId",
            "controls": [
                {"controlId": "name", "value": "新版报告"},
                {"controlId": "fujian", "editType": 0,
                 "valueType": 2,
                 "controlFiles": [{
                     "baseFile": "填写真实XLSX的Base64",
                     "fileName": "new.xlsx"
                 }]}
            ]
        },
        "editRows": {
            "rowIds": ["填写真实rowId1", "填写真实rowId2"],
            "control": {"controlId": "dec", "value": "统一更新描述"}
        },
        "editRows__rename": {
            "rowIds": ["填写真实rowId1", "填写真实rowId2"],
            "control": {"controlId": "name", "value": "批量统一书名"}
        },

        # ===== G. 删除记录 =====
        "deleteRow": {
            "rowId": "填写真实rowId"
        },
        "deleteRow__multiple": {
            "rowId": "填写真实rowId1,填写真实rowId2"  # SDK 接口支持逗号分隔
        }
    }

    # 4. 统一构造 URL / Body；__ 后仅用于区分示例，不属于接口地址
    if api not in apis:
        raise ValueError("未知 API 示例: " + api)
    endpoint = api.split("__", 1)[0]
    body = {**common, **apis[api]}
    return {
        "url": host + prefix + endpoint,
        "body": json.dumps(body, ensure_ascii=False),
    }
