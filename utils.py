def plus(num1, num2):
        try:
            return  float(num1) + float(num2)
        except OverflowError:
            raise
