// a partir do id
db.usuarios.deleteOne({ _id: ObjectId("id_do_seu_documento") });

// a partir de um campo existente do documento
db.usuarios.deleteOne({ nome: "Ace" });