import allure
import tests_cases.conftest as conf

class DBActions:
    @staticmethod
    @allure.step('Query builder')
    def query_builder(columns, table, where_name, where_value):
        """
        Builds a SQL SELECT query based on the given parameters.

        :param columns: List of column names to be selected.
        :param table: The name of the table.
        :param where_name: The column name for the WHERE condition.
        :param where_value: The value for the WHERE condition.
        :return: A string representing the SQL SELECT query.
        """

        cols=','.join(columns)         # Join columns with commas for the SELECT statement
        if isinstance(where_value, str):
            where_value = f"'{where_value}'"         # Ensure the where_value is properly quoted if it's a string
            # Build the query string
        query = f"SELECT {cols} FROM {table} WHERE {where_name} = {where_value}"
        return query


    @staticmethod
    @allure.step('Get Query Result')
    def get_query_result(columns, table, where_name, where_value):
        query = DBActions.query_builder(columns, table, where_name, where_value)
        db_cursor = conf.db_connector.cursor()
        db_cursor.execute(query)
        result = db_cursor.fatchall()
        return result # returns list of Tuples