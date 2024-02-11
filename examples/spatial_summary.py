"""New educational example; reconstructed archive dates are not creation dates.

Unweighted 2D Cartesian points only. No GIS projection or geodesic support.
"""
import json
import math


def summarize(points):
    values = [tuple(point) for point in points]
    if not values:
        raise ValueError("At least one point is required")
    if any(len(point) != 2 for point in values):
        raise ValueError("Each point must have exactly two coordinates")
    values = [(float(x), float(y)) for x, y in values]
    if any(not math.isfinite(v) for point in values for v in point):
        raise ValueError("Coordinates must be finite")
    count = len(values)
    cx = math.fsum(x / count for x, _ in values)
    cy = math.fsum(y / count for _, y in values)
    radius = math.sqrt(math.fsum(((x-cx)**2 + (y-cy)**2) / count for x,y in values))
    return {"count": count, "mean_center": [cx, cy], "standard_distance": radius}


if __name__ == "__main__":
    print(json.dumps(summarize([(0,0), (2,0), (0,2), (2,2)]), indent=2))
