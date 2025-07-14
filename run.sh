#!/bin/bash

PARAM1="$1"
PARAM2="$2"


if [ "$#" -ne 2 ]; then
    echo "Use ./run_all.sh <param1: dataset>  <param2: is_test>"
    exit 1
fi

# run
papermill data_preprocessing.ipynb output/data_preprocessing.ipynb -p dataset "$PARAM1" -p test "$PARAM2"
papermill concepts_generation.ipynb output/concepts_generation.ipynb -p test "$PARAM2"
papermill weak_label.ipynb output/weak_label.ipynb -p test "$PARAM2"
papermill train_scorer.ipynb output/train_scorer.ipynb -p test "$PARAM2"
papermill hcen.ipynb output/hcen.ipynb -p test "$PARAM2"
