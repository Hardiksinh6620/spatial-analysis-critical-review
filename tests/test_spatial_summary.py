"""Check known geometry and invariants of the new educational example."""
import math
import unittest
from examples.spatial_summary import summarize


class SpatialSummaryTests(unittest.TestCase):
    def test_square_has_known_center_and_radius(self):
        result = summarize([(0,0),(2,0),(0,2),(2,2)])
        self.assertEqual(result["mean_center"], [1.0,1.0])
        self.assertAlmostEqual(result["standard_distance"], math.sqrt(2))

    def test_translation_changes_center_not_spread(self):
        points = [(0,0),(2,0),(0,2),(2,2)]
        translated = summarize([(x+100,y-7) for x,y in points])
        self.assertEqual(translated["mean_center"], [101.0,-6.0])
        self.assertAlmostEqual(translated["standard_distance"], math.sqrt(2))

    def test_scaling_scales_spread(self):
        self.assertAlmostEqual(summarize([(0,0),(6,0)])['standard_distance'],3)

    def test_single_point_has_zero_spread(self):
        self.assertEqual(summarize([(5,7)])['standard_distance'],0)

    def test_rms_is_not_mean_distance(self):
        result=summarize([(0,0),(0,0),(3,0)])
        self.assertAlmostEqual(result['standard_distance'],math.sqrt(2))
        self.assertNotAlmostEqual(result['standard_distance'],4/3)

    def test_invalid_inputs(self):
        for points in [[],[(1,2,3)],[(float('nan'),0)],[(float('inf'),1)]]:
            with self.subTest(points=points), self.assertRaises(ValueError):
                summarize(points)


if __name__ == '__main__':
    unittest.main()
