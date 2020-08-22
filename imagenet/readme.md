# Imagenet classification

Inorder to run the tensorflow Serving server:

`tensorflow_model_server --model_base_path=Z:\codeplay\flask-apps\imagenet\my_image_classifier --rest_api_port=9000 --model_name=ImageClassifier`

This command doesn't work on windows
And Ill have to use docker for it to run
So stuck with tthis reference
Can be easily be done in a linux machine

Reference :
https://github.com/himanshurawlani/keras-and-tensorflow-serving/blob/master/

this needs to be run inside docker:
`apt-get install tensorflow-model-server`

Reference:
https://www.tensorflow.org/tfx/tutorials/serving/rest_simple