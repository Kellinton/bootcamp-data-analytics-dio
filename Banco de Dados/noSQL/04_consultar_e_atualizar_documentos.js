// operadores $set, $inc, $pus...



// consulta, e atualiza para ciclano, e por padrõa, retorna o último registro (fulano), o anterior, não atualizado
db.usuarios.findOneAndUpdate({"nome":"fulano"},{$set: {"nome":"ciclano"}});
// saída (retorno): {
//     _id: ObjectId('662526a5cfda927507e3df90'),
//     nome: 'fulano'
//   }

//  consulta, e atualiza para fulano, e retorna o registro atualizado (fulano)
db.usuarios.findOneAndUpdate(
    {"nome":"ciclano"}, // Critério de consulta
    {"$set": {"nome": "fulano"}}, // Dados de atualização
    {returnDocument: "after"} // Opção para retornar o documento após a atualização
);


// Atualiza todos os documentos na coleção "usuarios" onde o campo "cidade" é igual a "São Paulo",
// atribuindo o valor "SP" ao campo "estado".
// Se o campo "estado" não existir nos documentos onde o campo "cidade" 
// é igual a "São Paulo", o comando criará o campo "estado" e atribuirá 
// o valor "SP" a ele.
db.usuarios.updateMany(
    { cidade: "São Paulo" }, // Critério de consulta
    { $set: { estado: "SP" } } // Operação de atualização
);

// Incrementa o campo "estoque" de todos os documentos na coleção "produtos"
// onde o campo "tipo" é igual a "eletrônico" em 10 unidades.
db.produtos.updateMany(
    { tipo: "eletrônico" }, // Critério de consulta, apenas para consultar
    { $inc: { estoque: 10 } } // Operação de incremento. Ele incrementa o valor do campo "estoque" em 10 unidades para todos os documentos que correspondem ao critério de consulta.
    //OBS: Ele incrementa, então, se o estoque inicial for, por exemplo, 4 e você incrementar em 10 unidades, o novo valor será 14.
);

// Adiciona um novo item ao array "compras" de todos os documentos na coleção "clientes"
// onde o campo "ultimaCompra" é maior do que uma determinada data.
db.clientes.updateMany(
    { ultimaCompra: { $gt: new Date("2024-01-01") } }, // Critério de consulta
    { $push: { compras: "Novo Produto" } } // Operação de push
);
