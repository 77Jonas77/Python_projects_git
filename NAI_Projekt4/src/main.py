import pandas as pd
import k_means

TEST_DATA_PATH = "../data-files/iris_test.txt"
TRAINING_DATA_PATH = "../data-files/iris_training.txt"

tr_data = pd.DataFrame
test_data = pd.DataFrame


def load_data():
    """Load training and testing data"""
    global tr_data, test_data

    # loading data from files
    # dropping last column

    tr_data = pd.read_table(TRAINING_DATA_PATH, header=None, sep=r'\s+',
                            decimal=",")
    # tr_data = tr_data.drop(tr_data.columns[[-1]], axis=1)

    test_data = pd.read_table(TEST_DATA_PATH, header=None, sep=r'\s+',
                              decimal=",")
    # test_data = test_data.drop(test_data.columns[[-1]], axis=1)


if __name__ == '__main__':
    load_data()
    k_val = int(input("Provide k value for algorithm: "))
    k_means.KMeans(data=tr_data, k=k_val)
    # todo: finish later ...
