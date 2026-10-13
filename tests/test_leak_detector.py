from src.core.hasher import hash_value
from src.modules.leak_detector import luhn, scan_text


def test_luhn_valid_and_invalid():
    assert luhn("4111111111111111") is True
    assert luhn("4111 1111 1111 1111") is True
    assert luhn("4111111111111112") is False
    assert luhn("1234") is False


def test_scan_detects_all_types():
    text = (
        "mail john.doe@acmecorp.com card 4111 1111 1111 1111 "
        "md5 5f4dcc3b5aa765d61d8327deb882cf99 "
        "bcrypt $2b$12$KIXQ3j2Yl9wZ0oQ2f4J3Ke1b7c8d9e0f1g2h3i4j5k6l7m8n9o0p1"
    )
    kinds = {f.type for f in scan_text(text, ["acmecorp"])}
    assert {"EMAIL", "CARD", "HASH", "PASSWORD_HASH", "KEYWORD"} <= kinds


def test_invalid_card_is_ignored():
    findings = scan_text("card 4111 1111 1111 1112")
    assert all(f.type != "CARD" for f in findings)


def test_findings_are_masked_and_deduplicated():
    findings = scan_text("a@x.com a@x.com")
    emails = [f for f in findings if f.type == "EMAIL"]
    assert len(emails) == 1
    assert emails[0].value == "a@***om"
    assert "a@x.com" not in emails[0].value


def test_fingerprint_is_stable_hash():
    f = scan_text("u@x.com")[0]
    assert f.fingerprint == hash_value("u@x.com")


def test_critical_findings_sort_first():
    text = "u@x.com card 4111 1111 1111 1111"
    findings = scan_text(text)
    assert findings[0].severity == "CRITICAL"
    assert findings[0].type == "CARD"
