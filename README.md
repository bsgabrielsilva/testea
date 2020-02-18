# Teste Ambar - Consulta APIADVISOR - CLIMATEMPO

Projeto escrito utilizando a linguagem Python3 com o Flask

Todas as instruções para o teste foram cumpridas, até houveram inserções extras!

## Instruções para rodar este projeto

### Utilizando o Docker
1° Faça um clone deste repositório:
```
$ git clone https://github.com/bsgabrielsilva/testea.git
```
2° Em seguida, abra seu terminal dentro da pasta testea e rode o docker-compose:
```
$ sudo docker-compose up
```
3° Se tudo ocorrer bem, abra seu navegador e digite http://localhost:5000

## Endpoints

- **/cidade?id=*inteiro*** recebe um valor inteiro no parametro id, corresponde ao id da cidade, ao consultar na api, ela irá automaticamente verificar se a cidade já está gravada na base de dados e caso não esteja, ser salva. Retorna com os dados da relacionados/nested serializados, no caso da tabela Tempo. 
- **/cidade/cadastrar?cidade=nome&estado=UF** recebe o nome da cidade e a UF do estado para cadastrar uma cidade na base de dados
- **/analise?data_inicial=YYYY-mm-dd&data_final=YYYY-mm-dd** recebe como parametro data_inicial e data_final, e realiza o cálculo solicitado no desafio, do intervalo entre as datas

Qualquer dúvida, só me chamar no email ou telefone. Obrigado!
