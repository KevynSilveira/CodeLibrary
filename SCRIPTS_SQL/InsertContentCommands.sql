#Usa o Banco codeLibrary
use codeLibrary;

#Inseri o valor na tabela
insert into commands (language, command, description)
values
('SQL', 'TRUNCATE TABLE (Nome da tabela)', 'Exclui todos os dados da tabela indicada. '),
('SQL', 'SELECT * FROM (Nome da tabela) ORDER BY (Nome da coluna) ', 'Trará como resultado a tabela ordenado de acordo com a coluna, se for numero do maior para o menor e se for letra de a-z.'),
('SQL', 'ROOLBACK', 'Volta a alteração, caso o programador tenha usado o START TRANSACTION.'),
('SQL', 'START TRANSACTION', 'Backup para poder voltar a alteração.'),
('SQL', 'SHOW DATABASES', 'Mostra os bancos ativos.');


select * from commands
