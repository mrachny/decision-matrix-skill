#!/usr/bin/env python3
"""Build a standalone interactive decision-matrix HTML report from a JSON data file.

Usage:
    python3 build_report.py data.json report.html

See SKILL.md for the data schema. This script only does string templating + basic
validation; the actual interactivity lives in assets/report_template.html.
"""
import json
import sys
from pathlib import Path

TEMPLATE_PATH = Path(__file__).resolve().parent.parent / "assets" / "report_template.html"
START_MARKER = "/*__DECISION_DATA__*/"
END_MARKER = "/*__END_DECISION_DATA__*/"


def validate(data: dict) -> None:
    for key in ("meta", "criteria", "options", "scores"):
        if key not in data:
            raise SystemExit(f"data file is missing required top-level key: {key!r}")
    if not isinstance(data["meta"], dict) or not data["meta"].get("title"):
        raise SystemExit("meta.title is required")

    criteria = data["criteria"]
    options = data["options"]
    if len(criteria) < 2:
        raise SystemExit("need at least 2 criteria")
    if len(criteria) > 12:
        raise SystemExit(
            f"got {len(criteria)} criteria; this method works best with 5-10 — "
            "consolidate overlapping ones before building the report"
        )
    if len(options) < 2:
        raise SystemExit("need at least 2 options")
    if len(options) > 10:
        raise SystemExit(f"got {len(options)} options; shortlist to 10 or fewer first")

    crit_ids = [c.get("id") for c in criteria]
    opt_ids = [o.get("id") for o in options]
    if any(not cid for cid in crit_ids):
        raise SystemExit("every criterion needs a non-empty 'id'")
    if any(not oid for oid in opt_ids):
        raise SystemExit("every option needs a non-empty 'id'")
    if len(set(crit_ids)) != len(crit_ids):
        raise SystemExit("criteria ids must be unique")
    if len(set(opt_ids)) != len(opt_ids):
        raise SystemExit("option ids must be unique")

    for c in criteria:
        if not c.get("label"):
            raise SystemExit(f"criterion '{c.get('id')}' needs a 'label'")
        w = c.get("weight")
        if not isinstance(w, (int, float)) or not (1 <= w <= 10):
            raise SystemExit(f"criteria '{c['id']}' weight must be a number 1-10 (got {w!r})")

    for o in options:
        if not o.get("label"):
            raise SystemExit(f"option '{o.get('id')}' needs a 'label'")

    scores = data["scores"]
    for oid in opt_ids:
        row = scores.get(oid)
        if row is None:
            raise SystemExit(f"scores is missing option: {oid!r}")
        for cid in crit_ids:
            v = row.get(cid)
            if not isinstance(v, (int, float)) or not (1 <= v <= 10):
                raise SystemExit(
                    f"scores[{oid!r}][{cid!r}] must be a number 1-10 (got {v!r})"
                )


def build(data_path: str, output_path: str) -> None:
    data = json.loads(Path(data_path).read_text(encoding="utf-8"))
    validate(data)

    template = TEMPLATE_PATH.read_text(encoding="utf-8")
    start = template.find(START_MARKER)
    end = template.find(END_MARKER)
    if start == -1 or end == -1 or end < start:
        raise SystemExit(f"template is missing the {START_MARKER} ... {END_MARKER} markers")
    start += len(START_MARKER)

    payload = json.dumps(data, ensure_ascii=False)
    # guard against "</script>" inside a string value breaking out of the <script> tag
    payload = payload.replace("</", "<\\/")

    html = template[:start] + payload + template[end:]
    title = data["meta"]["title"]
    html = html.replace("{{TITLE}}", f"{title} — Decision Matrix".replace("&", "&amp;").replace("<", "&lt;"))
    Path(output_path).write_text(html, encoding="utf-8")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise SystemExit(f"usage: {sys.argv[0]} <data.json> <report.html>")
    build(sys.argv[1], sys.argv[2])
    print(f"wrote {sys.argv[2]}")
