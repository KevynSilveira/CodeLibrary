#Seleciona a toda a linha que conter em language o conteudo indicado
select * from commands where language like('% CONTEUDO DESEJADO %');

#Seleciona a toda a linha que conter em command o conteudo indicado
select * from commands where command like('% CONTEUDO DESEJADO %');

#Seleciona a toda a linha que conter em description o conteudo indicado
select * from commands where description like('% CONTEUDO DESEJADO %');