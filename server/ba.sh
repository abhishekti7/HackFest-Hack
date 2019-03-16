sudo docker run -v $PWD:/opt/app \
-e PYTHONPATH=$PYTHONPATH:/opt/app \
-it colemurray/medium-show-and-tell-caption-generator  \
python3 /opt/app/medium_show_and_tell_caption_generator/inference.py \
--model_path /opt/app/etc/show-and-tell.pb \
--vocab_file /opt/app/etc/word_counts.txt \
--input_files /opt/app/imgs/*
