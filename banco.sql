create table banco_proj3;
use banco_proj3;
create table usuarios(
	id int auto_increment primary key,
    nome varchar (100) not null,
    idade int not null,
    tipo_deficiencia varchar (100) not null
);
DELETE FROM usuarios WHERE id = 0;
