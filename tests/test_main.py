import json

import pytest

from src.main import main, validate_url


def test_validate_url_rejects_non_onion():
    with pytest.raises(SystemExit):
        validate_url("http://127.0.0.1:8080")
    with pytest.raises(SystemExit):
        validate_url("file:///etc/passwd")


def test_validate_url_accepts_onion():
    validate_url("http://abcdefghijklmnop.onion")


def test_cli_offline_sample(capsys):
    assert main(["--test", "--json"]) == 0
    out = capsys.readouterr().out
    findings = json.loads(out)
    types = {f["type"] for f in findings}
    assert "CARD" in types and "EMAIL" in types


def test_cli_missing_file_is_empty(tmp_path, capsys):
    target = tmp_path / "empty.txt"
    target.write_text("nada relevante aqui")
    assert main(["--file", str(target), "--json"]) == 0
    assert json.loads(capsys.readouterr().out) == []
