from app import fetch_by_id,fetch_all,add_employee,update_employee,delete_employee
from unittest import TestCase, main
from unittest.mock import patch


class TestEmployee(TestCase):
    
    @patch("app.sqlite3")
    def test_get_all(self, mock_class):
            # Given
            mock_class.connect.return_value.cursor.return_value.execute.return_value.fetchall.return_value = [(1,'mahdi','mahdi@gmail.com','88888888'),(2,'mathis','mathis@gmail.com','88888888'),
            (3,'joran','joran@gmail.com','88888888'),
             (5,'paul','paul@gmail.com','88888888'),
            (6,'Sarah','sarah@gmail.com','12345678')],

            expected_product =  [(1,'mahdi','mahdi@gmail.com','88888888'),(2,'mathis','mathis@gmail.com','88888888'),
            (3,'joran','joran@gmail.com','88888888'),
             (5,'paul','paul@gmail.com','88888888'),
            (6,'Sarah','sarah@gmail.com','12345678')],
             # When
            result_product =fetch_all()
            # Then
            self.assertEqual(expected_product, result_product)
    
    @patch("app.sqlite3")
    def test_addEmployee(self, mocked_object):
        # Given
        mock_execute=(mocked_object.connect.return_value.execute)
        # When
        add_employee('insat','insat@gmail.com','111111')
        # Then
        mock_execute.assert_called_once()



    @patch("app.sqlite3")
    def test_updateProduct(self, mocked_object):
        # Given
        mock_execute=(mocked_object.connect.return_value.execute)
        # When
        update_employee(2,'Mathis', 'Mathis@oulook.com','12345678')
        # Then
        mock_execute.assert_called_once()

    @patch("app.sqlite3")
    def test_deleteEmployee(self, mocked_object):
        # Given
        mock_execute=(mocked_object.connect.return_value.execute)
        # When
        delete_employee(4)
        # Then
        mock_execute.assert_called_once()


if __name__ == '__main__':
    main()