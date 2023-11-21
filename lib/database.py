from logging import INFO, Formatter, StreamHandler, getLogger
from traceback import format_exc
from typing import Optional

import mysql.connector

from config.config import DB_HOST, DB_PASSWORD, DB_PORT, DB_USER, SERVER_NAME


class DatabaseConnector:

    def __init__(self):
        self.config = {
            'user': DB_USER,
            'password': DB_PASSWORD,
            'host': DB_HOST,
            'port': DB_PORT,
        }
        self.database = "ipmi_explorer"
        self.table = SERVER_NAME
        self.logger = self.__configure_logger()

    def __configure_logger(self):
        logger = getLogger(__name__)
        if not logger.hasHandlers():
            logger.setLevel(INFO)
            formatter = Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            ch = StreamHandler()
            ch.setFormatter(formatter)
            logger.propagate = False
            logger.addHandler(ch)
        return logger

    def perform_healthcheck(self):
        try:
            cnx = mysql.connector.connect(**self.config)
            cur = cnx.cursor(buffered=True)
            cur.execute("SHOW STATUS LIKE 'Ssl_cipher'")
            cur.close()
            cnx.close()
            self.logger.info("Connexion à la base de données réussie.")
        except:
            self.logger.critical(
                "Erreur lors de la connexion à MariaDB.", exc_info=format_exc())
            exit(-1)

    def check_if_exists(self):
        sql = f"""SHOW DATABASES"""
        try:
            self.logger.info(
                f"Vérification de la présence de la base {self.database}...")
            cnx = mysql.connector.connect(**self.config)
            cur = cnx.cursor(buffered=True)
            cur.execute(sql)
            result = cur.fetchall()
            cur.close()
            cnx.close()
            exists = True if self.database in [
                rec[0] for rec in result] else False
            self.logger.info(
                f"La base {self.database} existe : {exists}")
            return exists
        except:
            self.logger.critical(
                f"Erreur lors de l'affichage des bases dans la base de données.", exc_info=format_exc())
            exit(-1)

    def __drop_database(self):
        sql = f"DROP DATABASE IF EXISTS {self.database}"
        try:
            cnx = mysql.connector.connect(**self.config)
            cur = cnx.cursor(buffered=True)
            cur.execute(sql)
            cur.close()
            cnx.close()
            self.logger.info(f"Base de données {self.database} supprimée (sous réserve d'existance).")
        except:
            self.logger.critical(
                f"Erreur lors de la suppression de la base {self.database}.", exc_info=format_exc())
            exit(-1)

    def __create_database(self):
        sql = f"CREATE DATABASE {self.database}"
        try:
            cnx = mysql.connector.connect(**self.config)
            cur = cnx.cursor(buffered=True)
            cur.execute(sql)
            cur.close()
            cnx.close()
            self.logger.info(f"Base de données {self.database} créée.")
        except:
            self.logger.critical(
                f"Erreur lors de la création de la base {self.database}.", exc_info=format_exc())
            exit(-1)

    def __create_table(self):
        sql = f"""CREATE TABLE {self.table} (
                name VARCHAR(255) NOT NULL,
                ID VARCHAR(255) NOT NULL,
                group_name VARCHAR(255) NOT NULL,
                value FLOAT,
                unit VARCHAR(255) NOT NULL,
                timestamp TIMESTAMP
            )"""
        try:
            custom_config = self.config
            custom_config["database"] = self.database
            cnx = mysql.connector.connect(**custom_config)
            cur = cnx.cursor(buffered=True)
            cur.execute(sql)
            cur.close()
            cnx.close()
            self.logger.info(f"Table {self.table} créée.")
        except:
            self.logger.critical(
                f"Erreur lors de la création de la table {self.table} dans la base {self.database}.", exc_info=format_exc())
            exit(-1)
            
    def __create_index(self):
        sql = f"""CREATE INDEX `index` ON `{self.table}` (`timestamp`)"""
        try:
            custom_config = self.config
            custom_config["database"] = self.database
            cnx = mysql.connector.connect(**custom_config)
            cur = cnx.cursor(buffered=True)
            cur.execute(sql)
            cur.close()
            cnx.close()
            self.logger.info(f"Table {self.table} indexée.")
        except:
            self.logger.critical(
                f"Erreur lors de l'indexation de la table {self.table} dans la base {self.database}.", exc_info=format_exc())
            exit(-1)
            
    def __send_query(self, query: str, val: tuple):
        try:
            custom_config = self.config
            custom_config["database"] = self.database
            cnx = mysql.connector.connect(**custom_config)
            cur = cnx.cursor(buffered=True)
            cur.execute(query, val)
            cnx.commit()
            cur.close()
            cnx.close()
        except:
            self.logger.critical(
                f"Erreur lors de l'exécution de la requête : {query}.", exc_info=format_exc())
            exit(-1)

    def insert_new_metric(self, values):
        sql = f"""INSERT INTO {self.table} (name, ID, group_name, value, unit, timestamp) VALUES (%s, %s, %s, %s, %s, %s)"""
        self.logger.info(f"Insertion de : {values} dans la table : {self.table}.")
        self.__send_query(sql, values)

    def setup_database(self):
        self.logger.info("Préparation de la base de données...")
        self.__drop_database()
        self.__create_database()
        self.__create_table()
        self.__create_index()
        self.logger.info("Base de données configurée.")
