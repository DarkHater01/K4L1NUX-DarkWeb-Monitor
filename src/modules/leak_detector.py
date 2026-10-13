import re
from dataclasses import dataclass

from src.core.hasher import hash_value

EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
CARD_RE = re.compile(r"\b(?:\d[ -]?){12,18}\d\b")
BCRYPT_RE = re.compile(r"\$2[aby]?\$\d{2}\$[./A-Za-z0-9]{53}")
HASH_RE = re.compile(r"\b[a-fA-F0-9]{32,64}\b")

SEVERITY = {
    "CARD": "CRITICAL",
    "PASSWORD_HASH": "HIGH",
    "EMAIL": "HIGH",
    "HASH": "MEDIUM",
    "KEYWORD": "LOW",
}

_ORDER = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}

MAX_SCAN_CHARS = 1_000_000


@dataclass(frozen=True)
class Finding:
    type: str
    severity: str
    value: str
    fingerprint: str


def luhn(number: str) -> bool:
    digits = [int(c) for c in re.sub(r"\D", "", number)]
    if not 13 <= len(digits) <= 19:
        return False
    total = 0
    for i, d in enumerate(reversed(digits)):
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total % 10 == 0


def _mask(value: str) -> str:
    if len(value) <= 4:
        return "*" * len(value)
    return value[:2] + "*" * (len(value) - 4) + value[-2:]


def scan_text(text: str, keywords: list[str] | None = None) -> list[Finding]:
    """Detecta datos sensibles en texto plano. Puro, sin red: testeable offline."""
    text = text[:MAX_SCAN_CHARS]
    keywords = keywords or []
    findings: list[Finding] = []
    seen: set[tuple[str, str]] = set()

    def add(kind: str, raw: str) -> None:
        fp = hash_value(raw.lower())
        key = (kind, fp)
        if key in seen:
            return
        seen.add(key)
        findings.append(Finding(kind, SEVERITY[kind], _mask(raw), fp))

    for m in BCRYPT_RE.finditer(text):
        add("PASSWORD_HASH", m.group())
    for m in EMAIL_RE.finditer(text):
        add("EMAIL", m.group())
    for m in CARD_RE.finditer(text):
        digits = re.sub(r"\D", "", m.group())
        if luhn(digits):
            add("CARD", digits)
    for m in HASH_RE.finditer(text):
        add("HASH", m.group())

    low = text.lower()
    for kw in keywords:
        kw = kw.strip()
        if kw and kw.lower() in low:
            add("KEYWORD", kw)

    return sorted(findings, key=lambda f: (_ORDER[f.severity], f.type, f.value))
