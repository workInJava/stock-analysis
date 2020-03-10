class mysql_config():


    def get_config(self, name):
        config = {
            'python': {
            'user': 'test',
            'password': 'whmline0',
            'host': '192.168.2.58',
            'database': 'python',
            'raise_on_warnings': True
            }
        }
        return config[name]