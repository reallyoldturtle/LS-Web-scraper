# LS-Web-scraper
 Aweb scraper with an easily extendable data model for web pages.

Usage:
python thumbs.py distorted_json_filename

distorted JSON file details:

    “xpath_test_query”: <xpath for an element that uniquely identifies the page (like a title)>,

    “xpath_test_result”: <expected result of the previous xpath query: if the xpath query equals to this, this is indeed the current page>,

    “xpath_button_to_click”: <xpath query for the href link that has to be followed>,

    “next_page_expected”: <string name of the next expected page after following the link>


