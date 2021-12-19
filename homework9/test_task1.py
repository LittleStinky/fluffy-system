import task1

class TestIsPassword:
    def test_paSSword(self):
        assert not task1.IsPassword('paSSword')
    def test_000000(self):
        assert not task1.IsPassword('000000')
    def test_abcdfu(self):
        assert not task1.IsPassword('abcdfu')  
    def test_abc(self):
        assert not task1.IsPassword('abc')
    def test_12345t(self):
        assert task1.IsPassword('12345t')
