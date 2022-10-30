create database todo_db;
use todo_db;
DROP table todo_items;
create table  todo_items (
id int NOT NULL AUTO_INCREMENT,
mssv int  NOT NULL,
name  varchar(150) CHARACTER SET utf8 NOT NULL,
diem int  NOT NULL,
status enum('Doing','Finished') DEFAULT 'Doing',
created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
updated_at timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP,
PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
