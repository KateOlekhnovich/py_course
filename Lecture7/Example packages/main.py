from package_bank import starts as bs, logic as bl, exports as be

def main():
    bs.start()
    bl.show()
    bl.add(345)
    bl.change(567)
    bl.delete(123)
    li=[1,2,3,4,5]
    be.export(li)


if __name__ == "__main__":
    print ("main.py was started")
    main()
