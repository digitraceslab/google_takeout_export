import os
import time
import logging

from django.conf import settings
import django


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_takeout_file(filepath):
    ''' Process a Google Takeout file. '''
    logger.info(f'Processing file at {filepath}')
    time.sleep(10)
    logger.info(f'File processed at {filepath}')
    output_filepath = filepath.replace('.zip', '.csv')
    with open(output_filepath, "w") as f:
        f.write('This is the processed file.')


def check_and_process_takeout_files():
    ''' Check for new Google Takeout files and process them. '''
    media_root = settings.MEDIA_ROOT
    for filename in os.listdir(media_root):
        if filename.endswith('.zip'):
            if filename.replace('.zip', '.csv') in os.listdir(media_root):
                continue
            filepath = os.path.join(media_root, filename)
            process_takeout_file(filepath)
            time.sleep(10)

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'google_takeout_export.settings')
    django.setup()
    while True:
        check_and_process_takeout_files()
        time.sleep(5)
