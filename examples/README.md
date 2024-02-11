> Reconstructed archive: this material was assembled on 2026-09-29. February 2024 author dates are assigned archival dates, not original work timestamps.

# Synthetic spatial-statistics example

Run `python examples/spatial_summary.py` from the repository root. Only Python's standard library is required. The example uses four invented Cartesian points, not the original report's GIS data.

Expected output: count 4, mean center `[1.0, 1.0]`, and standard distance approximately `1.4142135623730951` in the input coordinate units.

The implementation is deliberately small: unweighted, two-dimensional, finite coordinates at ordinary numeric scales. It is not a substitute for GIS reprojection, geodesic calculations, polygon centroids, or directional statistics. Very large magnitudes may exceed floating-point range. The script was written during this portfolio edition, not in February 2024.
