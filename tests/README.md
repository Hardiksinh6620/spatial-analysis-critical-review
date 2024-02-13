> Reconstructed archive: this material was assembled on 2026-09-29. February 2024 author dates are assigned archival dates, not original work timestamps.

# Validation

Run `python -m unittest discover -s tests -v` from the repository root. The checks use a square with known geometry, translation and scaling behaviour, a degenerate point, an asymmetric case distinguishing RMS from ordinary mean distance, and invalid inputs.

These checks validate the educational implementation within its documented scope. They do not validate the original report's unseen GIS inputs or establish the correctness of every claim in the archived PDF.
