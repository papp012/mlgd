from data import query
from mlgd import utils


def save_user_to_database(name, email, password):
    hashed_password = utils.hash_password(password)
    query.save_user_login(name, email, hashed_password)
