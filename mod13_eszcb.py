import unittest
import re
from datetime import datetime


def validate_symbol(symbol):
    return bool(re.fullmatch(r"[A-Z]{1,7}", symbol))


def validate_chart_type(chart_type):
    return bool(re.fullmatch(r"[12]", chart_type))


def validate_time_series(time_series):
    return bool(re.fullmatch(r"[1-4]", time_series))


def validate_date(date):
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        return False
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False





class TestSymbol(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(validate_symbol("A"))
        self.assertTrue(validate_symbol("AAPL"))
        self.assertTrue(validate_symbol("GOOGLEX"))

    def test_lowercase(self):
        self.assertFalse(validate_symbol("aapl"))
        self.assertFalse(validate_symbol("Aapl"))

    def test_too_long(self):
        self.assertFalse(validate_symbol("ABCDEFGH"))

    def test_empty(self):
        self.assertFalse(validate_symbol(""))

    def test_non_alpha(self):
        self.assertFalse(validate_symbol("AAP1"))
        self.assertFalse(validate_symbol("BRK.B"))


class TestChartType(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(validate_chart_type("1"))
        self.assertTrue(validate_chart_type("2"))

    def test_out_of_range(self):
        self.assertFalse(validate_chart_type("0"))
        self.assertFalse(validate_chart_type("3"))

    def test_too_long(self):
        self.assertFalse(validate_chart_type("12"))

    def test_non_numeric(self):
        self.assertFalse(validate_chart_type("a"))
        self.assertFalse(validate_chart_type(""))


class TestTimeSeries(unittest.TestCase):
    def test_valid(self):
        for value in ["1", "2", "3", "4"]:
            self.assertTrue(validate_time_series(value))

    def test_out_of_range(self):
        self.assertFalse(validate_time_series("0"))
        self.assertFalse(validate_time_series("5"))

    def test_too_long(self):
        self.assertFalse(validate_time_series("11"))

    def test_non_numeric(self):
        self.assertFalse(validate_time_series("x"))
        self.assertFalse(validate_time_series(""))


class TestStartDate(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(validate_date("2024-01-15"))

    def test_wrong_format(self):
        self.assertFalse(validate_date("01-15-2024"))
        self.assertFalse(validate_date("2024/01/15"))
        self.assertFalse(validate_date("2024-1-15"))

    def test_invalid_date(self):
        self.assertFalse(validate_date("2024-13-01"))
        self.assertFalse(validate_date("2024-02-30"))

    def test_empty(self):
        self.assertFalse(validate_date(""))


class TestEndDate(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(validate_date("2024-12-31"))

    def test_wrong_format(self):
        self.assertFalse(validate_date("12/31/2024"))
        self.assertFalse(validate_date("20241231"))

    def test_invalid_date(self):
        self.assertFalse(validate_date("2024-00-10"))
        self.assertFalse(validate_date("2023-02-29"))

    def test_non_date(self):
        self.assertFalse(validate_date("abcd-ef-gh"))


if __name__ == "__main__":
    unittest.main()
