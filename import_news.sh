#!/bin/bash

repository="https://github.com/jakekasan/news-source.git"

if [ -d "./news_source"]; then rm -Rf "./news_source"; fi
if [ -d "./news-source"]; then rm -Rf "./news-source"; fi

git clone "$repository"

mv ./news-source ./news_source