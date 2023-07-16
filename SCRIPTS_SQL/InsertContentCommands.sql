#Usa o Banco codeLibrary
use codeLibrary;

#Inseri o valor na tabela
insert into commands (language, command, description)
values
('SQL', 'create database (NOME DO BANCO)', 'Cria um banco de dados com o nome passado.'),
('SQL', 'use (NOME DO BANCO)', 'Acessa o banco de dados indicado para poder fazer alteracoes.'),
('SQL', 'drop schema (NOME DO BANCO)', 'Exclui o banco de dados indicado');


