import task2

class TestQuadratic:
    def test_0_0_0(self):
        assert task2.Quadratic(0, 0, 0) == []
    def test_1_6_1(self):
        assert task2.Quadratic(1, 6, 1) == [-0.1715728752538097, -5.82842712474619]
    def test_5_ьштгы5_5(self):
        assert task2.Quadratic(5, 5, 5) == [-75.0, -5.82842712474619]
    def test_1_minus2_1(self):
        assert task2.Quadratic(1, -2, 1) == [1.0]
    def test_5_6_2(self):
        assert task2.Quadratic(5, 6, 2) == [(-0.6+0.2j), (-0.6-0.2j)]
