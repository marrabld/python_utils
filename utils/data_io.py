import csv
import numpy as np


def csv_to_dict(input_file):
    reader = csv.DictReader(open(input_file, 'r'))
    data = dict.fromkeys(reader.fieldnames)

    for i_iter, row in enumerate(reader):
        for key in data.keys():
            if i_iter <= 0:
                data[key] = [row[key]]
            else:
                data[key].append(row[key])
    return data


def fill_na_nn(df, val=np.nan):
    """
    replace nans by using nearest neighbour

    :param df: dataframe
    :param val:
    :return:
    """

    df.where(df.replace(to_replace=val, value=np.nan),
             other=(df.fillna(method='ffill') + df.fillna(method='bfill')) / 2)

    return df
