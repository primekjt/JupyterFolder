@echo off
@echo ----------------------------------------------------------------------------
@echo === Douzone Job 업무자동화 ver.2019.04.19.002 ===
@echo ----------------------------------------------------------------------------
cd/
cd C:\Job\NsmData
echo ...프로그램 로딩중입니다. 잠시만 기다려 주세요~ 
python 더존NSM발주정보확인_ver2.py -f C:\Job\NsmData\Sheet1.xlsx
echo ----------------------------------------------------------------------------
echo ... 끝났습니다.
echo 아무 키나 누르시면 종료됩니다. 좋은 하루되세요.
pause