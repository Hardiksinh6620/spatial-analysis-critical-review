> Reconstructed archive: this material was assembled on 2026-09-29. February 2024 author dates are assigned archival dates, not original work timestamps.

# Standard distance and a report clarification

For unweighted 2D points, standard distance is `sqrt(mean((x-mean(x))**2 + (y-mean(y))**2))`.

The description on page 5 of the original report needs clarification: this is a root-mean-square distance, not simply the average distance. The ordinary 2D Standard Distance output is circular, while directional dispersion is a separate concept. The archived report is retained unchanged; this correction belongs to the new portfolio notes.

A single dispersion value does not describe every feature of a distribution. Different patterns can share the same center and standard distance. Review the locations themselves before using the summary to support a decision.

Reference: [Esri Standard Distance](https://doc.esri.com/en/arcgis-pro/latest/tool-reference/spatial-statistics/h-how-standard-distance-spatial-statistic-works.html).
