from statfunc.msis_scraper import get_msis_data


def test_get_msis_data():
    municipalities = {3416}
    msis = get_msis_data(municipalities)
    assert msis['Unnamed: 0'].str.contains('Eidskog').any()


