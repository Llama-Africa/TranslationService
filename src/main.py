import sys
import os

from src.api.aws_translate_api import AWSTranslateAPI

# Add the parent directory of `src` to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.insert(0, parent_dir)

from tqdm import tqdm

from src.api.open_source.opus_translate_api import OpusTranslateAPI
from src.api.open_source.meta_translate_api import MetaTranslateAPI
from src.api.i_translate_api import ITranslateAPI
from src.data.dataset_loader import DatasetLoader
import pandas as pd
from typing import Dict
from src.routing_condition.openai_router import OpenAIRouter
from src.routing_condition.ollama_router import OllamaRouter


def run():
    dataset_name = "yahma/alpaca-cleaned"
    dataset = DatasetLoader(dataset_name)
    FROM_LANGUAGE = 'en'
    LANGUAGES_TO_TRANSLATE_TO = ['af']
    api: ITranslateAPI = AWSTranslateAPI(FROM_LANGUAGE, LANGUAGES_TO_TRANSLATE_TO)
    column_names = dataset.df.columns
    router = OllamaRouter()

    for _, row in tqdm(dataset.df.iterrows(), colour='GREEN', total=dataset.df.shape[0]):
        print(router.is_code(row))
        # result: Dict[str, pd.DataFrame] = api.translate(row=row, column_names=column_names)
        # for to_language in LANGUAGES_TO_TRANSLATE_TO:
        #     dataset.write_to_csv(result[to_language], to_language)

run()
