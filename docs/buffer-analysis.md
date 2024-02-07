> Reconstructed archive: this material was assembled on 2026-09-29. February 2024 author dates are assigned archival dates, not original work timestamps.

# Buffer analysis: a reproduction checklist

The original report discusses buffers on PDF pages 3-4. Its example maps cannot be regenerated until the source layers and settings are recovered.

Record the input geometry, coordinate reference system, buffer distance and units, distance method, dissolve choice, and the output location. Check that the chosen distance answers a real study question rather than merely producing a convenient-looking map.

Current Esri documentation distinguishes planar and geodesic distance handling. The appropriate setting depends on the coordinate system and geographic extent. Dissolving overlapping buffers changes whether outputs describe individual features or a combined area.

For a later reproduction, compare feature counts, inspect invalid or empty geometries, and check a small sample of distances. A straight-line buffer is not automatically a walking or driving catchment. Routing needs a suitable network and travel assumptions.

The archived menu instructions have not been verified against every ArcGIS release. Use the documentation for the installed version.

Reference checked during portfolio preparation: [Esri Buffer](https://doc.esri.com/en/arcgis-pro/latest/tool-reference/analysis/buffer.html).
