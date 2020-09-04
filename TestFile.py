import pyspark
from pyspark.sql import SparkSession

if __name__ == "__main__":
    print("Test the file")
    a = 2+1
    print(a)

    k = 10
    for i in range(k):
        if i%2 == 0:
            print(i)
        if i+2 == 0:
            print(i)
        if i/2 == 0:
            print(i)
        if i*2 == 0:
            print(i)
        if i//2 == 0:
            print(i)