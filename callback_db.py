import sqlite3


class DatabaseHandler:
    """
    This class will handle the database transaction in order to
    obtain the caller ext.  and the  busy number ext.

    1) SQLITE3 connection
    2) Retrieve caller and callee  extn.
    3) Creating unique tracking data for each callback (call book)
    4) Then binding to SIP header and send to the remote MiTel Server.
    """

    def __init__(self):
        """
        callback.db is the db that will update by other pbx system with their own
        API. As an example:
            Asterisk PBX can create such update by using call file.
            call file will update the  cbregistry table

        callback.db
            CREATE TABLE `cbregistry` (
                            `id`	INTEGER NOT NULL,
                            `cbfrom`	TEXT NOT NULL,
                            `cbto`	TEXT NOT NULL,
                            `cbstatus`	TEXT NOT NULL,
                            PRIMARY KEY(`id`));
        """
        try:
            self.conn = sqlite3.connect('callback.db')  # db will update from other pbx API
            self.cur = self.conn.cursor()
        except Exception as e:
            print(f"callback.db Connection Error :{e}")
        pass

    def get_callback_ext(self):
        """
            This function will get  caller and callee ext numbers from  .db
            """
        if not self.conn.in_transaction:
            request_data = "SELECT * FROM callback"
            for data in  self.cur.execute(request_data):
                print(data)
