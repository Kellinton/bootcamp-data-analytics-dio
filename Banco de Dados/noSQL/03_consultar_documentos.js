// consultar/listar todos os documentos na coleção usuários
db.usuarios.find({});

// listar usuários (pode ser mais de 1) que tem o nome "Ace"
db.usuarios.find({"nome":"Ace"});

// lista apenas o primeiro usuário que tem o nome "Ace"
db.usuarios.findOne({"nome":"Ace"});