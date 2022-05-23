from data import connection


def save_user_login(name, email, password):
    query = """INSERT INTO users (name, email, password) VALUES(%(name)s, %(email)s, %(password)s)"""
    connection.execute_dml_statement(query, {'name': name, 'email': email, 'password': password})


