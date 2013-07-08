from geopandas import GeoDataFrame

def test_from_file_():
    # Data from http://www.nyc.gov/html/dcp/download/bytes/nybb_13a.zip
    # saved as geopandas/examples/nybb_13a.zip.
    df = GeoDataFrame.from_file(
        '/nybb_13a/nybb.shp', vfs='zip://examples/nybb_13a.zip')
    assert 'geometry' in df
    assert len(df) == 5