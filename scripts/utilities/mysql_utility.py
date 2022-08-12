import traceback
import pymysql.cursors
from scripts.config.app_configurations import host,port,user,password,database
from scripts.logging.application_logging import logger

class MYSQL_Utility(object):
    def __init__(self):
        try:
            # logger.info("my sql connection initialization")
            self.host = host
            self.username = user
            self.password = password
            self.db_name = database
        except Exception as e:
            logger.exception("Exception in the MySQL initialization" + str(e))

    def execute_query(self, query):
        connection = None
        # result=""
        flag = False
        try:
            connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.db_name,
                                         charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            with connection.cursor() as cursor:
                cursor.execute(query)
                rot=cursor.fetchall()
            connection.commit()
            flag = rot
        except Exception as e:
            logger.error("Exception while updating: " + str(e))
            traceback.print_exc()
        finally:
            try:
                if connection is not None:
                    connection.close()
            except Exception as e:
                logger.error("Exception while closing connection: " + str(e))
        return flag

    def select_mysql_table(self, query):
        """
        This method is used for selecting records from tables.
        :param query: The select query to be executed
        :return: status: The status True on success and False on failure and the list of rows
        """
        connection = None
        flag = False
        try:
            connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.db_name,
                                         charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            with connection.cursor() as cursor:
                cursor.execute(query)
                select=(cursor.fetchall())
                connection.commit()
            flag = select
        except Exception as e:
            logger.error("Exception while updating: " + str(e))
            traceback.print_exc()
        finally:
            try:
                if connection is not None:
                    connection.close()
            except Exception as e:
                logger.error("Exception while closing connection: " + str(e))
        return flag

    def update_mysql_table(self, query, data=None):
        """
        This method is used for updating tables.
        :param data: the list of values which needs to be updated
        :param query: The update query to be executed
        :return: status: The status True on success and False on failure
        """
        connection = None
        flag = False
        try:
            connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.db_name,
                                         charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            with connection.cursor() as cursor:
                cursor.execute(query, data)
                update=cursor.fetchall()
            connection.commit()
            flag = update
        except Exception as e:
            logger.error("Exception while updating: " + str(e))
            traceback.print_exc()
        finally:
            try:
                if connection is not None:
                    connection.close()
            except Exception as e:
                logger.error("Exception while closing connection: " + str(e))
        return flag

    def insert_mysql_table(self, query, data=None):
        """
        This method is used for inserting new records in tables.
        :param data: list of values which needs to be inserted
        :param query: The insert query to be executed
        :return: status: The status True on success and False on failure
        """
        connection = None
        flag = False
        try:
            connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.db_name,
                                         charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            with connection.cursor() as cursor:
                cursor.execute(query, data)
                insert=cursor.fetchall()
            connection.commit()
            flag = insert
        except Exception as e:
            logger.error("Exception while updating: " + str(e))
        finally:
            try:
                if connection is not None:
                    connection.close()
            except Exception as e:
                logger.error("Exception while closing connection: " + str(e))
        return flag

    def delete_mysql_table(self, query):
        """
        This method is used for updating tables.
        :param query: The update query to be executed
        :return: status: The status True on success and False on failure
        """
        connection = None
        flag = False
        try:
            connection = pymysql.connect(host=self.host, user=self.username, password=self.password, database=self.db_name,
                                         charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            with connection.cursor() as cursor:
                cursor.execute(query)
                delete=cursor.fetchall()
            connection.commit()
            flag = delete
        except Exception as e:
            logger.error("Exception while updating: " + str(e))
            traceback.print_exc()
        finally:
            try:
                if connection is not None:
                    connection.close()
            except Exception as e:
                logger.error("Exception while closing connection: " + str(e))
        return flag
    def select_mysql_fetchone(self, query):
        """
        This method is used for selecting records from tables.
        :param query: The select query to be executed
        :return: status: The status True on success and False on failure and the list of rows
        """
        connection = None
        result = ""
        flag = False
        try:
            print(query)
            connection = pymysql.connect(host=self.host, user=self.username, password=self.password, db=self.db_name,
                                         charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
            flag = True
        except Exception as e:
            logger.error("Exception while updating: " + str(e))
        finally:
            try:
                if connection is not None:
                    connection.close()
            except Exception as e:
                logger.error("Exception while closing connection: " + str(e))
        return flag, result

    def unique_id_generator(self, setup_name):
        """
        This method is used for sgetting a unique id for the setup.
        :param setup_name: The select setup_name
        :return: the unique id
        """
        connection = None
        unique_id = 100
        return_id = ""
        flag = False
        try:
            connection = pymysql.connect(host=self.host, user=self.username, password=self.password, db=self.db_name,
                                         charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cursor = connection.cursor()
            try:
                self.check_table_existence("tbl_setup_counter", "(setup_name VARCHAR(255), unique_id INT(255))")
                # query = """ CREATE TABLE IF NOT EXISTS tbl_setup_counter
                # (setup_name VARCHAR(255), unique_id INT(255));"""
                # cursor.execute(query)
            except Exception as e:
                logger.exception("Exception in the query execution" + str(e))

            try:
                record_query = """SELECT unique_id FROM tbl_setup_counter WHERE setup_name = """ + "'" + \
                               str(setup_name) + "'"
                cursor.execute(record_query)
                data_from_sql = cursor.fetchone()
                try:
                    if data_from_sql and "unique_id" in data_from_sql and data_from_sql["unique_id"] != 0:
                        count = data_from_sql["unique_id"]
                    else:
                        count = 0
                except Exception as e:
                    logger.exception("Exception in the data from the sql" + str(e))
                    count = 0
                if int(count) == 0:
                    try:
                        record_query_insert = "insert into tbl_setup_counter(setup_name, unique_id) values(%s,%s)"
                        self.update_mysql_table(record_query_insert, [setup_name, unique_id])
                    except Exception as e:
                        logger.exception("Exception" + str(e))
                else:
                    unique_id = int(count) + 1
                    update_query = "UPDATE tbl_setup_counter SET unique_id = '" + str(unique_id) + \
                                   "' WHERE setup_name = '" + str(setup_name) + "'"
                    self.update_mysql_table(update_query)
            except Exception as e:
                logger.exception("Exception in the record query" + str(e))
            flag = True
            return_id = str(setup_name) + "_" + str(unique_id)
        except Exception as e:
            logger.error("Exception while updating: " + str(e))
        finally:
            try:
                if connection is not None:
                    connection.close()
            except Exception as e:
                logger.error("Exception while closing connection: " + str(e))
        return flag, return_id

    def check_table_existence(self, table_name, parameter_tuple):
        connection = None
        try:
            connection = pymysql.connect(host=self.host, user=self.username, password=self.password, db=self.db_name,
                                         charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cursor = connection.cursor()
            try:
                query = """ CREATE TABLE IF NOT EXISTS """ + str(table_name) + " " + str(parameter_tuple) + """;"""
                cursor.execute(query)
            except Exception as e:
                logger.exception("Exception in the query execution" + str(e))

        except Exception as e:
            logger.exception("Exception in the check table existance definition" + str(e))

        finally:
            try:
                if connection is not None:
                    connection.close()
            except Exception as e:
                logger.error("Exception while closing connection: " + str(e))

    def fetch_list_data(self, query):
        list_of_lists = []
        connection = None
        try:
            connection = pymysql.connect(host=self.host, user=self.username, password=self.password, db=self.db_name,
                                         charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cursor = connection.cursor()
            try:
                cursor.execute(query)
                json = cursor.fetchall()
                list_of_lists = list(map(lambda each: [each['plant'], each['line'], each['machine']], json))
            except Exception as e:
                logger.error("Exception while fetching " + str(e))
        except Exception as e:
            logger.error("Exception while connecting " + str(e))
        finally:
            try:
                if connection is not None:
                    connection.close()
            except Exception as e:
                logger.error("Exception while closing connection: " + str(e))
        return list_of_lists

    def only_execute_query(self, query):
        connection = None
        try:
            connection = pymysql.connect(host=self.host, user=self.username, password=self.password, db=self.db_name,
                                         charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            cursor = connection.cursor()
            connection.commit()
            try:
                cursor.execute(query)
                query = "SELECT ROW_COUNT() as DelRowCount"
                cursor.execute(query)
                resp = cursor.fetchone()
                print('number of rows deleted', resp)
            except Exception as e:
                logger.exception("Exception in the query execution" + str(e))

        except Exception as e:
            logger.exception("ERROR OCCURRED WHILE DELETING TABLE" + str(e))

        finally:
            try:
                if connection is not None:
                    connection.commit()
                    connection.close()
            except Exception as e:
                logger.error("Exception while closing connection: " + str(e))

    def insert_many_mysql_table(self, query, data=None):
        """
        This method is used for inserting new records in tables.
        :param data: list of values which needs to be inserted
        :param query: The insert query to be executed
        :return: status: The status True on success and False on failure
        """
        connection = None
        flag = False
        try:
            connection = pymysql.connect(host=self.host, user=self.username, password=self.password, db=self.db_name,
                                         charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            with connection.cursor() as cursor:
                cursor.executemany(query, data)
            connection.commit()
            flag = True
        except Exception as e:
            logger.error("Exception while updating: " + str(e))
        finally:
            try:
                if connection is not None:
                    connection.close()
            except Exception as e:
                logger.error("Exception while closing connection: " + str(e))
        return flag

    def delete_many_mysql_table(self, query):
        """
            This method is used for updating tables.
            :param query: The update query to be executed
            :return: status: The status True on success and False on failure
        """
        connection = None
        flag = False
        try:
            connection = pymysql.connect(host=self.host, user=self.username, password=self.password, db=self.db_name,
                                         charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
            with connection.cursor() as cursor:
                cursor.executemany(query)
            connection.commit()
            flag = True
        except Exception as e:
            logger.error("Exception while updating: " + str(e))
            traceback.print_exc()
        finally:
            try:
                if connection is not None:
                    connection.close()
            except Exception as e:
                logger.error("Exception while closing connection: " + str(e))
        return flag

    def update_mysql_table_from_database(self, query, data=None):
        """
        This method is used for updating tables.
        :param data: the list of values which needs to be updated
        :param query: The update query to be executed
        :return: status: The status True on success and False on failure
        """
        connection = None
        flag = False
        try:
            connection = pymysql.connect(host=self.host, user=self.username,
                                         password=self.password, db=self.db_name,
                                         charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

            with connection.cursor() as cursor:
                cursor.execute(query, data)
            connection.commit()
            flag = True
        except Exception as e:
            logger.error("Exception while updating: " + str(e))
            traceback.print_exc()
        finally:
            try:
                if connection is not None:
                    connection.close()
            except Exception as e:
                logger.error("Exception while closing connection: " + str(e))
        return flag

    def select_mysql_table_from_database(self, query):
        """
        This method is used for selecting records from tables.
        :param query: The select query to be executed
        :return: status: The status True on success and False on failure and the list of rows
        """
        connection = None
        result = ""
        flag = False
        try:
            connection = pymysql.connect(host=self.host, user=self.username, password=self.password, db=self.db_name,
                                         charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
            flag = result
        except Exception as e:
            logger.error("Exception while updating: " + str(e))
        finally:
            try:
                if connection is not None:
                    connection.close()
            except Exception as e:
                logger.error("Exception while closing connection: " + str(e))
        return flag, result





