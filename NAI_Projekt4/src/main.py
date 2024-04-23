import pandas as pd
import k_means

# Global CONST
TEST_DATA_PATH = "../data-files/iris_test.txt"
TRAINING_DATA_PATH = "../data-files/iris_training.txt"

# Global VAR
tr_data: pd.DataFrame = None
test_data: pd.DataFrame = None


def load_data() -> None:
    """Load training and testing data"""
    global tr_data, test_data

    # loading data from files
    tr_data = pd.read_table(TRAINING_DATA_PATH, header=None, sep=r'\s+',
                            decimal=",")
    test_data = pd.read_table(TEST_DATA_PATH, header=None, sep=r'\s+',
                              decimal=",")

    # dropping last column
    # tr_data = tr_data.drop(tr_data.columns[[-1]], axis=1)
    # test_data = test_data.drop(test_data.columns[[-1]], axis=1)


def main() -> None:
    load_data()
    k_val = int(input("Provide k value for algorithm: "))
    algorithm = k_means.KMeans(data=tr_data, k=k_val)
    algorithm.run()


if __name__ == '__main__':
    main()
