#!/usr/bin/env bash
cd ~/Entrelazamiento-EMQR || { echo "No encuentro el repo"; bash; }

set +e
set +u
set +o pipefail 2>/dev/null

echo "=== TEST V16 ===" | tee v16_chrono_log.txt
python3 -m unittest tests/test_chronological_windows.py -v 2>&1 | tee -a v16_chrono_log.txt
TEST_STATUS=${PIPESTATUS[0]}

echo "=== RUN V16 ===" | tee -a v16_chrono_log.txt
python3 run_v16_chronological_confirmation.py 2>&1 | tee -a v16_chrono_log.txt
RUN_STATUS=${PIPESTATUS[0]}

echo "TEST_STATUS=$TEST_STATUS" | tee -a v16_chrono_log.txt
echo "RUN_STATUS=$RUN_STATUS" | tee -a v16_chrono_log.txt

if [ "$TEST_STATUS" -eq 0 ] && [ "$RUN_STATUS" -eq 0 ]; then
  git add cbr_ltt/emqr_chronological_windows.py \
    run_v16_chronological_confirmation.py \
    tests/test_chronological_windows.py \
    README_V16_CHRONOLOGICAL.md \
    cbr_ltt_real_v16_chronological_report.json \
    v16_chrono_log.txt \
    v16_run_and_push.sh

  git commit -m "Añade ventanas cronologicas EMQR V16" 2>&1 | tee -a v16_chrono_log.txt
  git push origin main 2>&1 | tee -a v16_chrono_log.txt
else
  echo "NO HAGO COMMIT: fallo V16" | tee -a v16_chrono_log.txt
fi

tail -100 v16_chrono_log.txt
echo "Pulsa Enter para terminar."
read _
