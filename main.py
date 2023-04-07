import Parse
if __name__ == '__main__':
    carsname,price=Parse.parser()
    Parse.writinginfile(carsname,price)