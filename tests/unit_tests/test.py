from app import fetch_by_id
from unittest import TestCase, main
from unittest.mock import patch


class TestApp(TestCase):

    @patch("app.sqlite3")
    def test_get_employee(self, mock_class):
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


if __name__ == '__main__':
    main()