import subprocess
import json

def test_cli_missing_required_args():
    """缺少必需参数时应退出码 2"""
    result = subprocess.run(
        ["python3", "cli.py"],
        capture_output=True, text=True
    )
    assert result.returncode == 2

def test_cli_help():
    """--help 应正常输出"""
    result = subprocess.run(
        ["python3", "cli.py", "--help"],
        capture_output=True, text=True
    )
    assert result.returncode == 0
    assert "--user" in result.stdout
    assert "--org" in result.stdout
    assert "--since" in result.stdout
    assert "--until" in result.stdout
