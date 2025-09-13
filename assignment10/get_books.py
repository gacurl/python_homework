# Task 1: Review robots.txt to Ensure Policy Compliance
    # Durham County Library robots.txt:
    # - User-agent section used: *
    # - Disallow: Disallow: /staff/
    # - Crawl-delay: n/a

    # Bibliocommons robots.txt:
    # - User-agent section used: *
    # - Disallow: /v2/availability/ but no issues for /v2/search/
    # - Crawl-delay: 120
    # - OK to fetch a single results page with 2s delay? Yes

# Task 2: Understanding HTML and the DOM for the Durham Library Site
# # ----- selectors from DOM -----
# CSS_RESULT_LI = "li.row.cp-search-result-item"
# CSS_TITLE = "h2.cp-title .title-content"
# CSS_AUTHOR_LINKS = ".cp-by-author-block a"
# CSS_FMT_YEAR_WRAPPER = ".cp-format-info .display-info"
# CSS_FMT_YEAR_SPAN = ".display-info-primary"
