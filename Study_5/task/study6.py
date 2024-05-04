#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.5),
    on Sat Aug  5 12:14:52 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.5'
expName = 'PRp_v1'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
# --- Show participant info dialog --
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
    originPath='/Users/paul/Documents_local/study6_pr2/study6.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='imac', color='whitesmoke', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "consent" ---
image_11 = visual.ImageStim(
    win=win,
    name='image_11', 
    image='sin', mask=None, anchor='center',
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

# --- Initialize components for Routine "consent1" ---
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='sin', mask=None, anchor='center',
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

# --- Initialize components for Routine "instructions" ---
text = visual.TextStim(win=win, name='text',
    text='In the task, you learn how to navigate through pictures. Each round, have TWO CHOICES that take you from one picture to another. \n\nIn the first part of this task you must learn how often other pictures tend to appear after starting at an initial picture. For example, you might need to learn how often you see an apple after starting at an image of a tree. \n\nThus, this task requires you to learn probabilities of image transitions. The probability of seeing an apple after a tree might be very different from the probability of seeing the apple after a rock. \n\nAfter this learning phase, you can use this knowledge to plan how to win points in a final phase. Importantly, you can earn money based on these points. You will be instructed later exactly how to win points. \n\nPress Space to continue',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# --- Initialize components for Routine "instruction2" ---
key_resp_2 = keyboard.Keyboard()
text_2 = visual.TextStim(win=win, name='text_2',
    text='PHASE 1: LEARN HOW TO NAVIGATE IN THE PICTURE WORLD\n\nYou will now be instructed which actions to take in the picture world. Your goal is to learn which new picture you will arrive at after selecting a picture by clicking the corresponding number on your keyboard.\n\nNOTE: There will be a SECOND PHASE after this first phase, where you can use what you learned to win even more money!\n\nPress Space to continue',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "stage1_instructions" ---
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
    image='trident.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.10), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
instructions_decisionrules = visual.TextStim(win=win, name='instructions_decisionrules',
    text='The first decision will say “START”. Here will you select the number underneath the starting image to see where it leads you!',
    font='Open Sans',
    pos=(0, 0.40), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
space_continue_instr1 = visual.TextStim(win=win, name='space_continue_instr1',
    text='Press Space to continue',
    font='Open Sans',
    pos=(0, -0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
one = visual.TextStim(win=win, name='one',
    text='1',
    font='Open Sans',
    pos=(0, -0.26), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "stage2_4_instructions" ---
responseleft = keyboard.Keyboard()
text_4 = visual.TextStim(win=win, name='text_4',
    text='After choosing the image, you will take a SECOND ACTION - either clicking A or L on the keyboard. Your goal is to remember which images tend to come after EACH action.\n\nTo show you what this looks like, you will do a practice round. You will be tested to see if you remember which images come after the starting image. Good luck! \n\nPress SPACE to continue',
    font='Open Sans',
    pos=(0, 0.0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "stage_2_4_practice" ---
image_22 = visual.ImageStim(
    win=win,
    name='image_22', 
    image='sin', mask=None, anchor='center',
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

# --- Initialize components for Routine "stage_2_4_practice_result" ---
image_20 = visual.ImageStim(
    win=win,
    name='image_20', 
    image='sin', mask=None, anchor='center',
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
    image='sin', mask=None, anchor='center',
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

# --- Initialize components for Routine "quiz_practice" ---
basket_2 = visual.ImageStim(
    win=win,
    name='basket_2', 
    image='basket.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.6, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
fireworks_2 = visual.ImageStim(
    win=win,
    name='fireworks_2', 
    image='fireworks.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.05), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
tree_2 = visual.ImageStim(
    win=win,
    name='tree_2', 
    image='sin', mask=None, anchor='center',
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

# --- Initialize components for Routine "feedback1" ---
text_10 = visual.TextStim(win=win, name='text_10',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "memory_quiz" ---
text_75 = visual.TextStim(win=win, name='text_75',
    text='When learning about how to get from one picture to another, you will be tested on your learning.\n\nEvery so often, you will be asked to use what you’ve learned to try to reach an image where money is hiding. Each of these questions has a correct answer, and we will reward you at the end of the study based on how well you did on these questions. \n\nSpecifically, we will pick a total of 5 rounds at random from these rounds where you can earn reward to determine how much money you win\n\nPress space to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_23 = keyboard.Keyboard()

# --- Initialize components for Routine "reminder_second_phase" ---
text_74 = visual.TextStim(win=win, name='text_74',
    text='After you complete many rounds of learning how to navigate between pictures in the picture game, you will have a SECOND PHASE where you can earn more money based off what you learned!\n\nIMPORTANT to do well on both phases, it is vital to remember that during training, the image that leads the most times to another image NEVER CHANGES. For example, if in the beginning of the task, the apple image has the best chance to lead to the basket image, it will ALWAYS be the best image to get to the basket image. The probabilities between images are constant throughout the task.\n\nPress space for a quiz on the instructions',
    font='Open Sans',
    pos=(0, 0), height=0.045, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_22 = keyboard.Keyboard()

# --- Initialize components for Routine "instructions_quiz_1" ---
text_43 = visual.TextStim(win=win, name='text_43',
    text='Instructions Quiz\n\n1. What is the goal of the picture game?\n\na.to learn the type of picture\n\nb.to learn the meaning of pictures\n\nc.to learn which pictures you tend to see after making a choice at an image\n\nd.to learn how actions you take at a picture give you rewards or punishments',
    font='Open Sans',
    pos=(0, 0), height=0.038, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_17 = keyboard.Keyboard()

# --- Initialize components for Routine "instructions_quiz_2" ---
text_70 = visual.TextStim(win=win, name='text_70',
    text='Instructions Quiz\n\n1. What happens at the second image you see?\n\na. you cannot select an action \n\nb.these images are new and never repeat\n\nc. you need to learn which image comes after a specific action at the second image.\n\nd. you do not transition to a third image',
    font='Open Sans',
    pos=(0, 0), height=0.038, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_18 = keyboard.Keyboard()

# --- Initialize components for Routine "instructions_quiz_3" ---
text_71 = visual.TextStim(win=win, name='text_71',
    text='Instructions Quiz\n\n1. What happens at the reward quiz?\n\na.you must recall how the pictures look\n\nb. you can use what you learned to reach images with points, which will give you possible bonus money\n\nc. you must recall all impossible image transitions.\n\nd. you cannot receive a bonus',
    font='Open Sans',
    pos=(0, 0), height=0.038, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_19 = keyboard.Keyboard()

# --- Initialize components for Routine "instructions_quiz_4" ---
text_72 = visual.TextStim(win=win, name='text_72',
    text="Instructions Quiz\n\n1. Your goal is to learn the how likely a certain image (e.g., basket) comes after a starting image (e.g., apple). The probabilities that determine transitions between images: \n\na. Change throughout the task, \n\nb. stay the same throughout the task. \n\nc. are impossible to learn\n\nd. are told to you explicitly, so you don't have to learn them\n",
    font='Open Sans',
    pos=(0, 0), height=0.038, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_20 = keyboard.Keyboard()

# --- Initialize components for Routine "result_quiz_instructions" ---
result_q_instr = visual.TextStim(win=win, name='result_q_instr',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "time_limit" ---
text_102 = visual.TextStim(win=win, name='text_102',
    text='Yo have 7 SECONDS to click the key instructed on each trial! If you fail to click in this time 5 times, you will be exited from the game without compensation. In order to avoid this, please make sure to do anything you need to complete now before starting the game, which will take around 60 minutes. Remember, you can earn more money once you start the game, so pay attention! \n\nPress space to continue to learning phase, and good luck!!!',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# --- Initialize components for Routine "instructions3" ---
text_7 = visual.TextStim(win=win, name='text_7',
    text='Press SPACE to start learning!',
    font='Open Sans',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()
# Run 'Begin Experiment' code from code_20
quiz1list=['apple.png','trident.png','fireworks.png','fox.png','bowling.png']
quiz2list=['window.png','bell.png','tree.png','watch.png']
q1left_correct=['1','3','5','2','7']
q1right_correct=['2','4','7','3','8']
q2left_correct=['5','1','6','2']
q2right_correct=['6','3','5','4']

learning_reward_goal_list=['planet.png','planet.png','planet.png','trident.png','trident.png','planet.png','planet.png','trident.png','planet.png','trident.png','trident.png','trident.png','planet.png','planet.png','trident.png','planet.png','planet.png','trident.png']
learning_reward_startingstate_list=[['north.png','hammer.png',3,7],['window.png','apple.png',9,8],['snorkel.png','compass.png',4,6],['apple.png','tophat.png',8,2],['houses.png','snorkel.png',5,4],['north.png','compass.png',3,6],['houses.png','train.png',5,1],['window.png','compass.png',9,6],['train.png','hammer.png',1,7],['snorkel.png','compass.png',4,6],['tophat.png','compass.png',2,6],['houses.png','north.png',5,3],['apple.png','tophat.png',8,2],['houses.png','train.png',5,1],['window.png','hammer.png',9,7],['train.png','apple.png',1,8],['snorkel.png','apple.png',4,8],['hammer.png','window.png',7,9]]
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

trial_learning_num=0


correct_quiz='p'
percent_correct=''
text_correct=''



# --- Initialize components for Routine "stage1" ---
click_action = keyboard.Keyboard()
text_9 = visual.TextStim(win=win, name='text_9',
    text='Press the key that appears below the image:',
    font='Open Sans',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
picture_image = visual.ImageStim(
    win=win,
    name='picture_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(0, -0.25), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "incorrect_answer" ---
incorrect_display = visual.TextStim(win=win, name='incorrect_display',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "learning_trial_sequence" ---
stage2_learning = visual.ImageStim(
    win=win,
    name='stage2_learning', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "stage2_2" ---
click_action_2 = keyboard.Keyboard()
text_78 = visual.TextStim(win=win, name='text_78',
    text='Press A or L in lowercase you see below:',
    font='Open Sans',
    pos=(0, 0.4), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
picture_image_2 = visual.ImageStim(
    win=win,
    name='picture_image_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_80 = visual.TextStim(win=win, name='text_80',
    text='',
    font='Open Sans',
    pos=(0, -0.25), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);

# --- Initialize components for Routine "learning_trial_sequence2" ---
stage2_learning_3 = visual.ImageStim(
    win=win,
    name='stage2_learning_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "memory_q" ---
text_92 = visual.TextStim(win=win, name='text_92',
    text='Memory quiz next. Pay Attention!',
    font='Open Sans',
    pos=(0, 0), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "prediction4" ---
outcome4 = visual.TextStim(win=win, name='outcome4',
    text='Choose the FIRST ACTION to get to goal',
    font='Open Sans',
    pos=(0, 0.36), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
picture_reward_goal = visual.ImageStim(
    win=win,
    name='picture_reward_goal', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.17), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
resp4 = keyboard.Keyboard()
memory_image1 = visual.ImageStim(
    win=win,
    name='memory_image1', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.25, -0.1), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
memory_image2 = visual.ImageStim(
    win=win,
    name='memory_image2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.25, -0.1), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
text_79 = visual.TextStim(win=win, name='text_79',
    text='',
    font='Open Sans',
    pos=(-0.25, -0.3), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
text_85 = visual.TextStim(win=win, name='text_85',
    text='',
    font='Open Sans',
    pos=(0.25, -0.30), height=0.07, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-7.0);

# --- Initialize components for Routine "prediction4_secondaction" ---
outcome4_2 = visual.TextStim(win=win, name='outcome4_2',
    text='enter next action (A or L) to get here:',
    font='Open Sans',
    pos=(0, 0.36), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
picture_reward_goal_2 = visual.ImageStim(
    win=win,
    name='picture_reward_goal_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.17), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
resp4_3 = keyboard.Keyboard()

# --- Initialize components for Routine "quiz_score" ---
text_5 = visual.TextStim(win=win, name='text_5',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.065, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "take_a_break" ---
text_39 = visual.TextStim(win=win, name='text_39',
    text='Next trial…',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "instructions_reward_stage" ---
instructions_rewardstage = visual.TextStim(win=win, name='instructions_rewardstage',
    text='Now use what you learned to get rewards. Each round you will be told if the planet or trident will give you points.\n\nYou will always be shown two images to try to reach either the planet or trident. You must choose the best TWO ACTIONS to get you to the reward. \n\nPress SPACE or MOVE ON in 20 SECONDS',
    font='Open Sans',
    pos=(0, 0), height=0.045, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_11 = keyboard.Keyboard()

# --- Initialize components for Routine "i2_reward" ---
text_42 = visual.TextStim(win=win, name='text_42',
    text='After you select TWO ACTIONS from the starting images try to reach the trident or planet, you will not see any more images aftewards. \n\nThis prevents you from learning anything else at this phase, as you need to use what you already learned to plan accordingly. The computer will simulate which images you reached and calculate your points, but this will not be shown to you. Instead you will be told how many points you won after this phase is over.\n\nPress Space or move on in 15 seconds',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_9 = keyboard.Keyboard()

# --- Initialize components for Routine "i3_reward" ---
text_113 = visual.TextStim(win=win, name='text_113',
    text='When you plan to actions in your head, the first action will be 1 through 9, to select a starting image. Then, depending on where you think you will get to, you will choise A or L to get to the reward image. \n\nBest of luck planning actions!\n\nPress Space or move on in 15 seconds',
    font='Open Sans',
    pos=(0, 0), height=0.035, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_15 = keyboard.Keyboard()

# --- Initialize components for Routine "practice_view_reward_info" ---
im1_example_choicephase = visual.ImageStim(
    win=win,
    name='im1_example_choicephase', 
    image='watch.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.30, 0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
resp4_2 = keyboard.Keyboard()
im2_example_choicephase = visual.ImageStim(
    win=win,
    name='im2_example_choicephase', 
    image='tree.png', mask=None, anchor='center',
    ori=0.0, pos=(0.30, 0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
example_trial_choice_phase = visual.TextStim(win=win, name='example_trial_choice_phase',
    text='What two actions gets you to bottom image?',
    font='Open Sans',
    pos=(0, 0.4), height=0.055, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
im1_rewvalue = visual.TextStim(win=win, name='im1_rewvalue',
    text='Win 100 points!',
    font='Open Sans',
    pos=(0, -0.28), height=0.045, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
text_28 = visual.TextStim(win=win, name='text_28',
    text='Press Space or MOVE ON in 10 seconds',
    font='Open Sans',
    pos=(0, -0.32), height=0.03, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
key_resp_3 = keyboard.Keyboard()
image_19 = visual.ImageStim(
    win=win,
    name='image_19', 
    image='planet.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.15), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)

# --- Initialize components for Routine "instructions_planning" ---
text_66 = visual.TextStim(win=win, name='text_66',
    text='When you have decided how to act after seeing all information, you will enter two action you think will get you to reward. You must select one of the two starting images as your first action:',
    font='Open Sans',
    pos=(0, 0.3), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
houses_choice_practice = visual.ImageStim(
    win=win,
    name='houses_choice_practice', 
    image='watch.png', mask=None, anchor='center',
    ori=0.0, pos=(0.3, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
train_choice_practice = visual.ImageStim(
    win=win,
    name='train_choice_practice', 
    image='tree.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.3, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
text_24 = visual.TextStim(win=win, name='text_24',
    text='Moving on in 7 seconds',
    font='Open Sans',
    pos=(0, -0.35), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);

# --- Initialize components for Routine "start_planning_trials" ---
text_67 = visual.TextStim(win=win, name='text_67',
    text='You are now ready to start the planning task. If you reach certain images, you can win more money! Good luck!\n\nYou have 15 SECONDS TO enter two actions for each question. You must answer all to get credit.\n\n\nMoving on in 10 seconds',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "info_choicephase" ---
im1_planning = visual.ImageStim(
    win=win,
    name='im1_planning', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.20, 0.15), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
im2_planning = visual.ImageStim(
    win=win,
    name='im2_planning', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.20, 0.15), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
example_trial_choice_phase_2 = visual.TextStim(win=win, name='example_trial_choice_phase_2',
    text='Starting at these images, plan 2 acitons to get you to reward below',
    font='Open Sans',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
im1_rewvalue_planning = visual.TextStim(win=win, name='im1_rewvalue_planning',
    text='',
    font='Open Sans',
    pos=(-0.20, 0), height=0.045, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
im2_rewvalue_planning = visual.TextStim(win=win, name='im2_rewvalue_planning',
    text='',
    font='Open Sans',
    pos=(0.20, 0), height=0.045, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
text_29 = visual.TextStim(win=win, name='text_29',
    text='Press Space or move on in 15 seconds',
    font='Open Sans',
    pos=(0, -0.45), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);
key_resp_24 = keyboard.Keyboard()
goal_image = visual.ImageStim(
    win=win,
    name='goal_image', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.12), size=(0.28, 0.28),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
im3_num_planning = visual.TextStim(win=win, name='im3_num_planning',
    text='',
    font='Open Sans',
    pos=(0, -0.30), height=0.045, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);

# --- Initialize components for Routine "stage1_choice_enact" ---
text_81 = visual.TextStim(win=win, name='text_81',
    text='Enter 2 actions: number first then letter',
    font='Open Sans',
    pos=(0, 0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
image1test = visual.ImageStim(
    win=win,
    name='image1test', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.30, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image2test = visual.ImageStim(
    win=win,
    name='image2test', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.3, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
key_resp_25 = keyboard.Keyboard()
text_31 = visual.TextStim(win=win, name='text_31',
    text='',
    font='Open Sans',
    pos=(-0.3, -0.20), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
text_82 = visual.TextStim(win=win, name='text_82',
    text='',
    font='Open Sans',
    pos=(0.3, -0.20), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "stage2_choice_enact" ---
text_110 = visual.TextStim(win=win, name='text_110',
    text='Enter 2 actions: number first then letter',
    font='Open Sans',
    pos=(0, 0.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
image1test_2 = visual.ImageStim(
    win=win,
    name='image1test_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.30, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
image2test_2 = visual.ImageStim(
    win=win,
    name='image2test_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.3, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
key_resp_34 = keyboard.Keyboard()
text_111 = visual.TextStim(win=win, name='text_111',
    text='',
    font='Open Sans',
    pos=(-0.3, -0.20), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
text_112 = visual.TextStim(win=win, name='text_112',
    text='',
    font='Open Sans',
    pos=(0.3, -0.20), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "final_stage5" ---
text_68 = visual.TextStim(win=win, name='text_68',
    text='Computer simulating images to calculate reward…',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_30 = visual.TextStim(win=win, name='text_30',
    text='You will find out your reward total after all this phase is completed.\n\nNext trial begins in 2 seconds.',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "transition_revaluation" ---
text_25 = visual.TextStim(win=win, name='text_25',
    text='BONUS ROUND',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_26 = visual.TextStim(win=win, name='text_26',
    text='The picture world you learned has CHANGED! Now, the TREE leads only to the TRIDENT, and the FOX leads only to the PLANET. Look below and use this new information to win more money next!',
    font='Open Sans',
    pos=(0, 0.20), height=0.04, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_8 = keyboard.Keyboard()
tree_reval = visual.ImageStim(
    win=win,
    name='tree_reval', 
    image='tree.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.2, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)
trident_reval = visual.ImageStim(
    win=win,
    name='trident_reval', 
    image='trident.png', mask=None, anchor='center',
    ori=0.0, pos=(0.2, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-5.0)
right_arrow = visual.ImageStim(
    win=win,
    name='right_arrow', 
    image='right.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.16, 0.16),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-6.0)
fox_reval = visual.ImageStim(
    win=win,
    name='fox_reval', 
    image='fox.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.2, -0.25), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)
right_arrow2 = visual.ImageStim(
    win=win,
    name='right_arrow2', 
    image='right.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.25), size=(0.16, 0.16),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-8.0)
planet_reval = visual.ImageStim(
    win=win,
    name='planet_reval', 
    image='planet.png', mask=None, anchor='center',
    ori=0.0, pos=(0.2, -0.25), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-9.0)
text_94 = visual.TextStim(win=win, name='text_94',
    text='Press Space or move on in 20 seconds',
    font='Open Sans',
    pos=(0, -0.4), height=0.045, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# --- Initialize components for Routine "info_choice_revaluation_2" ---
im1_planning_2 = visual.ImageStim(
    win=win,
    name='im1_planning_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.20, 0.15), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
im2_planning_2 = visual.ImageStim(
    win=win,
    name='im2_planning_2', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.20, 0.15), size=(0.20, 0.20),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
example_trial_choice_phase_4 = visual.TextStim(win=win, name='example_trial_choice_phase_4',
    text='What image gets to the BOTTOM goal more?',
    font='Open Sans',
    pos=(0, 0.35), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
im1_rewvalue_planning_2 = visual.TextStim(win=win, name='im1_rewvalue_planning_2',
    text='',
    font='Open Sans',
    pos=(0, -0.30), height=0.045, wrapWidth=None, ori=0.0, 
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
goal_transition_reval = visual.ImageStim(
    win=win,
    name='goal_transition_reval', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.12), size=(0.28, 0.28),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-7.0)

# --- Initialize components for Routine "choice_transistion_reval" ---
text_105 = visual.TextStim(win=win, name='text_105',
    text='Enter the best first action to take',
    font='Open Sans',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
trident_choice_3 = visual.ImageStim(
    win=win,
    name='trident_choice_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(-0.30, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
planet_choice_3 = visual.ImageStim(
    win=win,
    name='planet_choice_3', 
    image='sin', mask=None, anchor='center',
    ori=0.0, pos=(0.3, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)
transition_reval_choice = keyboard.Keyboard()
text_106 = visual.TextStim(win=win, name='text_106',
    text='',
    font='Open Sans',
    pos=(-0.3, -0.20), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);
text_107 = visual.TextStim(win=win, name='text_107',
    text='',
    font='Open Sans',
    pos=(0.3, -0.20), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-6.0);

# --- Initialize components for Routine "final_stage_Tr" ---
text_103 = visual.TextStim(win=win, name='text_103',
    text='Computer simulating images to calculate reward…',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_104 = visual.TextStim(win=win, name='text_104',
    text='You will find out your reward total after all this phase is completed.\n\nMoving on in 2 seconds',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "reward_total" ---
text_84 = visual.TextStim(win=win, name='text_84',
    text='Congrats! Your bonus points will be calculated soon and delivered to you on Prolific!',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# --- Initialize components for Routine "done" ---
text_62 = visual.TextStim(win=win, name='text_62',
    text='Thank you for participating!\n\nYou will be granted credit on Prolific within the next week.  ',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

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
    
    # --- Prepare to start Routine "consent" ---
    continueRoutine = True
    routineForceEnded = False
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
    frameN = -1
    
    # --- Run Routine "consent" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_11.started')
            image_11.setAutoDraw(True)
        
        # *consent1_next* updates
        waitOnFlip = False
        if consent1_next.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            consent1_next.frameNStart = frameN  # exact frame index
            consent1_next.tStart = t  # local t and not account for scr refresh
            consent1_next.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(consent1_next, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'consent1_next.started')
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_89.started')
            text_89.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in consentComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "consent" ---
    for thisComponent in consentComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if consent1_next.keys in ['', [], None]:  # No response was made
        consent1_next.keys = None
    instructions_get_right.addData('consent1_next.keys',consent1_next.keys)
    if consent1_next.keys != None:  # we had a response
        instructions_get_right.addData('consent1_next.rt', consent1_next.rt)
    # the Routine "consent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "consent1" ---
    continueRoutine = True
    routineForceEnded = False
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
    frameN = -1
    
    # --- Run Routine "consent1" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_13.started')
            image_13.setAutoDraw(True)
        
        # *consent1_next_2* updates
        waitOnFlip = False
        if consent1_next_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            consent1_next_2.frameNStart = frameN  # exact frame index
            consent1_next_2.tStart = t  # local t and not account for scr refresh
            consent1_next_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(consent1_next_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'consent1_next_2.started')
            consent1_next_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(consent1_next_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(consent1_next_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if consent1_next_2.status == STARTED and not waitOnFlip:
            theseKeys = consent1_next_2.getKeys(keyList=['y','n'], waitRelease=False)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_90.started')
            text_90.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in consent1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "consent1" ---
    for thisComponent in consent1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if consent1_next_2.keys in ['', [], None]:  # No response was made
        consent1_next_2.keys = None
    instructions_get_right.addData('consent1_next_2.keys',consent1_next_2.keys)
    if consent1_next_2.keys != None:  # we had a response
        instructions_get_right.addData('consent1_next_2.rt', consent1_next_2.rt)
    # Run 'End Routine' code from code_19
    if consent1_next_2.keys=='n':
        psychoJS.quit()
    # the Routine "consent1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions" ---
    continueRoutine = True
    routineForceEnded = False
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
    frameN = -1
    
    # --- Run Routine "instructions" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            text.setAutoDraw(True)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
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
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions" ---
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instruction2" ---
    continueRoutine = True
    routineForceEnded = False
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
    frameN = -1
    
    # --- Run Routine "instruction2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_2.started')
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_2.started')
            text_2.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instruction2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction2" ---
    for thisComponent in instruction2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instruction2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "stage1_instructions" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    keyboard_entry_instr1.keys = []
    keyboard_entry_instr1.rt = []
    _keyboard_entry_instr1_allKeys = []
    # keep track of which components have finished
    stage1_instructionsComponents = [keyboard_entry_instr1, start_instr1, trident_start, instructions_decisionrules, space_continue_instr1, one]
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
    frameN = -1
    
    # --- Run Routine "stage1_instructions" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'keyboard_entry_instr1.started')
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'start_instr1.started')
            start_instr1.setAutoDraw(True)
        
        # *trident_start* updates
        if trident_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trident_start.frameNStart = frameN  # exact frame index
            trident_start.tStart = t  # local t and not account for scr refresh
            trident_start.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trident_start, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trident_start.started')
            trident_start.setAutoDraw(True)
        
        # *instructions_decisionrules* updates
        if instructions_decisionrules.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_decisionrules.frameNStart = frameN  # exact frame index
            instructions_decisionrules.tStart = t  # local t and not account for scr refresh
            instructions_decisionrules.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_decisionrules, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instructions_decisionrules.started')
            instructions_decisionrules.setAutoDraw(True)
        
        # *space_continue_instr1* updates
        if space_continue_instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            space_continue_instr1.frameNStart = frameN  # exact frame index
            space_continue_instr1.tStart = t  # local t and not account for scr refresh
            space_continue_instr1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(space_continue_instr1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'space_continue_instr1.started')
            space_continue_instr1.setAutoDraw(True)
        
        # *one* updates
        if one.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            one.frameNStart = frameN  # exact frame index
            one.tStart = t  # local t and not account for scr refresh
            one.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(one, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'one.started')
            one.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stage1_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "stage1_instructions" ---
    for thisComponent in stage1_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "stage1_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "stage2_4_instructions" ---
    continueRoutine = True
    routineForceEnded = False
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
    frameN = -1
    
    # --- Run Routine "stage2_4_instructions" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'responseleft.started')
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_4.started')
            text_4.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stage2_4_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "stage2_4_instructions" ---
    for thisComponent in stage2_4_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
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
            
            # --- Prepare to start Routine "stage_2_4_practice" ---
            continueRoutine = True
            routineForceEnded = False
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
            frameN = -1
            
            # --- Run Routine "stage_2_4_practice" ---
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_22.started')
                    image_22.setAutoDraw(True)
                
                # *key_resp_10* updates
                waitOnFlip = False
                if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_10.frameNStart = frameN  # exact frame index
                    key_resp_10.tStart = t  # local t and not account for scr refresh
                    key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_10.started')
                    key_resp_10.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp_10.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_10.getKeys(keyList=[1,'1'], waitRelease=False)
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
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_40.started')
                    text_40.setAutoDraw(True)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in stage_2_4_practiceComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "stage_2_4_practice" ---
            for thisComponent in stage_2_4_practiceComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # check responses
            if key_resp_10.keys in ['', [], None]:  # No response was made
                key_resp_10.keys = None
            trials_3.addData('key_resp_10.keys',key_resp_10.keys)
            if key_resp_10.keys != None:  # we had a response
                trials_3.addData('key_resp_10.rt', key_resp_10.rt)
            # the Routine "stage_2_4_practice" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "stage_2_4_practice_result" ---
            continueRoutine = True
            routineForceEnded = False
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
            frameN = -1
            
            # --- Run Routine "stage_2_4_practice_result" ---
            while continueRoutine and routineTimer.getTime() < 5.8:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_20.started')
                    image_20.setAutoDraw(True)
                if image_20.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_20.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        image_20.tStop = t  # not accounting for scr refresh
                        image_20.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_20.stopped')
                        image_20.setAutoDraw(False)
                
                # *text_76* updates
                if text_76.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
                    # keep track of start time/frame for later
                    text_76.frameNStart = frameN  # exact frame index
                    text_76.tStart = t  # local t and not account for scr refresh
                    text_76.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_76, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_76.started')
                    text_76.setAutoDraw(True)
                if text_76.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_76.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        text_76.tStop = t  # not accounting for scr refresh
                        text_76.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_76.stopped')
                        text_76.setAutoDraw(False)
                
                # *image_12* updates
                if image_12.status == NOT_STARTED and tThisFlip >= 3.2-frameTolerance:
                    # keep track of start time/frame for later
                    image_12.frameNStart = frameN  # exact frame index
                    image_12.tStart = t  # local t and not account for scr refresh
                    image_12.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_12.started')
                    image_12.setAutoDraw(True)
                if image_12.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_12.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        image_12.tStop = t  # not accounting for scr refresh
                        image_12.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_12.stopped')
                        image_12.setAutoDraw(False)
                
                # *text_77* updates
                if text_77.status == NOT_STARTED and tThisFlip >= 4.8-frameTolerance:
                    # keep track of start time/frame for later
                    text_77.frameNStart = frameN  # exact frame index
                    text_77.tStart = t  # local t and not account for scr refresh
                    text_77.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_77, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_77.started')
                    text_77.setAutoDraw(True)
                if text_77.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_77.tStartRefresh + 1.0-frameTolerance:
                        # keep track of stop time/frame for later
                        text_77.tStop = t  # not accounting for scr refresh
                        text_77.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_77.stopped')
                        text_77.setAutoDraw(False)
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in stage_2_4_practice_resultComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "stage_2_4_practice_result" ---
            for thisComponent in stage_2_4_practice_resultComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-5.800000)
            thisExp.nextEntry()
            
        # completed 1.0 repeats of 'trials_3'
        
        
        # --- Prepare to start Routine "quiz_practice" ---
        continueRoutine = True
        routineForceEnded = False
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
        frameN = -1
        
        # --- Run Routine "quiz_practice" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'basket_2.started')
                basket_2.setAutoDraw(True)
            
            # *fireworks_2* updates
            if fireworks_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fireworks_2.frameNStart = frameN  # exact frame index
                fireworks_2.tStart = t  # local t and not account for scr refresh
                fireworks_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fireworks_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'fireworks_2.started')
                fireworks_2.setAutoDraw(True)
            
            # *tree_2* updates
            if tree_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                tree_2.frameNStart = frameN  # exact frame index
                tree_2.tStart = t  # local t and not account for scr refresh
                tree_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(tree_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'tree_2.started')
                tree_2.setAutoDraw(True)
            
            # *text_17* updates
            if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_17.frameNStart = frameN  # exact frame index
                text_17.tStart = t  # local t and not account for scr refresh
                text_17.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_17.started')
                text_17.setAutoDraw(True)
            
            # *text_21* updates
            if text_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_21.frameNStart = frameN  # exact frame index
                text_21.tStart = t  # local t and not account for scr refresh
                text_21.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_21, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_21.started')
                text_21.setAutoDraw(True)
            
            # *text_27* updates
            if text_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_27.frameNStart = frameN  # exact frame index
                text_27.tStart = t  # local t and not account for scr refresh
                text_27.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_27, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_27.started')
                text_27.setAutoDraw(True)
            
            # *practice_answer* updates
            waitOnFlip = False
            if practice_answer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                practice_answer.frameNStart = frameN  # exact frame index
                practice_answer.tStart = t  # local t and not account for scr refresh
                practice_answer.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(practice_answer, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'practice_answer.started')
                practice_answer.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(practice_answer.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(practice_answer.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if practice_answer.status == STARTED and not waitOnFlip:
                theseKeys = practice_answer.getKeys(keyList=['a','g','l'], waitRelease=False)
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_6.started')
                text_6.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in quiz_practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "quiz_practice" ---
        for thisComponent in quiz_practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
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
        # Run 'End Routine' code from code_21
        if practice_answer.corr:
            print('correct answer')
            practice_loop.finished = True
        # the Routine "quiz_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback1" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
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
        frameN = -1
        
        # --- Run Routine "feedback1" ---
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_10.started')
                text_10.setAutoDraw(True)
            if text_10.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_10.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    text_10.tStop = t  # not accounting for scr refresh
                    text_10.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_10.stopped')
                    text_10.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedback1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback1" ---
        for thisComponent in feedback1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        thisExp.nextEntry()
        
    # completed 500.0 repeats of 'practice_loop'
    
    
    # --- Prepare to start Routine "memory_quiz" ---
    continueRoutine = True
    routineForceEnded = False
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
    frameN = -1
    
    # --- Run Routine "memory_quiz" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_75.started')
            text_75.setAutoDraw(True)
        
        # *key_resp_23* updates
        waitOnFlip = False
        if key_resp_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_23.frameNStart = frameN  # exact frame index
            key_resp_23.tStart = t  # local t and not account for scr refresh
            key_resp_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_23, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_23.started')
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
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in memory_quizComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "memory_quiz" ---
    for thisComponent in memory_quizComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_23.keys in ['', [], None]:  # No response was made
        key_resp_23.keys = None
    instructions_get_right.addData('key_resp_23.keys',key_resp_23.keys)
    if key_resp_23.keys != None:  # we had a response
        instructions_get_right.addData('key_resp_23.rt', key_resp_23.rt)
    # the Routine "memory_quiz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "reminder_second_phase" ---
    continueRoutine = True
    routineForceEnded = False
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
    frameN = -1
    
    # --- Run Routine "reminder_second_phase" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_74.started')
            text_74.setAutoDraw(True)
        
        # *key_resp_22* updates
        waitOnFlip = False
        if key_resp_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_22.frameNStart = frameN  # exact frame index
            key_resp_22.tStart = t  # local t and not account for scr refresh
            key_resp_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_22, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_22.started')
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
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in reminder_second_phaseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "reminder_second_phase" ---
    for thisComponent in reminder_second_phaseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_22.keys in ['', [], None]:  # No response was made
        key_resp_22.keys = None
    instructions_get_right.addData('key_resp_22.keys',key_resp_22.keys)
    if key_resp_22.keys != None:  # we had a response
        instructions_get_right.addData('key_resp_22.rt', key_resp_22.rt)
    # the Routine "reminder_second_phase" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions_quiz_1" ---
    continueRoutine = True
    routineForceEnded = False
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
    frameN = -1
    
    # --- Run Routine "instructions_quiz_1" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_43.started')
            text_43.setAutoDraw(True)
        
        # *key_resp_17* updates
        waitOnFlip = False
        if key_resp_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_17.frameNStart = frameN  # exact frame index
            key_resp_17.tStart = t  # local t and not account for scr refresh
            key_resp_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_17, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_17.started')
            key_resp_17.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_17.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_17.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_17.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_17.getKeys(keyList=['a','b','c','d'], waitRelease=False)
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
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_quiz_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_quiz_1" ---
    for thisComponent in instructions_quiz_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_27
    correct=0
    if key_resp_17.keys=='c':
        correct+=1
    # check responses
    if key_resp_17.keys in ['', [], None]:  # No response was made
        key_resp_17.keys = None
    instructions_get_right.addData('key_resp_17.keys',key_resp_17.keys)
    if key_resp_17.keys != None:  # we had a response
        instructions_get_right.addData('key_resp_17.rt', key_resp_17.rt)
    # the Routine "instructions_quiz_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions_quiz_2" ---
    continueRoutine = True
    routineForceEnded = False
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
    frameN = -1
    
    # --- Run Routine "instructions_quiz_2" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_70.started')
            text_70.setAutoDraw(True)
        
        # *key_resp_18* updates
        waitOnFlip = False
        if key_resp_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_18.frameNStart = frameN  # exact frame index
            key_resp_18.tStart = t  # local t and not account for scr refresh
            key_resp_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_18.started')
            key_resp_18.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_18.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_18.getKeys(keyList=['a','b','c','d'], waitRelease=False)
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
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_quiz_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_quiz_2" ---
    for thisComponent in instructions_quiz_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_30
    if key_resp_18.keys=='c':
        correct+=1
    # check responses
    if key_resp_18.keys in ['', [], None]:  # No response was made
        key_resp_18.keys = None
    instructions_get_right.addData('key_resp_18.keys',key_resp_18.keys)
    if key_resp_18.keys != None:  # we had a response
        instructions_get_right.addData('key_resp_18.rt', key_resp_18.rt)
    # the Routine "instructions_quiz_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions_quiz_3" ---
    continueRoutine = True
    routineForceEnded = False
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
    frameN = -1
    
    # --- Run Routine "instructions_quiz_3" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_71.started')
            text_71.setAutoDraw(True)
        
        # *key_resp_19* updates
        waitOnFlip = False
        if key_resp_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_19.frameNStart = frameN  # exact frame index
            key_resp_19.tStart = t  # local t and not account for scr refresh
            key_resp_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_19, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_19.started')
            key_resp_19.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_19.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_19.getKeys(keyList=['a','b','c','d'], waitRelease=False)
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
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_quiz_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_quiz_3" ---
    for thisComponent in instructions_quiz_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_31
    if key_resp_19.keys=='b':
        correct+=1
    
    # check responses
    if key_resp_19.keys in ['', [], None]:  # No response was made
        key_resp_19.keys = None
    instructions_get_right.addData('key_resp_19.keys',key_resp_19.keys)
    if key_resp_19.keys != None:  # we had a response
        instructions_get_right.addData('key_resp_19.rt', key_resp_19.rt)
    # the Routine "instructions_quiz_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions_quiz_4" ---
    continueRoutine = True
    routineForceEnded = False
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
    frameN = -1
    
    # --- Run Routine "instructions_quiz_4" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_72.started')
            text_72.setAutoDraw(True)
        
        # *key_resp_20* updates
        waitOnFlip = False
        if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_20.frameNStart = frameN  # exact frame index
            key_resp_20.tStart = t  # local t and not account for scr refresh
            key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_20.started')
            key_resp_20.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_20.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_20.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_20.getKeys(keyList=['a','b','c','d'], waitRelease=False)
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
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_quiz_4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_quiz_4" ---
    for thisComponent in instructions_quiz_4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # Run 'End Routine' code from code_35
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
    # the Routine "instructions_quiz_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "result_quiz_instructions" ---
    continueRoutine = True
    routineForceEnded = False
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
    frameN = -1
    
    # --- Run Routine "result_quiz_instructions" ---
    while continueRoutine and routineTimer.getTime() < 2.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'result_q_instr.started')
            result_q_instr.setAutoDraw(True)
        if result_q_instr.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > result_q_instr.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                result_q_instr.tStop = t  # not accounting for scr refresh
                result_q_instr.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'result_q_instr.stopped')
                result_q_instr.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in result_quiz_instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "result_quiz_instructions" ---
    for thisComponent in result_quiz_instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.500000)
    thisExp.nextEntry()
    
# completed 500.0 repeats of 'instructions_get_right'


# --- Prepare to start Routine "time_limit" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
time_limitComponents = [text_102, key_resp_4]
for thisComponent in time_limitComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "time_limit" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_102* updates
    if text_102.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_102.frameNStart = frameN  # exact frame index
        text_102.tStart = t  # local t and not account for scr refresh
        text_102.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_102, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_102.started')
        text_102.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_4.started')
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in time_limitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "time_limit" ---
for thisComponent in time_limitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "time_limit" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "instructions3" ---
continueRoutine = True
routineForceEnded = False
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
frameN = -1

# --- Run Routine "instructions3" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_7.started')
        text_7.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_7.started')
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
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions3" ---
for thisComponent in instructions3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructions3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('newloop.csv'),
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
        
        # --- Prepare to start Routine "stage1" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_12
        if (trial_learning_num+1)%28==0:
            learning_reward_goal=learning_reward_goal_list[counter_reward_learning]
            im1_memory=learning_reward_startingstate_list[counter_reward_learning][0]
            im2_memory=learning_reward_startingstate_list[counter_reward_learning][1]
            num1=learning_reward_startingstate_list[counter_reward_learning][2]
            num2=learning_reward_startingstate_list[counter_reward_learning][3]
            counter_reward_learning+=1
            
        click_action.keys = []
        click_action.rt = []
        _click_action_allKeys = []
        picture_image.setImage(s1_image)
        text_3.setText(action1)
        # keep track of which components have finished
        stage1Components = [click_action, text_9, picture_image, text_3]
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
        frameN = -1
        
        # --- Run Routine "stage1" ---
        while continueRoutine and routineTimer.getTime() < 7.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *click_action* updates
            waitOnFlip = False
            if click_action.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
                # keep track of start time/frame for later
                click_action.frameNStart = frameN  # exact frame index
                click_action.tStart = t  # local t and not account for scr refresh
                click_action.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(click_action, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'click_action.started')
                click_action.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(click_action.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(click_action.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if click_action.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > click_action.tStartRefresh + 6.8-frameTolerance:
                    # keep track of stop time/frame for later
                    click_action.tStop = t  # not accounting for scr refresh
                    click_action.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'click_action.stopped')
                    click_action.status = FINISHED
            if click_action.status == STARTED and not waitOnFlip:
                theseKeys = click_action.getKeys(keyList=['1','2','3','4','5','6','7','8','9'], waitRelease=False)
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_9.started')
                text_9.setAutoDraw(True)
            if text_9.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_9.tStartRefresh + 7-frameTolerance:
                    # keep track of stop time/frame for later
                    text_9.tStop = t  # not accounting for scr refresh
                    text_9.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_9.stopped')
                    text_9.setAutoDraw(False)
            
            # *picture_image* updates
            if picture_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                picture_image.frameNStart = frameN  # exact frame index
                picture_image.tStart = t  # local t and not account for scr refresh
                picture_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(picture_image, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'picture_image.started')
                picture_image.setAutoDraw(True)
            if picture_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > picture_image.tStartRefresh + 7-frameTolerance:
                    # keep track of stop time/frame for later
                    picture_image.tStop = t  # not accounting for scr refresh
                    picture_image.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'picture_image.stopped')
                    picture_image.setAutoDraw(False)
            
            # *text_3* updates
            if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_3.frameNStart = frameN  # exact frame index
                text_3.tStart = t  # local t and not account for scr refresh
                text_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_3.started')
                text_3.setAutoDraw(True)
            if text_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_3.tStartRefresh + 7-frameTolerance:
                    # keep track of stop time/frame for later
                    text_3.tStop = t  # not accounting for scr refresh
                    text_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_3.stopped')
                    text_3.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in stage1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "stage1" ---
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
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-7.000000)
        
        # --- Prepare to start Routine "incorrect_answer" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code_11
        if click_action.corr:
            trial_learning_num+=1
            msg_incorrect='correct'
            action_selection.finished = True
            continueRoutine=False
            
        else:
            msg_incorrect='You clicked the wrong button! If you click the wrong button 5 times, the game will stop and you will NOT GET PAID because you failed to follow instructions!'
            incorrect_actions+=1
            continueRoutine=True
            
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
        frameN = -1
        
        # --- Run Routine "incorrect_answer" ---
        while continueRoutine and routineTimer.getTime() < 5.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'incorrect_display.started')
                incorrect_display.setAutoDraw(True)
            if incorrect_display.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > incorrect_display.tStartRefresh + 5-frameTolerance:
                    # keep track of stop time/frame for later
                    incorrect_display.tStop = t  # not accounting for scr refresh
                    incorrect_display.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'incorrect_display.stopped')
                    incorrect_display.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in incorrect_answerComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "incorrect_answer" ---
        for thisComponent in incorrect_answerComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-5.000000)
        thisExp.nextEntry()
        
    # completed 999.0 repeats of 'action_selection'
    
    
    # --- Prepare to start Routine "learning_trial_sequence" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    stage2_learning.setImage(s2_image)
    # Run 'Begin Routine' code from code_37
    if incorrect_actions>4:
        trials.finished = True
        continueRoutine=False
    # keep track of which components have finished
    learning_trial_sequenceComponents = [stage2_learning]
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
    frameN = -1
    
    # --- Run Routine "learning_trial_sequence" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stage2_learning* updates
        if stage2_learning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stage2_learning.frameNStart = frameN  # exact frame index
            stage2_learning.tStart = t  # local t and not account for scr refresh
            stage2_learning.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stage2_learning, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stage2_learning.started')
            stage2_learning.setAutoDraw(True)
        if stage2_learning.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stage2_learning.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                stage2_learning.tStop = t  # not accounting for scr refresh
                stage2_learning.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stage2_learning.stopped')
                stage2_learning.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learning_trial_sequenceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "learning_trial_sequence" ---
    for thisComponent in learning_trial_sequenceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # --- Prepare to start Routine "stage2_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    click_action_2.keys = []
    click_action_2.rt = []
    _click_action_2_allKeys = []
    picture_image_2.setImage(s2_image)
    text_80.setText(action2)
    # keep track of which components have finished
    stage2_2Components = [click_action_2, text_78, picture_image_2, text_80]
    for thisComponent in stage2_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "stage2_2" ---
    while continueRoutine and routineTimer.getTime() < 7.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *click_action_2* updates
        waitOnFlip = False
        if click_action_2.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            click_action_2.frameNStart = frameN  # exact frame index
            click_action_2.tStart = t  # local t and not account for scr refresh
            click_action_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(click_action_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'click_action_2.started')
            click_action_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(click_action_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(click_action_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if click_action_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > click_action_2.tStartRefresh + 6.8-frameTolerance:
                # keep track of stop time/frame for later
                click_action_2.tStop = t  # not accounting for scr refresh
                click_action_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'click_action_2.stopped')
                click_action_2.status = FINISHED
        if click_action_2.status == STARTED and not waitOnFlip:
            theseKeys = click_action_2.getKeys(keyList=['a','l'], waitRelease=False)
            _click_action_2_allKeys.extend(theseKeys)
            if len(_click_action_2_allKeys):
                click_action_2.keys = _click_action_2_allKeys[0].name  # just the first key pressed
                click_action_2.rt = _click_action_2_allKeys[0].rt
                # was this correct?
                if (click_action_2.keys == str(action1)) or (click_action_2.keys == action1):
                    click_action_2.corr = 1
                else:
                    click_action_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *text_78* updates
        if text_78.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_78.frameNStart = frameN  # exact frame index
            text_78.tStart = t  # local t and not account for scr refresh
            text_78.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_78, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_78.started')
            text_78.setAutoDraw(True)
        if text_78.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_78.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_78.tStop = t  # not accounting for scr refresh
                text_78.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_78.stopped')
                text_78.setAutoDraw(False)
        
        # *picture_image_2* updates
        if picture_image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            picture_image_2.frameNStart = frameN  # exact frame index
            picture_image_2.tStart = t  # local t and not account for scr refresh
            picture_image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(picture_image_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'picture_image_2.started')
            picture_image_2.setAutoDraw(True)
        if picture_image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > picture_image_2.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                picture_image_2.tStop = t  # not accounting for scr refresh
                picture_image_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'picture_image_2.stopped')
                picture_image_2.setAutoDraw(False)
        
        # *text_80* updates
        if text_80.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_80.frameNStart = frameN  # exact frame index
            text_80.tStart = t  # local t and not account for scr refresh
            text_80.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_80, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_80.started')
            text_80.setAutoDraw(True)
        if text_80.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_80.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_80.tStop = t  # not accounting for scr refresh
                text_80.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_80.stopped')
                text_80.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stage2_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "stage2_2" ---
    for thisComponent in stage2_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if click_action_2.keys in ['', [], None]:  # No response was made
        click_action_2.keys = None
        # was no response the correct answer?!
        if str(action1).lower() == 'none':
           click_action_2.corr = 1;  # correct non-response
        else:
           click_action_2.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('click_action_2.keys',click_action_2.keys)
    trials.addData('click_action_2.corr', click_action_2.corr)
    if click_action_2.keys != None:  # we had a response
        trials.addData('click_action_2.rt', click_action_2.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-7.000000)
    
    # --- Prepare to start Routine "learning_trial_sequence2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    stage2_learning_3.setImage(s3_image)
    # Run 'Begin Routine' code from code_50
    if incorrect_actions>4:
        trials.finished = True
        continueRoutine=False
    # keep track of which components have finished
    learning_trial_sequence2Components = [stage2_learning_3]
    for thisComponent in learning_trial_sequence2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "learning_trial_sequence2" ---
    while continueRoutine and routineTimer.getTime() < 2.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stage2_learning_3* updates
        if stage2_learning_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stage2_learning_3.frameNStart = frameN  # exact frame index
            stage2_learning_3.tStart = t  # local t and not account for scr refresh
            stage2_learning_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stage2_learning_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'stage2_learning_3.started')
            stage2_learning_3.setAutoDraw(True)
        if stage2_learning_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stage2_learning_3.tStartRefresh + 2.0-frameTolerance:
                # keep track of stop time/frame for later
                stage2_learning_3.tStop = t  # not accounting for scr refresh
                stage2_learning_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stage2_learning_3.stopped')
                stage2_learning_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learning_trial_sequence2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "learning_trial_sequence2" ---
    for thisComponent in learning_trial_sequence2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.000000)
    
    # --- Prepare to start Routine "memory_q" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_24
    if trial_learning_num%28==0:
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
    frameN = -1
    
    # --- Run Routine "memory_q" ---
    while continueRoutine and routineTimer.getTime() < 2.5:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_92.started')
            text_92.setAutoDraw(True)
        if text_92.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_92.tStartRefresh + 2.5-frameTolerance:
                # keep track of stop time/frame for later
                text_92.tStop = t  # not accounting for scr refresh
                text_92.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_92.stopped')
                text_92.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in memory_qComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "memory_q" ---
    for thisComponent in memory_qComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-2.500000)
    
    # --- Prepare to start Routine "prediction4" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_4
    if trial_learning_num%28==0:
        continueRoutine=True
        
    else:
        continueRoutine=False
    
    number_correct=0
    
    picture_reward_goal.setImage(learning_reward_goal)
    resp4.keys = []
    resp4.rt = []
    _resp4_allKeys = []
    memory_image1.setImage(im1_memory)
    memory_image2.setImage(im2_memory)
    text_79.setText(num1)
    text_85.setText(num2)
    # keep track of which components have finished
    prediction4Components = [outcome4, picture_reward_goal, resp4, memory_image1, memory_image2, text_79, text_85]
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
    frameN = -1
    
    # --- Run Routine "prediction4" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'outcome4.started')
            outcome4.setAutoDraw(True)
        
        # *picture_reward_goal* updates
        if picture_reward_goal.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            picture_reward_goal.frameNStart = frameN  # exact frame index
            picture_reward_goal.tStart = t  # local t and not account for scr refresh
            picture_reward_goal.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(picture_reward_goal, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'picture_reward_goal.started')
            picture_reward_goal.setAutoDraw(True)
        
        # *resp4* updates
        waitOnFlip = False
        if resp4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp4.frameNStart = frameN  # exact frame index
            resp4.tStart = t  # local t and not account for scr refresh
            resp4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resp4.started')
            resp4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp4.status == STARTED and not waitOnFlip:
            theseKeys = resp4.getKeys(keyList=['1','2','3','4','5','6','7','8','9'], waitRelease=False)
            _resp4_allKeys.extend(theseKeys)
            if len(_resp4_allKeys):
                resp4.keys = _resp4_allKeys[0].name  # just the first key pressed
                resp4.rt = _resp4_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        
        # *memory_image1* updates
        if memory_image1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            memory_image1.frameNStart = frameN  # exact frame index
            memory_image1.tStart = t  # local t and not account for scr refresh
            memory_image1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(memory_image1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'memory_image1.started')
            memory_image1.setAutoDraw(True)
        
        # *memory_image2* updates
        if memory_image2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            memory_image2.frameNStart = frameN  # exact frame index
            memory_image2.tStart = t  # local t and not account for scr refresh
            memory_image2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(memory_image2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'memory_image2.started')
            memory_image2.setAutoDraw(True)
        
        # *text_79* updates
        if text_79.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_79.frameNStart = frameN  # exact frame index
            text_79.tStart = t  # local t and not account for scr refresh
            text_79.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_79, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_79.started')
            text_79.setAutoDraw(True)
        
        # *text_85* updates
        if text_85.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_85.frameNStart = frameN  # exact frame index
            text_85.tStart = t  # local t and not account for scr refresh
            text_85.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_85, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_85.started')
            text_85.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prediction4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prediction4" ---
    for thisComponent in prediction4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp4.keys in ['', [], None]:  # No response was made
        resp4.keys = None
    trials.addData('resp4.keys',resp4.keys)
    if resp4.keys != None:  # we had a response
        trials.addData('resp4.rt', resp4.rt)
    # the Routine "prediction4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "prediction4_secondaction" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_56
    if trial_learning_num%28==0:
        continueRoutine=True
        
    else:
        continueRoutine=False
    
    number_correct=0
    
    picture_reward_goal_2.setImage(learning_reward_goal)
    resp4_3.keys = []
    resp4_3.rt = []
    _resp4_3_allKeys = []
    # keep track of which components have finished
    prediction4_secondactionComponents = [outcome4_2, picture_reward_goal_2, resp4_3]
    for thisComponent in prediction4_secondactionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "prediction4_secondaction" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *outcome4_2* updates
        if outcome4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            outcome4_2.frameNStart = frameN  # exact frame index
            outcome4_2.tStart = t  # local t and not account for scr refresh
            outcome4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(outcome4_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'outcome4_2.started')
            outcome4_2.setAutoDraw(True)
        
        # *picture_reward_goal_2* updates
        if picture_reward_goal_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            picture_reward_goal_2.frameNStart = frameN  # exact frame index
            picture_reward_goal_2.tStart = t  # local t and not account for scr refresh
            picture_reward_goal_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(picture_reward_goal_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'picture_reward_goal_2.started')
            picture_reward_goal_2.setAutoDraw(True)
        
        # *resp4_3* updates
        waitOnFlip = False
        if resp4_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp4_3.frameNStart = frameN  # exact frame index
            resp4_3.tStart = t  # local t and not account for scr refresh
            resp4_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp4_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resp4_3.started')
            resp4_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp4_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp4_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp4_3.status == STARTED and not waitOnFlip:
            theseKeys = resp4_3.getKeys(keyList=['a','l'], waitRelease=False)
            _resp4_3_allKeys.extend(theseKeys)
            if len(_resp4_3_allKeys):
                resp4_3.keys = _resp4_3_allKeys[0].name  # just the first key pressed
                resp4_3.rt = _resp4_3_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prediction4_secondactionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "prediction4_secondaction" ---
    for thisComponent in prediction4_secondactionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp4_3.keys in ['', [], None]:  # No response was made
        resp4_3.keys = None
    trials.addData('resp4_3.keys',resp4_3.keys)
    if resp4_3.keys != None:  # we had a response
        trials.addData('resp4_3.rt', resp4_3.rt)
    # the Routine "prediction4_secondaction" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "quiz_score" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_23
    if trial_learning_num%28==0:
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
    frameN = -1
    
    # --- Run Routine "quiz_score" ---
    while continueRoutine and routineTimer.getTime() < 1.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_5.started')
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_5.stopped')
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in quiz_scoreComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "quiz_score" ---
    for thisComponent in quiz_scoreComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-1.000000)
    
    # --- Prepare to start Routine "take_a_break" ---
    continueRoutine = True
    routineForceEnded = False
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
    frameN = -1
    
    # --- Run Routine "take_a_break" ---
    while continueRoutine and routineTimer.getTime() < 0.6:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_39.started')
            text_39.setAutoDraw(True)
        if text_39.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_39.tStartRefresh + 0.6-frameTolerance:
                # keep track of stop time/frame for later
                text_39.tStop = t  # not accounting for scr refresh
                text_39.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_39.stopped')
                text_39.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in take_a_breakComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "take_a_break" ---
    for thisComponent in take_a_breakComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-0.600000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# --- Prepare to start Routine "instructions_reward_stage" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_38
if incorrect_actions>4:
        continueRoutine=False
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
frameN = -1

# --- Run Routine "instructions_reward_stage" ---
while continueRoutine and routineTimer.getTime() < 20.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'instructions_rewardstage.started')
        instructions_rewardstage.setAutoDraw(True)
    if instructions_rewardstage.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > instructions_rewardstage.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            instructions_rewardstage.tStop = t  # not accounting for scr refresh
            instructions_rewardstage.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instructions_rewardstage.stopped')
            instructions_rewardstage.setAutoDraw(False)
    
    # *key_resp_11* updates
    waitOnFlip = False
    if key_resp_11.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.tStart = t  # local t and not account for scr refresh
        key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_11.started')
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_11.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_11.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_11.tStop = t  # not accounting for scr refresh
            key_resp_11.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_11.stopped')
            key_resp_11.status = FINISHED
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
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_reward_stageComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_reward_stage" ---
for thisComponent in instructions_reward_stageComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-20.000000)

# --- Prepare to start Routine "i2_reward" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_39
if incorrect_actions>4:
        continueRoutine=False
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
frameN = -1

# --- Run Routine "i2_reward" ---
while continueRoutine and routineTimer.getTime() < 15.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_42.started')
        text_42.setAutoDraw(True)
    if text_42.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_42.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            text_42.tStop = t  # not accounting for scr refresh
            text_42.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_42.stopped')
            text_42.setAutoDraw(False)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_9.started')
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_9.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_9.tStop = t  # not accounting for scr refresh
            key_resp_9.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_9.stopped')
            key_resp_9.status = FINISHED
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
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in i2_rewardComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "i2_reward" ---
for thisComponent in i2_rewardComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-15.000000)

# --- Prepare to start Routine "i3_reward" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_54
if incorrect_actions>4:
        continueRoutine=False
key_resp_15.keys = []
key_resp_15.rt = []
_key_resp_15_allKeys = []
# keep track of which components have finished
i3_rewardComponents = [text_113, key_resp_15]
for thisComponent in i3_rewardComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "i3_reward" ---
while continueRoutine and routineTimer.getTime() < 15.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_113* updates
    if text_113.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_113.frameNStart = frameN  # exact frame index
        text_113.tStart = t  # local t and not account for scr refresh
        text_113.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_113, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_113.started')
        text_113.setAutoDraw(True)
    if text_113.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_113.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            text_113.tStop = t  # not accounting for scr refresh
            text_113.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_113.stopped')
            text_113.setAutoDraw(False)
    
    # *key_resp_15* updates
    waitOnFlip = False
    if key_resp_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_15.frameNStart = frameN  # exact frame index
        key_resp_15.tStart = t  # local t and not account for scr refresh
        key_resp_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_15.started')
        key_resp_15.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_15.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_15.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_15.tStop = t  # not accounting for scr refresh
            key_resp_15.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_15.stopped')
            key_resp_15.status = FINISHED
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
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in i3_rewardComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "i3_reward" ---
for thisComponent in i3_rewardComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-15.000000)

# --- Prepare to start Routine "practice_view_reward_info" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_40
if incorrect_actions>4:
        continueRoutine=False
resp4_2.keys = []
resp4_2.rt = []
_resp4_2_allKeys = []
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
practice_view_reward_infoComponents = [im1_example_choicephase, resp4_2, im2_example_choicephase, example_trial_choice_phase, im1_rewvalue, text_28, key_resp_3, image_19]
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
frameN = -1

# --- Run Routine "practice_view_reward_info" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'im1_example_choicephase.started')
        im1_example_choicephase.setAutoDraw(True)
    if im1_example_choicephase.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > im1_example_choicephase.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            im1_example_choicephase.tStop = t  # not accounting for scr refresh
            im1_example_choicephase.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'im1_example_choicephase.stopped')
            im1_example_choicephase.setAutoDraw(False)
    
    # *resp4_2* updates
    waitOnFlip = False
    if resp4_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        resp4_2.frameNStart = frameN  # exact frame index
        resp4_2.tStart = t  # local t and not account for scr refresh
        resp4_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(resp4_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'resp4_2.started')
        resp4_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(resp4_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(resp4_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if resp4_2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > resp4_2.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            resp4_2.tStop = t  # not accounting for scr refresh
            resp4_2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'resp4_2.stopped')
            resp4_2.status = FINISHED
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'im2_example_choicephase.started')
        im2_example_choicephase.setAutoDraw(True)
    if im2_example_choicephase.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > im2_example_choicephase.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            im2_example_choicephase.tStop = t  # not accounting for scr refresh
            im2_example_choicephase.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'im2_example_choicephase.stopped')
            im2_example_choicephase.setAutoDraw(False)
    
    # *example_trial_choice_phase* updates
    if example_trial_choice_phase.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        example_trial_choice_phase.frameNStart = frameN  # exact frame index
        example_trial_choice_phase.tStart = t  # local t and not account for scr refresh
        example_trial_choice_phase.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(example_trial_choice_phase, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'example_trial_choice_phase.started')
        example_trial_choice_phase.setAutoDraw(True)
    if example_trial_choice_phase.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > example_trial_choice_phase.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            example_trial_choice_phase.tStop = t  # not accounting for scr refresh
            example_trial_choice_phase.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'example_trial_choice_phase.stopped')
            example_trial_choice_phase.setAutoDraw(False)
    
    # *im1_rewvalue* updates
    if im1_rewvalue.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        im1_rewvalue.frameNStart = frameN  # exact frame index
        im1_rewvalue.tStart = t  # local t and not account for scr refresh
        im1_rewvalue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(im1_rewvalue, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'im1_rewvalue.started')
        im1_rewvalue.setAutoDraw(True)
    if im1_rewvalue.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > im1_rewvalue.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            im1_rewvalue.tStop = t  # not accounting for scr refresh
            im1_rewvalue.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'im1_rewvalue.stopped')
            im1_rewvalue.setAutoDraw(False)
    
    # *text_28* updates
    if text_28.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
        # keep track of start time/frame for later
        text_28.frameNStart = frameN  # exact frame index
        text_28.tStart = t  # local t and not account for scr refresh
        text_28.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_28, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_28.started')
        text_28.setAutoDraw(True)
    if text_28.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_28.tStartRefresh + 9-frameTolerance:
            # keep track of stop time/frame for later
            text_28.tStop = t  # not accounting for scr refresh
            text_28.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_28.stopped')
            text_28.setAutoDraw(False)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 1.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_3.started')
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_3.tStartRefresh + 9-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_3.tStop = t  # not accounting for scr refresh
            key_resp_3.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_3.stopped')
            key_resp_3.status = FINISHED
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_19* updates
    if image_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_19.frameNStart = frameN  # exact frame index
        image_19.tStart = t  # local t and not account for scr refresh
        image_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_19, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'image_19.started')
        image_19.setAutoDraw(True)
    if image_19.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_19.tStartRefresh + 10.0-frameTolerance:
            # keep track of stop time/frame for later
            image_19.tStop = t  # not accounting for scr refresh
            image_19.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image_19.stopped')
            image_19.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_view_reward_infoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "practice_view_reward_info" ---
for thisComponent in practice_view_reward_infoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# --- Prepare to start Routine "instructions_planning" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_41
if incorrect_actions>4:
        continueRoutine=False
# keep track of which components have finished
instructions_planningComponents = [text_66, houses_choice_practice, train_choice_practice, text_24]
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
frameN = -1

# --- Run Routine "instructions_planning" ---
while continueRoutine and routineTimer.getTime() < 7.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_66.started')
        text_66.setAutoDraw(True)
    if text_66.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_66.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            text_66.tStop = t  # not accounting for scr refresh
            text_66.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_66.stopped')
            text_66.setAutoDraw(False)
    
    # *houses_choice_practice* updates
    if houses_choice_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        houses_choice_practice.frameNStart = frameN  # exact frame index
        houses_choice_practice.tStart = t  # local t and not account for scr refresh
        houses_choice_practice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(houses_choice_practice, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'houses_choice_practice.started')
        houses_choice_practice.setAutoDraw(True)
    if houses_choice_practice.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > houses_choice_practice.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            houses_choice_practice.tStop = t  # not accounting for scr refresh
            houses_choice_practice.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'houses_choice_practice.stopped')
            houses_choice_practice.setAutoDraw(False)
    
    # *train_choice_practice* updates
    if train_choice_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        train_choice_practice.frameNStart = frameN  # exact frame index
        train_choice_practice.tStart = t  # local t and not account for scr refresh
        train_choice_practice.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(train_choice_practice, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'train_choice_practice.started')
        train_choice_practice.setAutoDraw(True)
    if train_choice_practice.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > train_choice_practice.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            train_choice_practice.tStop = t  # not accounting for scr refresh
            train_choice_practice.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'train_choice_practice.stopped')
            train_choice_practice.setAutoDraw(False)
    
    # *text_24* updates
    if text_24.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        text_24.frameNStart = frameN  # exact frame index
        text_24.tStart = t  # local t and not account for scr refresh
        text_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_24, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_24.started')
        text_24.setAutoDraw(True)
    if text_24.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_24.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            text_24.tStop = t  # not accounting for scr refresh
            text_24.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_24.stopped')
            text_24.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_planningComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "instructions_planning" ---
for thisComponent in instructions_planningComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-7.000000)

# --- Prepare to start Routine "start_planning_trials" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_42
if incorrect_actions>4:
        continueRoutine=False
# keep track of which components have finished
start_planning_trialsComponents = [text_67]
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
frameN = -1

# --- Run Routine "start_planning_trials" ---
while continueRoutine and routineTimer.getTime() < 10.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_67.started')
        text_67.setAutoDraw(True)
    if text_67.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_67.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            text_67.tStop = t  # not accounting for scr refresh
            text_67.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_67.stopped')
            text_67.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_planning_trialsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "start_planning_trials" ---
for thisComponent in start_planning_trialsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-10.000000)

# set up handler to look after randomisation of conditions etc
PR_vs_SR = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('new_choicephase.xlsx'),
    seed=None, name='PR_vs_SR')
thisExp.addLoop(PR_vs_SR)  # add the loop to the experiment
thisPR_vs_SR = PR_vs_SR.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPR_vs_SR.rgb)
if thisPR_vs_SR != None:
    for paramName in thisPR_vs_SR:
        exec('{} = thisPR_vs_SR[paramName]'.format(paramName))

for thisPR_vs_SR in PR_vs_SR:
    currentLoop = PR_vs_SR
    # abbreviate parameter names if possible (e.g. rgb = thisPR_vs_SR.rgb)
    if thisPR_vs_SR != None:
        for paramName in thisPR_vs_SR:
            exec('{} = thisPR_vs_SR[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "info_choicephase" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_43
    if incorrect_actions>4:
            PR_vs_SR.finished=True
            continueRoutine=False
    im1_planning.setImage(r1)
    im2_planning.setImage(r2)
    im1_rewvalue_planning.setText(r1_num)
    im2_rewvalue_planning.setText(r2_num)
    key_resp_24.keys = []
    key_resp_24.rt = []
    _key_resp_24_allKeys = []
    goal_image.setImage(r3)
    im3_num_planning.setText(r3_num)
    # keep track of which components have finished
    info_choicephaseComponents = [im1_planning, im2_planning, example_trial_choice_phase_2, im1_rewvalue_planning, im2_rewvalue_planning, text_29, key_resp_24, goal_image, im3_num_planning]
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
    frameN = -1
    
    # --- Run Routine "info_choicephase" ---
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'im1_planning.started')
            im1_planning.setAutoDraw(True)
        if im1_planning.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > im1_planning.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                im1_planning.tStop = t  # not accounting for scr refresh
                im1_planning.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'im1_planning.stopped')
                im1_planning.setAutoDraw(False)
        
        # *im2_planning* updates
        if im2_planning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im2_planning.frameNStart = frameN  # exact frame index
            im2_planning.tStart = t  # local t and not account for scr refresh
            im2_planning.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im2_planning, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'im2_planning.started')
            im2_planning.setAutoDraw(True)
        if im2_planning.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > im2_planning.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                im2_planning.tStop = t  # not accounting for scr refresh
                im2_planning.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'im2_planning.stopped')
                im2_planning.setAutoDraw(False)
        
        # *example_trial_choice_phase_2* updates
        if example_trial_choice_phase_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            example_trial_choice_phase_2.frameNStart = frameN  # exact frame index
            example_trial_choice_phase_2.tStart = t  # local t and not account for scr refresh
            example_trial_choice_phase_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(example_trial_choice_phase_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'example_trial_choice_phase_2.started')
            example_trial_choice_phase_2.setAutoDraw(True)
        if example_trial_choice_phase_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > example_trial_choice_phase_2.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                example_trial_choice_phase_2.tStop = t  # not accounting for scr refresh
                example_trial_choice_phase_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'example_trial_choice_phase_2.stopped')
                example_trial_choice_phase_2.setAutoDraw(False)
        
        # *im1_rewvalue_planning* updates
        if im1_rewvalue_planning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im1_rewvalue_planning.frameNStart = frameN  # exact frame index
            im1_rewvalue_planning.tStart = t  # local t and not account for scr refresh
            im1_rewvalue_planning.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im1_rewvalue_planning, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'im1_rewvalue_planning.started')
            im1_rewvalue_planning.setAutoDraw(True)
        if im1_rewvalue_planning.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > im1_rewvalue_planning.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                im1_rewvalue_planning.tStop = t  # not accounting for scr refresh
                im1_rewvalue_planning.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'im1_rewvalue_planning.stopped')
                im1_rewvalue_planning.setAutoDraw(False)
        
        # *im2_rewvalue_planning* updates
        if im2_rewvalue_planning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im2_rewvalue_planning.frameNStart = frameN  # exact frame index
            im2_rewvalue_planning.tStart = t  # local t and not account for scr refresh
            im2_rewvalue_planning.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im2_rewvalue_planning, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'im2_rewvalue_planning.started')
            im2_rewvalue_planning.setAutoDraw(True)
        if im2_rewvalue_planning.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > im2_rewvalue_planning.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                im2_rewvalue_planning.tStop = t  # not accounting for scr refresh
                im2_rewvalue_planning.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'im2_rewvalue_planning.stopped')
                im2_rewvalue_planning.setAutoDraw(False)
        
        # *text_29* updates
        if text_29.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            text_29.frameNStart = frameN  # exact frame index
            text_29.tStart = t  # local t and not account for scr refresh
            text_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_29, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_29.started')
            text_29.setAutoDraw(True)
        if text_29.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_29.tStartRefresh + 14-frameTolerance:
                # keep track of stop time/frame for later
                text_29.tStop = t  # not accounting for scr refresh
                text_29.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_29.stopped')
                text_29.setAutoDraw(False)
        
        # *key_resp_24* updates
        waitOnFlip = False
        if key_resp_24.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_24.frameNStart = frameN  # exact frame index
            key_resp_24.tStart = t  # local t and not account for scr refresh
            key_resp_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_24, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_24.started')
            key_resp_24.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_24.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_24.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_24.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_24.tStartRefresh + 14-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_24.tStop = t  # not accounting for scr refresh
                key_resp_24.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_24.stopped')
                key_resp_24.status = FINISHED
        if key_resp_24.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_24.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_24_allKeys.extend(theseKeys)
            if len(_key_resp_24_allKeys):
                key_resp_24.keys = _key_resp_24_allKeys[-1].name  # just the last key pressed
                key_resp_24.rt = _key_resp_24_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *goal_image* updates
        if goal_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            goal_image.frameNStart = frameN  # exact frame index
            goal_image.tStart = t  # local t and not account for scr refresh
            goal_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(goal_image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'goal_image.started')
            goal_image.setAutoDraw(True)
        if goal_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > goal_image.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                goal_image.tStop = t  # not accounting for scr refresh
                goal_image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'goal_image.stopped')
                goal_image.setAutoDraw(False)
        
        # *im3_num_planning* updates
        if im3_num_planning.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im3_num_planning.frameNStart = frameN  # exact frame index
            im3_num_planning.tStart = t  # local t and not account for scr refresh
            im3_num_planning.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im3_num_planning, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'im3_num_planning.started')
            im3_num_planning.setAutoDraw(True)
        if im3_num_planning.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > im3_num_planning.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                im3_num_planning.tStop = t  # not accounting for scr refresh
                im3_num_planning.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'im3_num_planning.stopped')
                im3_num_planning.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in info_choicephaseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "info_choicephase" ---
    for thisComponent in info_choicephaseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_24.keys in ['', [], None]:  # No response was made
        key_resp_24.keys = None
    PR_vs_SR.addData('key_resp_24.keys',key_resp_24.keys)
    if key_resp_24.keys != None:  # we had a response
        PR_vs_SR.addData('key_resp_24.rt', key_resp_24.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # --- Prepare to start Routine "stage1_choice_enact" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_48
    if incorrect_actions>4:
            PR_vs_SR.finished=True
            continueRoutine=False
    image1test.setImage(r1)
    image2test.setImage(r2)
    key_resp_25.keys = []
    key_resp_25.rt = []
    _key_resp_25_allKeys = []
    text_31.setText(a1)
    text_82.setText(a2)
    # keep track of which components have finished
    stage1_choice_enactComponents = [text_81, image1test, image2test, key_resp_25, text_31, text_82]
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
    frameN = -1
    
    # --- Run Routine "stage1_choice_enact" ---
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_81.started')
            text_81.setAutoDraw(True)
        if text_81.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_81.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text_81.tStop = t  # not accounting for scr refresh
                text_81.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_81.stopped')
                text_81.setAutoDraw(False)
        
        # *image1test* updates
        if image1test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image1test.frameNStart = frameN  # exact frame index
            image1test.tStart = t  # local t and not account for scr refresh
            image1test.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image1test, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image1test.started')
            image1test.setAutoDraw(True)
        if image1test.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image1test.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                image1test.tStop = t  # not accounting for scr refresh
                image1test.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image1test.stopped')
                image1test.setAutoDraw(False)
        
        # *image2test* updates
        if image2test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image2test.frameNStart = frameN  # exact frame index
            image2test.tStart = t  # local t and not account for scr refresh
            image2test.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image2test, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image2test.started')
            image2test.setAutoDraw(True)
        if image2test.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image2test.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                image2test.tStop = t  # not accounting for scr refresh
                image2test.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image2test.stopped')
                image2test.setAutoDraw(False)
        
        # *key_resp_25* updates
        waitOnFlip = False
        if key_resp_25.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            key_resp_25.frameNStart = frameN  # exact frame index
            key_resp_25.tStart = t  # local t and not account for scr refresh
            key_resp_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_25, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_25.started')
            key_resp_25.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_25.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_25.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_25.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_25.tStartRefresh + 14.8-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_25.tStop = t  # not accounting for scr refresh
                key_resp_25.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_25.stopped')
                key_resp_25.status = FINISHED
        if key_resp_25.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_25.getKeys(keyList=['1','2','3','4','5','6','7','8','9'], waitRelease=False)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_31.started')
            text_31.setAutoDraw(True)
        if text_31.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_31.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text_31.tStop = t  # not accounting for scr refresh
                text_31.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_31.stopped')
                text_31.setAutoDraw(False)
        
        # *text_82* updates
        if text_82.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_82.frameNStart = frameN  # exact frame index
            text_82.tStart = t  # local t and not account for scr refresh
            text_82.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_82, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_82.started')
            text_82.setAutoDraw(True)
        if text_82.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_82.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text_82.tStop = t  # not accounting for scr refresh
                text_82.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_82.stopped')
                text_82.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stage1_choice_enactComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "stage1_choice_enact" ---
    for thisComponent in stage1_choice_enactComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_25.keys in ['', [], None]:  # No response was made
        key_resp_25.keys = None
    PR_vs_SR.addData('key_resp_25.keys',key_resp_25.keys)
    if key_resp_25.keys != None:  # we had a response
        PR_vs_SR.addData('key_resp_25.rt', key_resp_25.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # --- Prepare to start Routine "stage2_choice_enact" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_53
    if incorrect_actions>4:
            PR_vs_SR.finished=True
            continueRoutine=False
    image1test_2.setImage(r1)
    image2test_2.setImage(r2)
    key_resp_34.keys = []
    key_resp_34.rt = []
    _key_resp_34_allKeys = []
    text_111.setText(a1)
    text_112.setText(a2)
    # keep track of which components have finished
    stage2_choice_enactComponents = [text_110, image1test_2, image2test_2, key_resp_34, text_111, text_112]
    for thisComponent in stage2_choice_enactComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "stage2_choice_enact" ---
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_110* updates
        if text_110.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_110.frameNStart = frameN  # exact frame index
            text_110.tStart = t  # local t and not account for scr refresh
            text_110.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_110, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_110.started')
            text_110.setAutoDraw(True)
        if text_110.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_110.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text_110.tStop = t  # not accounting for scr refresh
                text_110.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_110.stopped')
                text_110.setAutoDraw(False)
        
        # *image1test_2* updates
        if image1test_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image1test_2.frameNStart = frameN  # exact frame index
            image1test_2.tStart = t  # local t and not account for scr refresh
            image1test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image1test_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image1test_2.started')
            image1test_2.setAutoDraw(True)
        if image1test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image1test_2.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                image1test_2.tStop = t  # not accounting for scr refresh
                image1test_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image1test_2.stopped')
                image1test_2.setAutoDraw(False)
        
        # *image2test_2* updates
        if image2test_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image2test_2.frameNStart = frameN  # exact frame index
            image2test_2.tStart = t  # local t and not account for scr refresh
            image2test_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image2test_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'image2test_2.started')
            image2test_2.setAutoDraw(True)
        if image2test_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image2test_2.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                image2test_2.tStop = t  # not accounting for scr refresh
                image2test_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'image2test_2.stopped')
                image2test_2.setAutoDraw(False)
        
        # *key_resp_34* updates
        waitOnFlip = False
        if key_resp_34.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            key_resp_34.frameNStart = frameN  # exact frame index
            key_resp_34.tStart = t  # local t and not account for scr refresh
            key_resp_34.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_34, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_34.started')
            key_resp_34.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_34.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_34.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_34.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_34.tStartRefresh + 14.8-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_34.tStop = t  # not accounting for scr refresh
                key_resp_34.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_34.stopped')
                key_resp_34.status = FINISHED
        if key_resp_34.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_34.getKeys(keyList=['a','l'], waitRelease=False)
            _key_resp_34_allKeys.extend(theseKeys)
            if len(_key_resp_34_allKeys):
                key_resp_34.keys = _key_resp_34_allKeys[-1].name  # just the last key pressed
                key_resp_34.rt = _key_resp_34_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_111* updates
        if text_111.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_111.frameNStart = frameN  # exact frame index
            text_111.tStart = t  # local t and not account for scr refresh
            text_111.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_111, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_111.started')
            text_111.setAutoDraw(True)
        if text_111.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_111.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text_111.tStop = t  # not accounting for scr refresh
                text_111.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_111.stopped')
                text_111.setAutoDraw(False)
        
        # *text_112* updates
        if text_112.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_112.frameNStart = frameN  # exact frame index
            text_112.tStart = t  # local t and not account for scr refresh
            text_112.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_112, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_112.started')
            text_112.setAutoDraw(True)
        if text_112.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_112.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text_112.tStop = t  # not accounting for scr refresh
                text_112.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_112.stopped')
                text_112.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in stage2_choice_enactComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "stage2_choice_enact" ---
    for thisComponent in stage2_choice_enactComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_34.keys in ['', [], None]:  # No response was made
        key_resp_34.keys = None
    PR_vs_SR.addData('key_resp_34.keys',key_resp_34.keys)
    if key_resp_34.keys != None:  # we had a response
        PR_vs_SR.addData('key_resp_34.rt', key_resp_34.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # --- Prepare to start Routine "final_stage5" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_49
    if incorrect_actions>4:
            PR_vs_SR.finished=True
            continueRoutine=False
    # keep track of which components have finished
    final_stage5Components = [text_68, text_30]
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
    frameN = -1
    
    # --- Run Routine "final_stage5" ---
    while continueRoutine and routineTimer.getTime() < 3.6:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_68.started')
            text_68.setAutoDraw(True)
        if text_68.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_68.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_68.tStop = t  # not accounting for scr refresh
                text_68.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_68.stopped')
                text_68.setAutoDraw(False)
        
        # *text_30* updates
        if text_30.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            text_30.frameNStart = frameN  # exact frame index
            text_30.tStart = t  # local t and not account for scr refresh
            text_30.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_30.started')
            text_30.setAutoDraw(True)
        if text_30.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_30.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_30.tStop = t  # not accounting for scr refresh
                text_30.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_30.stopped')
                text_30.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in final_stage5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "final_stage5" ---
    for thisComponent in final_stage5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.600000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'PR_vs_SR'


# --- Prepare to start Routine "transition_revaluation" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_44
if incorrect_actions>4:
        continueRoutine=False
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
transition_revaluationComponents = [text_25, text_26, key_resp_8, tree_reval, trident_reval, right_arrow, fox_reval, right_arrow2, planet_reval, text_94]
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
frameN = -1

# --- Run Routine "transition_revaluation" ---
while continueRoutine and routineTimer.getTime() < 20.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_25.started')
        text_25.setAutoDraw(True)
    if text_25.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_25.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            text_25.tStop = t  # not accounting for scr refresh
            text_25.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_25.stopped')
            text_25.setAutoDraw(False)
    
    # *text_26* updates
    if text_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_26.frameNStart = frameN  # exact frame index
        text_26.tStart = t  # local t and not account for scr refresh
        text_26.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_26, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_26.started')
        text_26.setAutoDraw(True)
    if text_26.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_26.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            text_26.tStop = t  # not accounting for scr refresh
            text_26.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_26.stopped')
            text_26.setAutoDraw(False)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'key_resp_8.started')
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_8.tStartRefresh + 17.5-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_8.tStop = t  # not accounting for scr refresh
            key_resp_8.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_8.stopped')
            key_resp_8.status = FINISHED
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *tree_reval* updates
    if tree_reval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        tree_reval.frameNStart = frameN  # exact frame index
        tree_reval.tStart = t  # local t and not account for scr refresh
        tree_reval.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(tree_reval, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'tree_reval.started')
        tree_reval.setAutoDraw(True)
    if tree_reval.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > tree_reval.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            tree_reval.tStop = t  # not accounting for scr refresh
            tree_reval.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'tree_reval.stopped')
            tree_reval.setAutoDraw(False)
    
    # *trident_reval* updates
    if trident_reval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        trident_reval.frameNStart = frameN  # exact frame index
        trident_reval.tStart = t  # local t and not account for scr refresh
        trident_reval.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(trident_reval, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'trident_reval.started')
        trident_reval.setAutoDraw(True)
    if trident_reval.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > trident_reval.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            trident_reval.tStop = t  # not accounting for scr refresh
            trident_reval.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trident_reval.stopped')
            trident_reval.setAutoDraw(False)
    
    # *right_arrow* updates
    if right_arrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        right_arrow.frameNStart = frameN  # exact frame index
        right_arrow.tStart = t  # local t and not account for scr refresh
        right_arrow.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(right_arrow, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'right_arrow.started')
        right_arrow.setAutoDraw(True)
    if right_arrow.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > right_arrow.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            right_arrow.tStop = t  # not accounting for scr refresh
            right_arrow.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'right_arrow.stopped')
            right_arrow.setAutoDraw(False)
    
    # *fox_reval* updates
    if fox_reval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        fox_reval.frameNStart = frameN  # exact frame index
        fox_reval.tStart = t  # local t and not account for scr refresh
        fox_reval.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(fox_reval, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'fox_reval.started')
        fox_reval.setAutoDraw(True)
    if fox_reval.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > fox_reval.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            fox_reval.tStop = t  # not accounting for scr refresh
            fox_reval.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'fox_reval.stopped')
            fox_reval.setAutoDraw(False)
    
    # *right_arrow2* updates
    if right_arrow2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        right_arrow2.frameNStart = frameN  # exact frame index
        right_arrow2.tStart = t  # local t and not account for scr refresh
        right_arrow2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(right_arrow2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'right_arrow2.started')
        right_arrow2.setAutoDraw(True)
    if right_arrow2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > right_arrow2.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            right_arrow2.tStop = t  # not accounting for scr refresh
            right_arrow2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'right_arrow2.stopped')
            right_arrow2.setAutoDraw(False)
    
    # *planet_reval* updates
    if planet_reval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        planet_reval.frameNStart = frameN  # exact frame index
        planet_reval.tStart = t  # local t and not account for scr refresh
        planet_reval.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(planet_reval, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'planet_reval.started')
        planet_reval.setAutoDraw(True)
    if planet_reval.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > planet_reval.tStartRefresh + 20-frameTolerance:
            # keep track of stop time/frame for later
            planet_reval.tStop = t  # not accounting for scr refresh
            planet_reval.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'planet_reval.stopped')
            planet_reval.setAutoDraw(False)
    
    # *text_94* updates
    if text_94.status == NOT_STARTED and tThisFlip >= 2.5-frameTolerance:
        # keep track of start time/frame for later
        text_94.frameNStart = frameN  # exact frame index
        text_94.tStart = t  # local t and not account for scr refresh
        text_94.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_94, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_94.started')
        text_94.setAutoDraw(True)
    if text_94.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_94.tStartRefresh + 17.5-frameTolerance:
            # keep track of stop time/frame for later
            text_94.tStop = t  # not accounting for scr refresh
            text_94.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_94.stopped')
            text_94.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in transition_revaluationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "transition_revaluation" ---
for thisComponent in transition_revaluationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-20.000000)

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
    
    # --- Prepare to start Routine "info_choice_revaluation_2" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_45
    if incorrect_actions>4:
            transition_revaluation_round.finished=True
            continueRoutine=False
    im1_planning_2.setImage(r1)
    im2_planning_2.setImage(r2)
    im1_rewvalue_planning_2.setText(r3_num)
    key_resp_29.keys = []
    key_resp_29.rt = []
    _key_resp_29_allKeys = []
    goal_transition_reval.setImage(r3)
    # keep track of which components have finished
    info_choice_revaluation_2Components = [im1_planning_2, im2_planning_2, example_trial_choice_phase_4, im1_rewvalue_planning_2, text_93, key_resp_29, goal_transition_reval]
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
    frameN = -1
    
    # --- Run Routine "info_choice_revaluation_2" ---
    while continueRoutine and routineTimer.getTime() < 20.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'im1_planning_2.started')
            im1_planning_2.setAutoDraw(True)
        if im1_planning_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > im1_planning_2.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                im1_planning_2.tStop = t  # not accounting for scr refresh
                im1_planning_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'im1_planning_2.stopped')
                im1_planning_2.setAutoDraw(False)
        
        # *im2_planning_2* updates
        if im2_planning_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im2_planning_2.frameNStart = frameN  # exact frame index
            im2_planning_2.tStart = t  # local t and not account for scr refresh
            im2_planning_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im2_planning_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'im2_planning_2.started')
            im2_planning_2.setAutoDraw(True)
        if im2_planning_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > im2_planning_2.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                im2_planning_2.tStop = t  # not accounting for scr refresh
                im2_planning_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'im2_planning_2.stopped')
                im2_planning_2.setAutoDraw(False)
        
        # *example_trial_choice_phase_4* updates
        if example_trial_choice_phase_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            example_trial_choice_phase_4.frameNStart = frameN  # exact frame index
            example_trial_choice_phase_4.tStart = t  # local t and not account for scr refresh
            example_trial_choice_phase_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(example_trial_choice_phase_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'example_trial_choice_phase_4.started')
            example_trial_choice_phase_4.setAutoDraw(True)
        if example_trial_choice_phase_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > example_trial_choice_phase_4.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                example_trial_choice_phase_4.tStop = t  # not accounting for scr refresh
                example_trial_choice_phase_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'example_trial_choice_phase_4.stopped')
                example_trial_choice_phase_4.setAutoDraw(False)
        
        # *im1_rewvalue_planning_2* updates
        if im1_rewvalue_planning_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            im1_rewvalue_planning_2.frameNStart = frameN  # exact frame index
            im1_rewvalue_planning_2.tStart = t  # local t and not account for scr refresh
            im1_rewvalue_planning_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(im1_rewvalue_planning_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'im1_rewvalue_planning_2.started')
            im1_rewvalue_planning_2.setAutoDraw(True)
        if im1_rewvalue_planning_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > im1_rewvalue_planning_2.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                im1_rewvalue_planning_2.tStop = t  # not accounting for scr refresh
                im1_rewvalue_planning_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'im1_rewvalue_planning_2.stopped')
                im1_rewvalue_planning_2.setAutoDraw(False)
        
        # *text_93* updates
        if text_93.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            text_93.frameNStart = frameN  # exact frame index
            text_93.tStart = t  # local t and not account for scr refresh
            text_93.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_93, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_93.started')
            text_93.setAutoDraw(True)
        if text_93.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_93.tStartRefresh + 18-frameTolerance:
                # keep track of stop time/frame for later
                text_93.tStop = t  # not accounting for scr refresh
                text_93.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_93.stopped')
                text_93.setAutoDraw(False)
        
        # *key_resp_29* updates
        waitOnFlip = False
        if key_resp_29.status == NOT_STARTED and tThisFlip >= 2.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_29.frameNStart = frameN  # exact frame index
            key_resp_29.tStart = t  # local t and not account for scr refresh
            key_resp_29.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_29, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_29.started')
            key_resp_29.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_29.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_29.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_29.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_29.tStartRefresh + 18-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_29.tStop = t  # not accounting for scr refresh
                key_resp_29.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_29.stopped')
                key_resp_29.status = FINISHED
        if key_resp_29.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_29.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_29_allKeys.extend(theseKeys)
            if len(_key_resp_29_allKeys):
                key_resp_29.keys = _key_resp_29_allKeys[-1].name  # just the last key pressed
                key_resp_29.rt = _key_resp_29_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *goal_transition_reval* updates
        if goal_transition_reval.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            goal_transition_reval.frameNStart = frameN  # exact frame index
            goal_transition_reval.tStart = t  # local t and not account for scr refresh
            goal_transition_reval.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(goal_transition_reval, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'goal_transition_reval.started')
            goal_transition_reval.setAutoDraw(True)
        if goal_transition_reval.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > goal_transition_reval.tStartRefresh + 20.0-frameTolerance:
                # keep track of stop time/frame for later
                goal_transition_reval.tStop = t  # not accounting for scr refresh
                goal_transition_reval.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'goal_transition_reval.stopped')
                goal_transition_reval.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in info_choice_revaluation_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "info_choice_revaluation_2" ---
    for thisComponent in info_choice_revaluation_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_29.keys in ['', [], None]:  # No response was made
        key_resp_29.keys = None
    transition_revaluation_round.addData('key_resp_29.keys',key_resp_29.keys)
    if key_resp_29.keys != None:  # we had a response
        transition_revaluation_round.addData('key_resp_29.rt', key_resp_29.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-20.000000)
    
    # --- Prepare to start Routine "choice_transistion_reval" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_52
    if incorrect_actions>4:
            transition_revaluation_round.finished=True
            continueRoutine=False
    trident_choice_3.setImage(r1)
    planet_choice_3.setImage(r2)
    transition_reval_choice.keys = []
    transition_reval_choice.rt = []
    _transition_reval_choice_allKeys = []
    text_106.setText(a1)
    text_107.setText(a2)
    # keep track of which components have finished
    choice_transistion_revalComponents = [text_105, trident_choice_3, planet_choice_3, transition_reval_choice, text_106, text_107]
    for thisComponent in choice_transistion_revalComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "choice_transistion_reval" ---
    while continueRoutine and routineTimer.getTime() < 20.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_105* updates
        if text_105.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_105.frameNStart = frameN  # exact frame index
            text_105.tStart = t  # local t and not account for scr refresh
            text_105.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_105, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_105.started')
            text_105.setAutoDraw(True)
        if text_105.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_105.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                text_105.tStop = t  # not accounting for scr refresh
                text_105.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_105.stopped')
                text_105.setAutoDraw(False)
        
        # *trident_choice_3* updates
        if trident_choice_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trident_choice_3.frameNStart = frameN  # exact frame index
            trident_choice_3.tStart = t  # local t and not account for scr refresh
            trident_choice_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trident_choice_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trident_choice_3.started')
            trident_choice_3.setAutoDraw(True)
        if trident_choice_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > trident_choice_3.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                trident_choice_3.tStop = t  # not accounting for scr refresh
                trident_choice_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'trident_choice_3.stopped')
                trident_choice_3.setAutoDraw(False)
        
        # *planet_choice_3* updates
        if planet_choice_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            planet_choice_3.frameNStart = frameN  # exact frame index
            planet_choice_3.tStart = t  # local t and not account for scr refresh
            planet_choice_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(planet_choice_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'planet_choice_3.started')
            planet_choice_3.setAutoDraw(True)
        if planet_choice_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > planet_choice_3.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                planet_choice_3.tStop = t  # not accounting for scr refresh
                planet_choice_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'planet_choice_3.stopped')
                planet_choice_3.setAutoDraw(False)
        
        # *transition_reval_choice* updates
        waitOnFlip = False
        if transition_reval_choice.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            transition_reval_choice.frameNStart = frameN  # exact frame index
            transition_reval_choice.tStart = t  # local t and not account for scr refresh
            transition_reval_choice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(transition_reval_choice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'transition_reval_choice.started')
            transition_reval_choice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(transition_reval_choice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(transition_reval_choice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if transition_reval_choice.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > transition_reval_choice.tStartRefresh + 19.8-frameTolerance:
                # keep track of stop time/frame for later
                transition_reval_choice.tStop = t  # not accounting for scr refresh
                transition_reval_choice.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'transition_reval_choice.stopped')
                transition_reval_choice.status = FINISHED
        if transition_reval_choice.status == STARTED and not waitOnFlip:
            theseKeys = transition_reval_choice.getKeys(keyList=['1','2','3','4','5','6','7','8','9'], waitRelease=False)
            _transition_reval_choice_allKeys.extend(theseKeys)
            if len(_transition_reval_choice_allKeys):
                transition_reval_choice.keys = _transition_reval_choice_allKeys[-1].name  # just the last key pressed
                transition_reval_choice.rt = _transition_reval_choice_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_106* updates
        if text_106.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_106.frameNStart = frameN  # exact frame index
            text_106.tStart = t  # local t and not account for scr refresh
            text_106.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_106, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_106.started')
            text_106.setAutoDraw(True)
        if text_106.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_106.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                text_106.tStop = t  # not accounting for scr refresh
                text_106.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_106.stopped')
                text_106.setAutoDraw(False)
        
        # *text_107* updates
        if text_107.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_107.frameNStart = frameN  # exact frame index
            text_107.tStart = t  # local t and not account for scr refresh
            text_107.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_107, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_107.started')
            text_107.setAutoDraw(True)
        if text_107.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_107.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                text_107.tStop = t  # not accounting for scr refresh
                text_107.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_107.stopped')
                text_107.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in choice_transistion_revalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "choice_transistion_reval" ---
    for thisComponent in choice_transistion_revalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if transition_reval_choice.keys in ['', [], None]:  # No response was made
        transition_reval_choice.keys = None
    transition_revaluation_round.addData('transition_reval_choice.keys',transition_reval_choice.keys)
    if transition_reval_choice.keys != None:  # we had a response
        transition_revaluation_round.addData('transition_reval_choice.rt', transition_reval_choice.rt)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-20.000000)
    
    # --- Prepare to start Routine "final_stage_Tr" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from code_51
    if incorrect_actions>4:
            transition_revaluation_round.finished=True
            continueRoutine=False
    # keep track of which components have finished
    final_stage_TrComponents = [text_103, text_104]
    for thisComponent in final_stage_TrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "final_stage_Tr" ---
    while continueRoutine and routineTimer.getTime() < 3.6:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_103* updates
        if text_103.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_103.frameNStart = frameN  # exact frame index
            text_103.tStart = t  # local t and not account for scr refresh
            text_103.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_103, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_103.started')
            text_103.setAutoDraw(True)
        if text_103.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_103.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                text_103.tStop = t  # not accounting for scr refresh
                text_103.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_103.stopped')
                text_103.setAutoDraw(False)
        
        # *text_104* updates
        if text_104.status == NOT_STARTED and tThisFlip >= 1.6-frameTolerance:
            # keep track of start time/frame for later
            text_104.frameNStart = frameN  # exact frame index
            text_104.tStart = t  # local t and not account for scr refresh
            text_104.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_104, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_104.started')
            text_104.setAutoDraw(True)
        if text_104.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_104.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                text_104.tStop = t  # not accounting for scr refresh
                text_104.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_104.stopped')
                text_104.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in final_stage_TrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "final_stage_Tr" ---
    for thisComponent in final_stage_TrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-3.600000)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'transition_revaluation_round'


# --- Prepare to start Routine "reward_total" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_46
if incorrect_actions>4:
        continueRoutine=False
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
frameN = -1

# --- Run Routine "reward_total" ---
while continueRoutine and routineTimer.getTime() < 2.5:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_84.started')
        text_84.setAutoDraw(True)
    if text_84.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_84.tStartRefresh + 2.5-frameTolerance:
            # keep track of stop time/frame for later
            text_84.tStop = t  # not accounting for scr refresh
            text_84.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_84.stopped')
            text_84.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in reward_totalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "reward_total" ---
for thisComponent in reward_totalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-2.500000)

# --- Prepare to start Routine "done" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# Run 'Begin Routine' code from code_47
if incorrect_actions>4:
        continueRoutine=False
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
frameN = -1

# --- Run Routine "done" ---
while continueRoutine and routineTimer.getTime() < 6.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
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
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'text_62.started')
        text_62.setAutoDraw(True)
    if text_62.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_62.tStartRefresh + 6.0-frameTolerance:
            # keep track of stop time/frame for later
            text_62.tStop = t  # not accounting for scr refresh
            text_62.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_62.stopped')
            text_62.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in doneComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "done" ---
for thisComponent in doneComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-6.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
