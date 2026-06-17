from pathlib import Path
import json
from cbr_ltt.emqr_lab import run_lab_confirmation

report = run_lab_confirmation()
Path("cbr_ltt_real_v14_lab_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(report, indent=2, ensure_ascii=False))
