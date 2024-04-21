// Seleciona ou cria o banco de dados "viagens"
// use viagens


// Cria a coleção "usuarios" no banco de dados
db.createCollection("usuarios")

// Cria a coleção "destinos" no banco de dados
db.createCollection("destinos")



// Outra forma de criar uma collection, é inserindo diretamente um documento ({}), e ele já irá criar a collection (usuarios_novo)
db.usuarios_novo.insertOne({});