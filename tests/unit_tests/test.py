from app import fetch_by_id,fetch_all,add_employee,update_employee,delete_employee
from unittest import TestCase, main
from unittest.mock import patch


class TestEmployee(TestCase):
    @patch("app.sqlite3")
    def test_get_employee_existant(self, mock_class):
        # given
        mock_class.connect().execute().fetchone.return_value = (4, 'paul','paul@gmail.com','88888888')

        expected_employee = {
            "id": 4,
            "name": "paul",
            "email":"paul@gmail.com",
            "phone":"88888888"
        }

        # when
        item = fetch_by_id(4)

        # then
        assert item == expected_employee
    
    @patch("app.sqlite3")
    def test_get_employee_inexistant(self, mock_class):
        # given
        mock_class.connect().execute().fetchone.return_value = (7, 'paul','paul@gmail.com','88888888')

        expected_employee = {
            "id": 4,
            "name": "paul",
            "email":"paul@gmail.com",
            "phone":"88888888"
        }

        # when
        item = fetch_by_id(7)

        # then
        assert item == expected_employee
    
    @patch("app.sqlite3")
    def test_get_all(self, mock_class):
            # Given
            mock_class.connect().cursor().execute().fetchall.return_value = [(2,'mathiddd','mathis@gmail.com','88888888'),
            (4,'paul','paul@gmail.com','88888888'),
            (6,'wassime','wassimeCenter@gmail.com','12345678'),
            (7,'maryem','ajlanimeryam@gmail.com','12345678')],

            expected_product = [(2,'mathiddd','mathis@gmail.com','88888888'),
            (4,'paul','paul@gmail.com','88888888'),
            (6,'wassime','wassimeCenter@gmail.com','12345678'),
            (7,'maryem','ajlanimeryam@gmail.com','12345678')]
             # When
            result_product =fetch_all()
            # Then
            self.assertEqual(expected_product, result_product)
    
    @patch("app.sqlite3")
    def test_addProduct(self, mocked_object):
        # Given
        mock_execute=(mocked_object.connect.return_value.execute)
        # When
        add_employee('test', 0,0)
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
    def test_deleteProduct(self, mocked_object):
        # Given
        mock_execute=(mocked_object.connect.return_value.execute)
        # When
        delete_employee(4)
        # Then
        mock_execute.assert_called_once()


if __name__ == '__main__':
    main()