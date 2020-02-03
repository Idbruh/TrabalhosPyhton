#Criar uma pagina para cadastro de squads (times de desenvolvimento)
# 1-Criar tabela Squad
# 2-Criar Dao Squad
# 3-Criar Model Squad
# 4-Criar controller Squad
# 5-Criar View tipo console para realizar as 4 operacoes de CRUD de Squads
# 6-Criar View tipo Web para realizar as 4 operacoes de CRUD de Squads
# Squad: Nome, Descricao, NumeroPessoas, LinguagemBackEnd, FrameworkFrontEnd 



#-- PARTE 2
# CRUD  -- LINGUAGEM BACKEND
# CRUD DE SGBDS (BD - EX: , SQLSERVER, ORACLE)
#  ADICIONAR VINCULO DESTAS 3 TABELAS NA TABELA SQUADS (FK) 


Definição de Squads

No contexto corporativo, squad é um modelo organizacional que consiste em dividir a equipe da empresa em pequenos times 
multidisciplinares.
Na HBSIS todas as equipes de produto são divididas em squads e possuem um stack padrão que envolve linguagem de programação backend, 
framework frontend e banco de dados. 
Recentemente foram contratados três novos programadores para compor as squads.
 Será preciso enviar cada novo programador para uma Squad de acordo com suas habilidades. 
Hoje são utilizados três bancos de dados no ambiente HBSIS, o MsSqlServer, PostgreSQL e o MongoDb.
As equipes que atualmente possuem vagas em aberto utilizam como linguagem de backend,  Python, Java e PHP. 
Como framework de frontend estão sendo utilizados o React, Angular e Vue. 
Existem várias squads que utilizam a mesma linguagem de backend porém utilizam banco de dados e framework frontend distintos. 
Os três programadores que foram contratados são; Mateus, Tiago e a Nicole. 
Cada um dos programadores possui conhecimento em um banco de dados, 
uma linguagem de backend e um framework frontend.Foi realizada uma avaliação com cada um dos programadores e
estipulado algumas regras para inseri-los nas squads. 
O programador que trabalha com Java também conhece PostgreSql. 
O framework de frontend de Nicole não é VUE. O programador que usa Angular trabalha com MongoDb. 
Mateus é especialista Python e não conhece MySqlServer. Tiago não sabe PHP. 

Crie um sistema que realize a validação da regras estipuladas 
e apenas permita que um programador seja inserido em uma squad se estiver de acordo com seus conhecimentos de linguagem, 
framework e banco de dados.
Usando as estruturas( Lista, Tuplas, Dicionarios), Classes, Metodos
Deve ser feito apenas no console - Usar esquema de cores.


connection name: mysql.padawans.dev
host:    mysql.padawans.dev
user: padawans17
senha: mb2019


ID, Nome, Descricao, NumeroPessoas, LinguagemBackEnd, FrameworkFrontEnd
