from pathlib import Path
import json
from cbr_ltt.emqr_chronological_windows import run_chronological_confirmation

report = run_chronological_confirmation(delay_seconds=0.25)
Path("cbr_ltt_real_v16_chronological_report.json").write_text(
    json.dumps(report, indent=2, ensure_ascii=False),
    encoding="utf-8",
)
print(json.dumps(report, indent=2, ensure_ascii=False))
