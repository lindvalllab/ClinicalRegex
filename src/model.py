import pandas as pd
import numpy as np
import os
import sys


# Maintains all of the data and handles the data manipulation for this
# application
class DataModel:
    def __init__(self):
        self.input_fname = None
        self.output_fname = None
        self.inpput_df = None
        self.output_df = None
        self.display_df = None
        self.save_df = None
        self.current_row_index = None
        self.num_notes = None
        self.annotation_key = 'ANNOTATION'

    def write_to_annotation(self):
        if self.save_df is None or self.current_row_index is None:
            return
        pathname = os.path.dirname(sys.argv[0])
        self.save_df.to_csv(
            os.path.join(
                pathname,
                self.output_fname),
            index=False)

    def get_annotation(self):
        if self.annotation_key in self.output_df:
            current_row_index = self.display_df.index[self.current_row_index]
            val = self.output_df.at[current_row_index, self.annotation_key]
            if val is not None and not pd.isnull(val):
                try:
                    return int(float(val))
                except BaseException:
                    return val
        return ''
