#! /usr/bin/env python3

# Copyright 2022 Alexandr Cherkaev, Anton Karmanov <a.karmanov@inventati.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import argparse
import logging
import os

from pali_bot.bot import Bot
from pali_bot.sutta_provider import SuttaProvider

import yaml

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Pali bot')
    parser.add_argument(
        '--config',
        required=False,
        default='config.yaml',
        type=argparse.FileType('r'),
        help='point to overriding config file', )
    return parser.parse_args()


def main() -> None:
    args = get_args()
    config = yaml.safe_load(args.config)

    logging.basicConfig(level=config.get('log_level'))
    sutta_provider = SuttaProvider(data_dir='./data/')
    bot = Bot(
        sutta_provider=sutta_provider,
        token=config.get('token') or os.environ.get('PALI_BOT_TOKEN'),
        about_text=config.get('about_message', '<i>NOT SPECIFIED</i>'))
    bot.run()


if __name__ == '__main__':
    main()
