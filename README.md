In order to run the code on gcloud, run the gcloud commmand in this directory. 

```sh
PROJECT_ID=$(gcloud config list project --format "value(core.project)")
BUCKET_NAME=${PROJECT_ID}-mlengine
REGION=us-east1
PACKAGE_PATH=fast
MODULE_NAME=fast.style
CHECKPOINT_DIR=gs://$BUCKET_NAME/fast/checkpoint
STYLE=gs://$BUCKET_NAME/examples/style/udnie.jpg
TRAIN_PATH=gs://$BUCKET_NAME/data/train2014
VGG_PATH=gs://$BUCKET_NAME/data/imagenet-vgg-verydeep-19.mat
JOB_NAME=style_transfer
OUTPUT_PATH=gs://$BUCKET_NAME/$JOB_NAME
```

```sh
gcloud ml-engine jobs submit training $JOB_NAME \
--job-dir $CHECKPOINT_DIR \
--runtime-version 1.2 \
--module-name $MODULE_NAME \
--package-path $PACKAGE_PATH/ \
--region $REGION \
--scale-tier BASIC_GPU \
-- \
--style $STYLE \
--train-path $TRAIN_PATH \
--vgg-path $VGG_PATH
```
