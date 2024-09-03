import requests
from ..common.config import VERSION, API_URLS


def check_for_updates():
    '''
    檢查更新
        API返回失敗時，返回None，None
        API返回成功時，并且需要更新時，返回最新版本號碼，更新資訊網址
        API返回成功時，但不需要更新時，返回最新版本號碼，None
    :return:
    '''
    print("检测是否有版本更新")
    # 從API獲取最新版本資訊
    try:
        latest_version = requests.get(API_URLS["latest_version"]).text
    # 如果獲取失敗，回傳False
    except requests.RequestException as e:
        print(f"获取最新版本信息失败,請檢查是否連接内網:{e}")
        return None, None

    # 比較版本資訊
    if parse_version(latest_version) > parse_version(VERSION):
        print(f"当前版本为{VERSION}，最新版本为{latest_version}。")
        return latest_version, API_URLS["get_changelog"]
    else:
        print(f"当前版本为{VERSION}，已是最新版本。")
        return latest_version, None


def parse_version(version):
    """解析带阶段性标识的版本号，返回一个可比较的元组"""
    # 定义阶段性标识的映射关系
    stage_precedence = {"Alpha": 0, "Beta": 1, "Release": 2, "": 2}  # 假设没有阶段性标识等同于正式发布
    parts = version.split(" ")

    if len(parts) == 2:  # 带有阶段性标识
        stage, version_number = parts
    else:  # 假设只有版本号
        stage = ""
        version_number = parts[0]

    major, minor, patch = map(int, version_number.split("."))

    # 返回一个元组，用于比较
    return (stage_precedence[stage], major, minor, patch)