# Shared control review

A local research-data analysis application using synthetic records. It keeps ingestion, descriptive analysis, and report serialization separate so each result can be reproduced offline.

## Requirements

Python 3.11 or newer; the application uses only the standard library.

## Run and test

From this directory, run `python -m unittest discover -s tests -v`. Generate a report with `python -m study_app --data data/sample.json --output report.json`. The input records are synthetic and may be edited locally.
