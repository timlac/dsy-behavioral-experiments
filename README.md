# dsy-behavioral-experiments

Currently complete video data and mostly complete response data is provided for one experiment. 

## Negotiation Game Theory

### General info

The method used within this experiment is largely based upon the 'iterated ultimatum game (iUG)', an experimental game previously used by Shaw et al. (2018) among others 
(more info here - https://www.nature.com/articles/s41598-018-29233-9). The idea is that pairs of participants negotiate over the division of a sum of money (100kr). 
Participants occupy the role of either 'proposer' or 'responder'. Roles are changed after every 5 negotiation rounds, with 20 rounds in total.

The videos (both those captured on Zoom and in the lab) are of varying lengths, with negotiation exchanges not limited by time restrictions. This means that segmentation 
of the videos, based on individual negotiation rounds, for example, can be extremely challenging. However, an effort was previously made to provide timestamps for each set 
of 5 rounds for the face-to-face videos. See Excel document 'Ultimatum Game Video Segmentation'. 
This document is not complete and the zoom videos are missing. In its current state it adds little benefit. 

All videos are in .mp4 format. However, the video quality varies across the two conditions. For example, the videos captured in the lab were recorded under lighting conditions, 
with the same Axis IP cameras used for all dyads. This was not the case for the Zoom videos. Some of the recordings are therefore better quality than others (potentially due to 
camera resolution, network latency and so on...). All lab videos were recorded at 25 frames per second (fps). Videos taken recorded via Zoom have differing rates (e.g. participant 
10B = 30fps, whereas 7B = 25fps).

Audio is available for all recordings taken via Zoom. Audio is not available for some of the video recordings taken in the lab (see 'Ultimatum Game Video Segmentation' 
Excel document for further details on which videos specifically). The loss of audio recording occurred due to an undetected fault with the microphone.

All Zoom recordings have been edited using ‘Camtasia’ software.  The ‘editing’ refers to the cropping of individual videos from the original recordings 
in Zoom (which contained images of both participants).  

### Files of interest

[Full Dataset](data/out/full_dataset.csv) contains the response data for all the videos. Each video has an id, 
e.g. `F18B` or `Z3A` 
- where the initial letter indicates setting (`Z`=zoom and `F`=studio).
- The number indicates the dyad id
- `A` and `B` indicates the participant in the dyad, each participant has a separate video. 

The video corresponds to the filenames of the videos as well as the output files from opensmile/openface. 

Silence detection has been performed on all the studio videos since microphone problems have been reported for this setting. 
See: [Silence Detection Notebook](silence_detection_notebook.ipynb). A flag has been added to the full dataset file where complete or partial silence has been identified.

The questionnaire items are present in the full dataset file, data is mostly complete, some missing for one dyad (2 participants). 
An overview of all item questions is also provided in [Items](data/out/items.csv) where each item has also been given a code. 
This code is not used elsewhere.

Apart from questionnaire items each id also has points, which indicate how many points each participant got in the experiment. 
This data is mostly complete, points are missing for 2 dyads (4 participants).

Most other files are intermediaries used to create the final Full Dataset file and can be disregarded. 

