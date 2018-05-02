#!/bin/bash
# export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim

python object_detection/dataset_tools/create_quiz_tf_record.py \
    --label_map_path=data/quiz-w8-data/labels_items.txt \
    --data_dir=data/quiz-w8-data/ \
    --output_dir=data