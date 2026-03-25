import os
import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class DataLakeManager:
    def __init__(self, base_path='data_lake'):
        self.base_path = base_path
        self.setup_structure()

    def setup_structure(self):
        os.makedirs(os.path.join(self.base_path, 'raw'), exist_ok=True)
        os.makedirs(os.path.join(self.base_path, 'processed'), exist_ok=True)
        os.makedirs(os.path.join(self.base_path, 'metadata'), exist_ok=True)
        os.makedirs(os.path.join(self.base_path, 'logs'), exist_ok=True)
        logging.info('DataLake structure set up.')

    def store_raw_data(self, data, source_name, file_format='json'):
        file_path = os.path.join(self.base_path, 'raw', f'{source_name}.{file_format}')
        with open(file_path, 'w') as f:
            json.dump(data, f)
        logging.info(f'Raw data stored in {file_path}')

    def store_processed_data(self, data, process_name, file_format='parquet'):
        file_path = os.path.join(self.base_path, 'processed', f'{process_name}.{file_format}')
        # This is a mock implementation, replace with actual parquet writing logic
        with open(file_path, 'w') as f:
            f.write('Parquet data placeholder')
        logging.info(f'Processed data stored in {file_path}')

    def list_raw_files(self):
        raw_files = os.listdir(os.path.join(self.base_path, 'raw'))
        logging.info(f'Listing raw files: {raw_files}')
        return raw_files

    def list_processed_files(self):
        processed_files = os.listdir(os.path.join(self.base_path, 'processed'))
        logging.info(f'Listing processed files: {processed_files}')
        return processed_files

    def get_file_metadata(self, filename):
        file_path = os.path.join(self.base_path, 'raw', filename)
        if os.path.isfile(file_path):
            metadata = {
                'filename': filename,
                'size': os.path.getsize(file_path),
                'last_modified': datetime.utcfromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
            }
            logging.info(f'Metadata for {filename}: {metadata}')
            return metadata
        else:
            logging.warning(f'File {filename} does not exist.')
            return None