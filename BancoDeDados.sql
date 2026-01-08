-- Apenas para teste -- 

-- Renovando os IDs --
DROP DATABASE IF EXISTS teste;

CREATE DATABASE teste CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE teste;

CREATE TABLE categoria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE
) ENGINE=InnoDB;

CREATE TABLE produto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(200) NOT NULL,
    preco DECIMAL(10,2) NOT NULL CHECK (preco >= 0),
    id_categoria INT NULL,  
    FOREIGN KEY (id_categoria) REFERENCES categoria(id) ON DELETE SET NULL
) ENGINE=InnoDB;

INSERT INTO categoria (nome) VALUES 
('Eletrônicos'),
('Alimentos'),
('Roupas'),
('Livros'),
('Informática'),
('Brinquedos'),
('Casa e Cozinha');
