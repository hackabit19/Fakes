# Fakes
<img src='https://github.com/hackabit19/Fakes/blob/master/Results/000164_0.jpg' /></t><img src='https://github.com/hackabit19/Fakes/blob/master/Results/000164_0.png' /><img src='https://github.com/hackabit19/Fakes/blob/master/Results/000568_1.jpg' />
</br>

## Table of contents
* [Introduction](#introduction)
* [Details](#details)
* [Implementation Details](#Implementation_details)

## Introduction :-
TryFirst is an interactive web-app which benefits users by allowing them to try-on a particular cloth to see how it suits them.
Thus, allowing consumers to virtually try on clothes will not only enhance their shopping experience, transforming the way
people shop for clothes, but also save cost for retailer. 
   
## Details
Frameworks Used :-</b>
* pytorch 1.3.0
* flask 
* matplotlib
* OpenPose
* Ranger Optimizer(current state of the art optimizer)

Dataset Used :-</b>
* MPV Dataset (contains person,cloth,cloth_mask,person_mask and poses)
Here is the link to the dataset [here](https://drive.google.com/open?id=1GiD74PMMykGAm3lwENpebewOYM1sgcNq)

Trained model is available [here](https://drive.google.com/open?id=1K1ZN4cNGzVHzQbC1Wz8_i-eivQhOFa3e)

## Implemenetation_details
* Pose Generation using openpose.
* Parser are generated using SS-nan (opensource pre-trained model) . 
* Used Generative Adversarial Networks with Adversarial loss, perceptual loss and L1 loss for smoothening.
* Used U-Net for generator and a downsampler for discriminator.

## Training process
* The pose generated and parser and person image are concatenated along with and cloth imgae are fedded to GMM.
* output of above is a warped cloth.
* Now that concatenated image along with warped cloth is feeded to Gans.
* Final output is image of person wearing desired cloth.
* Final loss of generator on validation : 3.62001
* Final loss of discriminator on validation :0.003821
* Epochs Trained : 50
* Optimizer : Ranger


## Resources
* Openpose - [here] https://github.com/CMU-Perceptual-Computing-Lab/openpose
* Parser  - [here] https://github.com/PeikeLi/Self-Correction-Human-Parsing
* viton - [here] https://arxiv.org/abs/1711.08447
