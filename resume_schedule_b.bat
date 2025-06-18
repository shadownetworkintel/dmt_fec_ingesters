@echo off
set PYTHONPATH=%CD%
python -m ingesters.schedule_b_ingester --resume-index 4111320241068394131 --resume-date 2024-06-05
pause