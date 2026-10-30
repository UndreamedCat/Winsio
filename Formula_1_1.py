class Formula_1_1():
    def __init__(self, k, b):
        """Define A Formula like kx + b = 0"""
        self.k = k
        self.b = b

    def __str__(self):
        return f"{self.k}x + {self.b} = 0"

    def solve(self):
        """Solve the equation"""
        # kx + b = 0 -> kx = -b -> x = -b / k
        return -self.b / self.k