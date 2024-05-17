# dota2_ad_data
Tools for scraping and pre-processing DOTA2 matches in the ability draft mode.

Overview of files:
* scraper/*: scripts for querying, filtering (only AD games are store, accounts for about 5% of all games), and storing match files in .json format.
* constants/*: contains json files for hero/ability IDs and info.
* raw_data_processor: a parser that parses key information (heros and ability drafted, game duration, the winning team) of match files and stores them into a single .csv file.
* data_processor: reindexing hero and ability IDs.