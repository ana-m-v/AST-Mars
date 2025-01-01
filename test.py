import unittest
from main import overlap_in_minutes

class TestMarsOverlap(unittest.TestCase):

    # 1. **Basic Overlap (Positive) pass **
    def test_simple_overlap_same_day(self):
        # This test case checks a simple overlap scenario where both intervals are within the same Mars day.
        self.assertEqual(overlap_in_minutes([13, 91], [23, 5], [22, 5], [24, 45]), 100)

    # 2. **No Overlap (Negative) pass**
    def test_no_overlap(self):
        # This case checks when the two intervals do not overlap at all.
        self.assertEqual(overlap_in_minutes([1, 0], [5, 0], [6, 0], [10, 0]), 0)

    # 3. **Twilight Rule (Touching at One Point) pass**
    def test_twilight_rule_single_point(self):
        # This tests the scenario where the intervals only touch at one point (1 minute of overlap).
        # It is important to check if the program correctly applies the Twilight Rule and returns 1 minute.
        self.assertEqual(overlap_in_minutes([12, 32], [17, 6], [17, 6], [19, 78]), 1)

    # 4. **Deimos Starts Late, Overlap Crosses Midnight pass**
    def test_overlap_across_midnight(self):
        # This test checks if the algorithm handles intervals crossing midnight.
        # Failing to handle this can lead to significant errors in calculating overlap across the Mars day boundary.
        self.assertEqual(overlap_in_minutes([24, 53], [7, 12], [5, 12], [8, 45]), 0)

    # 5. **Full Overlap (Positive) pass**
    def test_full_containment(self):
        # This test checks the case where one interval is completely contained within the other.
        # It's important to ensure the program returns the full duration of overlap.
        self.assertEqual(overlap_in_minutes([10, 30], [20, 30], [12, 0], [18, 0]), 600)

    # 6. **No Overlap, but Touching at One Point (Negative, Twilight Rule) pass*
    def test_adjacent_intervals_without_overlap(self):
        # This case tests intervals that are adjacent but do not overlap.
        # It's important to handle adjacent intervals properly, especially when they only touch at one point.
        self.assertEqual(overlap_in_minutes([10, 0], [15, 0], [15, 0], [20, 0]), 1)

    # 7. **Boundary Case: Interval Starts at Midnight (Positive) pass**
    def test_interval_starts_at_midnight(self):
        # This case checks if the program handles intervals starting exactly at midnight.
        # Since many experiments may start at midnight, it is critical to correctly calculate overlaps for this boundary case.
        self.assertEqual(overlap_in_minutes([0, 0], [5, 0], [0, 0], [6, 0]), 500)  # Expecting 360 minutes of overlap

    # 8. **Boundary Case: Interval Ends at Midnight (Negative)**
    def test_interval_ends_at_midnight(self):
        # This case checks if the program correctly handles intervals that end exactly at midnight.
        # Proper handling of this boundary is critical to avoid miscalculating overlaps just before midnight.
        self.assertEqual(overlap_in_minutes([23, 30], [0, 0], [0, 0], [1, 0]), 1)  # Expecting 30 minutes of overlap

    # 9. **Phobos Starts After Deimos (Positive)**
    def test_phobos_starts_after_deimos(self):
        # This case checks if the program handles the situation where Phobos starts after Deimos.
        # The program should still detect the overlap correctly.
        self.assertEqual(overlap_in_minutes([10, 0], [14, 30], [12, 0], [16, 0]), 230)

    # 10. **Phobos Fully Inside Deimos' Interval (Positive)**
    def test_phobos_fully_inside_deimos(self):
        # This case checks if Phobos' interval is fully contained within Deimos' interval.
        # It's important to ensure full overlap is detected.
        self.assertEqual(overlap_in_minutes([10, 30], [20, 30], [12, 0], [18, 0]), 600)

    # 11. **No Overlap, Phobos Starts Early and Ends Late (Negative)**
    def test_no_overlap_phobos_early_late(self):
        # This case ensures that no overlap is detected when Phobos starts early and ends late.
        self.assertEqual(overlap_in_minutes([20, 0], [2, 0], [6, 0], [10, 0]), 0)

    # 12. **Deimos Starts Early in the Day (Positive)**
    def test_deimos_starts_early(self):
        # This case checks if the program correctly handles Deimos starting early in the day.
        self.assertEqual(overlap_in_minutes([24, 30], [5, 0], [1, 0], [6, 30]), 0)

    # 13. **Deimos and Phobos Intervals Are Completely Different (Negative)**
    def test_deimos_phobos_completely_different(self):
        # This case checks if the program correctly handles completely non-overlapping intervals.
        self.assertEqual(overlap_in_minutes([12, 0], [14, 0], [16, 0], [18, 0]), 0)

    # 14. **Intervals Overlap for Exactly One Minute (Twilight Rule)**
    def test_intervals_overlap_one_minute(self):
        # This case checks if the program correctly handles a 1-minute overlap between intervals.
        # It is crucial to check if the Twilight Rule is applied and 1 minute of overlap is reported.
        self.assertEqual(overlap_in_minutes([12, 32], [17, 6], [17, 6], [19, 78]), 1)

    # 15. **Phobos' Interval Spans Midnight (Critical Negative)**
    def test_phobos_spans_midnight(self):
        # This case checks if the program handles the case where Phobos' interval spans midnight.
        # Failure to handle this case correctly could severely impact the program's accuracy in determining moon visibility.
        self.assertEqual(overlap_in_minutes([23, 0], [1, 0], [0, 0], [2, 0]), 0)

if __name__ == '__main__':
    unittest.main()
