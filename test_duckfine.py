import unittest

from duckfine import DuckFine


class DuckFineTest(unittest.TestCase):
    def setUp(self):
        self.duck_fine = DuckFine("member-1")

    def test_stores_member_id(self):
        self.assertEqual(self.duck_fine.member_id, "member-1")

    def test_initial_total_owed_is_zero(self):
        self.assertEqual(self.duck_fine.total_owed, 0.0)

    def test_no_late_days_have_no_fee(self):
        self.assertEqual(self.duck_fine.charge(0), 0.0)

    def test_first_two_late_days_are_forgiven(self):
        self.assertEqual(self.duck_fine.charge(2), 0.0)

    def test_chargeable_days_cost_fifty_cents_each(self):
        self.assertEqual(self.duck_fine.charge(4), 1.0)

    def test_deluxe_charge_is_doubled(self):
        self.assertEqual(self.duck_fine.charge(4, deluxe=True), 2.0)

    def test_single_charge_does_not_exceed_maximum_fee(self):
        self.assertEqual(self.duck_fine.charge(20), 5.0)

    def test_charges_are_added_to_total_owed(self):
        self.duck_fine.charge(4)
        self.duck_fine.charge(3)

        self.assertEqual(self.duck_fine.total_owed, 1.5)

    def test_negative_days_late_raise_value_error(self):
        with self.assertRaises(ValueError):
            self.duck_fine.charge(-1)


if __name__ == "__main__":
    unittest.main()