from src.etl.pipeline import etl
from config import *

if __name__ == '__main__':
    etl(dataset_path=DATASET_PATH,
        target_path=TARGET_PATH,
        columns=COLUMNS_TO_SELECT,
        data_types=DATA_TYPES,
        missing_values=MISSING_VALUES
        )
