#!/usr/bin/env python3
"""Validate public cases without network, credentials, or model calls."""
import argparse, json, pathlib, sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", required=True)
    args = parser.parse_args()
    path = pathlib.Path(args.cases)
    if not path.is_file():
        print(json.dumps({"status":"error","error":"cases_file_not_found"}))
        return 2
    rows=[]; ids=set(); errors=[]
    for n, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not raw.strip(): continue
        try: row=json.loads(raw)
        except json.JSONDecodeError as exc:
            errors.append({"line":n,"error":f"invalid_json:{exc.msg}"}); continue
        for key in ("case_id","suite","task","expected_mode"):
            if not row.get(key): errors.append({"line":n,"error":f"missing:{key}"})
        if row.get("case_id") in ids: errors.append({"line":n,"error":"duplicate_case_id"})
        ids.add(row.get("case_id")); rows.append(row)
    result={"status":"ok" if not errors else "error","network_calls":0,"secrets_read":0,"cases":len(rows),"unique_case_ids":len(ids),"errors":errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1

if __name__ == "__main__": sys.exit(main())
