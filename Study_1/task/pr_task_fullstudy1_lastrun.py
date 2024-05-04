#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.3),
    on Tue Jul 19 08:58:16 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.3'
expName = 'PRp_v1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/User/Documents/PR_vs_Guessing_FullStudy/pr_task_fullstudy1_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[2240, 1260], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='imac', color='whitesmoke', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "consent"
consentClock = core.Clock()
image_11 = visual.ImageStim(
    win=win,
    name='image_11', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.05), size=(0.65, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
consent1_next = keyboard.Keyboard()
text_89 = visual.TextStim(win=win, name='text_89',
    text='Click SPACE to Continue',
    font='Open Sans',
    pos=(0, -0.4), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "consent1"
consent1Clock = core.Clock()
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.1), size=(0.65, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
consent1_next_2 = keyboard.Keyboard()
text_90 = visual.TextStim(win=win, name='text_90',
    text='I certify that I have read the informed consent and received the information to contact the investigators if necessary.\n\nClick ‘y’ for YES\nClick ’n’ for NO, and you will EXIT the study',
    font='Open Sans',
    pos=(0, -0.35), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='In this task, you will learn how to navigate a picture game. Each time you navigate the game, you have a single choice to make. Each choice you make will take you from one picture to another. \n\nIn the first part of this task you must learn how often other pictures tend to appear after starting at an initial picture. For example, you might need to learn how often you see an apple after starting at an image of a tree. \n\nThus, this task requires you to learn probabilities of image transitions. The probability of seeing an apple after a tree might be very different from the probability of seeing the apple after a rock. \n\nAfter this learning phase, you can use this knowledge to plan how to win points in a final phase. Importantly, you can earn money based on these points. You will be instructed later exactly how to win points. \n\nPress Space to continue',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "instruction2"
instruction2Clock = core.Clock()
key_resp_2 = keyboard.Keyboard()
text_2 = visual.TextStim(win=win, name='text_2',
    text='PHASE 1: LEARN HOW TO NAVIGATE IN THE PICTURE WORLD\n\nYou will now be instructed which actions to take in the picture world. Your goal is to learn which new picture you will arrive at after selecting a picture by clicking the corresponding number on your keyboard.\n\nNOTE: There will be a SECOND PHASE after this first phase, where you can use what you learned to win even more money!\n\nPress Space to continue',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "stage1_instructions"
stage1_instructionsClock = core.Clock()
keyboard_entry_instr1 = keyboard.Keyboard()
start_instr1 = visual.TextStim(win=win, name='start_instr1',
    text='Start',
    font='Open Sans',
    pos=(0, 0.15), height=0.075, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
trident_start = visual.ImageStim(
    win=win,
    name='trident_start', 
    image='trident.png', mask=None,
    ori=0.0, pos=(-0.4, -0.10), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
planet_start = visual.ImageStim(
    win=win,
    name='planet_start', 
    image='planet.png', mask=None,
    ori=0.0, pos=(0.4, -0.10), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
instructions_decisionrules = visual.TextStim(win=win, name='instructions_decisionrules',
    text='The first decision will say “START”. Here, choosing 1 will ALWAYS get you to the TRIDENT, choosing 9 will ALWAYS get you to the PLANET.',
    font='Open Sans',
    pos=(0, 0.40), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
space_continue_instr1 = visual.TextStim(win=win, name='space_continue_instr1',
    text='Press Space to continue',
    font='Open Sans',
    pos=(0, -0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
one = visual.TextStim(win=win, name='one',
    text='1',
    font='Open Sans',
    pos=(-0.4, -0.26), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
nine = visual.TextStim(win=win, name='nine',
    text='9',
    font='Open Sans',
    pos=(0.4, -0.26), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "stage2_4_instructions"
stage2_4_instructionsClock = core.Clock()
responseleft = keyboard.Keyboard()
text_4 = visual.TextStim(win=win, name='text_4',
    text='After choosing the trident or the planet, you will see a series of TWO MORE IMAGES. Your goal is to remember which images tend to come after you start at either the trident or the planet image. \n\nTo show you what this looks like, you will do a practice round. You will be tested to see if you remember which images come after the starting image. Good luck! \n\nPress SPACE to continue',
    font='Open Sans',
    pos=(0, 0.0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "stage_2_4_practice"
stage_2_4_practiceClock = core.Clock()
image_22 = visual.ImageStim(
    win=win,
    name='image_22', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_10 = keyboard.Keyboard()
text_40 = visual.TextStim(win=win, name='text_40',
    text='Press 1',
    font='Open Sans',
    pos=(0, -0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "stage_2_4_practice_result"
stage_2_4_practice_resultClock = core.Clock()
image_20 = visual.ImageStim(
    win=win,
    name='image_20', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_76 = visual.TextStim(win=win, name='text_76',
    text='Moving to next image…',
    font='Open Sans',
    pos=(0, 0), height=0.055, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
image_12 = visual.ImageStim(
    win=win,
    name='image_12', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_77 = visual.TextStim(win=win, name='text_77',
    text='Done trial!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "quiz_practice"
quiz_practiceClock = core.Clock()
basket_2 = visual.ImageStim(
    win=win,
    name='basket_2', 
    image='basket.png', mask=None,
    ori=0.0, pos=(-0.6, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fireworks_2 = visual.ImageStim(
    win=win,
    name='fireworks_2', 
    image='fireworks.png', mask=None,
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
tree_2 = visual.ImageStim(
    win=win,
    name='tree_2', 
    image='sin', mask=None,
    ori=0.0, pos=(0.6, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_17 = visual.TextStim(win=win, name='text_17',
    text='A',
    font='Open Sans',
    pos=(-0.6, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
text_21 = visual.TextStim(win=win, name='text_21',
    text='G',
    font='Open Sans',
    pos=(0, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_27 = visual.TextStim(win=win, name='text_27',
    text='L',
    font='Open Sans',
    pos=(0.6, -0.25), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
practice_answer = keyboard.Keyboard()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Which image below did you see most often after clicking 1 at the apple image?',
    font='Open Sans',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "feedback1"
feedback1Clock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "memory_quiz"
memory_quizClock = core.Clock()
text_75 = visual.TextStim(win=win, name='text_75',
    text='During your learning about how to get from one picture to another, you will be tested on your learning.\n\nEvery so often, you will be asked to use what you’ve learned to try to reach an image where money is hiding. Each of these questions has a correct answer, and we will reward you at the end of the study based on how well you did on these questions. \n\nSpecifically, we will pick a total of 5 rounds at random from these rounds where you can earn reward to determine how much money you win\n\nPress space to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_23 = keyboard.Keyboard()

# Initialize components for Routine "reminder_second_phase"
reminder_second_phaseClock = core.Clock()
text_74 = visual.TextStim(win=win, name='text_74',
    text='After you complete many rounds of learning how to navigate between pictures in the picture game, you will have a SECOND PHASE where you can earn more money based off what you learned!\n\nIMPORTANT to do well on both phases, it is vital to remember that during training, the image that leads the most times to another image NEVER CHANGES. For example, if in the beginning of the task, the apple image has the best chance to lead to the basket image, it will ALWAYS be the best image to get to the basket image. The probabilities between images are constant throughout the task.\n\nPress space for a quiz on the instructions',
    font='Open Sans',
    pos=(0, 0), height=0.045, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_22 = keyboard.Keyboard()

# Initialize components for Routine "instructions_quiz_1"
instructions_quiz_1Clock = core.Clock()
text_43 = visual.TextStim(win=win, name='text_43',
    text='Instructions Quiz\n\n1. What is the goal of the picture game?\n\na.to learn the type of picture\n\nb.to learn the meaning of pictures\n\nc.to learn which pictures you tend to see after making an initial choice at a starting image\n\nd.to learn how actions you take at a picture give you rewards or punishments',
    font='Open Sans',
    pos=(0, 0), height=0.038, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_17 = keyboard.Keyboard()

# Initialize components for Routine "instructions_quiz_2"
instructions_quiz_2Clock = core.Clock()
text_70 = visual.TextStim(win=win, name='text_70',
    text='Instructions Quiz\n\n1. How are the second and third images different from the first?\n\na. you get to select actions at the second and third images \n\nb.these images are new every time\n\nc. you need to learn which second and third images you tend to see after taking an action at a starting image, but you don’t take any actions once you’re at the second and third images.\n\nd. you need to learn which second and third images you tend to see after taking an action at a starting image, and you MUST take NEW actions once you’re at the second image to see the third image.\n',
    font='Open Sans',
    pos=(0, 0), height=0.038, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_18 = keyboard.Keyboard()

# Initialize components for Routine "instructions_quiz_3"
instructions_quiz_3Clock = core.Clock()
text_71 = visual.TextStim(win=win, name='text_71',
    text='Instructions Quiz\n\n1. What happens during the reward quiz?\n\na.you must recall how the pictures look\n\nb. you are told that a picture has money hiding in it, and you must choose the action that has the best chance of getting you there. 5 of these rounds the computer chooses AT RANDOM will determine how much money you win!\n\nc. you must recall images you most likely DO NOT see after taking an action at a starting image\n\nd. you are told that a picture has money hiding in it, and you must choose the action that has the best chance of getting you there. Your TOTAL SCORE on these rounds will determine how much money you win!',
    font='Open Sans',
    pos=(0, 0), height=0.038, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_19 = keyboard.Keyboard()

# Initialize components for Routine "instructions_quiz_4"
instructions_quiz_4Clock = core.Clock()
text_72 = visual.TextStim(win=win, name='text_72',
    text='Instructions Quiz\n\n1. Your goal is to learn the how likely a certain image (e.g., basket) comes after a starting image (e.g., apple). The probabilities that determine transitions between images: \n\na. Change throughout the task, so the image that has the best chance to get you to the another image can CHANGE.\n\nb. NEVER CHANGE. Throughout the entire task, the probabilities that determine which image gets you to another image NEVER CHANGE. \n\nc. Are always 100%. If you want to get to the basket, there’s only one preceding image that could possibly get you there.\n\nd. Cannot be learned. The goal of the task is to guess which are the best images to get you to new images, because their probabilties are entirely random\n',
    font='Open Sans',
    pos=(0, 0), height=0.038, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_20 = keyboard.Keyboard()

# Initialize components for Routine "result_quiz_instructions"
result_quiz_instructionsClock = core.Clock()
result_q_instr = visual.TextStim(win=win, name='result_q_instr',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "instructions3"
instructions3Clock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Press SPACE to start learning!',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()
quiz1list=['apple.png','trident.png','fireworks.png','fox.png','bowling.png']
quiz2list=['window.png','bell.png','tree.png','watch.png']
q1left_correct=['1','3','5','2','7']
q1right_correct=['2','4','7','3','8']
q2left_correct=['5','1','6','2']
q2right_correct=['6','3','5','4']

learning_reward_goal_list=['compass.png', 'snorkel.png','train.png','north.png','houses.png','tophat.png','compass.png','microphone.png','houses.png','snorkel.png','thermometer.png','tophat.png','train.png','north.png','thermometer.png','microphone.png']
counter_reward_learning=0
learning_reward_goal=learning_reward_goal_list[0]
msg_new='lost'
action_list=['left.png','right.png']
quiz_counter=0
num_quiz_trials=10
stage2=['bell.png','watch.png','watch.png','fox.png','fireworks.png','watch.png','tree.png','bowling.png']
stage3=['houses.png','train.png','thermometer.png','compass.png','north.png','microphone.png','tophat.png','snorkel.png']
quizzes=[quiz1list,quiz2list]
predictions1=[stage2,stage2,stage3,stage3,stage3]
predictions2=[stage2,stage3,stage3,stage3]
predictions=[predictions1,predictions2]
trials_with_three=[11,12,13,14,15,16]
trials_with_four=[17,18]

incorrect_actions=0
action='left.png'



correct_quiz='p'
percent_correct=''
text_correct=''



# Initialize components for Routine "stage1"
stage1Clock = core.Clock()
click_action = keyboard.Keyboard()
text_9 = visual.TextStim(win=win, name='text_9',
    text='Choose the number that appears below one of the images:',
    font='Open Sans',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
trident_start_learning = visual.ImageStim(
    win=win,
    name='trident_start_learning', 
    image='trident.png', mask=None,
    ori=0.0, pos=(-0.4, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
planet_start_learning = visual.ImageStim(
    win=win,
    name='planet_start_learning', 
    image='sin', mask=None,
    ori=0.0, pos=(0.4, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(-0.25, -0.20), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "incorrect_answer"
incorrect_answerClock = core.Clock()
incorrect_display = visual.TextStim(win=win, name='incorrect_display',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "learning_trial_sequence"
learning_trial_sequenceClock = core.Clock()
stage1_learning = visual.ImageStim(
    win=win,
    name='stage1_learning', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
text_78 = visual.TextStim(win=win, name='text_78',
    text='Moving to next image…',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
stage2_learning = visual.ImageStim(
    win=win,
    name='stage2_learning', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_80 = visual.TextStim(win=win, name='text_80',
    text='Moving to the next image…',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
stage3_learning = visual.ImageStim(
    win=win,
    name='stage3_learning', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# Initialize components for Routine "memory_q"
memory_qClock = core.Clock()
text_92 = visual.TextStim(win=win, name='text_92',
    text='Memory quiz question next. Pay Attention!',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "prediction4"
prediction4Clock = core.Clock()
outcome4 = visual.TextStim(win=win, name='outcome4',
    text='Choose what most likley gets you to the following image',
    font='Open Sans',
    pos=(0, 0.36), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
picture_reward_goal = visual.ImageStim(
    win=win,
    name='picture_reward_goal', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0.17), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
resp4 = keyboard.Keyboard()
learning_rew_trident = visual.ImageStim(
    win=win,
    name='learning_rew_trident', 
    image='trident.png', mask=None,
    ori=0.0, pos=(-0.25, -0.1), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
learning_rew_planet = visual.ImageStim(
    win=win,
    name='learning_rew_planet', 
    image='planet.png', mask=None,
    ori=0.0, pos=(0.25, -0.1), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
text_79 = visual.TextStim(win=win, name='text_79',
    text='1',
    font='Open Sans',
    pos=(-0.25, -0.3), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
text_85 = visual.TextStim(win=win, name='text_85',
    text='9',
    font='Open Sans',
    pos=(0.25, -0.30), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "quiz_score"
quiz_scoreClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.065, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "take_a_break"
take_a_breakClock = core.Clock()
text_39 = visual.TextStim(win=win, name='text_39',
    text='Next trial…',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "instructions_reward_stage"
instructions_reward_stageClock = core.Clock()
instructions_rewardstage = visual.TextStim(win=win, name='instructions_rewardstage',
    text='Now it’s time to use what you learned to get rewards. Each time you enter the picture world to win money, you will be told which images will give you points! \n\nYou need to use this information to choose the trident or planet that’s most likely to get you points. For instance, it may be worth going for a smaller amount of points if it is much more likely you are to reach that image. You must use the probabilities you learned in training to make the best choice.\n\nPress Space to continue ',
    font='Open Sans',
    pos=(0, 0), height=0.045, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_11 = keyboard.Keyboard()

# Initialize components for Routine "i2_reward"
i2_rewardClock = core.Clock()
text_42 = visual.TextStim(win=win, name='text_42',
    text='Similarly a larger amount of points may be really hard to get to, so you must weight the likelihood of getting to an image against the amount of points you win if you get to the image. You must use this information to make the best decision to maximize how many points you win.\n\n\nIMPORTANT: After you select the trident or planet images to try to win points, you will not see any more images aftewards. This prevents you from learning anything else at this phase, as you need to use what you already learned to plan accordingly. The computer will simulate which images you reached and calculate your points, but this will not be shown to you. Instead you will be told how many points you won after this phase is over.\n\nPress Space to Continue\n',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "practice_view_reward_info"
practice_view_reward_infoClock = core.Clock()
im1_example_choicephase = visual.ImageStim(
    win=win,
    name='im1_example_choicephase', 
    image='watch.png', mask=None,
    ori=0.0, pos=(-0.30, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
resp4_2 = keyboard.Keyboard()
im2_example_choicephase = visual.ImageStim(
    win=win,
    name='im2_example_choicephase', 
    image='tree.png', mask=None,
    ori=0.0, pos=(0.30, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
example_trial_choice_phase = visual.TextStim(win=win, name='example_trial_choice_phase',
    text='An Example Trial',
    font='Open Sans',
    pos=(0, 0.4), height=0.055, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
im1_rewvalue = visual.TextStim(win=win, name='im1_rewvalue',
    text='Win 2 points!',
    font='Open Sans',
    pos=(-0.30, -0.2), height=0.045, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
im2_rewvalue = visual.TextStim(win=win, name='im2_rewvalue',
    text='Win 10 points!',
    font='Open Sans',
    pos=(0.3, -0.2), height=0.045, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
text_28 = visual.TextStim(win=win, name='text_28',
    text='Press Space To Continue',
    font='Open Sans',
    pos=(0, 0.25), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "instructions_planning"
instructions_planningClock = core.Clock()
text_66 = visual.TextStim(win=win, name='text_66',
    text='When you have decided how to act after seeing all information, you will choose either the trident or the planet image to try to get points!',
    font='Open Sans',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
houses_choice_practice = visual.ImageStim(
    win=win,
    name='houses_choice_practice', 
    image='trident.png', mask=None,
    ori=0.0, pos=(0.3, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
train_choice_practice = visual.ImageStim(
    win=win,
    name='train_choice_practice', 
    image='planet.png', mask=None,
    ori=0.0, pos=(-0.3, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
key_resp_12 = keyboard.Keyboard()
text_24 = visual.TextStim(win=win, name='text_24',
    text='Press Space to Continue',
    font='Open Sans',
    pos=(0, -0.35), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "start_planning_trials"
start_planning_trialsClock = core.Clock()
text_67 = visual.TextStim(win=win, name='text_67',
    text='You are now ready to start the task, using the knowledge you learned about how to navigate through the pictures. Good luck!\n\nPress Space to begin',
    font='Open Sans',
    pos=(0, 0), height=0.065, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_15 = keyboard.Keyboard()

# Initialize components for Routine "info_choicephase"
info_choicephaseClock = core.Clock()
im1_planning = visual.ImageStim(
    win=win,
    name='im1_planning', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.20, 0.15), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
im2_planning = visual.ImageStim(
    win=win,
    name='im2_planning', 
    image='sin', mask=None,
    ori=0.0, pos=(0.20, 0.15), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
example_trial_choice_phase_2 = visual.TextStim(win=win, name='example_trial_choice_phase_2',
    text='Reward information for upcoming trial:',
    font='Open Sans',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
im1_rewvalue_planning = visual.TextStim(win=win, name='im1_rewvalue_planning',
    text='',
    font='Open Sans',
    pos=(-0.20, 0), height=0.045, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
im2_rewvalue_planning = visual.TextStim(win=win, name='im2_rewvalue_planning',
    text='',
    font='Open Sans',
    pos=(0.20, 0), height=0.045, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_29 = visual.TextStim(win=win, name='text_29',
    text='Press Space To Continue',
    font='Open Sans',
    pos=(0, -0.45), height=0.045, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
key_resp_24 = keyboard.Keyboard()
im3_planning = visual.ImageStim(
    win=win,
    name='im3_planning', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.2, -0.20), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
im4_planning = visual.ImageStim(
    win=win,
    name='im4_planning', 
    image='sin', mask=None,
    ori=0.0, pos=(0.2, -0.20), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
im3_num_planning = visual.TextStim(win=win, name='im3_num_planning',
    text='',
    font='Open Sans',
    pos=(-0.2, -0.35), height=0.045, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
im4_num_planning = visual.TextStim(win=win, name='im4_num_planning',
    text='',
    font='Open Sans',
    pos=(0.2, -0.35), height=0.045, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "stage1_choice_enact"
stage1_choice_enactClock = core.Clock()
text_81 = visual.TextStim(win=win, name='text_81',
    text='Make your decision',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
trident_choice_2 = visual.ImageStim(
    win=win,
    name='trident_choice_2', 
    image='trident.png', mask=None,
    ori=0.0, pos=(-0.30, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
planet_choice_2 = visual.ImageStim(
    win=win,
    name='planet_choice_2', 
    image='planet.png', mask=None,
    ori=0.0, pos=(0.3, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
key_resp_25 = keyboard.Keyboard()
text_31 = visual.TextStim(win=win, name='text_31',
    text='Press 1',
    font='Open Sans',
    pos=(-0.3, -0.20), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_82 = visual.TextStim(win=win, name='text_82',
    text='Press 9',
    font='Open Sans',
    pos=(0.3, -0.20), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "final_stage5"
final_stage5Clock = core.Clock()
text_68 = visual.TextStim(win=win, name='text_68',
    text='Computer simulating images to calculate reward…',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_30 = visual.TextStim(win=win, name='text_30',
    text='You will find out your reward total after all this phase is completed.\n\nPress Space to Continue to Next Trial',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_16 = keyboard.Keyboard()

# Initialize components for Routine "reward_revaluation_choice"
reward_revaluation_choiceClock = core.Clock()
im1_planning_4 = visual.ImageStim(
    win=win,
    name='im1_planning_4', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.20, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
im2_planning_4 = visual.ImageStim(
    win=win,
    name='im2_planning_4', 
    image='sin', mask=None,
    ori=0.0, pos=(0.20, 0.0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
example_trial_choice_phase_6 = visual.TextStim(win=win, name='example_trial_choice_phase_6',
    text='Reward information for upcoming trial:',
    font='Open Sans',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
im1_rewvalue_planning_4 = visual.TextStim(win=win, name='im1_rewvalue_planning_4',
    text='',
    font='Open Sans',
    pos=(-0.2, -0.15), height=0.045, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
im2_rewvalue_planning_4 = visual.TextStim(win=win, name='im2_rewvalue_planning_4',
    text='',
    font='Open Sans',
    pos=(0.2, -0.15), height=0.045, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_101 = visual.TextStim(win=win, name='text_101',
    text='Press Space To Continue',
    font='Open Sans',
    pos=(0, -0.4), height=0.045, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
key_resp_33 = keyboard.Keyboard()

# Initialize components for Routine "reward_reval_choice"
reward_reval_choiceClock = core.Clock()
text_96 = visual.TextStim(win=win, name='text_96',
    text='Make your decision',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
trident_choice = visual.ImageStim(
    win=win,
    name='trident_choice', 
    image='trident.png', mask=None,
    ori=0.0, pos=(-0.30, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
planet_choice = visual.ImageStim(
    win=win,
    name='planet_choice', 
    image='planet.png', mask=None,
    ori=0.0, pos=(0.3, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
key_resp_31 = keyboard.Keyboard()
text_97 = visual.TextStim(win=win, name='text_97',
    text='Press 1',
    font='Open Sans',
    pos=(-0.3, -0.20), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_98 = visual.TextStim(win=win, name='text_98',
    text='Press 9',
    font='Open Sans',
    pos=(0.3, -0.20), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "reward_reval_see"
reward_reval_seeClock = core.Clock()
text_99 = visual.TextStim(win=win, name='text_99',
    text='Computer simulating images to calculate reward…',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_100 = visual.TextStim(win=win, name='text_100',
    text='You will find out your reward total after all this phase is completed.\n\nPress Space to Continue to Next Trial',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_32 = keyboard.Keyboard()

# Initialize components for Routine "transition_revaluation"
transition_revaluationClock = core.Clock()
text_25 = visual.TextStim(win=win, name='text_25',
    text='BONUS ROUND',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_26 = visual.TextStim(win=win, name='text_26',
    text='The picture world you learned has now CHANGED! Now, the TRIDENT leads only to the FOX, and the PLANET leads only to the BELL. Look below and use this new information to win more money next!\n\n\n ',
    font='Open Sans',
    pos=(0, 0.20), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_8 = keyboard.Keyboard()
trident_reval = visual.ImageStim(
    win=win,
    name='trident_reval', 
    image='trident.png', mask=None,
    ori=0.0, pos=(-0.2, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
fox_reval = visual.ImageStim(
    win=win,
    name='fox_reval', 
    image='fox.png', mask=None,
    ori=0.0, pos=(0.2, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
right_arrow = visual.ImageStim(
    win=win,
    name='right_arrow', 
    image='right.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.16, 0.16),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
planet_reval = visual.ImageStim(
    win=win,
    name='planet_reval', 
    image='planet.png', mask=None,
    ori=0.0, pos=(-0.2, -0.25), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
right_arrow2 = visual.ImageStim(
    win=win,
    name='right_arrow2', 
    image='right.png', mask=None,
    ori=0.0, pos=(0, -0.25), size=(0.16, 0.16),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
bell_reval = visual.ImageStim(
    win=win,
    name='bell_reval', 
    image='bell.png', mask=None,
    ori=0.0, pos=(0.2, -0.25), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
text_94 = visual.TextStim(win=win, name='text_94',
    text='Press Space to continue',
    font='Open Sans',
    pos=(0, -0.4), height=0.045, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "info_choice_revaluation_2"
info_choice_revaluation_2Clock = core.Clock()
im1_planning_2 = visual.ImageStim(
    win=win,
    name='im1_planning_2', 
    image='sin', mask=None,
    ori=0.0, pos=(-0.20, 0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
im2_planning_2 = visual.ImageStim(
    win=win,
    name='im2_planning_2', 
    image='sin', mask=None,
    ori=0.0, pos=(0.20, 0.0), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
example_trial_choice_phase_4 = visual.TextStim(win=win, name='example_trial_choice_phase_4',
    text='Reward information for upcoming trial:',
    font='Open Sans',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
im1_rewvalue_planning_2 = visual.TextStim(win=win, name='im1_rewvalue_planning_2',
    text='',
    font='Open Sans',
    pos=(-0.2, -0.15), height=0.045, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
im2_rewvalue_planning_2 = visual.TextStim(win=win, name='im2_rewvalue_planning_2',
    text='',
    font='Open Sans',
    pos=(0.2, -0.15), height=0.045, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_93 = visual.TextStim(win=win, name='text_93',
    text='Press Space To Continue',
    font='Open Sans',
    pos=(0, -0.4), height=0.045, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
key_resp_29 = keyboard.Keyboard()

# Initialize components for Routine "stage1_choice_enact"
stage1_choice_enactClock = core.Clock()
text_81 = visual.TextStim(win=win, name='text_81',
    text='Make your decision',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
trident_choice_2 = visual.ImageStim(
    win=win,
    name='trident_choice_2', 
    image='trident.png', mask=None,
    ori=0.0, pos=(-0.30, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
planet_choice_2 = visual.ImageStim(
    win=win,
    name='planet_choice_2', 
    image='planet.png', mask=None,
    ori=0.0, pos=(0.3, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
key_resp_25 = keyboard.Keyboard()
text_31 = visual.TextStim(win=win, name='text_31',
    text='Press 1',
    font='Open Sans',
    pos=(-0.3, -0.20), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_82 = visual.TextStim(win=win, name='text_82',
    text='Press 9',
    font='Open Sans',
    pos=(0.3, -0.20), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "final_stage5"
final_stage5Clock = core.Clock()
text_68 = visual.TextStim(win=win, name='text_68',
    text='Computer simulating images to calculate reward…',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_30 = visual.TextStim(win=win, name='text_30',
    text='You will find out your reward total after all this phase is completed.\n\nPress Space to Continue to Next Trial',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_16 = keyboard.Keyboard()

# Initialize components for Routine "reward_total"
reward_totalClock = core.Clock()
text_84 = visual.TextStim(win=win, name='text_84',
    text='Congrats! Your bonus points will be calculated soon and delivered to you on Prolific!',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "done"
doneClock = core.Clock()
text_62 = visual.TextStim(win=win, name='text_62',
    text='Thank you for participating!\n\nYou will be granted credit on Prolific within the next week.  ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
instructions_get_right = data.TrialHandler(nReps=500.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='instructions_get_right')
thisExp.addLoop(instructions_get_right)  # add the loop to the experiment
thisInstructions_get_right = instructions_get_right.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInstructions_get_right.rgb)
if thisInstructions_get_right != None:
    for paramName in thisInstructions_get_right:
        exec('{} = thisInstructions_get_right[paramName]'.format(paramName))

for thisInstructions_get_right in instructions_get_right:
    currentLoop = instructions_get_right
    # abbreviate parameter names if possible (e.g. rgb = thisInstructions_get_right.rgb)
    if thisInstructions_get_right != None:
        for paramName in thisInstructions_get_right:
            exec('{} = thisInstructions_get_right[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "consent"-------
    continueRoutine = True
    # update component parameters for each repeat
    image_11.setImage('consent1.png')
    consent1_next.keys = []
    consent1_next.rt = []
    _consent1_next_allKeys = []
    # keep track of which components have finished
    consentComponents = [image_11, consent1_next, text_89]
    for thisComponent in consentComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    consentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "consent"-------
    while continueRoutine:
        # get current time
        t = consentClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=consentClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_11* updates
        if image_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_11.frameNStart = frameN  # exact frame index
            image_11.tStart = t  # local t and not account for scr refresh
            image_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
            image_11.setAutoDraw(True)
        
        # *consent1_next* updates
        waitOnFlip = False
        if consent1_next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            consent1_next.frameNStart = frameN  # exact frame index
            consent1_next.tStart = t  # local t and not account for scr refresh
            consent1_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(consent1_next, 'tStartRefresh')  # time at next scr refresh
            consent1_next.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(consent1_next.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(consent1_next.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if consent1_next.status == STARTED and not waitOnFlip:
            theseKeys = consent1_next.getKeys(keyList=['space'], waitRelease=False)
            _consent1_next_allKeys.extend(theseKeys)
            if len(_consent1_next_allKeys):
                consent1_next.keys = _consent1_next_allKeys[-1].name  # just the last key pressed
                consent1_next.rt = _consent1_next_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_89* updates
        if text_89.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_89.frameNStart = frameN  # exact frame index
            text_89.tStart = t  # local t and not account for scr refresh
            text_89.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_89, 'tStartRefresh')  # time at next scr refresh
            text_89.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in consentComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "consent"-------
    for thisComponent in consentComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructions_get_right.addData('image_11.started', image_11.tStartRefresh)
    instructions_get_right.addData('image_11.stopped', image_11.tStopRefresh)
    # check responses
    if consent1_next.keys in ['', [], None]:  # No response was made
        consent1_next.keys = None
    instructions_get_right.addData('consent1_next.keys',consent1_next.keys)
    if consent1_next.keys != None:  # we had a response
        instructions_get_right.addData('consent1_next.rt', consent1_next.rt)
    instructions_get_right.addData('consent1_next.started', consent1_next.tStartRefresh)
    instructions_get_right.addData('consent1_next.stopped', consent1_next.tStopRefresh)
    instructions_get_right.addData('text_89.started', text_89.tStartRefresh)
    instructions_get_right.addData('text_89.stopped', text_89.tStopRefresh)
    # the Routine "consent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "consent1"-------
    continueRoutine = True
    # update component parameters for each repeat
    image_13.setImage('consent2.png')
    consent1_next_2.keys = []
    consent1_next_2.rt = []
    _consent1_next_2_allKeys = []
    # keep track of which components have finished
    consent1Components = [image_13, consent1_next_2, text_90]
    for thisComponent in consent1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    consent1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "consent1"-------
    while continueRoutine:
        # get current time
        t = consent1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=consent1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_13* updates
        if image_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_13.frameNStart = frameN  # exact frame index
            image_13.tStart = t  # local t and not account for scr refresh
            image_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
            image_13.setAutoDraw(True)
        
        # *consent1_next_2* updates
        waitOnFlip = False
        if consent1_next_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            consent1_next_2.frameNStart = frameN  # exact frame index
            consent1_next_2.tStart = t  # local t and not account for scr refresh
            consent1_next_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(consent1_next_2, 'tStartRefresh')  # time at next scr refresh
            consent1_next_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(consent1_next_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(consent1_next_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if consent1_next_2.status == STARTED and not waitOnFlip:
            theseKeys = consent1_next_2.getKeys(keyList=['y', 'n'], waitRelease=False)
            _consent1_next_2_allKeys.extend(theseKeys)
            if len(_consent1_next_2_allKeys):
                consent1_next_2.keys = _consent1_next_2_allKeys[-1].name  # just the last key pressed
                consent1_next_2.rt = _consent1_next_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_90* updates
        if text_90.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_90.frameNStart = frameN  # exact frame index
            text_90.tStart = t  # local t and not account for scr refresh
            text_90.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_90, 'tStartRefresh')  # time at next scr refresh
            text_90.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in consent1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "consent1"-------
    for thisComponent in consent1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructions_get_right.addData('image_13.started', image_13.tStartRefresh)
    instructions_get_right.addData('image_13.stopped', image_13.tStopRefresh)
    # check responses
    if consent1_next_2.keys in ['', [], None]:  # No response was made
        consent1_next_2.keys = None
    instructions_get_right.addData('consent1_next_2.keys',consent1_next_2.keys)
    if consent1_next_2.keys != None:  # we had a response
        instructions_get_right.addData('consent1_next_2.rt', consent1_next_2.rt)
    instructions_get_right.addData('consent1_next_2.started', consent1_next_2.tStartRefresh)
    instructions_get_right.addData('consent1_next_2.stopped', consent1_next_2.tStopRefresh)
    instructions_get_right.addData('text_90.started', text_90.tStartRefresh)
    instructions_get_right.addData('text_90.stopped', text_90.tStopRefresh)
    if consent1_next_2.keys=='n':
        psychoJS.quit()
    # the Routine "consent1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    instructionsComponents = [text, key_resp]
    for thisComponent in instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructions"-------
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructions_get_right.addData('text.started', text.tStartRefresh)
    instructions_get_right.addData('text.stopped', text.tStopRefresh)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instruction2"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    instruction2Components = [key_resp_2, text_2]
    for thisComponent in instruction2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instruction2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instruction2"-------
    while continueRoutine:
        # get current time
        t = instruction2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instruction2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instruction2"-------
    for thisComponent in instruction2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructions_get_right.addData('text_2.started', text_2.tStartRefresh)
    instructions_get_right.addData('text_2.stopped', text_2.tStopRefresh)
    # the Routine "instruction2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stage1_instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    keyboard_entry_instr1.keys = []
    keyboard_entry_instr1.rt = []
    _keyboard_entry_instr1_allKeys = []
    # keep track of which components have finished
    stage1_instructionsComponents = [keyboard_entry_instr1, start_instr1, trident_start, planet_start, instructions_decisionrules, space_continue_instr1, one, nine]
    for thisComponent in stage1_instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stage1_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stage1_instructions"-------
    while continueRoutine:
        # get current time
        t = stage1_instructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stage1_instructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *keyboard_entry_instr1* updates
        waitOnFlip = False
        if keyboard_entry_instr1.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            keyboard_entry_instr1.frameNStart = frameN  # exact frame index
            keyboard_entry_instr1.tStart = t  # local t and not account for scr refresh
            keyboard_entry_instr1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(keyboard_entry_instr1, 'tStartRefresh')  # time at next scr refresh
            keyboard_entry_instr1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(keyboard_entry_instr1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(keyboard_entry_instr1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if keyboard_entry_instr1.status == STARTED and not waitOnFlip:
            theseKeys = keyboard_entry_instr1.getKeys(keyList=['space'], waitRelease=False)
            _keyboard_entry_instr1_allKeys.extend(theseKeys)
            if len(_keyboard_entry_instr1_allKeys):
                keyboard_entry_instr1.keys = _keyboard_entry_instr1_allKeys[-1].name  # just the last key pressed
                keyboard_entry_instr1.rt = _keyboard_entry_instr1_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *start_instr1* updates
        if start_instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_instr1.frameNStart = frameN  # exact frame index
            start_instr1.tStart = t  # local t and not account for scr refresh
            start_instr1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_instr1, 'tStartRefresh')  # time at next scr refresh
            start_instr1.setAutoDraw(True)
        
        # *trident_start* updates
        if trident_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trident_start.frameNStart = frameN  # exact frame index
            trident_start.tStart = t  # local t and not account for scr refresh
            trident_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trident_start, 'tStartRefresh')  # time at next scr refresh
            trident_start.setAutoDraw(True)
        
        # *planet_start* updates
        if planet_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            planet_start.frameNStart = frameN  # exact frame index
            planet_start.tStart = t  # local t and not account for scr refresh
            planet_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(planet_start, 'tStartRefresh')  # time at next scr refresh
            planet_start.setAutoDraw(True)
        
        # *instructions_decisionrules* updates
        if instructions_decisionrules.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_decisionrules.frameNStart = frameN  # exact frame index
            instructions_decisionrules.tStart = t  # local t and not account for scr refresh
            instructions_decisionrules.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_decisionrules, 'tStartRefresh')  # time at next scr refresh
            instructions_decisionrules.setAutoDraw(True)
        
        # *space_continue_instr1* updates
        if space_continue_instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            space_continue_instr1.frameNStart = frameN  # exact frame index
            space_continue_instr1.tStart = t  # local t and not account for scr refresh
            space_continue_instr1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space_continue_instr1, 'tStartRefresh')  # time at next scr refresh
            space_continue_instr1.setAutoDraw(True)
        
        # *one* updates
        if one.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            one.frameNStart = frameN  # exact frame index
            one.tStart = t  # local t and not account for scr refresh
            one.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(one, 'tStartRefresh')  # time at next scr refresh
            one.setAutoDraw(True)
        
        # *nine* updates
        if nine.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nine.frameNStart = frameN  # exact frame index
            nine.tStart = t  # local t and not account for scr refresh
            nine.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nine, 'tStartRefresh')  # time at next scr refresh
            nine.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stage1_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stage1_instructions"-------
    for thisComponent in stage1_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructions_get_right.addData('start_instr1.started', start_instr1.tStartRefresh)
    instructions_get_right.addData('start_instr1.stopped', start_instr1.tStopRefresh)
    instructions_get_right.addData('trident_start.started', trident_start.tStartRefresh)
    instructions_get_right.addData('trident_start.stopped', trident_start.tStopRefresh)
    instructions_get_right.addData('planet_start.started', planet_start.tStartRefresh)
    instructions_get_right.addData('planet_start.stopped', planet_start.tStopRefresh)
    instructions_get_right.addData('instructions_decisionrules.started', instructions_decisionrules.tStartRefresh)
    instructions_get_right.addData('instructions_decisionrules.stopped', instructions_decisionrules.tStopRefresh)
    instructions_get_right.addData('space_continue_instr1.started', space_continue_instr1.tStartRefresh)
    instructions_get_right.addData('space_continue_instr1.stopped', space_continue_instr1.tStopRefresh)
    instructions_get_right.addData('one.started', one.tStartRefresh)
    instructions_get_right.addData('one.stopped', one.tStopRefresh)
    instructions_get_right.addData('nine.started', nine.tStartRefresh)
    instructions_get_right.addData('nine.stopped', nine.tStopRefresh)
    # the Routine "stage1_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stage2_4_instructions"-------
    continueRoutine = True
    # update component parameters for each repeat
    responseleft.keys = []
    responseleft.rt = []
    _responseleft_allKeys = []
    # keep track of which components have finished
    stage2_4_instructionsComponents = [responseleft, text_4]
    for thisComponent in stage2_4_instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stage2_4_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stage2_4_instructions"-------
    while continueRoutine:
        # get current time
        t = stage2_4_instructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stage2_4_instructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *responseleft* updates
        waitOnFlip = False
        if responseleft.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            responseleft.frameNStart = frameN  # exact frame index
            responseleft.tStart = t  # local t and not account for scr refresh
            responseleft.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(responseleft, 'tStartRefresh')  # time at next scr refresh
            responseleft.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(responseleft.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(responseleft.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if responseleft.status == STARTED and not waitOnFlip:
            theseKeys = responseleft.getKeys(keyList=['space'], waitRelease=False)
            _responseleft_allKeys.extend(theseKeys)
            if len(_responseleft_allKeys):
                responseleft.keys = _responseleft_allKeys[-1].name  # just the last key pressed
                responseleft.rt = _responseleft_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stage2_4_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stage2_4_instructions"-------
    for thisComponent in stage2_4_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructions_get_right.addData('text_4.started', text_4.tStartRefresh)
    instructions_get_right.addData('text_4.stopped', text_4.tStopRefresh)
    # the Routine "stage2_4_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practice_loop = data.TrialHandler(nReps=500.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='practice_loop')
    thisExp.addLoop(practice_loop)  # add the loop to the experiment
    thisPractice_loop = practice_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
    if thisPractice_loop != None:
        for paramName in thisPractice_loop:
            exec('{} = thisPractice_loop[paramName]'.format(paramName))
    
    for thisPractice_loop in practice_loop:
        currentLoop = practice_loop
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
        if thisPractice_loop != None:
            for paramName in thisPractice_loop:
                exec('{} = thisPractice_loop[paramName]'.format(paramName))
        
        # set up handler to look after randomisation of conditions etc
        trials_3 = data.TrialHandler(nReps=1.0, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('stage2_4_practice.csv'),
            seed=None, name='trials_3')
        thisExp.addLoop(trials_3)  # add the loop to the experiment
        thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
        if thisTrial_3 != None:
            for paramName in thisTrial_3:
                exec('{} = thisTrial_3[paramName]'.format(paramName))
        
        for thisTrial_3 in trials_3:
            currentLoop = trials_3
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
            if thisTrial_3 != None:
                for paramName in thisTrial_3:
                    exec('{} = thisTrial_3[paramName]'.format(paramName))
            
            # ------Prepare to start Routine "stage_2_4_practice"-------
            continueRoutine = True
            # update component parameters for each repeat
            image_22.setImage('apple.png')
            key_resp_10.keys = []
            key_resp_10.rt = []
            _key_resp_10_allKeys = []
            # keep track of which components have finished
            stage_2_4_practiceComponents = [image_22, key_resp_10, text_40]
            for thisComponent in stage_2_4_practiceComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            stage_2_4_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "stage_2_4_practice"-------
            while continueRoutine:
                # get current time
                t = stage_2_4_practiceClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=stage_2_4_practiceClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_22* updates
                if image_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_22.frameNStart = frameN  # exact frame index
                    image_22.tStart = t  # local t and not account for scr refresh
                    image_22.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_22, 'tStartRefresh')  # time at next scr refresh
                    image_22.setAutoDraw(True)
                
                # *key_resp_10* updates
                waitOnFlip = False
                if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_10.frameNStart = frameN  # exact frame index
                    key_resp_10.tStart = t  # local t and not account for scr refresh
                    key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
                    key_resp_10.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_10.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_10.getKeys(keyList=[1, '1'], waitRelease=False)
                    _key_resp_10_allKeys.extend(theseKeys)
                    if len(_key_resp_10_allKeys):
                        key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
                        key_resp_10.rt = _key_resp_10_allKeys[-1].rt
                        # a response ends the routine
                        continueRoutine = False
                
                # *text_40* updates
                if text_40.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_40.frameNStart = frameN  # exact frame index
                    text_40.tStart = t  # local t and not account for scr refresh
                    text_40.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_40, 'tStartRefresh')  # time at next scr refresh
                    text_40.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in stage_2_4_practiceComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "stage_2_4_practice"-------
            for thisComponent in stage_2_4_practiceComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_3.addData('image_22.started', image_22.tStartRefresh)
            trials_3.addData('image_22.stopped', image_22.tStopRefresh)
            # check responses
            if key_resp_10.keys in ['', [], None]:  # No response was made
                key_resp_10.keys = None
            trials_3.addData('key_resp_10.keys',key_resp_10.keys)
            if key_resp_10.keys != None:  # we had a response
                trials_3.addData('key_resp_10.rt', key_resp_10.rt)
            trials_3.addData('key_resp_10.started', key_resp_10.tStartRefresh)
            trials_3.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
            trials_3.addData('text_40.started', text_40.tStartRefresh)
            trials_3.addData('text_40.stopped', text_40.tStopRefresh)
            # the Routine "stage_2_4_practice" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # ------Prepare to start Routine "stage_2_4_practice_result"-------
            continueRoutine = True
            routineTimer.add(5.800000)
            # update component parameters for each repeat
            image_20.setImage(image_prac1)
            image_12.setImage(image_prac2)
            # keep track of which components have finished
            stage_2_4_practice_resultComponents = [image_20, text_76, image_12, text_77]
            for thisComponent in stage_2_4_practice_resultComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            stage_2_4_practice_resultClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
            frameN = -1
            
            # -------Run Routine "stage_2_4_practice_result"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = stage_2_4_practice_resultClock.getTime()
                tThisFlip = win.getFutureFlipTime(clock=stage_2_4_practice_resultClock)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_20* updates
                if image_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_20.frameNStart = frameN  # exact frame index
                    image_20.tStart = t  # local t and not account for scr refresh
                    image_20.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_20, 'tStartRefresh')  # time at next scr refresh
                    image_20.setAutoDraw(True)
                if image_20.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_20.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        image_20.tStop = t  # not accounting for scr refresh
                        image_20.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(image_20, 'tStopRefresh')  # time at next scr refresh
                        image_20.setAutoDraw(False)
                
                # *text_76* updates
                if text_76.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
                    # keep track of start time/frame for later
                    text_76.frameNStart = frameN  # exact frame index
                    text_76.tStart = t  # local t and not account for scr refresh
                    text_76.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_76, 'tStartRefresh')  # time at next scr refresh
                    text_76.setAutoDraw(True)
                if text_76.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_76.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        text_76.tStop = t  # not accounting for scr refresh
                        text_76.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_76, 'tStopRefresh')  # time at next scr refresh
                        text_76.setAutoDraw(False)
                
                # *image_12* updates
                if image_12.status == NOT_STARTED and tThisFlip >= 3.2-frameTolerance:
                    # keep track of start time/frame for later
                    image_12.frameNStart = frameN  # exact frame index
                    image_12.tStart = t  # local t and not account for scr refresh
                    image_12.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
                    image_12.setAutoDraw(True)
                if image_12.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_12.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        image_12.tStop = t  # not accounting for scr refresh
                        image_12.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(image_12, 'tStopRefresh')  # time at next scr refresh
                        image_12.setAutoDraw(False)
                
                # *text_77* updates
                if text_77.status == NOT_STARTED and tThisFlip >= 4.8-frameTolerance:
                    # keep track of start time/frame for later
                    text_77.frameNStart = frameN  # exact frame index
                    text_77.tStart = t  # local t and not account for scr refresh
                    text_77.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_77, 'tStartRefresh')  # time at next scr refresh
                    text_77.setAutoDraw(True)
                if text_77.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_77.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        text_77.tStop = t  # not accounting for scr refresh
                        text_77.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(text_77, 'tStopRefresh')  # time at next scr refresh
                        text_77.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in stage_2_4_practice_resultComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "stage_2_4_practice_result"-------
            for thisComponent in stage_2_4_practice_resultComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            trials_3.addData('image_20.started', image_20.tStartRefresh)
            trials_3.addData('image_20.stopped', image_20.tStopRefresh)
            trials_3.addData('text_76.started', text_76.tStartRefresh)
            trials_3.addData('text_76.stopped', text_76.tStopRefresh)
            trials_3.addData('image_12.started', image_12.tStartRefresh)
            trials_3.addData('image_12.stopped', image_12.tStopRefresh)
            trials_3.addData('text_77.started', text_77.tStartRefresh)
            trials_3.addData('text_77.stopped', text_77.tStopRefresh)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trials_3'
        
        
        # ------Prepare to start Routine "quiz_practice"-------
        continueRoutine = True
        # update component parameters for each repeat
        tree_2.setImage('tree.png')
        practice_answer.keys = []
        practice_answer.rt = []
        _practice_answer_allKeys = []
        # keep track of which components have finished
        quiz_practiceComponents = [basket_2, fireworks_2, tree_2, text_17, text_21, text_27, practice_answer, text_6]
        for thisComponent in quiz_practiceComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        quiz_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "quiz_practice"-------
        while continueRoutine:
            # get current time
            t = quiz_practiceClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=quiz_practiceClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *basket_2* updates
            if basket_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                basket_2.frameNStart = frameN  # exact frame index
                basket_2.tStart = t  # local t and not account for scr refresh
                basket_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(basket_2, 'tStartRefresh')  # time at next scr refresh
                basket_2.setAutoDraw(True)
            
            # *fireworks_2* updates
            if fireworks_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fireworks_2.frameNStart = frameN  # exact frame index
                fireworks_2.tStart = t  # local t and not account for scr refresh
                fireworks_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fireworks_2, 'tStartRefresh')  # time at next scr refresh
                fireworks_2.setAutoDraw(True)
            
            # *tree_2* updates
            if tree_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tree_2.frameNStart = frameN  # exact frame index
                tree_2.tStart = t  # local t and not account for scr refresh
                tree_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree_2, 'tStartRefresh')  # time at next scr refresh
                tree_2.setAutoDraw(True)
            
            # *text_17* updates
            if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_17.frameNStart = frameN  # exact frame index
                text_17.tStart = t  # local t and not account for scr refresh
                text_17.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
                text_17.setAutoDraw(True)
            
            # *text_21* updates
            if text_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_21.frameNStart = frameN  # exact frame index
                text_21.tStart = t  # local t and not account for scr refresh
                text_21.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_21, 'tStartRefresh')  # time at next scr refresh
                text_21.setAutoDraw(True)
            
            # *text_27* updates
            if text_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_27.frameNStart = frameN  # exact frame index
                text_27.tStart = t  # local t and not account for scr refresh
                text_27.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_27, 'tStartRefresh')  # time at next scr refresh
                text_27.setAutoDraw(True)
            
            # *practice_answer* updates
            waitOnFlip = False
            if practice_answer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practice_answer.frameNStart = frameN  # exact frame index
                practice_answer.tStart = t  # local t and not account for scr refresh
                practice_answer.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_answer, 'tStartRefresh')  # time at next scr refresh
                practice_answer.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(practice_answer.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(practice_answer.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if practice_answer.status == STARTED and not waitOnFlip:
                theseKeys = practice_answer.getKeys(keyList=['a', 'g', 'l'], waitRelease=False)
                _practice_answer_allKeys.extend(theseKeys)
                if len(_practice_answer_allKeys):
                    practice_answer.keys = _practice_answer_allKeys[-1].name  # just the last key pressed
                    practice_answer.rt = _practice_answer_allKeys[-1].rt
                    # was this correct?
                    if (practice_answer.keys == str('a')) or (practice_answer.keys == 'a'):
                        practice_answer.corr = 1
                    else:
                        practice_answer.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_6* updates
            if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_6.frameNStart = frameN  # exact frame index
                text_6.tStart = t  # local t and not account for scr refresh
                text_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                text_6.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in quiz_practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "quiz_practice"-------
        for thisComponent in quiz_practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practice_loop.addData('basket_2.started', basket_2.tStartRefresh)
        practice_loop.addData('basket_2.stopped', basket_2.tStopRefresh)
        practice_loop.addData('fireworks_2.started', fireworks_2.tStartRefresh)
        practice_loop.addData('fireworks_2.stopped', fireworks_2.tStopRefresh)
        practice_loop.addData('tree_2.started', tree_2.tStartRefresh)
        practice_loop.addData('tree_2.stopped', tree_2.tStopRefresh)
        practice_loop.addData('text_17.started', text_17.tStartRefresh)
        practice_loop.addData('text_17.stopped', text_17.tStopRefresh)
        practice_loop.addData('text_21.started', text_21.tStartRefresh)
        practice_loop.addData('text_21.stopped', text_21.tStopRefresh)
        practice_loop.addData('text_27.started', text_27.tStartRefresh)
        practice_loop.addData('text_27.stopped', text_27.tStopRefresh)
        # check responses
        if practice_answer.keys in ['', [], None]:  # No response was made
            practice_answer.keys = None
            # was no response the correct answer?!
            if str('a').lower() == 'none':
               practice_answer.corr = 1;  # correct non-response
            else:
               practice_answer.corr = 0;  # failed to respond (incorrectly)
        # store data for practice_loop (TrialHandler)
        practice_loop.addData('practice_answer.keys',practice_answer.keys)
        practice_loop.addData('practice_answer.corr', practice_answer.corr)
        if practice_answer.keys != None:  # we had a response
            practice_loop.addData('practice_answer.rt', practice_answer.rt)
        practice_loop.addData('practice_answer.started', practice_answer.tStartRefresh)
        practice_loop.addData('practice_answer.stopped', practice_answer.tStopRefresh)
        if practice_answer.corr:
            print('correct answer')
            practice_loop.finished = True
        practice_loop.addData('text_6.started', text_6.tStartRefresh)
        practice_loop.addData('text_6.stopped', text_6.tStopRefresh)
        # the Routine "quiz_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "feedback1"-------
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        if practice_answer.corr:
          msg="Correct!" 
        else:
          msg="Wrong! Re-starting practice"
        text_10.setText(msg)
        # keep track of which components have finished
        feedback1Components = [text_10]
        for thisComponent in feedback1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        feedback1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "feedback1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedback1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=feedback1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_10* updates
            if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_10.frameNStart = frameN  # exact frame index
                text_10.tStart = t  # local t and not account for scr refresh
                text_10.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
                text_10.setAutoDraw(True)
            if text_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_10.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_10.tStop = t  # not accounting for scr refresh
                    text_10.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_10, 'tStopRefresh')  # time at next scr refresh
                    text_10.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedback1"-------
        for thisComponent in feedback1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        practice_loop.addData('text_10.started', text_10.tStartRefresh)
        practice_loop.addData('text_10.stopped', text_10.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 500.0 repeats of 'practice_loop'
    
    
    # ------Prepare to start Routine "memory_quiz"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_23.keys = []
    key_resp_23.rt = []
    _key_resp_23_allKeys = []
    # keep track of which components have finished
    memory_quizComponents = [text_75, key_resp_23]
    for thisComponent in memory_quizComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    memory_quizClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "memory_quiz"-------
    while continueRoutine:
        # get current time
        t = memory_quizClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=memory_quizClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_75* updates
        if text_75.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_75.frameNStart = frameN  # exact frame index
            text_75.tStart = t  # local t and not account for scr refresh
            text_75.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_75, 'tStartRefresh')  # time at next scr refresh
            text_75.setAutoDraw(True)
        
        # *key_resp_23* updates
        waitOnFlip = False
        if key_resp_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_23.frameNStart = frameN  # exact frame index
            key_resp_23.tStart = t  # local t and not account for scr refresh
            key_resp_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_23, 'tStartRefresh')  # time at next scr refresh
            key_resp_23.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_23.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_23.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_23.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_23.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_23_allKeys.extend(theseKeys)
            if len(_key_resp_23_allKeys):
                key_resp_23.keys = _key_resp_23_allKeys[-1].name  # just the last key pressed
                key_resp_23.rt = _key_resp_23_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in memory_quizComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "memory_quiz"-------
    for thisComponent in memory_quizComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructions_get_right.addData('text_75.started', text_75.tStartRefresh)
    instructions_get_right.addData('text_75.stopped', text_75.tStopRefresh)
    # check responses
    if key_resp_23.keys in ['', [], None]:  # No response was made
        key_resp_23.keys = None
    instructions_get_right.addData('key_resp_23.keys',key_resp_23.keys)
    if key_resp_23.keys != None:  # we had a response
        instructions_get_right.addData('key_resp_23.rt', key_resp_23.rt)
    instructions_get_right.addData('key_resp_23.started', key_resp_23.tStartRefresh)
    instructions_get_right.addData('key_resp_23.stopped', key_resp_23.tStopRefresh)
    # the Routine "memory_quiz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "reminder_second_phase"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_22.keys = []
    key_resp_22.rt = []
    _key_resp_22_allKeys = []
    # keep track of which components have finished
    reminder_second_phaseComponents = [text_74, key_resp_22]
    for thisComponent in reminder_second_phaseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    reminder_second_phaseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "reminder_second_phase"-------
    while continueRoutine:
        # get current time
        t = reminder_second_phaseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=reminder_second_phaseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_74* updates
        if text_74.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_74.frameNStart = frameN  # exact frame index
            text_74.tStart = t  # local t and not account for scr refresh
            text_74.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_74, 'tStartRefresh')  # time at next scr refresh
            text_74.setAutoDraw(True)
        
        # *key_resp_22* updates
        waitOnFlip = False
        if key_resp_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_22.frameNStart = frameN  # exact frame index
            key_resp_22.tStart = t  # local t and not account for scr refresh
            key_resp_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_22, 'tStartRefresh')  # time at next scr refresh
            key_resp_22.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_22.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_22.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_22.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_22.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_22_allKeys.extend(theseKeys)
            if len(_key_resp_22_allKeys):
                key_resp_22.keys = _key_resp_22_allKeys[-1].name  # just the last key pressed
                key_resp_22.rt = _key_resp_22_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reminder_second_phaseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "reminder_second_phase"-------
    for thisComponent in reminder_second_phaseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructions_get_right.addData('text_74.started', text_74.tStartRefresh)
    instructions_get_right.addData('text_74.stopped', text_74.tStopRefresh)
    # check responses
    if key_resp_22.keys in ['', [], None]:  # No response was made
        key_resp_22.keys = None
    instructions_get_right.addData('key_resp_22.keys',key_resp_22.keys)
    if key_resp_22.keys != None:  # we had a response
        instructions_get_right.addData('key_resp_22.rt', key_resp_22.rt)
    instructions_get_right.addData('key_resp_22.started', key_resp_22.tStartRefresh)
    instructions_get_right.addData('key_resp_22.stopped', key_resp_22.tStopRefresh)
    # the Routine "reminder_second_phase" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instructions_quiz_1"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_17.keys = []
    key_resp_17.rt = []
    _key_resp_17_allKeys = []
    # keep track of which components have finished
    instructions_quiz_1Components = [text_43, key_resp_17]
    for thisComponent in instructions_quiz_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructions_quiz_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructions_quiz_1"-------
    while continueRoutine:
        # get current time
        t = instructions_quiz_1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructions_quiz_1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_43* updates
        if text_43.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_43.frameNStart = frameN  # exact frame index
            text_43.tStart = t  # local t and not account for scr refresh
            text_43.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_43, 'tStartRefresh')  # time at next scr refresh
            text_43.setAutoDraw(True)
        
        # *key_resp_17* updates
        waitOnFlip = False
        if key_resp_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_17.frameNStart = frameN  # exact frame index
            key_resp_17.tStart = t  # local t and not account for scr refresh
            key_resp_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_17, 'tStartRefresh')  # time at next scr refresh
            key_resp_17.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_17.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_17.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_17.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_17.getKeys(keyList=['a', 'b', 'c', 'd'], waitRelease=False)
            _key_resp_17_allKeys.extend(theseKeys)
            if len(_key_resp_17_allKeys):
                key_resp_17.keys = _key_resp_17_allKeys[-1].name  # just the last key pressed
                key_resp_17.rt = _key_resp_17_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_quiz_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions_quiz_1"-------
    for thisComponent in instructions_quiz_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructions_get_right.addData('text_43.started', text_43.tStartRefresh)
    instructions_get_right.addData('text_43.stopped', text_43.tStopRefresh)
    correct=0
    if key_resp_17.keys=='c':
        correct+=1
    # check responses
    if key_resp_17.keys in ['', [], None]:  # No response was made
        key_resp_17.keys = None
    instructions_get_right.addData('key_resp_17.keys',key_resp_17.keys)
    if key_resp_17.keys != None:  # we had a response
        instructions_get_right.addData('key_resp_17.rt', key_resp_17.rt)
    instructions_get_right.addData('key_resp_17.started', key_resp_17.tStartRefresh)
    instructions_get_right.addData('key_resp_17.stopped', key_resp_17.tStopRefresh)
    # the Routine "instructions_quiz_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instructions_quiz_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_18.keys = []
    key_resp_18.rt = []
    _key_resp_18_allKeys = []
    # keep track of which components have finished
    instructions_quiz_2Components = [text_70, key_resp_18]
    for thisComponent in instructions_quiz_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructions_quiz_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructions_quiz_2"-------
    while continueRoutine:
        # get current time
        t = instructions_quiz_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructions_quiz_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_70* updates
        if text_70.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_70.frameNStart = frameN  # exact frame index
            text_70.tStart = t  # local t and not account for scr refresh
            text_70.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_70, 'tStartRefresh')  # time at next scr refresh
            text_70.setAutoDraw(True)
        
        # *key_resp_18* updates
        waitOnFlip = False
        if key_resp_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_18.frameNStart = frameN  # exact frame index
            key_resp_18.tStart = t  # local t and not account for scr refresh
            key_resp_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
            key_resp_18.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_18.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_18.getKeys(keyList=['a', 'b', 'c', 'd'], waitRelease=False)
            _key_resp_18_allKeys.extend(theseKeys)
            if len(_key_resp_18_allKeys):
                key_resp_18.keys = _key_resp_18_allKeys[-1].name  # just the last key pressed
                key_resp_18.rt = _key_resp_18_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_quiz_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions_quiz_2"-------
    for thisComponent in instructions_quiz_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructions_get_right.addData('text_70.started', text_70.tStartRefresh)
    instructions_get_right.addData('text_70.stopped', text_70.tStopRefresh)
    if key_resp_18.keys=='c':
        correct+=1
    # check responses
    if key_resp_18.keys in ['', [], None]:  # No response was made
        key_resp_18.keys = None
    instructions_get_right.addData('key_resp_18.keys',key_resp_18.keys)
    if key_resp_18.keys != None:  # we had a response
        instructions_get_right.addData('key_resp_18.rt', key_resp_18.rt)
    instructions_get_right.addData('key_resp_18.started', key_resp_18.tStartRefresh)
    instructions_get_right.addData('key_resp_18.stopped', key_resp_18.tStopRefresh)
    # the Routine "instructions_quiz_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instructions_quiz_3"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_19.keys = []
    key_resp_19.rt = []
    _key_resp_19_allKeys = []
    # keep track of which components have finished
    instructions_quiz_3Components = [text_71, key_resp_19]
    for thisComponent in instructions_quiz_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructions_quiz_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructions_quiz_3"-------
    while continueRoutine:
        # get current time
        t = instructions_quiz_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructions_quiz_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_71* updates
        if text_71.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_71.frameNStart = frameN  # exact frame index
            text_71.tStart = t  # local t and not account for scr refresh
            text_71.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_71, 'tStartRefresh')  # time at next scr refresh
            text_71.setAutoDraw(True)
        
        # *key_resp_19* updates
        waitOnFlip = False
        if key_resp_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_19.frameNStart = frameN  # exact frame index
            key_resp_19.tStart = t  # local t and not account for scr refresh
            key_resp_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_19, 'tStartRefresh')  # time at next scr refresh
            key_resp_19.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_19.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_19.getKeys(keyList=['a', 'b', 'c', 'd'], waitRelease=False)
            _key_resp_19_allKeys.extend(theseKeys)
            if len(_key_resp_19_allKeys):
                key_resp_19.keys = _key_resp_19_allKeys[-1].name  # just the last key pressed
                key_resp_19.rt = _key_resp_19_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_quiz_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions_quiz_3"-------
    for thisComponent in instructions_quiz_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructions_get_right.addData('text_71.started', text_71.tStartRefresh)
    instructions_get_right.addData('text_71.stopped', text_71.tStopRefresh)
    if key_resp_19.keys=='b':
        correct+=1
    
    # check responses
    if key_resp_19.keys in ['', [], None]:  # No response was made
        key_resp_19.keys = None
    instructions_get_right.addData('key_resp_19.keys',key_resp_19.keys)
    if key_resp_19.keys != None:  # we had a response
        instructions_get_right.addData('key_resp_19.rt', key_resp_19.rt)
    instructions_get_right.addData('key_resp_19.started', key_resp_19.tStartRefresh)
    instructions_get_right.addData('key_resp_19.stopped', key_resp_19.tStopRefresh)
    # the Routine "instructions_quiz_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "instructions_quiz_4"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_20.keys = []
    key_resp_20.rt = []
    _key_resp_20_allKeys = []
    # keep track of which components have finished
    instructions_quiz_4Components = [text_72, key_resp_20]
    for thisComponent in instructions_quiz_4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instructions_quiz_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instructions_quiz_4"-------
    while continueRoutine:
        # get current time
        t = instructions_quiz_4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instructions_quiz_4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_72* updates
        if text_72.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_72.frameNStart = frameN  # exact frame index
            text_72.tStart = t  # local t and not account for scr refresh
            text_72.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_72, 'tStartRefresh')  # time at next scr refresh
            text_72.setAutoDraw(True)
        
        # *key_resp_20* updates
        waitOnFlip = False
        if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_20.frameNStart = frameN  # exact frame index
            key_resp_20.tStart = t  # local t and not account for scr refresh
            key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
            key_resp_20.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_20.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_20.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_20.getKeys(keyList=['a', 'b', 'c', 'd'], waitRelease=False)
            _key_resp_20_allKeys.extend(theseKeys)
            if len(_key_resp_20_allKeys):
                key_resp_20.keys = _key_resp_20_allKeys[-1].name  # just the last key pressed
                key_resp_20.rt = _key_resp_20_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_quiz_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions_quiz_4"-------
    for thisComponent in instructions_quiz_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructions_get_right.addData('text_72.started', text_72.tStartRefresh)
    instructions_get_right.addData('text_72.stopped', text_72.tStopRefresh)
    if key_resp_20.keys=='b':
        correct+=1
    
    if correct==4:
        instructions_get_right.finished = True
        msg='Correct! You can now move on'
    else:
        msg='Incorrect! You need to repeat the instructions.'
    # check responses
    if key_resp_20.keys in ['', [], None]:  # No response was made
        key_resp_20.keys = None
    instructions_get_right.addData('key_resp_20.keys',key_resp_20.keys)
    if key_resp_20.keys != None:  # we had a response
        instructions_get_right.addData('key_resp_20.rt', key_resp_20.rt)
    instructions_get_right.addData('key_resp_20.started', key_resp_20.tStartRefresh)
    instructions_get_right.addData('key_resp_20.stopped', key_resp_20.tStopRefresh)
    # the Routine "instructions_quiz_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "result_quiz_instructions"-------
    continueRoutine = True
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    result_q_instr.setText(msg)
    # keep track of which components have finished
    result_quiz_instructionsComponents = [result_q_instr]
    for thisComponent in result_quiz_instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    result_quiz_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "result_quiz_instructions"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = result_quiz_instructionsClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=result_quiz_instructionsClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *result_q_instr* updates
        if result_q_instr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            result_q_instr.frameNStart = frameN  # exact frame index
            result_q_instr.tStart = t  # local t and not account for scr refresh
            result_q_instr.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(result_q_instr, 'tStartRefresh')  # time at next scr refresh
            result_q_instr.setAutoDraw(True)
        if result_q_instr.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > result_q_instr.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                result_q_instr.tStop = t  # not accounting for scr refresh
                result_q_instr.frameNStop = frameN  # exact frame index
                win.timeOnFlip(result_q_instr, 'tStopRefresh')  # time at next scr refresh
                result_q_instr.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in result_quiz_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "result_quiz_instructions"-------
    for thisComponent in result_quiz_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    instructions_get_right.addData('result_q_instr.started', result_q_instr.tStartRefresh)
    instructions_get_right.addData('result_q_instr.stopped', result_q_instr.tStopRefresh)
    thisExp.nextEntry()
    
# completed 500.0 repeats of 'instructions_get_right'


# ------Prepare to start Routine "instructions3"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
instructions3Components = [text_7, key_resp_7]
for thisComponent in instructions3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions3"-------
while continueRoutine:
    # get current time
    t = instructions3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions3"-------
for thisComponent in instructions3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
# the Routine "instructions3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('pr_learning_trials_0actions_easier_r2.csv'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # set up handler to look after randomisation of conditions etc
    action_selection = data.TrialHandler(nReps=999.0, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='action_selection')
    thisExp.addLoop(action_selection)  # add the loop to the experiment
    thisAction_selection = action_selection.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisAction_selection.rgb)
    if thisAction_selection != None:
        for paramName in thisAction_selection:
            exec('{} = thisAction_selection[paramName]'.format(paramName))
    
    for thisAction_selection in action_selection:
        currentLoop = action_selection
        # abbreviate parameter names if possible (e.g. rgb = thisAction_selection.rgb)
        if thisAction_selection != None:
            for paramName in thisAction_selection:
                exec('{} = thisAction_selection[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "stage1"-------
        continueRoutine = True
        # update component parameters for each repeat
        click_action.keys = []
        click_action.rt = []
        _click_action_allKeys = []
        planet_start_learning.setImage('planet.png')
        text_3.setText(action1)
        if action1==1:
            text_3.pos = [-0.4,-0.2]
        elif action1==9:
            text_3.pos=[0.4,-0.2]
            
        if trials.thisN%30==0 and trials.thisN!=0:
            learning_reward_goal=learning_reward_goal_list[counter_reward_learning]
            print(learning_reward_goal)
            counter_reward_learning+=1
        # keep track of which components have finished
        stage1Components = [click_action, text_9, trident_start_learning, planet_start_learning, text_3]
        for thisComponent in stage1Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        stage1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "stage1"-------
        while continueRoutine:
            # get current time
            t = stage1Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=stage1Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *click_action* updates
            waitOnFlip = False
            if click_action.status == NOT_STARTED and tThisFlip >= 0.35-frameTolerance:
                # keep track of start time/frame for later
                click_action.frameNStart = frameN  # exact frame index
                click_action.tStart = t  # local t and not account for scr refresh
                click_action.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(click_action, 'tStartRefresh')  # time at next scr refresh
                click_action.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(click_action.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(click_action.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if click_action.status == STARTED and not waitOnFlip:
                theseKeys = click_action.getKeys(keyList=['1', '9'], waitRelease=False)
                _click_action_allKeys.extend(theseKeys)
                if len(_click_action_allKeys):
                    click_action.keys = _click_action_allKeys[0].name  # just the first key pressed
                    click_action.rt = _click_action_allKeys[0].rt
                    # was this correct?
                    if (click_action.keys == str(action1)) or (click_action.keys == action1):
                        click_action.corr = 1
                    else:
                        click_action.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_9* updates
            if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_9.frameNStart = frameN  # exact frame index
                text_9.tStart = t  # local t and not account for scr refresh
                text_9.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
                text_9.setAutoDraw(True)
            
            # *trident_start_learning* updates
            if trident_start_learning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trident_start_learning.frameNStart = frameN  # exact frame index
                trident_start_learning.tStart = t  # local t and not account for scr refresh
                trident_start_learning.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trident_start_learning, 'tStartRefresh')  # time at next scr refresh
                trident_start_learning.setAutoDraw(True)
            
            # *planet_start_learning* updates
            if planet_start_learning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                planet_start_learning.frameNStart = frameN  # exact frame index
                planet_start_learning.tStart = t  # local t and not account for scr refresh
                planet_start_learning.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(planet_start_learning, 'tStartRefresh')  # time at next scr refresh
                planet_start_learning.setAutoDraw(True)
            
            # *text_3* updates
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                text_3.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stage1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "stage1"-------
        for thisComponent in stage1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if click_action.keys in ['', [], None]:  # No response was made
            click_action.keys = None
            # was no response the correct answer?!
            if str(action1).lower() == 'none':
               click_action.corr = 1;  # correct non-response
            else:
               click_action.corr = 0;  # failed to respond (incorrectly)
        # store data for action_selection (TrialHandler)
        action_selection.addData('click_action.keys',click_action.keys)
        action_selection.addData('click_action.corr', click_action.corr)
        if click_action.keys != None:  # we had a response
            action_selection.addData('click_action.rt', click_action.rt)
        action_selection.addData('click_action.started', click_action.tStartRefresh)
        action_selection.addData('click_action.stopped', click_action.tStopRefresh)
        action_selection.addData('text_9.started', text_9.tStartRefresh)
        action_selection.addData('text_9.stopped', text_9.tStopRefresh)
        action_selection.addData('trident_start_learning.started', trident_start_learning.tStartRefresh)
        action_selection.addData('trident_start_learning.stopped', trident_start_learning.tStopRefresh)
        action_selection.addData('planet_start_learning.started', planet_start_learning.tStartRefresh)
        action_selection.addData('planet_start_learning.stopped', planet_start_learning.tStopRefresh)
        action_selection.addData('text_3.started', text_3.tStartRefresh)
        action_selection.addData('text_3.stopped', text_3.tStopRefresh)
        # the Routine "stage1" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "incorrect_answer"-------
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        if click_action.corr:
            msg_incorrect='correct'
            action_selection.finished = True
            continueRoutine=False
            
        else:
            msg_incorrect='You clicked the wrong button! If you click the wrong button 5 times, the game will stop and you will NOT GET PAID because you failed to follow instructions!'
            incorrect_actions+=1
            continueRoutine=True
            if incorrect_actions>4:
                psychoJS.quit()
        incorrect_display.setText(msg_incorrect)
        # keep track of which components have finished
        incorrect_answerComponents = [incorrect_display]
        for thisComponent in incorrect_answerComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        incorrect_answerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "incorrect_answer"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = incorrect_answerClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=incorrect_answerClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *incorrect_display* updates
            if incorrect_display.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                incorrect_display.frameNStart = frameN  # exact frame index
                incorrect_display.tStart = t  # local t and not account for scr refresh
                incorrect_display.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(incorrect_display, 'tStartRefresh')  # time at next scr refresh
                incorrect_display.setAutoDraw(True)
            if incorrect_display.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > incorrect_display.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    incorrect_display.tStop = t  # not accounting for scr refresh
                    incorrect_display.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(incorrect_display, 'tStopRefresh')  # time at next scr refresh
                    incorrect_display.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in incorrect_answerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "incorrect_answer"-------
        for thisComponent in incorrect_answerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        action_selection.addData('incorrect_display.started', incorrect_display.tStartRefresh)
        action_selection.addData('incorrect_display.stopped', incorrect_display.tStopRefresh)
        thisExp.nextEntry()
        
    # completed 999.0 repeats of 'action_selection'
    
    
    # ------Prepare to start Routine "learning_trial_sequence"-------
    continueRoutine = True
    routineTimer.add(7.600000)
    # update component parameters for each repeat
    stage1_learning.setImage(s1_image)
    stage2_learning.setImage(s2_image)
    stage3_learning.setImage(s3_image)
    # keep track of which components have finished
    learning_trial_sequenceComponents = [stage1_learning, text_78, stage2_learning, text_80, stage3_learning]
    for thisComponent in learning_trial_sequenceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learning_trial_sequenceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learning_trial_sequence"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = learning_trial_sequenceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learning_trial_sequenceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stage1_learning* updates
        if stage1_learning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stage1_learning.frameNStart = frameN  # exact frame index
            stage1_learning.tStart = t  # local t and not account for scr refresh
            stage1_learning.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stage1_learning, 'tStartRefresh')  # time at next scr refresh
            stage1_learning.setAutoDraw(True)
        if stage1_learning.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stage1_learning.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                stage1_learning.tStop = t  # not accounting for scr refresh
                stage1_learning.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stage1_learning, 'tStopRefresh')  # time at next scr refresh
                stage1_learning.setAutoDraw(False)
        
        # *text_78* updates
        if text_78.status == NOT_STARTED and tThisFlip >= 2.1-frameTolerance:
            # keep track of start time/frame for later
            text_78.frameNStart = frameN  # exact frame index
            text_78.tStart = t  # local t and not account for scr refresh
            text_78.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_78, 'tStartRefresh')  # time at next scr refresh
            text_78.setAutoDraw(True)
        if text_78.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_78.tStartRefresh + 0.6-frameTolerance:
                # keep track of stop time/frame for later
                text_78.tStop = t  # not accounting for scr refresh
                text_78.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_78, 'tStopRefresh')  # time at next scr refresh
                text_78.setAutoDraw(False)
        
        # *stage2_learning* updates
        if stage2_learning.status == NOT_STARTED and tThisFlip >= 2.8-frameTolerance:
            # keep track of start time/frame for later
            stage2_learning.frameNStart = frameN  # exact frame index
            stage2_learning.tStart = t  # local t and not account for scr refresh
            stage2_learning.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stage2_learning, 'tStartRefresh')  # time at next scr refresh
            stage2_learning.setAutoDraw(True)
        if stage2_learning.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stage2_learning.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                stage2_learning.tStop = t  # not accounting for scr refresh
                stage2_learning.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stage2_learning, 'tStopRefresh')  # time at next scr refresh
                stage2_learning.setAutoDraw(False)
        
        # *text_80* updates
        if text_80.status == NOT_STARTED and tThisFlip >= 4.9-frameTolerance:
            # keep track of start time/frame for later
            text_80.frameNStart = frameN  # exact frame index
            text_80.tStart = t  # local t and not account for scr refresh
            text_80.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_80, 'tStartRefresh')  # time at next scr refresh
            text_80.setAutoDraw(True)
        if text_80.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_80.tStartRefresh + 0.6-frameTolerance:
                # keep track of stop time/frame for later
                text_80.tStop = t  # not accounting for scr refresh
                text_80.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_80, 'tStopRefresh')  # time at next scr refresh
                text_80.setAutoDraw(False)
        
        # *stage3_learning* updates
        if stage3_learning.status == NOT_STARTED and tThisFlip >= 5.6-frameTolerance:
            # keep track of start time/frame for later
            stage3_learning.frameNStart = frameN  # exact frame index
            stage3_learning.tStart = t  # local t and not account for scr refresh
            stage3_learning.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stage3_learning, 'tStartRefresh')  # time at next scr refresh
            stage3_learning.setAutoDraw(True)
        if stage3_learning.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stage3_learning.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                stage3_learning.tStop = t  # not accounting for scr refresh
                stage3_learning.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stage3_learning, 'tStopRefresh')  # time at next scr refresh
                stage3_learning.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learning_trial_sequenceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learning_trial_sequence"-------
    for thisComponent in learning_trial_sequenceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('stage1_learning.started', stage1_learning.tStartRefresh)
    trials.addData('stage1_learning.stopped', stage1_learning.tStopRefresh)
    trials.addData('text_78.started', text_78.tStartRefresh)
    trials.addData('text_78.stopped', text_78.tStopRefresh)
    trials.addData('stage2_learning.started', stage2_learning.tStartRefresh)
    trials.addData('stage2_learning.stopped', stage2_learning.tStopRefresh)
    trials.addData('text_80.started', text_80.tStartRefresh)
    trials.addData('text_80.stopped', text_80.tStopRefresh)
    trials.addData('stage3_learning.started', stage3_learning.tStartRefresh)
    trials.addData('stage3_learning.stopped', stage3_learning.tStopRefresh)
    
    # ------Prepare to start Routine "memory_q"-------
    continueRoutine = True
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    if trials.thisN%30==0:
        continueRoutine=True
    else:
        continueRoutine=False
    
    number_correct=0
    
    # keep track of which components have finished
    memory_qComponents = [text_92]
    for thisComponent in memory_qComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    memory_qClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "memory_q"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = memory_qClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=memory_qClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_92* updates
        if text_92.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_92.frameNStart = frameN  # exact frame index
            text_92.tStart = t  # local t and not account for scr refresh
            text_92.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_92, 'tStartRefresh')  # time at next scr refresh
            text_92.setAutoDraw(True)
        if text_92.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_92.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                text_92.tStop = t  # not accounting for scr refresh
                text_92.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_92, 'tStopRefresh')  # time at next scr refresh
                text_92.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in memory_qComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "memory_q"-------
    for thisComponent in memory_qComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_92.started', text_92.tStartRefresh)
    trials.addData('text_92.stopped', text_92.tStopRefresh)
    
    # ------Prepare to start Routine "prediction4"-------
    continueRoutine = True
    # update component parameters for each repeat
    if trials.thisN%30==0:
        continueRoutine=True
        
    else:
        continueRoutine=False
    
    number_correct=0
    
    picture_reward_goal.setImage(learning_reward_goal)
    resp4.keys = []
    resp4.rt = []
    _resp4_allKeys = []
    # keep track of which components have finished
    prediction4Components = [outcome4, picture_reward_goal, resp4, learning_rew_trident, learning_rew_planet, text_79, text_85]
    for thisComponent in prediction4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    prediction4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "prediction4"-------
    while continueRoutine:
        # get current time
        t = prediction4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=prediction4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *outcome4* updates
        if outcome4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            outcome4.frameNStart = frameN  # exact frame index
            outcome4.tStart = t  # local t and not account for scr refresh
            outcome4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(outcome4, 'tStartRefresh')  # time at next scr refresh
            outcome4.setAutoDraw(True)
        
        # *picture_reward_goal* updates
        if picture_reward_goal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            picture_reward_goal.frameNStart = frameN  # exact frame index
            picture_reward_goal.tStart = t  # local t and not account for scr refresh
            picture_reward_goal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(picture_reward_goal, 'tStartRefresh')  # time at next scr refresh
            picture_reward_goal.setAutoDraw(True)
        
        # *resp4* updates
        waitOnFlip = False
        if resp4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp4.frameNStart = frameN  # exact frame index
            resp4.tStart = t  # local t and not account for scr refresh
            resp4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp4, 'tStartRefresh')  # time at next scr refresh
            resp4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp4.status == STARTED and not waitOnFlip:
            theseKeys = resp4.getKeys(keyList=['1', '9'], waitRelease=False)
            _resp4_allKeys.extend(theseKeys)
            if len(_resp4_allKeys):
                resp4.keys = _resp4_allKeys[-1].name  # just the last key pressed
                resp4.rt = _resp4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *learning_rew_trident* updates
        if learning_rew_trident.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            learning_rew_trident.frameNStart = frameN  # exact frame index
            learning_rew_trident.tStart = t  # local t and not account for scr refresh
            learning_rew_trident.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learning_rew_trident, 'tStartRefresh')  # time at next scr refresh
            learning_rew_trident.setAutoDraw(True)
        
        # *learning_rew_planet* updates
        if learning_rew_planet.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            learning_rew_planet.frameNStart = frameN  # exact frame index
            learning_rew_planet.tStart = t  # local t and not account for scr refresh
            learning_rew_planet.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(learning_rew_planet, 'tStartRefresh')  # time at next scr refresh
            learning_rew_planet.setAutoDraw(True)
        
        # *text_79* updates
        if text_79.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_79.frameNStart = frameN  # exact frame index
            text_79.tStart = t  # local t and not account for scr refresh
            text_79.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_79, 'tStartRefresh')  # time at next scr refresh
            text_79.setAutoDraw(True)
        
        # *text_85* updates
        if text_85.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_85.frameNStart = frameN  # exact frame index
            text_85.tStart = t  # local t and not account for scr refresh
            text_85.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_85, 'tStartRefresh')  # time at next scr refresh
            text_85.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prediction4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prediction4"-------
    for thisComponent in prediction4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('outcome4.started', outcome4.tStartRefresh)
    trials.addData('outcome4.stopped', outcome4.tStopRefresh)
    trials.addData('picture_reward_goal.started', picture_reward_goal.tStartRefresh)
    trials.addData('picture_reward_goal.stopped', picture_reward_goal.tStopRefresh)
    # check responses
    if resp4.keys in ['', [], None]:  # No response was made
        resp4.keys = None
    trials.addData('resp4.keys',resp4.keys)
    if resp4.keys != None:  # we had a response
        trials.addData('resp4.rt', resp4.rt)
    trials.addData('resp4.started', resp4.tStartRefresh)
    trials.addData('resp4.stopped', resp4.tStopRefresh)
    trials.addData('learning_rew_trident.started', learning_rew_trident.tStartRefresh)
    trials.addData('learning_rew_trident.stopped', learning_rew_trident.tStopRefresh)
    trials.addData('learning_rew_planet.started', learning_rew_planet.tStartRefresh)
    trials.addData('learning_rew_planet.stopped', learning_rew_planet.tStopRefresh)
    trials.addData('text_79.started', text_79.tStartRefresh)
    trials.addData('text_79.stopped', text_79.tStopRefresh)
    trials.addData('text_85.started', text_85.tStartRefresh)
    trials.addData('text_85.stopped', text_85.tStopRefresh)
    # the Routine "prediction4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "quiz_score"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if trials.thisN%30==0:
        continueRoutine=True
    else:
        continueRoutine=False
    
    number_correct=0
    
    text_5.setText('You will see the correct score at the end of the game')
    # keep track of which components have finished
    quiz_scoreComponents = [text_5]
    for thisComponent in quiz_scoreComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    quiz_scoreClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "quiz_score"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = quiz_scoreClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=quiz_scoreClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in quiz_scoreComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "quiz_score"-------
    for thisComponent in quiz_scoreComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_5.started', text_5.tStartRefresh)
    trials.addData('text_5.stopped', text_5.tStopRefresh)
    
    # ------Prepare to start Routine "take_a_break"-------
    continueRoutine = True
    routineTimer.add(0.600000)
    # update component parameters for each repeat
    # keep track of which components have finished
    take_a_breakComponents = [text_39]
    for thisComponent in take_a_breakComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    take_a_breakClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "take_a_break"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = take_a_breakClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=take_a_breakClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_39* updates
        if text_39.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_39.frameNStart = frameN  # exact frame index
            text_39.tStart = t  # local t and not account for scr refresh
            text_39.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_39, 'tStartRefresh')  # time at next scr refresh
            text_39.setAutoDraw(True)
        if text_39.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_39.tStartRefresh + 0.6-frameTolerance:
                # keep track of stop time/frame for later
                text_39.tStop = t  # not accounting for scr refresh
                text_39.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_39, 'tStopRefresh')  # time at next scr refresh
                text_39.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in take_a_breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "take_a_break"-------
    for thisComponent in take_a_breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_39.started', text_39.tStartRefresh)
    trials.addData('text_39.stopped', text_39.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "instructions_reward_stage"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_11.keys = []
key_resp_11.rt = []
_key_resp_11_allKeys = []
# keep track of which components have finished
instructions_reward_stageComponents = [instructions_rewardstage, key_resp_11]
for thisComponent in instructions_reward_stageComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions_reward_stageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions_reward_stage"-------
while continueRoutine:
    # get current time
    t = instructions_reward_stageClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions_reward_stageClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructions_rewardstage* updates
    if instructions_rewardstage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructions_rewardstage.frameNStart = frameN  # exact frame index
        instructions_rewardstage.tStart = t  # local t and not account for scr refresh
        instructions_rewardstage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructions_rewardstage, 'tStartRefresh')  # time at next scr refresh
        instructions_rewardstage.setAutoDraw(True)
    
    # *key_resp_11* updates
    waitOnFlip = False
    if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.tStart = t  # local t and not account for scr refresh
        key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_11.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_11.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_11_allKeys.extend(theseKeys)
        if len(_key_resp_11_allKeys):
            key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
            key_resp_11.rt = _key_resp_11_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_reward_stageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions_reward_stage"-------
for thisComponent in instructions_reward_stageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructions_rewardstage.started', instructions_rewardstage.tStartRefresh)
thisExp.addData('instructions_rewardstage.stopped', instructions_rewardstage.tStopRefresh)
# the Routine "instructions_reward_stage" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "i2_reward"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
i2_rewardComponents = [text_42, key_resp_9]
for thisComponent in i2_rewardComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
i2_rewardClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "i2_reward"-------
while continueRoutine:
    # get current time
    t = i2_rewardClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=i2_rewardClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_42* updates
    if text_42.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_42.frameNStart = frameN  # exact frame index
        text_42.tStart = t  # local t and not account for scr refresh
        text_42.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_42, 'tStartRefresh')  # time at next scr refresh
        text_42.setAutoDraw(True)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in i2_rewardComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "i2_reward"-------
for thisComponent in i2_rewardComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_42.started', text_42.tStartRefresh)
thisExp.addData('text_42.stopped', text_42.tStopRefresh)
# the Routine "i2_reward" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practice_view_reward_info"-------
continueRoutine = True
# update component parameters for each repeat
resp4_2.keys = []
resp4_2.rt = []
_resp4_2_allKeys = []
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
practice_view_reward_infoComponents = [im1_example_choicephase, resp4_2, im2_example_choicephase, example_trial_choice_phase, im1_rewvalue, im2_rewvalue, text_28, key_resp_3]
for thisComponent in practice_view_reward_infoComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_view_reward_infoClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_view_reward_info"-------
while continueRoutine:
    # get current time
    t = practice_view_reward_infoClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_view_reward_infoClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *im1_example_choicephase* updates
    if im1_example_choicephase.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        im1_example_choicephase.frameNStart = frameN  # exact frame index
        im1_example_choicephase.tStart = t  # local t and not account for scr refresh
        im1_example_choicephase.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(im1_example_choicephase, 'tStartRefresh')  # time at next scr refresh
        im1_example_choicephase.setAutoDraw(True)
    
    # *resp4_2* updates
    waitOnFlip = False
    if resp4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp4_2.frameNStart = frameN  # exact frame index
        resp4_2.tStart = t  # local t and not account for scr refresh
        resp4_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp4_2, 'tStartRefresh')  # time at next scr refresh
        resp4_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp4_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp4_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp4_2.status == STARTED and not waitOnFlip:
        theseKeys = resp4_2.getKeys(keyList=['space'], waitRelease=False)
        _resp4_2_allKeys.extend(theseKeys)
        if len(_resp4_2_allKeys):
            resp4_2.keys = _resp4_2_allKeys[-1].name  # just the last key pressed
            resp4_2.rt = _resp4_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *im2_example_choicephase* updates
    if im2_example_choicephase.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        im2_example_choicephase.frameNStart = frameN  # exact frame index
        im2_example_choicephase.tStart = t  # local t and not account for scr refresh
        im2_example_choicephase.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(im2_example_choicephase, 'tStartRefresh')  # time at next scr refresh
        im2_example_choicephase.setAutoDraw(True)
    
    # *example_trial_choice_phase* updates
    if example_trial_choice_phase.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        example_trial_choice_phase.frameNStart = frameN  # exact frame index
        example_trial_choice_phase.tStart = t  # local t and not account for scr refresh
        example_trial_choice_phase.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(example_trial_choice_phase, 'tStartRefresh')  # time at next scr refresh
        example_trial_choice_phase.setAutoDraw(True)
    
    # *im1_rewvalue* updates
    if im1_rewvalue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        im1_rewvalue.frameNStart = frameN  # exact frame index
        im1_rewvalue.tStart = t  # local t and not account for scr refresh
        im1_rewvalue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(im1_rewvalue, 'tStartRefresh')  # time at next scr refresh
        im1_rewvalue.setAutoDraw(True)
    
    # *im2_rewvalue* updates
    if im2_rewvalue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        im2_rewvalue.frameNStart = frameN  # exact frame index
        im2_rewvalue.tStart = t  # local t and not account for scr refresh
        im2_rewvalue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(im2_rewvalue, 'tStartRefresh')  # time at next scr refresh
        im2_rewvalue.setAutoDraw(True)
    
    # *text_28* updates
    if text_28.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        text_28.frameNStart = frameN  # exact frame index
        text_28.tStart = t  # local t and not account for scr refresh
        text_28.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_28, 'tStartRefresh')  # time at next scr refresh
        text_28.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_view_reward_infoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_view_reward_info"-------
for thisComponent in practice_view_reward_infoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('im1_example_choicephase.started', im1_example_choicephase.tStartRefresh)
thisExp.addData('im1_example_choicephase.stopped', im1_example_choicephase.tStopRefresh)
thisExp.addData('im2_example_choicephase.started', im2_example_choicephase.tStartRefresh)
thisExp.addData('im2_example_choicephase.stopped', im2_example_choicephase.tStopRefresh)
thisExp.addData('example_trial_choice_phase.started', example_trial_choice_phase.tStartRefresh)
thisExp.addData('example_trial_choice_phase.stopped', example_trial_choice_phase.tStopRefresh)
thisExp.addData('im1_rewvalue.started', im1_rewvalue.tStartRefresh)
thisExp.addData('im1_rewvalue.stopped', im1_rewvalue.tStopRefresh)
thisExp.addData('im2_rewvalue.started', im2_rewvalue.tStartRefresh)
thisExp.addData('im2_rewvalue.stopped', im2_rewvalue.tStopRefresh)
thisExp.addData('text_28.started', text_28.tStartRefresh)
thisExp.addData('text_28.stopped', text_28.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "practice_view_reward_info" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instructions_planning"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_12.keys = []
key_resp_12.rt = []
_key_resp_12_allKeys = []
# keep track of which components have finished
instructions_planningComponents = [text_66, houses_choice_practice, train_choice_practice, key_resp_12, text_24]
for thisComponent in instructions_planningComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions_planningClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions_planning"-------
while continueRoutine:
    # get current time
    t = instructions_planningClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions_planningClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_66* updates
    if text_66.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_66.frameNStart = frameN  # exact frame index
        text_66.tStart = t  # local t and not account for scr refresh
        text_66.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_66, 'tStartRefresh')  # time at next scr refresh
        text_66.setAutoDraw(True)
    
    # *houses_choice_practice* updates
    if houses_choice_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        houses_choice_practice.frameNStart = frameN  # exact frame index
        houses_choice_practice.tStart = t  # local t and not account for scr refresh
        houses_choice_practice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(houses_choice_practice, 'tStartRefresh')  # time at next scr refresh
        houses_choice_practice.setAutoDraw(True)
    
    # *train_choice_practice* updates
    if train_choice_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        train_choice_practice.frameNStart = frameN  # exact frame index
        train_choice_practice.tStart = t  # local t and not account for scr refresh
        train_choice_practice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(train_choice_practice, 'tStartRefresh')  # time at next scr refresh
        train_choice_practice.setAutoDraw(True)
    
    # *key_resp_12* updates
    waitOnFlip = False
    if key_resp_12.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.tStart = t  # local t and not account for scr refresh
        key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_12.getKeys(keyList=['left', 'right', 'space'], waitRelease=False)
        _key_resp_12_allKeys.extend(theseKeys)
        if len(_key_resp_12_allKeys):
            key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
            key_resp_12.rt = _key_resp_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_24* updates
    if text_24.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
        # keep track of start time/frame for later
        text_24.frameNStart = frameN  # exact frame index
        text_24.tStart = t  # local t and not account for scr refresh
        text_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_24, 'tStartRefresh')  # time at next scr refresh
        text_24.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_planningComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions_planning"-------
for thisComponent in instructions_planningComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_66.started', text_66.tStartRefresh)
thisExp.addData('text_66.stopped', text_66.tStopRefresh)
thisExp.addData('houses_choice_practice.started', houses_choice_practice.tStartRefresh)
thisExp.addData('houses_choice_practice.stopped', houses_choice_practice.tStopRefresh)
thisExp.addData('train_choice_practice.started', train_choice_practice.tStartRefresh)
thisExp.addData('train_choice_practice.stopped', train_choice_practice.tStopRefresh)
# check responses
if key_resp_12.keys in ['', [], None]:  # No response was made
    key_resp_12.keys = None
thisExp.addData('key_resp_12.keys',key_resp_12.keys)
if key_resp_12.keys != None:  # we had a response
    thisExp.addData('key_resp_12.rt', key_resp_12.rt)
thisExp.addData('key_resp_12.started', key_resp_12.tStartRefresh)
thisExp.addData('key_resp_12.stopped', key_resp_12.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_24.started', text_24.tStartRefresh)
thisExp.addData('text_24.stopped', text_24.tStopRefresh)
# the Routine "instructions_planning" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "start_planning_trials"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_15.keys = []
key_resp_15.rt = []
_key_resp_15_allKeys = []
# keep track of which components have finished
start_planning_trialsComponents = [text_67, key_resp_15]
for thisComponent in start_planning_trialsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
start_planning_trialsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start_planning_trials"-------
while continueRoutine:
    # get current time
    t = start_planning_trialsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=start_planning_trialsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_67* updates
    if text_67.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_67.frameNStart = frameN  # exact frame index
        text_67.tStart = t  # local t and not account for scr refresh
        text_67.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_67, 'tStartRefresh')  # time at next scr refresh
        text_67.setAutoDraw(True)
    
    # *key_resp_15* updates
    waitOnFlip = False
    if key_resp_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_15.frameNStart = frameN  # exact frame index
        key_resp_15.tStart = t  # local t and not account for scr refresh
        key_resp_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
        key_resp_15.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_15.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_15.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_15_allKeys.extend(theseKeys)
        if len(_key_resp_15_allKeys):
            key_resp_15.keys = _key_resp_15_allKeys[-1].name  # just the last key pressed
            key_resp_15.rt = _key_resp_15_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_planning_trialsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start_planning_trials"-------
for thisComponent in start_planning_trialsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_67.started', text_67.tStartRefresh)
thisExp.addData('text_67.stopped', text_67.tStopRefresh)
# check responses
if key_resp_15.keys in ['', [], None]:  # No response was made
    key_resp_15.keys = None
thisExp.addData('key_resp_15.keys',key_resp_15.keys)
if key_resp_15.keys != None:  # we had a response
    thisExp.addData('key_resp_15.rt', key_resp_15.rt)
thisExp.addData('key_resp_15.started', key_resp_15.tStartRefresh)
thisExp.addData('key_resp_15.stopped', key_resp_15.tStopRefresh)
thisExp.nextEntry()
# the Routine "start_planning_trials" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
PRG_vs_Guessing = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('new_choicephase.xlsx'),
    seed=None, name='PRG_vs_Guessing')
thisExp.addLoop(PRG_vs_Guessing)  # add the loop to the experiment
thisPRG_vs_Guessing = PRG_vs_Guessing.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPRG_vs_Guessing.rgb)
if thisPRG_vs_Guessing != None:
    for paramName in thisPRG_vs_Guessing:
        exec('{} = thisPRG_vs_Guessing[paramName]'.format(paramName))

for thisPRG_vs_Guessing in PRG_vs_Guessing:
    currentLoop = PRG_vs_Guessing
    # abbreviate parameter names if possible (e.g. rgb = thisPRG_vs_Guessing.rgb)
    if thisPRG_vs_Guessing != None:
        for paramName in thisPRG_vs_Guessing:
            exec('{} = thisPRG_vs_Guessing[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "info_choicephase"-------
    continueRoutine = True
    # update component parameters for each repeat
    im1_planning.setImage(r1)
    im2_planning.setImage(r2)
    im1_rewvalue_planning.setText(r1_num)
    im2_rewvalue_planning.setText(r2_num)
    key_resp_24.keys = []
    key_resp_24.rt = []
    _key_resp_24_allKeys = []
    im3_planning.setImage(r3)
    im4_planning.setImage(r4)
    im3_num_planning.setText(r3_num)
    im4_num_planning.setText(r4_num)
    # keep track of which components have finished
    info_choicephaseComponents = [im1_planning, im2_planning, example_trial_choice_phase_2, im1_rewvalue_planning, im2_rewvalue_planning, text_29, key_resp_24, im3_planning, im4_planning, im3_num_planning, im4_num_planning]
    for thisComponent in info_choicephaseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    info_choicephaseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "info_choicephase"-------
    while continueRoutine:
        # get current time
        t = info_choicephaseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=info_choicephaseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *im1_planning* updates
        if im1_planning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im1_planning.frameNStart = frameN  # exact frame index
            im1_planning.tStart = t  # local t and not account for scr refresh
            im1_planning.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im1_planning, 'tStartRefresh')  # time at next scr refresh
            im1_planning.setAutoDraw(True)
        
        # *im2_planning* updates
        if im2_planning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im2_planning.frameNStart = frameN  # exact frame index
            im2_planning.tStart = t  # local t and not account for scr refresh
            im2_planning.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im2_planning, 'tStartRefresh')  # time at next scr refresh
            im2_planning.setAutoDraw(True)
        
        # *example_trial_choice_phase_2* updates
        if example_trial_choice_phase_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            example_trial_choice_phase_2.frameNStart = frameN  # exact frame index
            example_trial_choice_phase_2.tStart = t  # local t and not account for scr refresh
            example_trial_choice_phase_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(example_trial_choice_phase_2, 'tStartRefresh')  # time at next scr refresh
            example_trial_choice_phase_2.setAutoDraw(True)
        
        # *im1_rewvalue_planning* updates
        if im1_rewvalue_planning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im1_rewvalue_planning.frameNStart = frameN  # exact frame index
            im1_rewvalue_planning.tStart = t  # local t and not account for scr refresh
            im1_rewvalue_planning.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im1_rewvalue_planning, 'tStartRefresh')  # time at next scr refresh
            im1_rewvalue_planning.setAutoDraw(True)
        
        # *im2_rewvalue_planning* updates
        if im2_rewvalue_planning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im2_rewvalue_planning.frameNStart = frameN  # exact frame index
            im2_rewvalue_planning.tStart = t  # local t and not account for scr refresh
            im2_rewvalue_planning.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im2_rewvalue_planning, 'tStartRefresh')  # time at next scr refresh
            im2_rewvalue_planning.setAutoDraw(True)
        
        # *text_29* updates
        if text_29.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            text_29.frameNStart = frameN  # exact frame index
            text_29.tStart = t  # local t and not account for scr refresh
            text_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_29, 'tStartRefresh')  # time at next scr refresh
            text_29.setAutoDraw(True)
        
        # *key_resp_24* updates
        waitOnFlip = False
        if key_resp_24.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_24.frameNStart = frameN  # exact frame index
            key_resp_24.tStart = t  # local t and not account for scr refresh
            key_resp_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_24, 'tStartRefresh')  # time at next scr refresh
            key_resp_24.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_24.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_24.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_24.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_24.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_24_allKeys.extend(theseKeys)
            if len(_key_resp_24_allKeys):
                key_resp_24.keys = _key_resp_24_allKeys[-1].name  # just the last key pressed
                key_resp_24.rt = _key_resp_24_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *im3_planning* updates
        if im3_planning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im3_planning.frameNStart = frameN  # exact frame index
            im3_planning.tStart = t  # local t and not account for scr refresh
            im3_planning.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im3_planning, 'tStartRefresh')  # time at next scr refresh
            im3_planning.setAutoDraw(True)
        
        # *im4_planning* updates
        if im4_planning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im4_planning.frameNStart = frameN  # exact frame index
            im4_planning.tStart = t  # local t and not account for scr refresh
            im4_planning.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im4_planning, 'tStartRefresh')  # time at next scr refresh
            im4_planning.setAutoDraw(True)
        
        # *im3_num_planning* updates
        if im3_num_planning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im3_num_planning.frameNStart = frameN  # exact frame index
            im3_num_planning.tStart = t  # local t and not account for scr refresh
            im3_num_planning.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im3_num_planning, 'tStartRefresh')  # time at next scr refresh
            im3_num_planning.setAutoDraw(True)
        
        # *im4_num_planning* updates
        if im4_num_planning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im4_num_planning.frameNStart = frameN  # exact frame index
            im4_num_planning.tStart = t  # local t and not account for scr refresh
            im4_num_planning.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im4_num_planning, 'tStartRefresh')  # time at next scr refresh
            im4_num_planning.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in info_choicephaseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "info_choicephase"-------
    for thisComponent in info_choicephaseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PRG_vs_Guessing.addData('im1_planning.started', im1_planning.tStartRefresh)
    PRG_vs_Guessing.addData('im1_planning.stopped', im1_planning.tStopRefresh)
    PRG_vs_Guessing.addData('im2_planning.started', im2_planning.tStartRefresh)
    PRG_vs_Guessing.addData('im2_planning.stopped', im2_planning.tStopRefresh)
    PRG_vs_Guessing.addData('example_trial_choice_phase_2.started', example_trial_choice_phase_2.tStartRefresh)
    PRG_vs_Guessing.addData('example_trial_choice_phase_2.stopped', example_trial_choice_phase_2.tStopRefresh)
    PRG_vs_Guessing.addData('im1_rewvalue_planning.started', im1_rewvalue_planning.tStartRefresh)
    PRG_vs_Guessing.addData('im1_rewvalue_planning.stopped', im1_rewvalue_planning.tStopRefresh)
    PRG_vs_Guessing.addData('im2_rewvalue_planning.started', im2_rewvalue_planning.tStartRefresh)
    PRG_vs_Guessing.addData('im2_rewvalue_planning.stopped', im2_rewvalue_planning.tStopRefresh)
    PRG_vs_Guessing.addData('text_29.started', text_29.tStartRefresh)
    PRG_vs_Guessing.addData('text_29.stopped', text_29.tStopRefresh)
    # check responses
    if key_resp_24.keys in ['', [], None]:  # No response was made
        key_resp_24.keys = None
    PRG_vs_Guessing.addData('key_resp_24.keys',key_resp_24.keys)
    if key_resp_24.keys != None:  # we had a response
        PRG_vs_Guessing.addData('key_resp_24.rt', key_resp_24.rt)
    PRG_vs_Guessing.addData('key_resp_24.started', key_resp_24.tStartRefresh)
    PRG_vs_Guessing.addData('key_resp_24.stopped', key_resp_24.tStopRefresh)
    PRG_vs_Guessing.addData('im3_planning.started', im3_planning.tStartRefresh)
    PRG_vs_Guessing.addData('im3_planning.stopped', im3_planning.tStopRefresh)
    PRG_vs_Guessing.addData('im4_planning.started', im4_planning.tStartRefresh)
    PRG_vs_Guessing.addData('im4_planning.stopped', im4_planning.tStopRefresh)
    PRG_vs_Guessing.addData('im3_num_planning.started', im3_num_planning.tStartRefresh)
    PRG_vs_Guessing.addData('im3_num_planning.stopped', im3_num_planning.tStopRefresh)
    PRG_vs_Guessing.addData('im4_num_planning.started', im4_num_planning.tStartRefresh)
    PRG_vs_Guessing.addData('im4_num_planning.stopped', im4_num_planning.tStopRefresh)
    # the Routine "info_choicephase" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stage1_choice_enact"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_25.keys = []
    key_resp_25.rt = []
    _key_resp_25_allKeys = []
    # keep track of which components have finished
    stage1_choice_enactComponents = [text_81, trident_choice_2, planet_choice_2, key_resp_25, text_31, text_82]
    for thisComponent in stage1_choice_enactComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stage1_choice_enactClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stage1_choice_enact"-------
    while continueRoutine:
        # get current time
        t = stage1_choice_enactClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stage1_choice_enactClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_81* updates
        if text_81.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_81.frameNStart = frameN  # exact frame index
            text_81.tStart = t  # local t and not account for scr refresh
            text_81.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_81, 'tStartRefresh')  # time at next scr refresh
            text_81.setAutoDraw(True)
        
        # *trident_choice_2* updates
        if trident_choice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trident_choice_2.frameNStart = frameN  # exact frame index
            trident_choice_2.tStart = t  # local t and not account for scr refresh
            trident_choice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trident_choice_2, 'tStartRefresh')  # time at next scr refresh
            trident_choice_2.setAutoDraw(True)
        
        # *planet_choice_2* updates
        if planet_choice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            planet_choice_2.frameNStart = frameN  # exact frame index
            planet_choice_2.tStart = t  # local t and not account for scr refresh
            planet_choice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(planet_choice_2, 'tStartRefresh')  # time at next scr refresh
            planet_choice_2.setAutoDraw(True)
        
        # *key_resp_25* updates
        waitOnFlip = False
        if key_resp_25.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            key_resp_25.frameNStart = frameN  # exact frame index
            key_resp_25.tStart = t  # local t and not account for scr refresh
            key_resp_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_25, 'tStartRefresh')  # time at next scr refresh
            key_resp_25.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_25.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_25.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_25.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_25.getKeys(keyList=['1', '9'], waitRelease=False)
            _key_resp_25_allKeys.extend(theseKeys)
            if len(_key_resp_25_allKeys):
                key_resp_25.keys = _key_resp_25_allKeys[-1].name  # just the last key pressed
                key_resp_25.rt = _key_resp_25_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_31* updates
        if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_31.frameNStart = frameN  # exact frame index
            text_31.tStart = t  # local t and not account for scr refresh
            text_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
            text_31.setAutoDraw(True)
        
        # *text_82* updates
        if text_82.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_82.frameNStart = frameN  # exact frame index
            text_82.tStart = t  # local t and not account for scr refresh
            text_82.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_82, 'tStartRefresh')  # time at next scr refresh
            text_82.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stage1_choice_enactComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stage1_choice_enact"-------
    for thisComponent in stage1_choice_enactComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PRG_vs_Guessing.addData('text_81.started', text_81.tStartRefresh)
    PRG_vs_Guessing.addData('text_81.stopped', text_81.tStopRefresh)
    PRG_vs_Guessing.addData('trident_choice_2.started', trident_choice_2.tStartRefresh)
    PRG_vs_Guessing.addData('trident_choice_2.stopped', trident_choice_2.tStopRefresh)
    PRG_vs_Guessing.addData('planet_choice_2.started', planet_choice_2.tStartRefresh)
    PRG_vs_Guessing.addData('planet_choice_2.stopped', planet_choice_2.tStopRefresh)
    # check responses
    if key_resp_25.keys in ['', [], None]:  # No response was made
        key_resp_25.keys = None
    PRG_vs_Guessing.addData('key_resp_25.keys',key_resp_25.keys)
    if key_resp_25.keys != None:  # we had a response
        PRG_vs_Guessing.addData('key_resp_25.rt', key_resp_25.rt)
    PRG_vs_Guessing.addData('key_resp_25.started', key_resp_25.tStartRefresh)
    PRG_vs_Guessing.addData('key_resp_25.stopped', key_resp_25.tStopRefresh)
    PRG_vs_Guessing.addData('text_31.started', text_31.tStartRefresh)
    PRG_vs_Guessing.addData('text_31.stopped', text_31.tStopRefresh)
    PRG_vs_Guessing.addData('text_82.started', text_82.tStartRefresh)
    PRG_vs_Guessing.addData('text_82.stopped', text_82.tStopRefresh)
    # the Routine "stage1_choice_enact" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "final_stage5"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_16.keys = []
    key_resp_16.rt = []
    _key_resp_16_allKeys = []
    # keep track of which components have finished
    final_stage5Components = [text_68, text_30, key_resp_16]
    for thisComponent in final_stage5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    final_stage5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "final_stage5"-------
    while continueRoutine:
        # get current time
        t = final_stage5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=final_stage5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_68* updates
        if text_68.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_68.frameNStart = frameN  # exact frame index
            text_68.tStart = t  # local t and not account for scr refresh
            text_68.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_68, 'tStartRefresh')  # time at next scr refresh
            text_68.setAutoDraw(True)
        if text_68.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_68.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_68.tStop = t  # not accounting for scr refresh
                text_68.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_68, 'tStopRefresh')  # time at next scr refresh
                text_68.setAutoDraw(False)
        
        # *text_30* updates
        if text_30.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            text_30.frameNStart = frameN  # exact frame index
            text_30.tStart = t  # local t and not account for scr refresh
            text_30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
            text_30.setAutoDraw(True)
        
        # *key_resp_16* updates
        waitOnFlip = False
        if key_resp_16.status == NOT_STARTED and tThisFlip >= 1.75-frameTolerance:
            # keep track of start time/frame for later
            key_resp_16.frameNStart = frameN  # exact frame index
            key_resp_16.tStart = t  # local t and not account for scr refresh
            key_resp_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_16, 'tStartRefresh')  # time at next scr refresh
            key_resp_16.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_16.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_16.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_16.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_16.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_16_allKeys.extend(theseKeys)
            if len(_key_resp_16_allKeys):
                key_resp_16.keys = _key_resp_16_allKeys[-1].name  # just the last key pressed
                key_resp_16.rt = _key_resp_16_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in final_stage5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "final_stage5"-------
    for thisComponent in final_stage5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PRG_vs_Guessing.addData('text_68.started', text_68.tStartRefresh)
    PRG_vs_Guessing.addData('text_68.stopped', text_68.tStopRefresh)
    PRG_vs_Guessing.addData('text_30.started', text_30.tStartRefresh)
    PRG_vs_Guessing.addData('text_30.stopped', text_30.tStopRefresh)
    # the Routine "final_stage5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'PRG_vs_Guessing'


# set up handler to look after randomisation of conditions etc
reward_reval_real = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('choicephase_afterevaluation.xlsx'),
    seed=None, name='reward_reval_real')
thisExp.addLoop(reward_reval_real)  # add the loop to the experiment
thisReward_reval_real = reward_reval_real.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisReward_reval_real.rgb)
if thisReward_reval_real != None:
    for paramName in thisReward_reval_real:
        exec('{} = thisReward_reval_real[paramName]'.format(paramName))

for thisReward_reval_real in reward_reval_real:
    currentLoop = reward_reval_real
    # abbreviate parameter names if possible (e.g. rgb = thisReward_reval_real.rgb)
    if thisReward_reval_real != None:
        for paramName in thisReward_reval_real:
            exec('{} = thisReward_reval_real[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "reward_revaluation_choice"-------
    continueRoutine = True
    # update component parameters for each repeat
    im1_planning_4.setImage(r1)
    im2_planning_4.setImage(r2)
    im1_rewvalue_planning_4.setText(r1_num)
    im2_rewvalue_planning_4.setText(r2_num)
    key_resp_33.keys = []
    key_resp_33.rt = []
    _key_resp_33_allKeys = []
    # keep track of which components have finished
    reward_revaluation_choiceComponents = [im1_planning_4, im2_planning_4, example_trial_choice_phase_6, im1_rewvalue_planning_4, im2_rewvalue_planning_4, text_101, key_resp_33]
    for thisComponent in reward_revaluation_choiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    reward_revaluation_choiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "reward_revaluation_choice"-------
    while continueRoutine:
        # get current time
        t = reward_revaluation_choiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=reward_revaluation_choiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *im1_planning_4* updates
        if im1_planning_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im1_planning_4.frameNStart = frameN  # exact frame index
            im1_planning_4.tStart = t  # local t and not account for scr refresh
            im1_planning_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im1_planning_4, 'tStartRefresh')  # time at next scr refresh
            im1_planning_4.setAutoDraw(True)
        
        # *im2_planning_4* updates
        if im2_planning_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im2_planning_4.frameNStart = frameN  # exact frame index
            im2_planning_4.tStart = t  # local t and not account for scr refresh
            im2_planning_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im2_planning_4, 'tStartRefresh')  # time at next scr refresh
            im2_planning_4.setAutoDraw(True)
        
        # *example_trial_choice_phase_6* updates
        if example_trial_choice_phase_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            example_trial_choice_phase_6.frameNStart = frameN  # exact frame index
            example_trial_choice_phase_6.tStart = t  # local t and not account for scr refresh
            example_trial_choice_phase_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(example_trial_choice_phase_6, 'tStartRefresh')  # time at next scr refresh
            example_trial_choice_phase_6.setAutoDraw(True)
        
        # *im1_rewvalue_planning_4* updates
        if im1_rewvalue_planning_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im1_rewvalue_planning_4.frameNStart = frameN  # exact frame index
            im1_rewvalue_planning_4.tStart = t  # local t and not account for scr refresh
            im1_rewvalue_planning_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im1_rewvalue_planning_4, 'tStartRefresh')  # time at next scr refresh
            im1_rewvalue_planning_4.setAutoDraw(True)
        
        # *im2_rewvalue_planning_4* updates
        if im2_rewvalue_planning_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im2_rewvalue_planning_4.frameNStart = frameN  # exact frame index
            im2_rewvalue_planning_4.tStart = t  # local t and not account for scr refresh
            im2_rewvalue_planning_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im2_rewvalue_planning_4, 'tStartRefresh')  # time at next scr refresh
            im2_rewvalue_planning_4.setAutoDraw(True)
        
        # *text_101* updates
        if text_101.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            text_101.frameNStart = frameN  # exact frame index
            text_101.tStart = t  # local t and not account for scr refresh
            text_101.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_101, 'tStartRefresh')  # time at next scr refresh
            text_101.setAutoDraw(True)
        
        # *key_resp_33* updates
        waitOnFlip = False
        if key_resp_33.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_33.frameNStart = frameN  # exact frame index
            key_resp_33.tStart = t  # local t and not account for scr refresh
            key_resp_33.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_33, 'tStartRefresh')  # time at next scr refresh
            key_resp_33.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_33.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_33.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_33.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_33.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_33_allKeys.extend(theseKeys)
            if len(_key_resp_33_allKeys):
                key_resp_33.keys = _key_resp_33_allKeys[-1].name  # just the last key pressed
                key_resp_33.rt = _key_resp_33_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reward_revaluation_choiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "reward_revaluation_choice"-------
    for thisComponent in reward_revaluation_choiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    reward_reval_real.addData('im1_planning_4.started', im1_planning_4.tStartRefresh)
    reward_reval_real.addData('im1_planning_4.stopped', im1_planning_4.tStopRefresh)
    reward_reval_real.addData('im2_planning_4.started', im2_planning_4.tStartRefresh)
    reward_reval_real.addData('im2_planning_4.stopped', im2_planning_4.tStopRefresh)
    reward_reval_real.addData('example_trial_choice_phase_6.started', example_trial_choice_phase_6.tStartRefresh)
    reward_reval_real.addData('example_trial_choice_phase_6.stopped', example_trial_choice_phase_6.tStopRefresh)
    reward_reval_real.addData('im1_rewvalue_planning_4.started', im1_rewvalue_planning_4.tStartRefresh)
    reward_reval_real.addData('im1_rewvalue_planning_4.stopped', im1_rewvalue_planning_4.tStopRefresh)
    reward_reval_real.addData('im2_rewvalue_planning_4.started', im2_rewvalue_planning_4.tStartRefresh)
    reward_reval_real.addData('im2_rewvalue_planning_4.stopped', im2_rewvalue_planning_4.tStopRefresh)
    reward_reval_real.addData('text_101.started', text_101.tStartRefresh)
    reward_reval_real.addData('text_101.stopped', text_101.tStopRefresh)
    # check responses
    if key_resp_33.keys in ['', [], None]:  # No response was made
        key_resp_33.keys = None
    reward_reval_real.addData('key_resp_33.keys',key_resp_33.keys)
    if key_resp_33.keys != None:  # we had a response
        reward_reval_real.addData('key_resp_33.rt', key_resp_33.rt)
    reward_reval_real.addData('key_resp_33.started', key_resp_33.tStartRefresh)
    reward_reval_real.addData('key_resp_33.stopped', key_resp_33.tStopRefresh)
    # the Routine "reward_revaluation_choice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "reward_reval_choice"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_31.keys = []
    key_resp_31.rt = []
    _key_resp_31_allKeys = []
    # keep track of which components have finished
    reward_reval_choiceComponents = [text_96, trident_choice, planet_choice, key_resp_31, text_97, text_98]
    for thisComponent in reward_reval_choiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    reward_reval_choiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "reward_reval_choice"-------
    while continueRoutine:
        # get current time
        t = reward_reval_choiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=reward_reval_choiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_96* updates
        if text_96.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_96.frameNStart = frameN  # exact frame index
            text_96.tStart = t  # local t and not account for scr refresh
            text_96.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_96, 'tStartRefresh')  # time at next scr refresh
            text_96.setAutoDraw(True)
        
        # *trident_choice* updates
        if trident_choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trident_choice.frameNStart = frameN  # exact frame index
            trident_choice.tStart = t  # local t and not account for scr refresh
            trident_choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trident_choice, 'tStartRefresh')  # time at next scr refresh
            trident_choice.setAutoDraw(True)
        
        # *planet_choice* updates
        if planet_choice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            planet_choice.frameNStart = frameN  # exact frame index
            planet_choice.tStart = t  # local t and not account for scr refresh
            planet_choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(planet_choice, 'tStartRefresh')  # time at next scr refresh
            planet_choice.setAutoDraw(True)
        
        # *key_resp_31* updates
        waitOnFlip = False
        if key_resp_31.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            key_resp_31.frameNStart = frameN  # exact frame index
            key_resp_31.tStart = t  # local t and not account for scr refresh
            key_resp_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_31, 'tStartRefresh')  # time at next scr refresh
            key_resp_31.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_31.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_31.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_31.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_31.getKeys(keyList=['1', '9'], waitRelease=False)
            _key_resp_31_allKeys.extend(theseKeys)
            if len(_key_resp_31_allKeys):
                key_resp_31.keys = _key_resp_31_allKeys[-1].name  # just the last key pressed
                key_resp_31.rt = _key_resp_31_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_97* updates
        if text_97.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_97.frameNStart = frameN  # exact frame index
            text_97.tStart = t  # local t and not account for scr refresh
            text_97.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_97, 'tStartRefresh')  # time at next scr refresh
            text_97.setAutoDraw(True)
        
        # *text_98* updates
        if text_98.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_98.frameNStart = frameN  # exact frame index
            text_98.tStart = t  # local t and not account for scr refresh
            text_98.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_98, 'tStartRefresh')  # time at next scr refresh
            text_98.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reward_reval_choiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "reward_reval_choice"-------
    for thisComponent in reward_reval_choiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    reward_reval_real.addData('text_96.started', text_96.tStartRefresh)
    reward_reval_real.addData('text_96.stopped', text_96.tStopRefresh)
    reward_reval_real.addData('trident_choice.started', trident_choice.tStartRefresh)
    reward_reval_real.addData('trident_choice.stopped', trident_choice.tStopRefresh)
    reward_reval_real.addData('planet_choice.started', planet_choice.tStartRefresh)
    reward_reval_real.addData('planet_choice.stopped', planet_choice.tStopRefresh)
    # check responses
    if key_resp_31.keys in ['', [], None]:  # No response was made
        key_resp_31.keys = None
    reward_reval_real.addData('key_resp_31.keys',key_resp_31.keys)
    if key_resp_31.keys != None:  # we had a response
        reward_reval_real.addData('key_resp_31.rt', key_resp_31.rt)
    reward_reval_real.addData('key_resp_31.started', key_resp_31.tStartRefresh)
    reward_reval_real.addData('key_resp_31.stopped', key_resp_31.tStopRefresh)
    reward_reval_real.addData('text_97.started', text_97.tStartRefresh)
    reward_reval_real.addData('text_97.stopped', text_97.tStopRefresh)
    reward_reval_real.addData('text_98.started', text_98.tStartRefresh)
    reward_reval_real.addData('text_98.stopped', text_98.tStopRefresh)
    # the Routine "reward_reval_choice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "reward_reval_see"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_32.keys = []
    key_resp_32.rt = []
    _key_resp_32_allKeys = []
    # keep track of which components have finished
    reward_reval_seeComponents = [text_99, text_100, key_resp_32]
    for thisComponent in reward_reval_seeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    reward_reval_seeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "reward_reval_see"-------
    while continueRoutine:
        # get current time
        t = reward_reval_seeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=reward_reval_seeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_99* updates
        if text_99.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_99.frameNStart = frameN  # exact frame index
            text_99.tStart = t  # local t and not account for scr refresh
            text_99.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_99, 'tStartRefresh')  # time at next scr refresh
            text_99.setAutoDraw(True)
        if text_99.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_99.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_99.tStop = t  # not accounting for scr refresh
                text_99.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_99, 'tStopRefresh')  # time at next scr refresh
                text_99.setAutoDraw(False)
        
        # *text_100* updates
        if text_100.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            text_100.frameNStart = frameN  # exact frame index
            text_100.tStart = t  # local t and not account for scr refresh
            text_100.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_100, 'tStartRefresh')  # time at next scr refresh
            text_100.setAutoDraw(True)
        
        # *key_resp_32* updates
        waitOnFlip = False
        if key_resp_32.status == NOT_STARTED and tThisFlip >= 1.75-frameTolerance:
            # keep track of start time/frame for later
            key_resp_32.frameNStart = frameN  # exact frame index
            key_resp_32.tStart = t  # local t and not account for scr refresh
            key_resp_32.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_32, 'tStartRefresh')  # time at next scr refresh
            key_resp_32.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_32.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_32.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_32.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_32.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_32_allKeys.extend(theseKeys)
            if len(_key_resp_32_allKeys):
                key_resp_32.keys = _key_resp_32_allKeys[-1].name  # just the last key pressed
                key_resp_32.rt = _key_resp_32_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reward_reval_seeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "reward_reval_see"-------
    for thisComponent in reward_reval_seeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    reward_reval_real.addData('text_99.started', text_99.tStartRefresh)
    reward_reval_real.addData('text_99.stopped', text_99.tStopRefresh)
    reward_reval_real.addData('text_100.started', text_100.tStartRefresh)
    reward_reval_real.addData('text_100.stopped', text_100.tStopRefresh)
    # the Routine "reward_reval_see" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'reward_reval_real'


# ------Prepare to start Routine "transition_revaluation"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
transition_revaluationComponents = [text_25, text_26, key_resp_8, trident_reval, fox_reval, right_arrow, planet_reval, right_arrow2, bell_reval, text_94]
for thisComponent in transition_revaluationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
transition_revaluationClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "transition_revaluation"-------
while continueRoutine:
    # get current time
    t = transition_revaluationClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=transition_revaluationClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_25* updates
    if text_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_25.frameNStart = frameN  # exact frame index
        text_25.tStart = t  # local t and not account for scr refresh
        text_25.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_25, 'tStartRefresh')  # time at next scr refresh
        text_25.setAutoDraw(True)
    
    # *text_26* updates
    if text_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_26.frameNStart = frameN  # exact frame index
        text_26.tStart = t  # local t and not account for scr refresh
        text_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_26, 'tStartRefresh')  # time at next scr refresh
        text_26.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *trident_reval* updates
    if trident_reval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trident_reval.frameNStart = frameN  # exact frame index
        trident_reval.tStart = t  # local t and not account for scr refresh
        trident_reval.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trident_reval, 'tStartRefresh')  # time at next scr refresh
        trident_reval.setAutoDraw(True)
    
    # *fox_reval* updates
    if fox_reval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fox_reval.frameNStart = frameN  # exact frame index
        fox_reval.tStart = t  # local t and not account for scr refresh
        fox_reval.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fox_reval, 'tStartRefresh')  # time at next scr refresh
        fox_reval.setAutoDraw(True)
    
    # *right_arrow* updates
    if right_arrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        right_arrow.frameNStart = frameN  # exact frame index
        right_arrow.tStart = t  # local t and not account for scr refresh
        right_arrow.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(right_arrow, 'tStartRefresh')  # time at next scr refresh
        right_arrow.setAutoDraw(True)
    
    # *planet_reval* updates
    if planet_reval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        planet_reval.frameNStart = frameN  # exact frame index
        planet_reval.tStart = t  # local t and not account for scr refresh
        planet_reval.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(planet_reval, 'tStartRefresh')  # time at next scr refresh
        planet_reval.setAutoDraw(True)
    
    # *right_arrow2* updates
    if right_arrow2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        right_arrow2.frameNStart = frameN  # exact frame index
        right_arrow2.tStart = t  # local t and not account for scr refresh
        right_arrow2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(right_arrow2, 'tStartRefresh')  # time at next scr refresh
        right_arrow2.setAutoDraw(True)
    
    # *bell_reval* updates
    if bell_reval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        bell_reval.frameNStart = frameN  # exact frame index
        bell_reval.tStart = t  # local t and not account for scr refresh
        bell_reval.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(bell_reval, 'tStartRefresh')  # time at next scr refresh
        bell_reval.setAutoDraw(True)
    
    # *text_94* updates
    if text_94.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
        # keep track of start time/frame for later
        text_94.frameNStart = frameN  # exact frame index
        text_94.tStart = t  # local t and not account for scr refresh
        text_94.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_94, 'tStartRefresh')  # time at next scr refresh
        text_94.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in transition_revaluationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "transition_revaluation"-------
for thisComponent in transition_revaluationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_25.started', text_25.tStartRefresh)
thisExp.addData('text_25.stopped', text_25.tStopRefresh)
thisExp.addData('text_26.started', text_26.tStartRefresh)
thisExp.addData('text_26.stopped', text_26.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('trident_reval.started', trident_reval.tStartRefresh)
thisExp.addData('trident_reval.stopped', trident_reval.tStopRefresh)
thisExp.addData('fox_reval.started', fox_reval.tStartRefresh)
thisExp.addData('fox_reval.stopped', fox_reval.tStopRefresh)
thisExp.addData('right_arrow.started', right_arrow.tStartRefresh)
thisExp.addData('right_arrow.stopped', right_arrow.tStopRefresh)
thisExp.addData('planet_reval.started', planet_reval.tStartRefresh)
thisExp.addData('planet_reval.stopped', planet_reval.tStopRefresh)
thisExp.addData('right_arrow2.started', right_arrow2.tStartRefresh)
thisExp.addData('right_arrow2.stopped', right_arrow2.tStopRefresh)
thisExp.addData('bell_reval.started', bell_reval.tStartRefresh)
thisExp.addData('bell_reval.stopped', bell_reval.tStopRefresh)
thisExp.addData('text_94.started', text_94.tStartRefresh)
thisExp.addData('text_94.stopped', text_94.tStopRefresh)
# the Routine "transition_revaluation" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
transition_revaluation_round = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('choicephase_afterevaluation.xlsx'),
    seed=None, name='transition_revaluation_round')
thisExp.addLoop(transition_revaluation_round)  # add the loop to the experiment
thisTransition_revaluation_round = transition_revaluation_round.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTransition_revaluation_round.rgb)
if thisTransition_revaluation_round != None:
    for paramName in thisTransition_revaluation_round:
        exec('{} = thisTransition_revaluation_round[paramName]'.format(paramName))

for thisTransition_revaluation_round in transition_revaluation_round:
    currentLoop = transition_revaluation_round
    # abbreviate parameter names if possible (e.g. rgb = thisTransition_revaluation_round.rgb)
    if thisTransition_revaluation_round != None:
        for paramName in thisTransition_revaluation_round:
            exec('{} = thisTransition_revaluation_round[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "info_choice_revaluation_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    im1_planning_2.setImage(r1)
    im2_planning_2.setImage(r2)
    im1_rewvalue_planning_2.setText(r1_num)
    im2_rewvalue_planning_2.setText(r2_num)
    key_resp_29.keys = []
    key_resp_29.rt = []
    _key_resp_29_allKeys = []
    # keep track of which components have finished
    info_choice_revaluation_2Components = [im1_planning_2, im2_planning_2, example_trial_choice_phase_4, im1_rewvalue_planning_2, im2_rewvalue_planning_2, text_93, key_resp_29]
    for thisComponent in info_choice_revaluation_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    info_choice_revaluation_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "info_choice_revaluation_2"-------
    while continueRoutine:
        # get current time
        t = info_choice_revaluation_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=info_choice_revaluation_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *im1_planning_2* updates
        if im1_planning_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im1_planning_2.frameNStart = frameN  # exact frame index
            im1_planning_2.tStart = t  # local t and not account for scr refresh
            im1_planning_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im1_planning_2, 'tStartRefresh')  # time at next scr refresh
            im1_planning_2.setAutoDraw(True)
        
        # *im2_planning_2* updates
        if im2_planning_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im2_planning_2.frameNStart = frameN  # exact frame index
            im2_planning_2.tStart = t  # local t and not account for scr refresh
            im2_planning_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im2_planning_2, 'tStartRefresh')  # time at next scr refresh
            im2_planning_2.setAutoDraw(True)
        
        # *example_trial_choice_phase_4* updates
        if example_trial_choice_phase_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            example_trial_choice_phase_4.frameNStart = frameN  # exact frame index
            example_trial_choice_phase_4.tStart = t  # local t and not account for scr refresh
            example_trial_choice_phase_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(example_trial_choice_phase_4, 'tStartRefresh')  # time at next scr refresh
            example_trial_choice_phase_4.setAutoDraw(True)
        
        # *im1_rewvalue_planning_2* updates
        if im1_rewvalue_planning_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im1_rewvalue_planning_2.frameNStart = frameN  # exact frame index
            im1_rewvalue_planning_2.tStart = t  # local t and not account for scr refresh
            im1_rewvalue_planning_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im1_rewvalue_planning_2, 'tStartRefresh')  # time at next scr refresh
            im1_rewvalue_planning_2.setAutoDraw(True)
        
        # *im2_rewvalue_planning_2* updates
        if im2_rewvalue_planning_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im2_rewvalue_planning_2.frameNStart = frameN  # exact frame index
            im2_rewvalue_planning_2.tStart = t  # local t and not account for scr refresh
            im2_rewvalue_planning_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im2_rewvalue_planning_2, 'tStartRefresh')  # time at next scr refresh
            im2_rewvalue_planning_2.setAutoDraw(True)
        
        # *text_93* updates
        if text_93.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            text_93.frameNStart = frameN  # exact frame index
            text_93.tStart = t  # local t and not account for scr refresh
            text_93.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_93, 'tStartRefresh')  # time at next scr refresh
            text_93.setAutoDraw(True)
        
        # *key_resp_29* updates
        waitOnFlip = False
        if key_resp_29.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_29.frameNStart = frameN  # exact frame index
            key_resp_29.tStart = t  # local t and not account for scr refresh
            key_resp_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_29, 'tStartRefresh')  # time at next scr refresh
            key_resp_29.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_29.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_29.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_29.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_29.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_29_allKeys.extend(theseKeys)
            if len(_key_resp_29_allKeys):
                key_resp_29.keys = _key_resp_29_allKeys[-1].name  # just the last key pressed
                key_resp_29.rt = _key_resp_29_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in info_choice_revaluation_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "info_choice_revaluation_2"-------
    for thisComponent in info_choice_revaluation_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    transition_revaluation_round.addData('im1_planning_2.started', im1_planning_2.tStartRefresh)
    transition_revaluation_round.addData('im1_planning_2.stopped', im1_planning_2.tStopRefresh)
    transition_revaluation_round.addData('im2_planning_2.started', im2_planning_2.tStartRefresh)
    transition_revaluation_round.addData('im2_planning_2.stopped', im2_planning_2.tStopRefresh)
    transition_revaluation_round.addData('example_trial_choice_phase_4.started', example_trial_choice_phase_4.tStartRefresh)
    transition_revaluation_round.addData('example_trial_choice_phase_4.stopped', example_trial_choice_phase_4.tStopRefresh)
    transition_revaluation_round.addData('im1_rewvalue_planning_2.started', im1_rewvalue_planning_2.tStartRefresh)
    transition_revaluation_round.addData('im1_rewvalue_planning_2.stopped', im1_rewvalue_planning_2.tStopRefresh)
    transition_revaluation_round.addData('im2_rewvalue_planning_2.started', im2_rewvalue_planning_2.tStartRefresh)
    transition_revaluation_round.addData('im2_rewvalue_planning_2.stopped', im2_rewvalue_planning_2.tStopRefresh)
    transition_revaluation_round.addData('text_93.started', text_93.tStartRefresh)
    transition_revaluation_round.addData('text_93.stopped', text_93.tStopRefresh)
    # check responses
    if key_resp_29.keys in ['', [], None]:  # No response was made
        key_resp_29.keys = None
    transition_revaluation_round.addData('key_resp_29.keys',key_resp_29.keys)
    if key_resp_29.keys != None:  # we had a response
        transition_revaluation_round.addData('key_resp_29.rt', key_resp_29.rt)
    transition_revaluation_round.addData('key_resp_29.started', key_resp_29.tStartRefresh)
    transition_revaluation_round.addData('key_resp_29.stopped', key_resp_29.tStopRefresh)
    # the Routine "info_choice_revaluation_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "stage1_choice_enact"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_25.keys = []
    key_resp_25.rt = []
    _key_resp_25_allKeys = []
    # keep track of which components have finished
    stage1_choice_enactComponents = [text_81, trident_choice_2, planet_choice_2, key_resp_25, text_31, text_82]
    for thisComponent in stage1_choice_enactComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    stage1_choice_enactClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "stage1_choice_enact"-------
    while continueRoutine:
        # get current time
        t = stage1_choice_enactClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=stage1_choice_enactClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_81* updates
        if text_81.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_81.frameNStart = frameN  # exact frame index
            text_81.tStart = t  # local t and not account for scr refresh
            text_81.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_81, 'tStartRefresh')  # time at next scr refresh
            text_81.setAutoDraw(True)
        
        # *trident_choice_2* updates
        if trident_choice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trident_choice_2.frameNStart = frameN  # exact frame index
            trident_choice_2.tStart = t  # local t and not account for scr refresh
            trident_choice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trident_choice_2, 'tStartRefresh')  # time at next scr refresh
            trident_choice_2.setAutoDraw(True)
        
        # *planet_choice_2* updates
        if planet_choice_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            planet_choice_2.frameNStart = frameN  # exact frame index
            planet_choice_2.tStart = t  # local t and not account for scr refresh
            planet_choice_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(planet_choice_2, 'tStartRefresh')  # time at next scr refresh
            planet_choice_2.setAutoDraw(True)
        
        # *key_resp_25* updates
        waitOnFlip = False
        if key_resp_25.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            key_resp_25.frameNStart = frameN  # exact frame index
            key_resp_25.tStart = t  # local t and not account for scr refresh
            key_resp_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_25, 'tStartRefresh')  # time at next scr refresh
            key_resp_25.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_25.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_25.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_25.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_25.getKeys(keyList=['1', '9'], waitRelease=False)
            _key_resp_25_allKeys.extend(theseKeys)
            if len(_key_resp_25_allKeys):
                key_resp_25.keys = _key_resp_25_allKeys[-1].name  # just the last key pressed
                key_resp_25.rt = _key_resp_25_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_31* updates
        if text_31.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_31.frameNStart = frameN  # exact frame index
            text_31.tStart = t  # local t and not account for scr refresh
            text_31.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
            text_31.setAutoDraw(True)
        
        # *text_82* updates
        if text_82.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_82.frameNStart = frameN  # exact frame index
            text_82.tStart = t  # local t and not account for scr refresh
            text_82.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_82, 'tStartRefresh')  # time at next scr refresh
            text_82.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stage1_choice_enactComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "stage1_choice_enact"-------
    for thisComponent in stage1_choice_enactComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    transition_revaluation_round.addData('text_81.started', text_81.tStartRefresh)
    transition_revaluation_round.addData('text_81.stopped', text_81.tStopRefresh)
    transition_revaluation_round.addData('trident_choice_2.started', trident_choice_2.tStartRefresh)
    transition_revaluation_round.addData('trident_choice_2.stopped', trident_choice_2.tStopRefresh)
    transition_revaluation_round.addData('planet_choice_2.started', planet_choice_2.tStartRefresh)
    transition_revaluation_round.addData('planet_choice_2.stopped', planet_choice_2.tStopRefresh)
    # check responses
    if key_resp_25.keys in ['', [], None]:  # No response was made
        key_resp_25.keys = None
    transition_revaluation_round.addData('key_resp_25.keys',key_resp_25.keys)
    if key_resp_25.keys != None:  # we had a response
        transition_revaluation_round.addData('key_resp_25.rt', key_resp_25.rt)
    transition_revaluation_round.addData('key_resp_25.started', key_resp_25.tStartRefresh)
    transition_revaluation_round.addData('key_resp_25.stopped', key_resp_25.tStopRefresh)
    transition_revaluation_round.addData('text_31.started', text_31.tStartRefresh)
    transition_revaluation_round.addData('text_31.stopped', text_31.tStopRefresh)
    transition_revaluation_round.addData('text_82.started', text_82.tStartRefresh)
    transition_revaluation_round.addData('text_82.stopped', text_82.tStopRefresh)
    # the Routine "stage1_choice_enact" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "final_stage5"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_16.keys = []
    key_resp_16.rt = []
    _key_resp_16_allKeys = []
    # keep track of which components have finished
    final_stage5Components = [text_68, text_30, key_resp_16]
    for thisComponent in final_stage5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    final_stage5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "final_stage5"-------
    while continueRoutine:
        # get current time
        t = final_stage5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=final_stage5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_68* updates
        if text_68.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_68.frameNStart = frameN  # exact frame index
            text_68.tStart = t  # local t and not account for scr refresh
            text_68.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_68, 'tStartRefresh')  # time at next scr refresh
            text_68.setAutoDraw(True)
        if text_68.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_68.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_68.tStop = t  # not accounting for scr refresh
                text_68.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_68, 'tStopRefresh')  # time at next scr refresh
                text_68.setAutoDraw(False)
        
        # *text_30* updates
        if text_30.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            text_30.frameNStart = frameN  # exact frame index
            text_30.tStart = t  # local t and not account for scr refresh
            text_30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
            text_30.setAutoDraw(True)
        
        # *key_resp_16* updates
        waitOnFlip = False
        if key_resp_16.status == NOT_STARTED and tThisFlip >= 1.75-frameTolerance:
            # keep track of start time/frame for later
            key_resp_16.frameNStart = frameN  # exact frame index
            key_resp_16.tStart = t  # local t and not account for scr refresh
            key_resp_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_16, 'tStartRefresh')  # time at next scr refresh
            key_resp_16.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_16.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_16.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_16.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_16.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_16_allKeys.extend(theseKeys)
            if len(_key_resp_16_allKeys):
                key_resp_16.keys = _key_resp_16_allKeys[-1].name  # just the last key pressed
                key_resp_16.rt = _key_resp_16_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in final_stage5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "final_stage5"-------
    for thisComponent in final_stage5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    transition_revaluation_round.addData('text_68.started', text_68.tStartRefresh)
    transition_revaluation_round.addData('text_68.stopped', text_68.tStopRefresh)
    transition_revaluation_round.addData('text_30.started', text_30.tStartRefresh)
    transition_revaluation_round.addData('text_30.stopped', text_30.tStopRefresh)
    # the Routine "final_stage5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'transition_revaluation_round'


# ------Prepare to start Routine "reward_total"-------
continueRoutine = True
routineTimer.add(2.500000)
# update component parameters for each repeat
# keep track of which components have finished
reward_totalComponents = [text_84]
for thisComponent in reward_totalComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
reward_totalClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "reward_total"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = reward_totalClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=reward_totalClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_84* updates
    if text_84.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_84.frameNStart = frameN  # exact frame index
        text_84.tStart = t  # local t and not account for scr refresh
        text_84.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_84, 'tStartRefresh')  # time at next scr refresh
        text_84.setAutoDraw(True)
    if text_84.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_84.tStartRefresh + 2.5-frameTolerance:
            # keep track of stop time/frame for later
            text_84.tStop = t  # not accounting for scr refresh
            text_84.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_84, 'tStopRefresh')  # time at next scr refresh
            text_84.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in reward_totalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "reward_total"-------
for thisComponent in reward_totalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_84.started', text_84.tStartRefresh)
thisExp.addData('text_84.stopped', text_84.tStopRefresh)

# ------Prepare to start Routine "done"-------
continueRoutine = True
routineTimer.add(6.000000)
# update component parameters for each repeat
# keep track of which components have finished
doneComponents = [text_62]
for thisComponent in doneComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
doneClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "done"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = doneClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=doneClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_62* updates
    if text_62.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_62.frameNStart = frameN  # exact frame index
        text_62.tStart = t  # local t and not account for scr refresh
        text_62.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_62, 'tStartRefresh')  # time at next scr refresh
        text_62.setAutoDraw(True)
    if text_62.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_62.tStartRefresh + 6.0-frameTolerance:
            # keep track of stop time/frame for later
            text_62.tStop = t  # not accounting for scr refresh
            text_62.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_62, 'tStopRefresh')  # time at next scr refresh
            text_62.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in doneComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "done"-------
for thisComponent in doneComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_62.started', text_62.tStartRefresh)
thisExp.addData('text_62.stopped', text_62.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
