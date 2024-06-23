import unittest
from models.engine.dbStorage import DBstorage


class TestDBConnection(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures"""
        self.db = DBstorage()

    def test_db_connection(self):
        """Test if we can reach the database"""
        try:
            self.db.reload()
        except Exception as e:
            self.fail(f"Test failed due to {e}")


if __name__ == '__main__':
    unittest.main()
