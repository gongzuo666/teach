@echo off
echo ����-�̹�ϵͳ�ӿ��Զ�������׼����ʼ......
@echo on



del /f /s /q  E:\songqin\teach\report\tmp\*.json
del /f /s /q  E:\songqin\teach\report\tmp\*.jpg
del /f /s /q  E:\songqin\teach\report\report



@echo off
echo �����ļ�ɾ��������ɣ���ʼ���нű�......
@echo on


cd  E:\songqin\teach\testCaseTeach
pytest  -sq --alluredir=../report/tmp --allure-severities=normal,critical
allure generate  ../report/tmp -o ../report/report --clean


@echo off
echo �ӿ��Զ������гɹ�
pause

