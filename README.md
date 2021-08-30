---

# Crud com Python com framework Flask e SQL Server

---

### Nesse programa iremos fazer um Crud com Python ( Flask ) e o banco de dados sql server. Funcionando no Windows e Linux ( apt ).

### Antes de tudo teremos que baixar o python e o sql server. Abaixo terá os links.

### Python

[Download Python](https://www.python.org/downloads/)

### SQL Server

[Downloads do SQL Server | Microsoft](https://www.microsoft.com/pt-br/sql-server/sql-server-downloads)

---

### Sobre a questão da versão testada, está funcionando no python ( 3.9.5 ) e o SQL Server 19.

---

### Após as instalações faça um clone do repositório e abra os arquivos no seu editor de texto, abaixo tem um link do vscode.

### Visual Studio

[Download Visual Studio Code - Mac, Linux, Windows](https://code.visualstudio.com/download)

---

### No final teremos algo como assim.

![https://github.com/Danilo-Oliveira/Projeto-Sicad/blob/master/imagem/tela.png](https://github.com/Danilo-Oliveira/Projeto-Sicad/blob/master/imagem/tela.png)

### A seguir é necessario instalar algumas bibliotecas para o python, para fazer isso usaremos o "pip" onde o mesmo é instalado automaticamente no Windows, sendo assim apenas temos que instalar o "Flask" pelo terminal. Teremos que baixar o ODBC  Driver 17 no Windows, o driver responsável para conexão com o banco. Abaixo veremos como instalamos para Linux no terminal, qualquer dúvida segue a documentação do pip abaixo.

[Installation - pip documentation v21.2.2](https://pip.pypa.io/en/stable/installation/)

---

Windows ( Microsoft ODBC Driver 17 )

[Microsoft® ODBC Driver 17 for SQL Server® - Windows, Linux e macOS](https://www.microsoft.com/pt-BR/download/details.aspx?id=56567)

```powershell
pip install flask
pip install requests
```

Linux

```
sudo apt install python3-pip
sudo apt install python3-pyodbc
pip3 install flask
pip3 install requests
```

---

### Configure o seu banco de dados com as suas informações: server, database, username e password de sua preferência. Qualquer dúvida documentação do SQL Server abaixo.

![https://github.com/Danilo-Oliveira/Projeto-Sicad/blob/master/imagem/conexao.png](https://github.com/Danilo-Oliveira/Projeto-Sicad/blob/master/imagem/conexao.png)

### Documentação do SQL Server

[Documentação do Microsoft SQL - SQL Server](https://docs.microsoft.com/pt-br/sql/?view=sql-server-ver15)

---

### Pronto, com as bibliotecas instaladas e banco configurado podemos agora executar o código.

---

### Essa é a tela inicial quando o programa executa, clique com o ctrl esquerdo + clique esquerdo do mouse ou digite na url no seu navegador http://127.0.0.1:500/

![https://github.com/Danilo-Oliveira/Projeto-Sicad/blob/master/imagem/executando.png](https://github.com/Danilo-Oliveira/Projeto-Sicad/blob/master/imagem/executando.png)

---

### Depois de iniciar, veremos uma tela onde podemos cadastrar um aluno

![https://github.com/Danilo-Oliveira/Projeto-Sicad/blob/master/imagem/cadastro.png](https://github.com/Danilo-Oliveira/Projeto-Sicad/blob/master/imagem/cadastro.png)

---

### Após cadastrar seremos redirecionados para uma tela de login, onde podemos fazer nosso login com o aluno novo.

![https://github.com/Danilo-Oliveira/Projeto-Sicad/blob/master/imagem/login.png](https://github.com/Danilo-Oliveira/Projeto-Sicad/blob/master/imagem/login.png)

---

### Por padrão já existe alunos cadastrado para o teste, tendo também um usuário Adiministrador para olharmos todos os alunos cadastrados

![https://github.com/Danilo-Oliveira/Projeto-Sicad/blob/master/imagem/admin.png](https://github.com/Danilo-Oliveira/Projeto-Sicad/blob/master/imagem/admin.png)

---

### Agora com o nosso aluno logado, temos as seguites opções: Editar ou Deletar esse aluno.

![https://github.com/Danilo-Oliveira/Projeto-Sicad/blob/master/imagem/editar-delete.png](https://github.com/Danilo-Oliveira/Projeto-Sicad/blob/master/imagem/editar-delete.png)

---

### Editando Aluno

![https://github.com/Danilo-Oliveira/Projeto-Sicad/blob/master/imagem/editar.png](https://github.com/Danilo-Oliveira/Projeto-Sicad/blob/master/imagem/editar.png)

---

### Deletando Aluno

![https://github.com/Danilo-Oliveira/Projeto-Sicad/blob/master/imagem/delete.png](https://github.com/Danilo-Oliveira/Projeto-Sicad/blob/master/imagem/delete.png)

# Assim terminando nosso programa Crud com Python ( Flask ) com Sql Server. Agradeço! [❤](https://www.notion.so/PostgresqlWithPython-b08d46e640404827928210116a2e3fd7)

---

<h3> :man: &nbsp;Sobre mim </h3>

- 💼 &nbsp; Trabalhando como **Estágiario** na **Procurement Garage**

### [💻 Meu Conhecimento](#-workspace-spec-)

  ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
  ![Condas](https://img.shields.io/badge/conda-342B029.svg?&style=for-the-badge&logo=anaconda&logoColor=white)
  ![C#](https://img.shields.io/badge/C%23-239120?style=for-the-badge&logo=c-sharp&logoColor=white)
  ![Json](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white)
  ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
  ![CSS](https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white)
  ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
  ![Postgresql](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
  ![MongoDB](	https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)
  ![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
---

### [🚀 Repositório e versionamentos](#-frameworks-)

  ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
  ![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)
  ![Azure DevOps](https://img.shields.io/badge/Azure_DevOps-0078D7?style=for-the-badge&logo=azure-devops&logoColor=white)

---

### [☁ Cloud](#-cloud-)

  ![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
  ![Microsoft Azure](https://img.shields.io/badge/microsoft%20azure-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white)

---

### [👩‍💻 Ferramentas de Desenvolvimento](#-ide-)

  ![Visual Studio Code](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
  ![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=notion&logoColor=white)
  ![Trello](https://img.shields.io/badge/Trello-0052CC?style=for-the-badge&logo=trello&logoColor=white)
  ![Insomnia](https://img.shields.io/badge/Insomnia-5849be?style=for-the-badge&logo=Insomnia&logoColor=white)
  ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=white)

---

### [💻 Sistemas Operacionais](#-os-)
  ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
  ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

---

<h3> :earth_americas: &nbsp;Onde me encontrar: </h3> 

[![Linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/danilo-oliveira-rodrigues-dos-santos/)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](danilo.o.r.santos@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Danilo-Oliveira/)



---
