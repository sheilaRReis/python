BEGIN TRANSACTION;
INSERT INTO "TestResult" VALUES (1,2,'Teste para Classe 1 - P1x/R3/Mx/Tx','Auto Sequence','Este teste está previsto para os equipamentos:
P10, P12, P15, M8, R3, Tx
Para mais de 10 partes aplicadas seguir os seguintes passos:
 - Usar a caixa de derivação ligada no terminal V6 do Fluke e ligar as partes 
excedentes nesta caixa;
 - Executar o teste completo;
 - Fazer o rodízio entre as partes que estavam na caixa de derivação e as 
partes que estavam ligadas diretamente no Fluke;
 - Repetir estes teste completo;
 - Repetir o rodízio e os testes até que todas as partes tenham sido testadas 
quando ligadas diretamente no Fluke');
INSERT INTO "TestResultItem" VALUES (1,1,'Test Group ',9999.0,'MOhm',NULL,NULL,'User defined
IEC 60601');
INSERT INTO "TestResultItem" VALUES (2,1,'Neutro - Terra',0.3,'V',20.0,NULL,'User defined
IEC 60601');
COMMIT;
