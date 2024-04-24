-- SET nome nomePessoa
-- KEYS nome
-- DEL nome
-- INCR acessos (incrementar)
-- DCR acessos (decrementar)
-- LPUSH usuarios "Luffy" "Ace" "Sanji" "Zoro"(criar array em redis)
-- LRANGE usuarios 0 -1 (visualizar do início 0, até o último -1 da lista do array)
-- LLEN usuarios (tamanho do array 4)




-- redis.call é usado para enviar o comando SET diretamente para o servidor Redis.
local redis = require "redis"

-- redis.call('SET', 'chave', 'valor')
redis.call('SET', 'nome', 'Ace')
redis.call('GET', 'nome') -- Ace
redis.call('DEL', 'nome')
redis.call('KEYS', 'nome')


-- Exemplo utilizando uma biblioteca cliente Redis (lua-redis) em Lua, usando 
-- os métodos fornecidos pela biblioteca para interagir com o servidor Redis


local redis = require "redis"
local client = redis.connect('127.0.0.1', 6379)

client:set('nome', 'Ace')
client:keys('nome')
client:del('nome')
client:set('acessos', 1)
client:incr('acessos') -- 2
client:decr('acessos') -- 1
client:lpush('nomes', 'Ace', 'Luffy', 'Sanji', 'Zoro')
client:lrange('nomes', 0, -1)
client:llen('nomes')

client:quit()

-- redis.call é usado para executar comandos Redis 
-- diretamente do script Lua, enquanto client:set 
-- (ou qualquer método similar fornecido por 
-- uma biblioteca cliente Redis) é usado quando 
-- está interagindo com o Redis por meio 
-- de uma biblioteca cliente em Lua


