from Hanoi import Hanoi

def move (f, t):
    """
    move from position f to position t
    @param f, from
    @param t, target
    """
    print (f"move from {f} to {t}")

def solve (n, f, h, t):
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
    elif n == 1:
        move (f, t)
    else:
        solve (n-1, f, t, h)
        move (f, t)
        solve (n-1, h, f, t)

def main ():
    """
    function based
    disks = 3
    solve (disks, "A", "B", "C")
    """
    
    # class based
    h = Hanoi(3)
    h.solve("a", "b", "c")
    

if __name__ == "__main__" :
    main()