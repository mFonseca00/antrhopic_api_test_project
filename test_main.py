import unittest
from unittest.mock import patch
from io import StringIO
from main import greeting


class TestGreeting(unittest.TestCase):

    @patch("sys.stdout", new_callable=StringIO)
    def test_greeting_prints_hello(self, mock_stdout):
        """Verifica se 'Hello' é impresso."""
        greeting()
        output = mock_stdout.getvalue()
        self.assertIn("Hello", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_greeting_prints_goodbye(self, mock_stdout):
        """Verifica se 'Goodbye' é impresso."""
        greeting()
        output = mock_stdout.getvalue()
        self.assertIn("Goodbye", output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_greeting_prints_hello_before_goodbye(self, mock_stdout):
        """Verifica se 'Hello' aparece antes de 'Goodbye'."""
        greeting()
        output = mock_stdout.getvalue()
        hello_position = output.index("Hello")
        goodbye_position = output.index("Goodbye")
        self.assertLess(hello_position, goodbye_position)

    @patch("sys.stdout", new_callable=StringIO)
    def test_greeting_output_lines(self, mock_stdout):
        """Verifica se a saída contém exatamente 2 linhas não vazias."""
        greeting()
        lines = [line for line in mock_stdout.getvalue().splitlines() if line]
        self.assertEqual(len(lines), 2)


if __name__ == "__main__":
    unittest.main()
