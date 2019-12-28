


class Hanoi():
    
    def __init__(self, discs = 3):
        """
        initiates a towers of hanoi game with a given number of disks
        @param discs, number of discs for the game
        """
        self.discs = discs
        self.steps = 0  # counter
    
    def solve (self, f = "a", h = "b", t = "c"):
        self._solve(self.discs, f, h, t)
        
    def _solve (self, n, f, h, t):
        """
        solve towers of hanoi for n disks
        @param n, number of disks
        @param f, from
        @param h, helper
        @param t, target
        """        
        if n == 0:
            # we are done
            pass

        else:
            self._solve (n-1, f, t, h)
            self.move (f, t)
            self._solve (n-1, h, f, t)
        
    def move (self, a, b):
        """
        move from position a to position b
        @param a, from
        @param b, target
        """
        self.steps += 1
        print (f"{self.steps}. move from {a} to {b}")
        