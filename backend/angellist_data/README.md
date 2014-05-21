AngelList Dataset for PredictionIO Sample Project
==============================================

What is this?
---------------------

This dataset contains data collected from the public AngelList API on May, 2014.

The demo illustrates the use of PredictionIO's Item Similarity engine to generate predictions for "If you follow this startup, you may also want to follow these X, Y and Z startups".

Using the AngelList API we retrieved all startups belonging to the following accelerators (or incubators):

* https://angel.co/500startups
* https://angel.co/y-combinator
* https://angel.co/techstars
* https://angel.co/startx

With duplicates removed we then retrieved all users following these startups. This dataset then provided the users, items (i.e., startups) and interactions (i.e., follows) to build an Item Similarity model in PredictionIO.

Files
---------------------

All files are comma-delimited .csv files.

* follows.csv - list of ids for startups and users who follow the startup
* startup_id_name_url_incubator.csv - list of startups with ids, names, AngelList URL and incubators
* startups.csv - list of unique startup ids
* users.csv - list of unique user ids
* markets.csv - list of market tags for each startup

License
---------------------

The data is made available for non-commercial use. For more information see AngelList API terms of service - https://angel.co/api/terms

References
---------------------

When using this dataset you must reference the AngelList API webpage - https://angel.co/api


Contact
---------------------

This data was collected by Thomas Stone e-mail thomas [at] prediction.io
