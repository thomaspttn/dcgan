# ARTDCGAN

## Introduction
This is my attempt at an art DCGAN based off the DCGAN tutorial available on the PyTorch website. The primary advancements for this DCGAN are an updated ``scrape.py`` which can be used for the new Wikiart design. In addition, this DCGAN focuses on trying to mimic the style of a particular artist, rather than the style of a genre. For this project, that artist is Claude Monet. 

## Getting Started
Make sure to use ```src/scrape.py``` to pull images from Wikiart. This is currently far from optimized, but it works well for pulling the images without the use of libraries like Selenium by simulating requests to the Wikiart server. In the future this may be generalized to support an arbitrary artist, but for this project I was only concerned with getting data for Monet. 

In addition, you will need to create an ``images`` directory in the same level as ``src``, and within this directory you should have some subdirectory containing images for training. Furthermore, you should make a directory ``save/unfiled`` within ``src`` to store output images (should you want them). This, again, is not optimized in the slightest and may be altered in a future update / when I learn to use GIT properly.

## Hyperparameter Settings
You are welcome to tweak hyperparameter settings to better fit your project. These were the ones that worked best for me with Monet's work, though. 

```
manualSeed = 999        # random seed
random.seed(manualSeed)
torch.manual_seed(manualSeed)
dataroot = "../images"        # image locations
workers = 2
batch_size = 128
image_size = 64
nc = 3          # number of channels for training images
nz = 100        # size of latent vector
ngf = 64        # size of feature maps in generator
ndf = 64        # size of feature maps in discriminator
num_epochs = 500
dlr = 0.0002    # discrim learning rate
glr = 0.0002    # generator learning rate
beta1 = 0.5
ngpu = 1
```

## Acknowledgements
A massive thanks to Robbie Barrat for inspiration for this project - mine is essentially a Python version of his. Also a huge thanks to PyTorch for providing the sample DCGAN code. I have modified it slightly, but the general structure of the networks as well as the training loop are all the same.
