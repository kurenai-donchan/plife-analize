@echo off
cd /d %~dp0

REM ------------------------------------------------------------------------
REM plife �N���pbat�t�@�C��
REM ------------------------------------------------------------------------

cd ../src/scripts

python get_plife_slot_payout.py

exit 0