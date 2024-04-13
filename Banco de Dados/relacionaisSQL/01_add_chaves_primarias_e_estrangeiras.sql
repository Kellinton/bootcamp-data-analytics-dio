-- CREATE TABLE viagens.usuarios (
--     id INT COMMENT 'Identificador',
--     nome VARCHAR(255) NOT NULL COMMENT 'Nome de usuário',
--     email VARCHAR(100) NOT NULL UNIQUE COMMENT 'E-mail do usuário',
--     endereco VARCHAR(50) NOT NULL COMMENT 'Endereço',
--     data_nascimento DATE NOT NULL COMMENT 'Data de nascimento'
-- );

-- CREATE TABLE viagens.destinos (
--     id INT COMMENT 'Identificador do destino',
--     nome VARCHAR(255) NOT NULL UNIQUE COMMENT 'Nome do destino',
--     descricao text NOT NULL COMMENT 'Descrição do destino'
-- );

-- CREATE TABLE viagens.reservas (
-- 	id INT COMMENT 'Identificador único da reserva',
-- 	id_usuario INT COMMENT 'Referência ao ID do usuário que fez a reserva',
--     id_destino INT COMMENT 'Referência ao ID do destino da reserva',
--     data DATE COMMENT 'Data da reserva',
--     status VARCHAR(255) DEFAULT 'pendente' COMMENT 'Status da reserva (confirmada, pendente, cancelada, etc...)'
-- );


-- Chave Primária e auto incremento em uma tabela existente

ALTER TABLE usuarios
MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY (id);

ALTER TABLE destinos
MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY (id);

ALTER TABLE reservas
MODIFY COLUMN id INT AUTO_INCREMENT,
ADD PRIMARY KEY (id);

-- Chave estrangeira 

ALTER TABLE reservas
ADD CONSTRAINT fk_reservas_usuarios
FOREIGN KEY (id_usuario)
REFERENCES usuarios (id);

ALTER TABLE reservas
ADD CONSTRAINT fk_reservas_destinos
FOREIGN KEY (id_destino)
REFERENCES destinos (id);