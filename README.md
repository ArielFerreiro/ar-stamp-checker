# ar-stamp-checker: TOBACCO STAMPS CHECKER :: ARGENTINA LABELS

Deep learning model to verify tobacco tax stamps in Argentina. 

<img src="http://blogs.infobae.com/maldita-nicotina/files/2013/07/FOTOOO-1.jpg"
     alt="Tobacco Stamps Argentina"
     style="float: left; margin-right: 10px; height: 50%; width: 50%;" />
     
The idea is to develop a model that given a picture (taken with a mobile phone) will:

1) Detect automatically the positioning of the label in the image
2) Analize the label characteristics and detect if the label is genuine or fake

For this task we will use Keras and Tensorflow libraries using the following techniques:

- Transfer learning (testing differents CNNs topologies: VGG, ResNet, Inception) pretrained with Imagenet dataset
- Adjusting final layers to achieve our needs using multitask learning to adjust the points of the label in the image
- Check if we can continue an additional task for the classification or to stack a new net on top of it for this purpose

The outcome of this model will be a TensorFlow Lite file to be exported and used in a mobile app.

### ***Datasets:***

To train the net we will use a set of pictures of around 1000 genuine products and another set of around 10000 images of fake
labeled products. We also have a balanced set of soft label products and hinge lid producsts which have a different disposition of
the label on the pack as you can see in the picture below.

To be able to train reasonable amoung of data we will use Albumentation techniques.

To annotate bounding boxes we used https://www.makesense.ai/ tool.
