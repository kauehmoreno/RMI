# RMI (REMOTE METHOD INVOCATION)

### PROJETO DE FACULDADE - MATÉRIA SISTEMAS DISTRIBUÍDOS


> Baseado no concetio de RMI do JAVA
> este projeto simula de maneira bem simples, didatica como um method
> pode ser invocado funcionando como um lambda da amazon...

`lembrando que este projeto visa apenas de maneira conceitual simular o RMI`


### COMO FUNCIONA ?

```
 Há duas rotas - `localhost:8000/`

Uma rota irá entregar o valor de get e tambem post

a grande brincadeira está no middleware criado que irá invocar um metodo a partir

do tipo de request.method selecionado....

A simulação é como se fosse um hook, o qual uma aplicação faz uma ação e precisa
pegar um conteúdo .. ela passará o method get para um determinado endpoint no caso
localhost:8000/

suponhamos que agora é necessário executar uma função de post .. essa aplicação bate no mesmo
endpoint que irá por sua vez invocar um outro método que irá retornar o payload passado

para ele no request.
```

### exemplo

`post em localhost:8000/`


#### envio
```json
{
  "foto": "img/kaueh.png",
  "curso": "Ciencia da computacao",
  "periodo": "sétimo",
  "cidade": "Rio de Janeiro",
  "data_nascimento": "1992-12-29",
  "aluno": "Kaueh M ",
  "endereco": "Teste",
  "email": "lala@gmail.com"
}
```

#### fallback

```json

{
  "materia": "Sistemas Distribuidos",
  "data_consulta": "2017-10-28",
  "faculdade": "Universidade Veiga de Almeida",
  "professor": "Marcelo Costa",
  "additional_information":{
    "foto": "img/kaueh.png",
    "curso": "Ciencia da computacao",
    "periodo": "sétimo",
    "cidade": "Rio de Janeiro",
    "data_nascimento": "1992-12-29",
    "aluno": "Kaueh M ",
    "endereco": "Teste",
    "email": "lala@gmail.com"
  },
  "trabalho": "RMI(Remote Project Invocation)",
  "method": "POST"
}

```

## USAR

* `seguir Makefile do projeto`
*  `utilizar o browser para get`
* `curl ou Rest client do browser para o post`

## SIMULANDO CLIENTE

#### exemplo de POST

```
curl -H "Content-Type: application/json" -X POST -d '{"username":"xyz","password":"xyz"}' http://localhost:8000
```

#### exemplo de GET
```
 curl -X GET  http://localhost:8000
```

### forçando method get de outro RMI
```
curl -H "RMI: rmi " -X GET http://localhost:8000
```
