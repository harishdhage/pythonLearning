import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def addNumbers(a, b):
    logging.debug(f"Calculating sum of {a} and {b}")
    sum = a + b
    logging.info(f"Numbers added {a} + {b} and result = {sum}")
    return sum

if __name__ == "__main__":
    logging.info('Started program')
    result = addNumbers(1,2)
    logging.info('Program ended')
