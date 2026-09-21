CREATE DATABASE projeto_cep;
USE projeto_cep;

CREATE TABLE consultas_cep (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cep VARCHAR(9) NOT NULL,
    logradouro VARCHAR(150),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf VARCHAR(2),
    data_consulta TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SHOW TABLES;