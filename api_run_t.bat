@echo off
echo 松勤-教管系统接口自动化运行准备开始......
@echo on



del /f /s /q  E:\songqin\teach\report\tmp\*.json
del /f /s /q  E:\songqin\teach\report\tmp\*.jpg
del /f /s /q  E:\songqin\teach\report\report



@echo off
echo 环境文件删除工作完成，开始运行脚本......
@echo on


cd  E:\songqin\teach\testCaseTeach
pytest  -sq --alluredir=../report/tmp --allure-severities=normal,critical
allure generate  ../report/tmp -o ../report/report --clean


@echo off
echo 接口自动化运行成功
pause

