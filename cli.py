"""GitHub PR 数据采集 CLI，输出结构化 JSON。"""

import argparse
import json
import sys


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="采集 GitHub PR 数据，输出 JSON")
    parser.add_argument("--user", required=True, help="GitHub 用户名")
    parser.add_argument("--org", required=True, help="GitHub 组织名")
    parser.add_argument("--since", required=True, help="开始日期（含），格式 YYYY-MM-DD")
    parser.add_argument("--until", required=True, help="结束日期（含），格式 YYYY-MM-DD")
    parser.add_argument("--token", default=None, help="GitHub token，默认读取 GITHUB_TOKEN 环境变量")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    # TODO: 实现数据采集
    json.dump([], sys.stdout, ensure_ascii=False, indent=2)
    print()


if __name__ == "__main__":
    main()
