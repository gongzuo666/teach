cd E:\songqin\teach\testCaseTeach
pytest -sq --alluredir=../report/tmp
allurre generate  ../report/tmp -o ../report/report --clean