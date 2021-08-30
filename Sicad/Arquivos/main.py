import logging

from flask import Flask, render_template, request, make_response, escape, session, url_for, redirect, flash


app = Flask(__name__)
app.secret_key = "flash message"
app.config['SECRET_KEY'] = "1234"

app = Flask(__name__)

#--------------------------------------------------------------------------------------#
@app.route('/')
def hello():
    return render_template('index.html')
    
    
#--------------------------------------------------------------------------------------#
@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500
    
    
#--------------------------------------------------------------------------------------#    
def conexao():
    server = 'DESKTOP-RBIFR2M'
    database = 'Formulario'

    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                          server+';DATABASE='+database+';Trusted_Connection=yes;')
    cursor = cnxn.cursor()
    return cursor


#--------------------------------------------------------------------------------------#
@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':
        emailForm = request.form['email']
        passwordForm = request.form['password']

        global email_global    

        email_global = emailForm       
      
        emailAdmim = request.form['email']
        passwordAdmim = request.form['password']
        cursor = conexao()
        sql = "select email from formulario where email = '{}' and senha = '{}'".format(
            emailForm, passwordForm)
        cursor.execute(sql)
        result_set = cursor.fetchall()

        aut = False
        for row in result_set:
            if(row.email != ''):
                aut = True

        if(aut == True and emailAdmim == 'Ahrkan@gmail.com' and passwordAdmim == '1234' or emailAdmim == '2@2' and passwordAdmim == '2'):
            session['autenticacao'] = True
            return redirect(url_for('lista'))

        if(aut == True and emailAdmim == '1@1' and passwordAdmim == '1'):
            session['autenticacao'] = True
            return redirect(url_for('index'))

        if(aut == True):
            session['autenticacao'] = True 
            return redirect(url_for('meuPerfil'))
        else:
            return redirect(url_for('loginUsuario'))
       

#--------------------------------------------------------------------------------------#
@app.route('/logout')
def logout():
    session.pop('autenticacao', None)  # Apaga os dados de login lá da session
    return redirect(url_for('index'))


#--------------------------------------------------------------------------------------#
@app.route('/resultado', methods=['POST', 'GET'])
def resultado():
    if request.method == 'POST':

        name = request.form['Name']
        nascimento = request.form['Nascimento']
        idade = request.form['Idade']
        genero = request.form['Genero']
        email = request.form['Email']
        password = request.form['Senha']
        objetivo = request.form['Objetivo']

        cursor = conexao()

        cursor.execute("INSERT INTO formulario values ('" + name + "','" + nascimento + "','" +
                       idade + "','" + genero + "','" + email + "','" + password + "','" + objetivo + "')")

        cursor.commit()
        cursor.close()

        return redirect("http://127.0.0.1:5000/loginUsuario")


#--------------------------------------------------------------------------------------#
@app.route('/list/')
def lista():
    cursor = conexao()

    cursor.execute("SELECT * FROM formulario")

    result_set = cursor.fetchall()
    return render_template('tabela.html', listando=result_set)


#--------------------------------------------------------------------------------------#
@app.route('/meuPerfil', methods=['GET', 'POST'])
def meuPerfil():
    if 'autenticacao' in session:
        if(session['autenticacao'] == True):
            emailM = email_global

            cursor = conexao()
            cursor.execute(
                "SELECT nome_completo, data_de_nascimento, idade, inserir_genero, email, senha, objetivo_da_graduacao FROM formulario where email = '{}'".format(emailM))

            result_set = cursor.fetchall()
            return render_template('meuPerfil.html', mostrar=result_set)
    else:
        return redirect(url_for('loginUsuario'))


#--------------------------------------------------------------------------------------#
@app.route('/editar/<email>', methods=['POST', 'GET'])
def editar(email):
    if request.method == 'POST':

        name = request.form['NameU']
        nascimento = request.form['NascimentoU']
        idade = request.form['IdadeU']
        genero = request.form['GeneroU']

        password = request.form['SenhaU']
        objetivo = request.form['ObjetivoU']

        cursor = conexao()

        cursor.execute("Update formulario set nome_completo = '" + name + "', data_de_nascimento = '" + nascimento + "', idade = '" + idade + "', inserir_genero = '" +
                       genero + "', senha = '" + password + "', objetivo_da_graduacao = '" + objetivo + "' where email ='" + email_global + "'")

        cursor.commit()
        cursor.close()

        return redirect("http://127.0.0.1:5000/meuPerfil")


#--------------------------------------------------------------------------------------#
@app.route('/excluir/<emailUsr>')
def excluir(emailUsr):

    cursor = conexao()

    cursor.execute("DELETE from formulario where email ='" + emailUsr + "'")

    flash("Usuário Excluido com sucesso!")
    cursor.commit()
    cursor.close()

    return redirect("http://127.0.0.1:5000/")
    return emailUsr

#--------------------------------------------------------------------------------------#
@app.route('/editarAdmim/', methods=['POST', 'GET'])
def editarAdmim():
    if request.method == 'POST':
        id_pessoas = request.form['id_pessoas']
        name = request.form['Name']
        nascimento = request.form['Nascimento']
        idade = request.form['Idade']
        genero = request.form['Genero']
        email = request.form['Email']
        password = request.form['Senha']
        objetivo = request.form['Objetivo']

        cursor = conexao()

        cursor.execute("Update formulario set nome_completo = '" + name + "', data_de_nascimento = '" + nascimento + "', idade = '" + idade + "', inserir_genero = '" +
                       genero + "', email = '" + email + "', senha = '" + password + "', objetivo_da_graduacao = '" + objetivo + "' where id_pessoas ='" + id_pessoas + "'")
        flash("Perfil Alterado com sucesso!")
        cursor.commit()
        cursor.close()

        return redirect("http://127.0.0.1:5000/list/")


#--------------------------------------------------------------------------------------#
@app.route('/excluirAdmim/<idUsr>')
def excluirAdmim(idUsr):

    cursor = conexao()

    cursor.execute("DELETE from formulario where id_pessoas ='" + idUsr + "'")

    flash("Usuário Excluido com sucesso!")
    cursor.commit()
    cursor.close()

    return redirect("http://127.0.0.1:5000/list/")
    return idUsr

    
#--------------------------------------------------------------------------------------#  
if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
