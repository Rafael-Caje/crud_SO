# CRUD (backend) - PYTHON - Oracle VirtualBox - MySQL
Conexão remota através de autenticação SSH na máquina virtual debian (linux), com comunicação com banco de dados MySQL. 

### Recursos do CRUD

- Criação automática do Banco de Dados MySQL nomeado "debiandb" (so_create_db.py);
- Criação da Tabela nomeada "inventory" e inserção de dados (so_create.py) ***;
- Leitura da Tabela "inventory" (so_read.py);
- Atualização da Tabela via INPUT de dados pelo usuário (so_update.py);
- Exclusão de dados via INPUT do usuário (so_delete.py).

### Requisitos

- Máquina Virtual instalada e ATIVA com pacote ssh configurado para acesso remoto. Alterar ip e porta da máquina como desejar. Aqui anote o ip e a porta pois será necessário informar no arquivo "so_config.py", juntamente com seu login e senha da máquina.

- MySQL instalado na máquina virtual, configuração de ip e porta do banco, que também serão informados no arquivo "so_config.py".

- Após configurar arquivo "so_config.py" renomeá-lo para "config.py";

- Instalar pacotes pendentes para os devidos "IMPORTs".

>>> Rodar o Crud em Python!

*** Toda vez que executar o arquivo "so_create.py" a tabela será removida e substituída por uma nova conforme informações do código.