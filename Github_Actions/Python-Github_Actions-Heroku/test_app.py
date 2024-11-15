from app import index

def test_index():
    assert "Python Webapp Deployment on Heroku Using Github Actions" in index()