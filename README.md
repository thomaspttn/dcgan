# ARTDCGAN

## Introduction
This is my attempt at an art DCGAN based off the DCGAN tutorial available on the PyTorch website. The primary advancements for this DCGAN are an updated ``scrape.py`` which can be used for Wikiart, but which can also be modified to be used on a specific artist.

## Getting Started
Make sure to use ```src/scrape.py``` to pull images from Wikiart. This is currently far from optimized, but it works well for pulling the images without the use of libraries like Selenium by simulating requests to the Wikiart server. In the future this may be generalized, but I'm currently more concerned with getting a better result.

## Hyperparameter Settings
Since the number of samples for my first trial (landscape style works by Monet) was only around 800, there wasn't a whole lot of data. I used a ``batch_size`` of 4 and 50 epochs to generate a somewhat nice output.

## Acknowledgements
A massive thanks to Robbie Barrat for inspiration for this project. My project is essentially a Python version of his. 
