// Operadores lógicos

// NoSQL        JavaScript
// ------------------------------
// $and          &&
// $or           ||
// $not          !
// $eq           ==
// $gt            >
// $gte           >=
// $lt            <
// $lte           <=
// $ne            !=
// $in            verificar se um ou mais dados estão (estão contidos) em um array
// $nin   (not in) é o inverso do in, os dados passados não irão ser retornados no array, na consulta



// Update Operadores
// Usando o operador $set para definir o valor de um campo específico
db.usuarios.updateOne({ nome: "João" }, { $set: { idade: 26 } });

// Usando o operador $inc para incrementar o valor de um campo numérico
db.usuarios.updateOne({ nome: "João" }, { $inc: { idade: 1 } });

// Usando o operador $rename para renomear um campo existente
db.usuarios.updateOne({ nome: "João" }, { $rename: { "endereco.rua": "endereco.nomeRua" } });

// Usando o operador $unset para remover um campo específico de um documento
db.usuarios.updateOne({ nome: "João" }, { $unset: { endereco: "" } });

// Delete
// Usando o método deleteOne() para excluir o primeiro documento que corresponde ao filtro especificado
db.usuarios.deleteOne({ nome: "João" });

// Usando o método deleteMany() para excluir todos os documentos que correspondem ao filtro especificado
db.usuarios.deleteMany({ cidade: "São Paulo" });


// Operadores Lógicos

// maior ou igual $gte
db.usuarios.find({ $and: [{ idade: { $gte: 18 } }, { cidade: "São Paulo" }] });
// menor $lt ou $or
db.usuarios.find({ $or: [{ idade: { $lt: 18 } }, { cidade: "Rio de Janeiro" }] });
// não tem $not
db.usuarios.find({ idade: { $not: { $eq: 25 } } });

// Operadores de Comparação

// igual $eq
db.usuarios.find({ idade: { $eq: 25 } });

// diferente $ne
db.usuarios.find({ idade: { $ne: 30 } });

db.usuarios.find({ idade: { $gt: 30 } });

db.usuarios.find({ idade: { $gte: 30 } });

db.usuarios.find({ idade: { $lt: 30 } });

// menor ou igual $lte
db.usuarios.find({ idade: { $lte: 30 } });

db.usuarios.find({ cidade: { $in: ["São Paulo", "Rio de Janeiro"] } });

db.usuarios.find({ cidade: { $nin: ["São Paulo", "Rio de Janeiro"] } });


// Projeção
db.usuarios.find({}, { nome: 1, idade: 1 })

// Ordenação
db.usuarios.find().sort({ idade: 1 })
// Limitação
db.usuarios.find().limit(10)
// Paginação
db.usuarios.find().skip(10).limit(5)