import pickle
from classes import Hospital


class Unpickle:
    # read the pickle file
    pickle_file = open('details', 'rb')
    # unpickle the data_frame
    details = pickle.load(pickle_file)
    # close pickle file
    pickle_file.close()

    # print the data_frame
    print(type(details))
    details.__str__()
