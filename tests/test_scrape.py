from gtrending.scrape import scrape_repos, scrape_developers


def test_scrape_repos(repo_assertion):
    repos = scrape_repos()
    repo_assertion(repos)


def test_scrape_developers(developer_assertion):
    repos = scrape_developers()
    developer_assertion(repos)
