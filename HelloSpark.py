from pyspark.sql import *

from lib.logger import Log4J

if __name__ == "__main__":

    spark = SparkSession.builder.appName("Hello Spark").master("local[5]").getOrCreate()

    logger = Log4J(spark)
    logger.info("Just Started")
    logger.info("Finished the project")

    print("Welcome to the world of Big data")
    print("You have to do it Venkat")

    # spark.stop()