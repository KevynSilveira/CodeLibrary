#iniciando transacao 
Start transaction;

#criando banco de dados
create database CodeLibrary;

use codelibrary;

create table commands(

id int primary key auto_increment not null,
language char (50) not null,
command varchar (200) not null,
description varchar (1000) not null

);

#rollback caso seja necessario voltar a acao
#rollback

