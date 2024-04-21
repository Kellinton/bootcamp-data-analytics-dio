// Você pode inserir diretamente um documento em uma coleção e se a coleção não existir, ela será criada automaticamente.
// Aqui está sendo inserido um documento vazio na coleção "usuarios"
db.usuarios.insertOne({});
// Aqui está sendo inserido um documento vazio na coleção "destinos"
db.destinos.insertOne({});

// formas de inserir documentos
db.usuarios.insertOne({}); // Inserir apenas 1 documento


// Inserindo o primeiro documento
db.usuarios.insertOne({
    "nome": "Ace",
    "idade": 18,
    "email": "portgasd_ace@gmail.com"
});


db.destinos.insertMany([{}]); // Inserir muitos documento, aceita um array de objetos separado por vírgula

db.usuarios.insertMany([
    {   
        "nome": "Luffy",
        "idade": 30,
        "email": "luffy@gmail.com",
    },
    {   
        "nome": "Ace",
        "idade": 31,
        "email": "ace@gmail.com",
    },

]);

//Inserindo mais usuarios

// Inserir documentos na coleção "usuarios"
db.usuarios.insertMany([{
    nome: "João",
    idade: 25,
    cidade: "São Paulo",
    estado: "SP",
    endereco: {
      rua: "Avenida Principal",
      numero: 123,
      cidade: "São Paulo",
      estado: "SP"
    }
  }, {
    nome: "Maria",
    idade: 30,
    cidade: "Rio de Janeiro",
    estado: "RJ",
    endereco: {
      rua: "Rua Secundária",
      numero: 456,
      cidade: "Rio de Janeiro",
      estado: "RJ"
    }
},{
    nome: "Carlos",
    idade: 20,
    cidade: "São Paulo",
    estado: "SP",
    endereco: {
      rua: "Rua Principal",
      numero: 789,
      cidade: "São Paulo",
      estado: "SP"
    }
  },{
    nome: "Ana",
    idade: 35,
    cidade: "São Paulo",
    estado: "SP",
    endereco: {
      rua: "Avenida Secundária",
      numero: 1011,
      cidade: "São Paulo",
      estado: "SP"
    }
    }
    ,  
    {
    nome: "Pedro",
    idade: 28,
    cidade: "Belo Horizonte",
    estado: "MG",
    endereco: {
      rua: "Rua Principal",
      numero: 1314,
      cidade: "Belo Horizonte",
      estado: "MG"
    }
  }]);
  
