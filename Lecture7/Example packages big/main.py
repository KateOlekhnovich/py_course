from packages.bank import starts as bs, logic as bl, exports as be
from packages.crm import starts as cs, logic as cl, exports as ce
def main():
    bs.start()
    bl.show()
    bl.add(345)
    bl.change(567)
    bl.delete(123)
    li=[1,2,3,4,5]
    be.export(li)

    print("part2")
    cs.start()
    cl.show()
    cl.add(345)
    cl.change(567)
    cl.delete(123)
    li=[1,2,3,4,5]
    ce.export(li)



if __name__ == "__main__":
    print ("main.py was started")
    main()
