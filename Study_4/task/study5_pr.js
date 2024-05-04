/****************** 
 * Study5_Pr Test *
 ******************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2022.2.5.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'study5_pr';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color('whitesmoke'),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
const instructions_get_rightLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(instructions_get_rightLoopBegin(instructions_get_rightLoopScheduler));
flowScheduler.add(instructions_get_rightLoopScheduler);
flowScheduler.add(instructions_get_rightLoopEnd);
flowScheduler.add(time_limitRoutineBegin());
flowScheduler.add(time_limitRoutineEachFrame());
flowScheduler.add(time_limitRoutineEnd());
flowScheduler.add(instructions3RoutineBegin());
flowScheduler.add(instructions3RoutineEachFrame());
flowScheduler.add(instructions3RoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
const trials_2LoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trials_2LoopBegin(trials_2LoopScheduler));
flowScheduler.add(trials_2LoopScheduler);
flowScheduler.add(trials_2LoopEnd);
flowScheduler.add(instructions_reward_stageRoutineBegin());
flowScheduler.add(instructions_reward_stageRoutineEachFrame());
flowScheduler.add(instructions_reward_stageRoutineEnd());
flowScheduler.add(instructions_planning_2phaseRoutineBegin());
flowScheduler.add(instructions_planning_2phaseRoutineEachFrame());
flowScheduler.add(instructions_planning_2phaseRoutineEnd());
flowScheduler.add(i2_rewardRoutineBegin());
flowScheduler.add(i2_rewardRoutineEachFrame());
flowScheduler.add(i2_rewardRoutineEnd());
flowScheduler.add(practice_view_reward_infoRoutineBegin());
flowScheduler.add(practice_view_reward_infoRoutineEachFrame());
flowScheduler.add(practice_view_reward_infoRoutineEnd());
flowScheduler.add(instructions_planningRoutineBegin());
flowScheduler.add(instructions_planningRoutineEachFrame());
flowScheduler.add(instructions_planningRoutineEnd());
flowScheduler.add(start_planning_trialsRoutineBegin());
flowScheduler.add(start_planning_trialsRoutineEachFrame());
flowScheduler.add(start_planning_trialsRoutineEnd());
const PR_vs_SRLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(PR_vs_SRLoopBegin(PR_vs_SRLoopScheduler));
flowScheduler.add(PR_vs_SRLoopScheduler);
flowScheduler.add(PR_vs_SRLoopEnd);
flowScheduler.add(transition_revaluationRoutineBegin());
flowScheduler.add(transition_revaluationRoutineEachFrame());
flowScheduler.add(transition_revaluationRoutineEnd());
const transition_revaluation_roundLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(transition_revaluation_roundLoopBegin(transition_revaluation_roundLoopScheduler));
flowScheduler.add(transition_revaluation_roundLoopScheduler);
flowScheduler.add(transition_revaluation_roundLoopEnd);
flowScheduler.add(reward_totalRoutineBegin());
flowScheduler.add(reward_totalRoutineEachFrame());
flowScheduler.add(reward_totalRoutineEnd());
flowScheduler.add(doneRoutineBegin());
flowScheduler.add(doneRoutineEachFrame());
flowScheduler.add(doneRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'consent2.png', 'path': 'consent2.png'},
    {'name': 'houses.png', 'path': 'houses.png'},
    {'name': 'basket.png', 'path': 'basket.png'},
    {'name': 'bell.png', 'path': 'bell.png'},
    {'name': 'fox.png', 'path': 'fox.png'},
    {'name': 'trident.png', 'path': 'trident.png'},
    {'name': 'tree.png', 'path': 'tree.png'},
    {'name': 'train.png', 'path': 'train.png'},
    {'name': 'tophat.png', 'path': 'tophat.png'},
    {'name': 'fireworks.png', 'path': 'fireworks.png'},
    {'name': 'stage2_4_practice.csv', 'path': 'stage2_4_practice.csv'},
    {'name': 'unicorn.png', 'path': 'unicorn.png'},
    {'name': 'consent1.png', 'path': 'consent1.png'},
    {'name': 'planet.png', 'path': 'planet.png'},
    {'name': 'watch.png', 'path': 'watch.png'},
    {'name': 'choicephase_afterevaluation.xlsx', 'path': 'choicephase_afterevaluation.xlsx'},
    {'name': 'apple.png', 'path': 'apple.png'},
    {'name': 'north.png', 'path': 'north.png'},
    {'name': 'wm.png', 'path': 'wm.png'},
    {'name': 'action2_loop.csv', 'path': 'action2_loop.csv'},
    {'name': 'right.png', 'path': 'right.png'},
    {'name': 'snorkel.png', 'path': 'snorkel.png'},
    {'name': 'new_trials.csv', 'path': 'new_trials.csv'},
    {'name': 'compass.png', 'path': 'compass.png'},
    {'name': 'new_choicephase.xlsx', 'path': 'new_choicephase.xlsx'},
    {'name': 'hammer.png', 'path': 'hammer.png'},
    {'name': 'window.png', 'path': 'window.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.5';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls('https://app.prolific.co/submissions/complete?cc=C1EI1MLP', '');


  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);


  return Scheduler.Event.NEXT;
}


var consentClock;
var image_11;
var consent1_next;
var text_89;
var consent1Clock;
var image_13;
var consent1_next_2;
var text_90;
var instructionsClock;
var text;
var key_resp;
var instruction2Clock;
var key_resp_2;
var text_2;
var stage1_instructionsClock;
var keyboard_entry_instr1;
var start_instr1;
var trident_start;
var planet_start;
var instructions_decisionrules;
var space_continue_instr1;
var one;
var nine;
var stage2_4_instructionsClock;
var responseleft;
var text_4;
var stage_2_4_practiceClock;
var image_22;
var key_resp_10;
var text_40;
var stage_2_4_practice_resultClock;
var image_20;
var text_76;
var image_12;
var text_77;
var quiz_practiceClock;
var basket_2;
var fireworks_2;
var tree_2;
var text_17;
var text_21;
var text_27;
var practice_answer;
var text_6;
var feedback1Clock;
var text_10;
var memory_quizClock;
var text_75;
var key_resp_23;
var reminder_second_phaseClock;
var text_74;
var key_resp_22;
var instructions_quiz_1Clock;
var text_43;
var key_resp_17;
var instructions_quiz_2Clock;
var text_70;
var key_resp_18;
var instructions_quiz_3Clock;
var text_71;
var key_resp_19;
var instructions_quiz_4Clock;
var text_72;
var key_resp_20;
var result_quiz_instructionsClock;
var result_q_instr;
var time_limitClock;
var text_102;
var key_resp_4;
var instructions3Clock;
var text_7;
var key_resp_7;
var quiz1list;
var quiz2list;
var q1left_correct;
var q1right_correct;
var q2left_correct;
var q2right_correct;
var learning_reward_goal_list;
var counter_reward_learning;
var learning_reward_goal;
var msg_new;
var action_list;
var quiz_counter;
var num_quiz_trials;
var stage2;
var stage3;
var quizzes;
var predictions1;
var predictions2;
var predictions;
var trials_with_three;
var trials_with_four;
var incorrect_actions;
var action;
var trial_learning_num;
var correct_quiz;
var percent_correct;
var text_correct;
var stage1Clock;
var click_action;
var text_9;
var trident_start_learning;
var text_3;
var incorrect_answerClock;
var incorrect_display;
var stage2_2Clock;
var click_action_2;
var text_108;
var trident_start_learning_2;
var text_109;
var learning_trial_step2_to_step3Clock;
var stage2_learning_3;
var memory_qClock;
var text_92;
var prediction4Clock;
var outcome4;
var picture_reward_goal;
var resp4;
var learning_rew_trident;
var learning_rew_planet;
var text_79;
var text_85;
var quiz_scoreClock;
var text_5;
var take_a_breakClock;
var text_39;
var prediction5Clock;
var outcome4_2;
var picture_reward_goal_2;
var resp4_3;
var learning_rew_trident_2;
var text_80;
var instructions_reward_stageClock;
var instructions_rewardstage;
var key_resp_11;
var instructions_planning_2phaseClock;
var instructions_rewardstage_2;
var key_resp_35;
var i2_rewardClock;
var text_42;
var key_resp_9;
var practice_view_reward_infoClock;
var im1_example_choicephase;
var resp4_2;
var im2_example_choicephase;
var example_trial_choice_phase;
var im1_rewvalue;
var im2_rewvalue;
var text_28;
var key_resp_3;
var instructions_planningClock;
var text_66;
var key_resp_12;
var text_24;
var start_planning_trialsClock;
var text_67;
var key_resp_15;
var info_choicephaseClock;
var im1_planning;
var im2_planning;
var example_trial_choice_phase_2;
var im1_rewvalue_planning;
var im2_rewvalue_planning;
var text_29;
var key_resp_24;
var im3_planning;
var im4_planning;
var im3_num_planning;
var im4_num_planning;
var stage1_choice_enactClock;
var text_81;
var key_resp_25;
var stage2_choice_enactClock;
var text_82;
var key_resp_36;
var final_stage5Clock;
var text_68;
var text_30;
var key_resp_16;
var transition_revaluationClock;
var text_25;
var text_26;
var key_resp_8;
var trident_reval;
var watch_reval;
var right_arrow;
var planet_reval;
var right_arrow2;
var fox_reval;
var text_94;
var info_choice_revaluation_2Clock;
var im1_planning_2;
var im2_planning_2;
var example_trial_choice_phase_4;
var im1_rewvalue_planning_2;
var im2_rewvalue_planning_2;
var text_93;
var key_resp_29;
var choice_transistion_revalClock;
var text_105;
var transition_reval_choice;
var choice_transition2Clock;
var text_106;
var transition_reval_choice_2;
var final_stage_TrClock;
var text_103;
var text_104;
var key_resp_34;
var reward_totalClock;
var text_84;
var doneClock;
var text_62;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "consent"
  consentClock = new util.Clock();
  image_11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_11', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0.05], size : [0.65, 0.75],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  consent1_next = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_89 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_89',
    text: 'Click SPACE to Continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "consent1"
  consent1Clock = new util.Clock();
  image_13 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_13', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0.1], size : [0.65, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  consent1_next_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_90 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_90',
    text: 'I certify that I have read the informed consent and received the information to contact the investigators if necessary.\n\nClick ‘y’ for YES\nClick ’n’ for NO, and you will EXIT the study',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.35)], height: 0.03,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'In this task, you will learn how to navigate a picture game. Each time you navigate in the game, you have two choices to make. Each choice you make will take you from one picture to another. \n\nFor example, you might need to learn how often you see an apple after starting at an image of a tree. \n\nThus, this task requires you to learn probabilities of image transitions. The probability of seeing an apple after a tree might be very different from the probability of seeing the apple after a rock. \n\nAfter this learning phase, you can use this knowledge to plan how to win points in a final phase. Importantly, you can earn money based on these points. You will be instructed later exactly how to win points. \n\nPress Space to continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instruction2"
  instruction2Clock = new util.Clock();
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'PHASE 1: LEARN HOW TO NAVIGATE IN THE PICTURE WORLD\n\nYou will now be instructed which actions to take in the picture world. Your goal is to learn which new picture you will arrive at after selecting a picture by clicking the corresponding number on your keyboard.\n\nNOTE: There will be a SECOND PHASE after this first phase, where you can use what you learned to win even more money!\n\nPress Space to continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "stage1_instructions"
  stage1_instructionsClock = new util.Clock();
  keyboard_entry_instr1 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  start_instr1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'start_instr1',
    text: 'Start',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.15], height: 0.075,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  trident_start = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trident_start', units : undefined, 
    image : 'trident.png', mask : undefined,
    ori : 0.0, pos : [(- 0.4), (- 0.1)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  planet_start = new visual.ImageStim({
    win : psychoJS.window,
    name : 'planet_start', units : undefined, 
    image : 'planet.png', mask : undefined,
    ori : 0.0, pos : [0.4, (- 0.1)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  instructions_decisionrules = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_decisionrules',
    text: 'The first decision will say “START”. 1 takes you from TRIDENT to a new image. 9 takes you from PLANET to a new image.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.38], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  space_continue_instr1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'space_continue_instr1',
    text: 'Press Space to continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -5.0 
  });
  
  one = new visual.TextStim({
    win: psychoJS.window,
    name: 'one',
    text: '1',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.4), (- 0.26)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -6.0 
  });
  
  nine = new visual.TextStim({
    win: psychoJS.window,
    name: 'nine',
    text: '9',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.4, (- 0.26)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -7.0 
  });
  
  // Initialize components for Routine "stage2_4_instructions"
  stage2_4_instructionsClock = new util.Clock();
  responseleft = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'After choosing the trident or the planet, you will arrive at a new image. Then you will take a SECOND ACTION to see a final, third image.\n\nYour goal is to remember which images tend to come after acting at a specific starting image. For instance, what image tends to most often come after clicking 1 at trident? \n\nTo show you what this looks like, you will do a practice round. \n\nPress SPACE to continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "stage_2_4_practice"
  stage_2_4_practiceClock = new util.Clock();
  image_22 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_22', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_10 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_40 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_40',
    text: 'Press 1',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.35)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "stage_2_4_practice_result"
  stage_2_4_practice_resultClock = new util.Clock();
  image_20 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_20', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  text_76 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_76',
    text: 'Moving to next image…',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.055,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  image_12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_12', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  text_77 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_77',
    text: 'Done trial!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "quiz_practice"
  quiz_practiceClock = new util.Clock();
  basket_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'basket_2', units : undefined, 
    image : 'basket.png', mask : undefined,
    ori : 0.0, pos : [(- 0.6), (- 0.05)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  fireworks_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fireworks_2', units : undefined, 
    image : 'fireworks.png', mask : undefined,
    ori : 0.0, pos : [0, (- 0.05)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  tree_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'tree_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.6, (- 0.05)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  text_17 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_17',
    text: 'A',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.6), (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  text_21 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_21',
    text: 'G',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  text_27 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_27',
    text: 'L',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.6, (- 0.25)], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -5.0 
  });
  
  practice_answer = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: 'Which image below did you see most often after clicking 1 at the apple image?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.2], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -8.0 
  });
  
  // Initialize components for Routine "feedback1"
  feedback1Clock = new util.Clock();
  text_10 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_10',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "memory_quiz"
  memory_quizClock = new util.Clock();
  text_75 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_75',
    text: 'During your learning about how to get from one picture to another, you will be tested on your learning.\n\nEvery so often, you will be asked to use what you’ve learned to try to reach an image where money is hiding. Each of these questions has a correct answer, and we will reward you at the end of the study based on how well you did on these questions. \n\nSpecifically, we will pick a total of 5 rounds at random from these rounds where you can earn reward to determine how much money you win\n\nPress space to continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_23 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "reminder_second_phase"
  reminder_second_phaseClock = new util.Clock();
  text_74 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_74',
    text: 'After you complete many rounds of learning how to navigate between pictures in the picture game, you will have a SECOND PHASE where you can earn more money based off what you learned!\n\nIMPORTANT to do well on both phases, it is vital to remember that during training, the image that leads the most times to another image NEVER CHANGES. For example, if in the beginning of the task, the apple image has the best chance to lead to the basket image, it will ALWAYS be the best image to get to the basket image. The probabilities between images are constant throughout the task.\n\nPress space for a quiz on the instructions',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_22 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions_quiz_1"
  instructions_quiz_1Clock = new util.Clock();
  text_43 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_43',
    text: 'Instructions Quiz\n\n1. What is the goal of the picture game?\n\na.to learn the type of picture\n\nb.to learn the meaning of pictures\n\nc.to learn which pictures you tend to see after making an initial choice at a starting image\n\nd.to learn how actions you take at a picture give you rewards or punishments',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.038,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_17 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions_quiz_2"
  instructions_quiz_2Clock = new util.Clock();
  text_70 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_70',
    text: 'Instructions Quiz\n\n1. How are the second and third images different from the first?\n\na. these images are different every time\n\nb.these images are new every time\n\nc. you get to select actions at the second and see how you get to the third image.\n\n\nd. you take no actions at these images.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.038,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_18 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions_quiz_3"
  instructions_quiz_3Clock = new util.Clock();
  text_71 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_71',
    text: 'Instructions Quiz\n\n1. What happens during the reward quiz?\n\na.you must recall how the pictures look\n\nb. you are told that a picture has money hiding in it, and you must choose the action that has the best chance of getting you there. 5 of these rounds the computer chooses AT RANDOM will determine how much money you win!\n\nc. you must recall images you most likely DO NOT see after taking an action at a starting image\n\nd. you are told that a picture has money hiding in it, and you must get those points regardess of how well you choose.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.038,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_19 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions_quiz_4"
  instructions_quiz_4Clock = new util.Clock();
  text_72 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_72',
    text: 'Instructions Quiz\n\n1. Your goal is to learn the how likely a certain image (e.g., basket) comes after a starting image (e.g., apple). The probabilities that determine transitions between images: \n\na. Change throughout the task, so the image that has the best chance to get you to the another image can CHANGE.\n\nb. NEVER CHANGE. Throughout the entire task, the probabilities that determine which image gets you to another image NEVER CHANGE. \n\nc. Are always 100%. If you want to get to the basket, there’s only one preceding image that could possibly get you there.\n\nd. Cannot be learned. The goal of the task is to guess which are the best images to get you to new images, because their probabilties are entirely random\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.038,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_20 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "result_quiz_instructions"
  result_quiz_instructionsClock = new util.Clock();
  result_q_instr = new visual.TextStim({
    win: psychoJS.window,
    name: 'result_q_instr',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "time_limit"
  time_limitClock = new util.Clock();
  text_102 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_102',
    text: 'You will have 7 SECONDS to click the arrow instructed on screen on each trial! If you fail to click within this time 5 times, you will be exited from the game without compensation. In order to avoid this, please make sure to do anything you need to complete now before starting the game, which will take around 80 minutes. Remember, you can earn more money once you start the game, so pay attention! \n\nPress space to continue to learning phase, and good luck!!!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions3"
  instructions3Clock = new util.Clock();
  text_7 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_7',
    text: 'Press SPACE to start learning!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Run 'Begin Experiment' code from code_20
  quiz1list = ["apple.png", "trident.png", "fireworks.png", "fox.png", "bowling.png"];
  quiz2list = ["window.png", "bell.png", "tree.png", "watch.png"];
  q1left_correct = ["1", "3", "5", "2", "7"];
  q1right_correct = ["2", "4", "7", "3", "8"];
  q2left_correct = ["5", "1", "6", "2"];
  q2right_correct = ["6", "3", "5", "4"];
  learning_reward_goal_list = learning_reward_goal_list = ["snorkel.png", "tophat.png", "houses.png", "north.png", "train.png", "hammer.png", "apple.png", "window.png", "compass.png", "tophat.png", "snorkel.png", "train.png", "north.png", "hammer.png", "apple.png", "houses.png", "compass.png", "window.png"];
  counter_reward_learning = 0;
  learning_reward_goal = learning_reward_goal_list[0];
  msg_new = "lost";
  action_list = ["left.png", "right.png"];
  quiz_counter = 0;
  num_quiz_trials = 10;
  stage2 = ["bell.png", "watch.png", "watch.png", "fox.png", "fireworks.png", "watch.png", "tree.png", "bowling.png"];
  stage3 = ["houses.png", "train.png", "thermometer.png", "compass.png", "north.png", "microphone.png", "tophat.png", "snorkel.png"];
  quizzes = [quiz1list, quiz2list];
  predictions1 = [stage2, stage2, stage3, stage3, stage3];
  predictions2 = [stage2, stage3, stage3, stage3];
  predictions = [predictions1, predictions2];
  trials_with_three = [11, 12, 13, 14, 15, 16];
  trials_with_four = [17, 18];
  incorrect_actions = 0;
  action = "left.png";
  trial_learning_num = 0;
  correct_quiz = "p";
  percent_correct = "";
  text_correct = "";
  
  // Initialize components for Routine "stage1"
  stage1Clock = new util.Clock();
  click_action = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_9 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_9',
    text: 'Choose the number below the image:',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  trident_start_learning = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trident_start_learning', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "incorrect_answer"
  incorrect_answerClock = new util.Clock();
  incorrect_display = new visual.TextStim({
    win: psychoJS.window,
    name: 'incorrect_display',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "stage2_2"
  stage2_2Clock = new util.Clock();
  click_action_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_108 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_108',
    text: 'Choose the number below the image:',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  trident_start_learning_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trident_start_learning_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  text_109 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_109',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.15)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "learning_trial_step2_to_step3"
  learning_trial_step2_to_step3Clock = new util.Clock();
  stage2_learning_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stage2_learning_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "memory_q"
  memory_qClock = new util.Clock();
  text_92 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_92',
    text: 'Memory quiz question next. Pay Attention!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "prediction4"
  prediction4Clock = new util.Clock();
  outcome4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'outcome4',
    text: 'Choose what most likley gets you to the following image',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.36], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  picture_reward_goal = new visual.ImageStim({
    win : psychoJS.window,
    name : 'picture_reward_goal', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0.17], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  resp4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  learning_rew_trident = new visual.ImageStim({
    win : psychoJS.window,
    name : 'learning_rew_trident', units : undefined, 
    image : 'trident.png', mask : undefined,
    ori : 0.0, pos : [(- 0.25), (- 0.1)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  learning_rew_planet = new visual.ImageStim({
    win : psychoJS.window,
    name : 'learning_rew_planet', units : undefined, 
    image : 'planet.png', mask : undefined,
    ori : 0.0, pos : [0.25, (- 0.1)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  text_79 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_79',
    text: '1',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.25), (- 0.3)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -6.0 
  });
  
  text_85 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_85',
    text: '9',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.25, (- 0.3)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -7.0 
  });
  
  // Initialize components for Routine "quiz_score"
  quiz_scoreClock = new util.Clock();
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.065,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "take_a_break"
  take_a_breakClock = new util.Clock();
  text_39 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_39',
    text: 'Next trial…',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "prediction5"
  prediction5Clock = new util.Clock();
  outcome4_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'outcome4_2',
    text: 'Choose action 2 or 8 that gets you to image below:',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.36], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  picture_reward_goal_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'picture_reward_goal_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0.17], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  resp4_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  learning_rew_trident_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'learning_rew_trident_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, (- 0.1)], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  text_80 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_80',
    text: 'From this starting image above',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "instructions_reward_stage"
  instructions_reward_stageClock = new util.Clock();
  instructions_rewardstage = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_rewardstage',
    text: 'Now it’s time to use what you learned to get rewards. Each time you enter the picture world to win money, you will be told which images will give you points! \n\nYou need to use this information plan and choose the sequence of TWO ACTIONS that’s most likely to get you points. You can choose them in forwards or backwards order depending on the direction in which you plan. \n\nPress Space to continue ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_11 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions_planning_2phase"
  instructions_planning_2phaseClock = new util.Clock();
  instructions_rewardstage_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_rewardstage_2',
    text: 'You can enter your two actions in a forward or backward direction. Forward would be first selecting 1 or 9 to get to planet and trident and then 2 or 8 to get to the final image.\n\nBackward would be the reverse: first 2 or 8 to get from the final to the second image, and the 1 or 9 to get back to your starting point at the trident or planet. This choice is up to you!\n\nPress Space to continue ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_35 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "i2_reward"
  i2_rewardClock = new util.Clock();
  text_42 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_42',
    text: '\nIMPORTANT: After you plan and enter 2 ACTIONS to get to images to try to win points, you will not see any more images aftewards. This prevents you from learning anything else at this phase, as you need to use what you already learned to plan accordingly. The computer will simulate which images you reached and calculate your points, but this will not be shown to you. Instead you will be told how many points you won after this phase is over.\n\nPress Space to Continue\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_9 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "practice_view_reward_info"
  practice_view_reward_infoClock = new util.Clock();
  im1_example_choicephase = new visual.ImageStim({
    win : psychoJS.window,
    name : 'im1_example_choicephase', units : undefined, 
    image : 'watch.png', mask : undefined,
    ori : 0.0, pos : [(- 0.3), 0], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  resp4_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  im2_example_choicephase = new visual.ImageStim({
    win : psychoJS.window,
    name : 'im2_example_choicephase', units : undefined, 
    image : 'tree.png', mask : undefined,
    ori : 0.0, pos : [0.3, 0], size : [0.25, 0.25],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  example_trial_choice_phase = new visual.TextStim({
    win: psychoJS.window,
    name: 'example_trial_choice_phase',
    text: 'An Example Trial',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.4], height: 0.055,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  im1_rewvalue = new visual.TextStim({
    win: psychoJS.window,
    name: 'im1_rewvalue',
    text: 'Win 2 points!',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.3), (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -5.0 
  });
  
  im2_rewvalue = new visual.TextStim({
    win: psychoJS.window,
    name: 'im2_rewvalue',
    text: 'Win 10 points!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.3, (- 0.2)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -6.0 
  });
  
  text_28 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_28',
    text: 'Press Space To Continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.25], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -7.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions_planning"
  instructions_planningClock = new util.Clock();
  text_66 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_66',
    text: 'When you have decided how to plan your actions , you will input the sequence of 2 actions to get you to the images with points:\n\nFor example, press 1 and then press 8.\n\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_12 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_24 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_24',
    text: 'Press Space to Continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.35)], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  // Initialize components for Routine "start_planning_trials"
  start_planning_trialsClock = new util.Clock();
  text_67 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_67',
    text: 'You are now ready to start the task, using the knowledge you learned about how to navigate through the pictures. Good luck!\n\nPress Space to begin',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.065,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_15 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "info_choicephase"
  info_choicephaseClock = new util.Clock();
  im1_planning = new visual.ImageStim({
    win : psychoJS.window,
    name : 'im1_planning', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.2), 0.15], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  im2_planning = new visual.ImageStim({
    win : psychoJS.window,
    name : 'im2_planning', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.2, 0.15], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  example_trial_choice_phase_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'example_trial_choice_phase_2',
    text: 'Reward information for upcoming trial:',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.35], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  im1_rewvalue_planning = new visual.TextStim({
    win: psychoJS.window,
    name: 'im1_rewvalue_planning',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.2), 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  im2_rewvalue_planning = new visual.TextStim({
    win: psychoJS.window,
    name: 'im2_rewvalue_planning',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.2, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -5.0 
  });
  
  text_29 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_29',
    text: 'Press Space To Continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.45)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -6.0 
  });
  
  key_resp_24 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  im3_planning = new visual.ImageStim({
    win : psychoJS.window,
    name : 'im3_planning', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.2), (- 0.2)], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  im4_planning = new visual.ImageStim({
    win : psychoJS.window,
    name : 'im4_planning', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.2, (- 0.2)], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -9.0 
  });
  im3_num_planning = new visual.TextStim({
    win: psychoJS.window,
    name: 'im3_num_planning',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.2), (- 0.35)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -10.0 
  });
  
  im4_num_planning = new visual.TextStim({
    win: psychoJS.window,
    name: 'im4_num_planning',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.2, (- 0.35)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -11.0 
  });
  
  // Initialize components for Routine "stage1_choice_enact"
  stage1_choice_enactClock = new util.Clock();
  text_81 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_81',
    text: 'Press two actions in sequence:',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_25 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "stage2_choice_enact"
  stage2_choice_enactClock = new util.Clock();
  text_82 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_82',
    text: 'Press two actions in sequence:',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_36 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "final_stage5"
  final_stage5Clock = new util.Clock();
  text_68 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_68',
    text: 'Computer simulating images to calculate reward…',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_30 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_30',
    text: 'You will find out your reward total after all this phase is completed.\n\nPress Space to Continue to Next Trial',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_16 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "transition_revaluation"
  transition_revaluationClock = new util.Clock();
  text_25 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_25',
    text: 'BONUS ROUND',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_26 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_26',
    text: 'The picture world you learned has CHANGED! Now, the TRIDENT leads only to the WATCH, and the PLANET leads only to the FOX. Look below and use this new information to win more money next!\n\n\n ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.2], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  trident_reval = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trident_reval', units : undefined, 
    image : 'trident.png', mask : undefined,
    ori : 0.0, pos : [(- 0.2), 0], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  watch_reval = new visual.ImageStim({
    win : psychoJS.window,
    name : 'watch_reval', units : undefined, 
    image : 'watch.png', mask : undefined,
    ori : 0.0, pos : [0.2, 0], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  right_arrow = new visual.ImageStim({
    win : psychoJS.window,
    name : 'right_arrow', units : undefined, 
    image : 'right.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.16, 0.16],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  planet_reval = new visual.ImageStim({
    win : psychoJS.window,
    name : 'planet_reval', units : undefined, 
    image : 'planet.png', mask : undefined,
    ori : 0.0, pos : [(- 0.2), (- 0.25)], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  right_arrow2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'right_arrow2', units : undefined, 
    image : 'right.png', mask : undefined,
    ori : 0.0, pos : [0, (- 0.25)], size : [0.16, 0.16],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  fox_reval = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fox_reval', units : undefined, 
    image : 'fox.png', mask : undefined,
    ori : 0.0, pos : [0.2, (- 0.25)], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -9.0 
  });
  text_94 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_94',
    text: 'Press Space to continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -10.0 
  });
  
  // Initialize components for Routine "info_choice_revaluation_2"
  info_choice_revaluation_2Clock = new util.Clock();
  im1_planning_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'im1_planning_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.2), 0], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  im2_planning_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'im2_planning_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.2, 0.0], size : [0.2, 0.2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  example_trial_choice_phase_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'example_trial_choice_phase_4',
    text: 'Reward information for upcoming trial:',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.35], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  im1_rewvalue_planning_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'im1_rewvalue_planning_2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.2), (- 0.15)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  im2_rewvalue_planning_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'im2_rewvalue_planning_2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.2, (- 0.15)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -5.0 
  });
  
  text_93 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_93',
    text: 'Press Space To Continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -6.0 
  });
  
  key_resp_29 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "choice_transistion_reval"
  choice_transistion_revalClock = new util.Clock();
  text_105 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_105',
    text: 'Press two actions in sequence:',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  transition_reval_choice = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "choice_transition2"
  choice_transition2Clock = new util.Clock();
  text_106 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_106',
    text: 'Press two actions in sequence:',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  transition_reval_choice_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "final_stage_Tr"
  final_stage_TrClock = new util.Clock();
  text_103 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_103',
    text: 'Computer simulating images to calculate reward…',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_104 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_104',
    text: 'You will find out your reward total after all this phase is completed.\n\nPress Space to Continue to Next Trial',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_34 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "reward_total"
  reward_totalClock = new util.Clock();
  text_84 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_84',
    text: 'Congrats! Your bonus points will be calculated soon and delivered to you on Prolific!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "done"
  doneClock = new util.Clock();
  text_62 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_62',
    text: 'Thank you for participating!\n\nYou will be granted credit on Prolific within the next week.  ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var instructions_get_right;
function instructions_get_rightLoopBegin(instructions_get_rightLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    instructions_get_right = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 500, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'instructions_get_right'
    });
    psychoJS.experiment.addLoop(instructions_get_right); // add the loop to the experiment
    currentLoop = instructions_get_right;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisInstructions_get_right of instructions_get_right) {
      snapshot = instructions_get_right.getSnapshot();
      instructions_get_rightLoopScheduler.add(importConditions(snapshot));
      instructions_get_rightLoopScheduler.add(consentRoutineBegin(snapshot));
      instructions_get_rightLoopScheduler.add(consentRoutineEachFrame());
      instructions_get_rightLoopScheduler.add(consentRoutineEnd(snapshot));
      instructions_get_rightLoopScheduler.add(consent1RoutineBegin(snapshot));
      instructions_get_rightLoopScheduler.add(consent1RoutineEachFrame());
      instructions_get_rightLoopScheduler.add(consent1RoutineEnd(snapshot));
      instructions_get_rightLoopScheduler.add(instructionsRoutineBegin(snapshot));
      instructions_get_rightLoopScheduler.add(instructionsRoutineEachFrame());
      instructions_get_rightLoopScheduler.add(instructionsRoutineEnd(snapshot));
      instructions_get_rightLoopScheduler.add(instruction2RoutineBegin(snapshot));
      instructions_get_rightLoopScheduler.add(instruction2RoutineEachFrame());
      instructions_get_rightLoopScheduler.add(instruction2RoutineEnd(snapshot));
      instructions_get_rightLoopScheduler.add(stage1_instructionsRoutineBegin(snapshot));
      instructions_get_rightLoopScheduler.add(stage1_instructionsRoutineEachFrame());
      instructions_get_rightLoopScheduler.add(stage1_instructionsRoutineEnd(snapshot));
      instructions_get_rightLoopScheduler.add(stage2_4_instructionsRoutineBegin(snapshot));
      instructions_get_rightLoopScheduler.add(stage2_4_instructionsRoutineEachFrame());
      instructions_get_rightLoopScheduler.add(stage2_4_instructionsRoutineEnd(snapshot));
      const practice_loopLoopScheduler = new Scheduler(psychoJS);
      instructions_get_rightLoopScheduler.add(practice_loopLoopBegin(practice_loopLoopScheduler, snapshot));
      instructions_get_rightLoopScheduler.add(practice_loopLoopScheduler);
      instructions_get_rightLoopScheduler.add(practice_loopLoopEnd);
      instructions_get_rightLoopScheduler.add(memory_quizRoutineBegin(snapshot));
      instructions_get_rightLoopScheduler.add(memory_quizRoutineEachFrame());
      instructions_get_rightLoopScheduler.add(memory_quizRoutineEnd(snapshot));
      instructions_get_rightLoopScheduler.add(reminder_second_phaseRoutineBegin(snapshot));
      instructions_get_rightLoopScheduler.add(reminder_second_phaseRoutineEachFrame());
      instructions_get_rightLoopScheduler.add(reminder_second_phaseRoutineEnd(snapshot));
      instructions_get_rightLoopScheduler.add(instructions_quiz_1RoutineBegin(snapshot));
      instructions_get_rightLoopScheduler.add(instructions_quiz_1RoutineEachFrame());
      instructions_get_rightLoopScheduler.add(instructions_quiz_1RoutineEnd(snapshot));
      instructions_get_rightLoopScheduler.add(instructions_quiz_2RoutineBegin(snapshot));
      instructions_get_rightLoopScheduler.add(instructions_quiz_2RoutineEachFrame());
      instructions_get_rightLoopScheduler.add(instructions_quiz_2RoutineEnd(snapshot));
      instructions_get_rightLoopScheduler.add(instructions_quiz_3RoutineBegin(snapshot));
      instructions_get_rightLoopScheduler.add(instructions_quiz_3RoutineEachFrame());
      instructions_get_rightLoopScheduler.add(instructions_quiz_3RoutineEnd(snapshot));
      instructions_get_rightLoopScheduler.add(instructions_quiz_4RoutineBegin(snapshot));
      instructions_get_rightLoopScheduler.add(instructions_quiz_4RoutineEachFrame());
      instructions_get_rightLoopScheduler.add(instructions_quiz_4RoutineEnd(snapshot));
      instructions_get_rightLoopScheduler.add(result_quiz_instructionsRoutineBegin(snapshot));
      instructions_get_rightLoopScheduler.add(result_quiz_instructionsRoutineEachFrame());
      instructions_get_rightLoopScheduler.add(result_quiz_instructionsRoutineEnd(snapshot));
      instructions_get_rightLoopScheduler.add(instructions_get_rightLoopEndIteration(instructions_get_rightLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var practice_loop;
function practice_loopLoopBegin(practice_loopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practice_loop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 500, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'practice_loop'
    });
    psychoJS.experiment.addLoop(practice_loop); // add the loop to the experiment
    currentLoop = practice_loop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPractice_loop of practice_loop) {
      snapshot = practice_loop.getSnapshot();
      practice_loopLoopScheduler.add(importConditions(snapshot));
      const trials_3LoopScheduler = new Scheduler(psychoJS);
      practice_loopLoopScheduler.add(trials_3LoopBegin(trials_3LoopScheduler, snapshot));
      practice_loopLoopScheduler.add(trials_3LoopScheduler);
      practice_loopLoopScheduler.add(trials_3LoopEnd);
      practice_loopLoopScheduler.add(quiz_practiceRoutineBegin(snapshot));
      practice_loopLoopScheduler.add(quiz_practiceRoutineEachFrame());
      practice_loopLoopScheduler.add(quiz_practiceRoutineEnd(snapshot));
      practice_loopLoopScheduler.add(feedback1RoutineBegin(snapshot));
      practice_loopLoopScheduler.add(feedback1RoutineEachFrame());
      practice_loopLoopScheduler.add(feedback1RoutineEnd(snapshot));
      practice_loopLoopScheduler.add(practice_loopLoopEndIteration(practice_loopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var trials_3;
function trials_3LoopBegin(trials_3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'stage2_4_practice.csv',
      seed: undefined, name: 'trials_3'
    });
    psychoJS.experiment.addLoop(trials_3); // add the loop to the experiment
    currentLoop = trials_3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_3 of trials_3) {
      snapshot = trials_3.getSnapshot();
      trials_3LoopScheduler.add(importConditions(snapshot));
      trials_3LoopScheduler.add(stage_2_4_practiceRoutineBegin(snapshot));
      trials_3LoopScheduler.add(stage_2_4_practiceRoutineEachFrame());
      trials_3LoopScheduler.add(stage_2_4_practiceRoutineEnd(snapshot));
      trials_3LoopScheduler.add(stage_2_4_practice_resultRoutineBegin(snapshot));
      trials_3LoopScheduler.add(stage_2_4_practice_resultRoutineEachFrame());
      trials_3LoopScheduler.add(stage_2_4_practice_resultRoutineEnd(snapshot));
      trials_3LoopScheduler.add(trials_3LoopEndIteration(trials_3LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function practice_loopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practice_loop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practice_loopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function instructions_get_rightLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(instructions_get_right);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function instructions_get_rightLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'new_trials.csv',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial of trials) {
      snapshot = trials.getSnapshot();
      trialsLoopScheduler.add(importConditions(snapshot));
      const action_selectionLoopScheduler = new Scheduler(psychoJS);
      trialsLoopScheduler.add(action_selectionLoopBegin(action_selectionLoopScheduler, snapshot));
      trialsLoopScheduler.add(action_selectionLoopScheduler);
      trialsLoopScheduler.add(action_selectionLoopEnd);
      trialsLoopScheduler.add(stage2_2RoutineBegin(snapshot));
      trialsLoopScheduler.add(stage2_2RoutineEachFrame());
      trialsLoopScheduler.add(stage2_2RoutineEnd(snapshot));
      trialsLoopScheduler.add(learning_trial_step2_to_step3RoutineBegin(snapshot));
      trialsLoopScheduler.add(learning_trial_step2_to_step3RoutineEachFrame());
      trialsLoopScheduler.add(learning_trial_step2_to_step3RoutineEnd(snapshot));
      trialsLoopScheduler.add(memory_qRoutineBegin(snapshot));
      trialsLoopScheduler.add(memory_qRoutineEachFrame());
      trialsLoopScheduler.add(memory_qRoutineEnd(snapshot));
      trialsLoopScheduler.add(prediction4RoutineBegin(snapshot));
      trialsLoopScheduler.add(prediction4RoutineEachFrame());
      trialsLoopScheduler.add(prediction4RoutineEnd(snapshot));
      trialsLoopScheduler.add(quiz_scoreRoutineBegin(snapshot));
      trialsLoopScheduler.add(quiz_scoreRoutineEachFrame());
      trialsLoopScheduler.add(quiz_scoreRoutineEnd(snapshot));
      trialsLoopScheduler.add(take_a_breakRoutineBegin(snapshot));
      trialsLoopScheduler.add(take_a_breakRoutineEachFrame());
      trialsLoopScheduler.add(take_a_breakRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var action_selection;
function action_selectionLoopBegin(action_selectionLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    action_selection = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 999, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'action_selection'
    });
    psychoJS.experiment.addLoop(action_selection); // add the loop to the experiment
    currentLoop = action_selection;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisAction_selection of action_selection) {
      snapshot = action_selection.getSnapshot();
      action_selectionLoopScheduler.add(importConditions(snapshot));
      action_selectionLoopScheduler.add(stage1RoutineBegin(snapshot));
      action_selectionLoopScheduler.add(stage1RoutineEachFrame());
      action_selectionLoopScheduler.add(stage1RoutineEnd(snapshot));
      action_selectionLoopScheduler.add(incorrect_answerRoutineBegin(snapshot));
      action_selectionLoopScheduler.add(incorrect_answerRoutineEachFrame());
      action_selectionLoopScheduler.add(incorrect_answerRoutineEnd(snapshot));
      action_selectionLoopScheduler.add(action_selectionLoopEndIteration(action_selectionLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function action_selectionLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(action_selection);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function action_selectionLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials_2;
function trials_2LoopBegin(trials_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'action2_loop.csv',
      seed: undefined, name: 'trials_2'
    });
    psychoJS.experiment.addLoop(trials_2); // add the loop to the experiment
    currentLoop = trials_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_2 of trials_2) {
      snapshot = trials_2.getSnapshot();
      trials_2LoopScheduler.add(importConditions(snapshot));
      trials_2LoopScheduler.add(prediction5RoutineBegin(snapshot));
      trials_2LoopScheduler.add(prediction5RoutineEachFrame());
      trials_2LoopScheduler.add(prediction5RoutineEnd(snapshot));
      trials_2LoopScheduler.add(trials_2LoopEndIteration(trials_2LoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function trials_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trials_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var PR_vs_SR;
function PR_vs_SRLoopBegin(PR_vs_SRLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    PR_vs_SR = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'new_choicephase.xlsx',
      seed: undefined, name: 'PR_vs_SR'
    });
    psychoJS.experiment.addLoop(PR_vs_SR); // add the loop to the experiment
    currentLoop = PR_vs_SR;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisPR_vs_SR of PR_vs_SR) {
      snapshot = PR_vs_SR.getSnapshot();
      PR_vs_SRLoopScheduler.add(importConditions(snapshot));
      PR_vs_SRLoopScheduler.add(info_choicephaseRoutineBegin(snapshot));
      PR_vs_SRLoopScheduler.add(info_choicephaseRoutineEachFrame());
      PR_vs_SRLoopScheduler.add(info_choicephaseRoutineEnd(snapshot));
      PR_vs_SRLoopScheduler.add(stage1_choice_enactRoutineBegin(snapshot));
      PR_vs_SRLoopScheduler.add(stage1_choice_enactRoutineEachFrame());
      PR_vs_SRLoopScheduler.add(stage1_choice_enactRoutineEnd(snapshot));
      PR_vs_SRLoopScheduler.add(stage2_choice_enactRoutineBegin(snapshot));
      PR_vs_SRLoopScheduler.add(stage2_choice_enactRoutineEachFrame());
      PR_vs_SRLoopScheduler.add(stage2_choice_enactRoutineEnd(snapshot));
      PR_vs_SRLoopScheduler.add(final_stage5RoutineBegin(snapshot));
      PR_vs_SRLoopScheduler.add(final_stage5RoutineEachFrame());
      PR_vs_SRLoopScheduler.add(final_stage5RoutineEnd(snapshot));
      PR_vs_SRLoopScheduler.add(PR_vs_SRLoopEndIteration(PR_vs_SRLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function PR_vs_SRLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(PR_vs_SR);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function PR_vs_SRLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var transition_revaluation_round;
function transition_revaluation_roundLoopBegin(transition_revaluation_roundLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    transition_revaluation_round = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'choicephase_afterevaluation.xlsx',
      seed: undefined, name: 'transition_revaluation_round'
    });
    psychoJS.experiment.addLoop(transition_revaluation_round); // add the loop to the experiment
    currentLoop = transition_revaluation_round;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTransition_revaluation_round of transition_revaluation_round) {
      snapshot = transition_revaluation_round.getSnapshot();
      transition_revaluation_roundLoopScheduler.add(importConditions(snapshot));
      transition_revaluation_roundLoopScheduler.add(info_choice_revaluation_2RoutineBegin(snapshot));
      transition_revaluation_roundLoopScheduler.add(info_choice_revaluation_2RoutineEachFrame());
      transition_revaluation_roundLoopScheduler.add(info_choice_revaluation_2RoutineEnd(snapshot));
      transition_revaluation_roundLoopScheduler.add(choice_transistion_revalRoutineBegin(snapshot));
      transition_revaluation_roundLoopScheduler.add(choice_transistion_revalRoutineEachFrame());
      transition_revaluation_roundLoopScheduler.add(choice_transistion_revalRoutineEnd(snapshot));
      transition_revaluation_roundLoopScheduler.add(choice_transition2RoutineBegin(snapshot));
      transition_revaluation_roundLoopScheduler.add(choice_transition2RoutineEachFrame());
      transition_revaluation_roundLoopScheduler.add(choice_transition2RoutineEnd(snapshot));
      transition_revaluation_roundLoopScheduler.add(final_stage_TrRoutineBegin(snapshot));
      transition_revaluation_roundLoopScheduler.add(final_stage_TrRoutineEachFrame());
      transition_revaluation_roundLoopScheduler.add(final_stage_TrRoutineEnd(snapshot));
      transition_revaluation_roundLoopScheduler.add(transition_revaluation_roundLoopEndIteration(transition_revaluation_roundLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function transition_revaluation_roundLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(transition_revaluation_round);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function transition_revaluation_roundLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var t;
var frameN;
var continueRoutine;
var _consent1_next_allKeys;
var consentComponents;
function consentRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'consent' ---
    t = 0;
    consentClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    image_11.setImage('consent1.png');
    consent1_next.keys = undefined;
    consent1_next.rt = undefined;
    _consent1_next_allKeys = [];
    // keep track of which components have finished
    consentComponents = [];
    consentComponents.push(image_11);
    consentComponents.push(consent1_next);
    consentComponents.push(text_89);
    
    for (const thisComponent of consentComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function consentRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'consent' ---
    // get current time
    t = consentClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_11* updates
    if (t >= 0.0 && image_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_11.tStart = t;  // (not accounting for frame time here)
      image_11.frameNStart = frameN;  // exact frame index
      
      image_11.setAutoDraw(true);
    }

    
    // *consent1_next* updates
    if (t >= 0.0 && consent1_next.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consent1_next.tStart = t;  // (not accounting for frame time here)
      consent1_next.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { consent1_next.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { consent1_next.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { consent1_next.clearEvents(); });
    }

    if (consent1_next.status === PsychoJS.Status.STARTED) {
      let theseKeys = consent1_next.getKeys({keyList: ['space'], waitRelease: false});
      _consent1_next_allKeys = _consent1_next_allKeys.concat(theseKeys);
      if (_consent1_next_allKeys.length > 0) {
        consent1_next.keys = _consent1_next_allKeys[_consent1_next_allKeys.length - 1].name;  // just the last key pressed
        consent1_next.rt = _consent1_next_allKeys[_consent1_next_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_89* updates
    if (t >= 0.0 && text_89.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_89.tStart = t;  // (not accounting for frame time here)
      text_89.frameNStart = frameN;  // exact frame index
      
      text_89.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of consentComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function consentRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'consent' ---
    for (const thisComponent of consentComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(consent1_next.corr, level);
    }
    psychoJS.experiment.addData('consent1_next.keys', consent1_next.keys);
    if (typeof consent1_next.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('consent1_next.rt', consent1_next.rt);
        routineTimer.reset();
        }
    
    consent1_next.stop();
    // the Routine "consent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _consent1_next_2_allKeys;
var consent1Components;
function consent1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'consent1' ---
    t = 0;
    consent1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    image_13.setImage('consent2.png');
    consent1_next_2.keys = undefined;
    consent1_next_2.rt = undefined;
    _consent1_next_2_allKeys = [];
    // keep track of which components have finished
    consent1Components = [];
    consent1Components.push(image_13);
    consent1Components.push(consent1_next_2);
    consent1Components.push(text_90);
    
    for (const thisComponent of consent1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function consent1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'consent1' ---
    // get current time
    t = consent1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_13* updates
    if (t >= 0.0 && image_13.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_13.tStart = t;  // (not accounting for frame time here)
      image_13.frameNStart = frameN;  // exact frame index
      
      image_13.setAutoDraw(true);
    }

    
    // *consent1_next_2* updates
    if (t >= 0.0 && consent1_next_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      consent1_next_2.tStart = t;  // (not accounting for frame time here)
      consent1_next_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { consent1_next_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { consent1_next_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { consent1_next_2.clearEvents(); });
    }

    if (consent1_next_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = consent1_next_2.getKeys({keyList: ['y', 'n'], waitRelease: false});
      _consent1_next_2_allKeys = _consent1_next_2_allKeys.concat(theseKeys);
      if (_consent1_next_2_allKeys.length > 0) {
        consent1_next_2.keys = _consent1_next_2_allKeys[_consent1_next_2_allKeys.length - 1].name;  // just the last key pressed
        consent1_next_2.rt = _consent1_next_2_allKeys[_consent1_next_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_90* updates
    if (t >= 0.0 && text_90.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_90.tStart = t;  // (not accounting for frame time here)
      text_90.frameNStart = frameN;  // exact frame index
      
      text_90.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of consent1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function consent1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'consent1' ---
    for (const thisComponent of consent1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(consent1_next_2.corr, level);
    }
    psychoJS.experiment.addData('consent1_next_2.keys', consent1_next_2.keys);
    if (typeof consent1_next_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('consent1_next_2.rt', consent1_next_2.rt);
        routineTimer.reset();
        }
    
    consent1_next_2.stop();
    // Run 'End Routine' code from code_19
    if ((consent1_next_2.keys === "n")) {
        psychoJS.quit();
    }
    
    // the Routine "consent1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_allKeys;
var instructionsComponents;
function instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions' ---
    t = 0;
    instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    instructionsComponents = [];
    instructionsComponents.push(text);
    instructionsComponents.push(key_resp);
    
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions' ---
    // get current time
    t = instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions' ---
    for (const thisComponent of instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp.stop();
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_2_allKeys;
var instruction2Components;
function instruction2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instruction2' ---
    t = 0;
    instruction2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    instruction2Components = [];
    instruction2Components.push(key_resp_2);
    instruction2Components.push(text_2);
    
    for (const thisComponent of instruction2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instruction2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instruction2' ---
    // get current time
    t = instruction2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instruction2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instruction2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instruction2' ---
    for (const thisComponent of instruction2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp_2.stop();
    // the Routine "instruction2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _keyboard_entry_instr1_allKeys;
var stage1_instructionsComponents;
function stage1_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'stage1_instructions' ---
    t = 0;
    stage1_instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    keyboard_entry_instr1.keys = undefined;
    keyboard_entry_instr1.rt = undefined;
    _keyboard_entry_instr1_allKeys = [];
    // keep track of which components have finished
    stage1_instructionsComponents = [];
    stage1_instructionsComponents.push(keyboard_entry_instr1);
    stage1_instructionsComponents.push(start_instr1);
    stage1_instructionsComponents.push(trident_start);
    stage1_instructionsComponents.push(planet_start);
    stage1_instructionsComponents.push(instructions_decisionrules);
    stage1_instructionsComponents.push(space_continue_instr1);
    stage1_instructionsComponents.push(one);
    stage1_instructionsComponents.push(nine);
    
    for (const thisComponent of stage1_instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function stage1_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'stage1_instructions' ---
    // get current time
    t = stage1_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *keyboard_entry_instr1* updates
    if (t >= 0 && keyboard_entry_instr1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      keyboard_entry_instr1.tStart = t;  // (not accounting for frame time here)
      keyboard_entry_instr1.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { keyboard_entry_instr1.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { keyboard_entry_instr1.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { keyboard_entry_instr1.clearEvents(); });
    }

    if (keyboard_entry_instr1.status === PsychoJS.Status.STARTED) {
      let theseKeys = keyboard_entry_instr1.getKeys({keyList: ['space'], waitRelease: false});
      _keyboard_entry_instr1_allKeys = _keyboard_entry_instr1_allKeys.concat(theseKeys);
      if (_keyboard_entry_instr1_allKeys.length > 0) {
        keyboard_entry_instr1.keys = _keyboard_entry_instr1_allKeys[_keyboard_entry_instr1_allKeys.length - 1].name;  // just the last key pressed
        keyboard_entry_instr1.rt = _keyboard_entry_instr1_allKeys[_keyboard_entry_instr1_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *start_instr1* updates
    if (t >= 0.0 && start_instr1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_instr1.tStart = t;  // (not accounting for frame time here)
      start_instr1.frameNStart = frameN;  // exact frame index
      
      start_instr1.setAutoDraw(true);
    }

    
    // *trident_start* updates
    if (t >= 0.0 && trident_start.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trident_start.tStart = t;  // (not accounting for frame time here)
      trident_start.frameNStart = frameN;  // exact frame index
      
      trident_start.setAutoDraw(true);
    }

    
    // *planet_start* updates
    if (t >= 0.0 && planet_start.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      planet_start.tStart = t;  // (not accounting for frame time here)
      planet_start.frameNStart = frameN;  // exact frame index
      
      planet_start.setAutoDraw(true);
    }

    
    // *instructions_decisionrules* updates
    if (t >= 0.0 && instructions_decisionrules.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_decisionrules.tStart = t;  // (not accounting for frame time here)
      instructions_decisionrules.frameNStart = frameN;  // exact frame index
      
      instructions_decisionrules.setAutoDraw(true);
    }

    
    // *space_continue_instr1* updates
    if (t >= 0.0 && space_continue_instr1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_continue_instr1.tStart = t;  // (not accounting for frame time here)
      space_continue_instr1.frameNStart = frameN;  // exact frame index
      
      space_continue_instr1.setAutoDraw(true);
    }

    
    // *one* updates
    if (t >= 0.0 && one.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      one.tStart = t;  // (not accounting for frame time here)
      one.frameNStart = frameN;  // exact frame index
      
      one.setAutoDraw(true);
    }

    
    // *nine* updates
    if (t >= 0.0 && nine.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      nine.tStart = t;  // (not accounting for frame time here)
      nine.frameNStart = frameN;  // exact frame index
      
      nine.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of stage1_instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stage1_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'stage1_instructions' ---
    for (const thisComponent of stage1_instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    keyboard_entry_instr1.stop();
    // the Routine "stage1_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _responseleft_allKeys;
var stage2_4_instructionsComponents;
function stage2_4_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'stage2_4_instructions' ---
    t = 0;
    stage2_4_instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    responseleft.keys = undefined;
    responseleft.rt = undefined;
    _responseleft_allKeys = [];
    // keep track of which components have finished
    stage2_4_instructionsComponents = [];
    stage2_4_instructionsComponents.push(responseleft);
    stage2_4_instructionsComponents.push(text_4);
    
    for (const thisComponent of stage2_4_instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function stage2_4_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'stage2_4_instructions' ---
    // get current time
    t = stage2_4_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *responseleft* updates
    if (t >= 0.2 && responseleft.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      responseleft.tStart = t;  // (not accounting for frame time here)
      responseleft.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { responseleft.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { responseleft.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { responseleft.clearEvents(); });
    }

    if (responseleft.status === PsychoJS.Status.STARTED) {
      let theseKeys = responseleft.getKeys({keyList: ['space'], waitRelease: false});
      _responseleft_allKeys = _responseleft_allKeys.concat(theseKeys);
      if (_responseleft_allKeys.length > 0) {
        responseleft.keys = _responseleft_allKeys[_responseleft_allKeys.length - 1].name;  // just the last key pressed
        responseleft.rt = _responseleft_allKeys[_responseleft_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of stage2_4_instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stage2_4_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'stage2_4_instructions' ---
    for (const thisComponent of stage2_4_instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    responseleft.stop();
    // the Routine "stage2_4_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_10_allKeys;
var stage_2_4_practiceComponents;
function stage_2_4_practiceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'stage_2_4_practice' ---
    t = 0;
    stage_2_4_practiceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    image_22.setImage('apple.png');
    key_resp_10.keys = undefined;
    key_resp_10.rt = undefined;
    _key_resp_10_allKeys = [];
    // keep track of which components have finished
    stage_2_4_practiceComponents = [];
    stage_2_4_practiceComponents.push(image_22);
    stage_2_4_practiceComponents.push(key_resp_10);
    stage_2_4_practiceComponents.push(text_40);
    
    for (const thisComponent of stage_2_4_practiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function stage_2_4_practiceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'stage_2_4_practice' ---
    // get current time
    t = stage_2_4_practiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_22* updates
    if (t >= 0.0 && image_22.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_22.tStart = t;  // (not accounting for frame time here)
      image_22.frameNStart = frameN;  // exact frame index
      
      image_22.setAutoDraw(true);
    }

    
    // *key_resp_10* updates
    if (t >= 0.2 && key_resp_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_10.tStart = t;  // (not accounting for frame time here)
      key_resp_10.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_10.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_10.clearEvents(); });
    }

    if (key_resp_10.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_10.getKeys({keyList: [1, '1'], waitRelease: false});
      _key_resp_10_allKeys = _key_resp_10_allKeys.concat(theseKeys);
      if (_key_resp_10_allKeys.length > 0) {
        key_resp_10.keys = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].name;  // just the last key pressed
        key_resp_10.rt = _key_resp_10_allKeys[_key_resp_10_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_40* updates
    if (t >= 0.0 && text_40.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_40.tStart = t;  // (not accounting for frame time here)
      text_40.frameNStart = frameN;  // exact frame index
      
      text_40.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of stage_2_4_practiceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stage_2_4_practiceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'stage_2_4_practice' ---
    for (const thisComponent of stage_2_4_practiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_10.corr, level);
    }
    psychoJS.experiment.addData('key_resp_10.keys', key_resp_10.keys);
    if (typeof key_resp_10.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_10.rt', key_resp_10.rt);
        routineTimer.reset();
        }
    
    key_resp_10.stop();
    // the Routine "stage_2_4_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var stage_2_4_practice_resultComponents;
function stage_2_4_practice_resultRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'stage_2_4_practice_result' ---
    t = 0;
    stage_2_4_practice_resultClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.800000);
    // update component parameters for each repeat
    image_20.setImage(image_prac1);
    image_12.setImage(image_prac2);
    // keep track of which components have finished
    stage_2_4_practice_resultComponents = [];
    stage_2_4_practice_resultComponents.push(image_20);
    stage_2_4_practice_resultComponents.push(text_76);
    stage_2_4_practice_resultComponents.push(image_12);
    stage_2_4_practice_resultComponents.push(text_77);
    
    for (const thisComponent of stage_2_4_practice_resultComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function stage_2_4_practice_resultRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'stage_2_4_practice_result' ---
    // get current time
    t = stage_2_4_practice_resultClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_20* updates
    if (t >= 0.0 && image_20.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_20.tStart = t;  // (not accounting for frame time here)
      image_20.frameNStart = frameN;  // exact frame index
      
      image_20.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_20.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_20.setAutoDraw(false);
    }
    
    // *text_76* updates
    if (t >= 1.6 && text_76.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_76.tStart = t;  // (not accounting for frame time here)
      text_76.frameNStart = frameN;  // exact frame index
      
      text_76.setAutoDraw(true);
    }

    frameRemains = 1.6 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_76.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_76.setAutoDraw(false);
    }
    
    // *image_12* updates
    if (t >= 3.2 && image_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_12.tStart = t;  // (not accounting for frame time here)
      image_12.frameNStart = frameN;  // exact frame index
      
      image_12.setAutoDraw(true);
    }

    frameRemains = 3.2 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (image_12.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_12.setAutoDraw(false);
    }
    
    // *text_77* updates
    if (t >= 4.8 && text_77.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_77.tStart = t;  // (not accounting for frame time here)
      text_77.frameNStart = frameN;  // exact frame index
      
      text_77.setAutoDraw(true);
    }

    frameRemains = 4.8 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_77.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_77.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of stage_2_4_practice_resultComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stage_2_4_practice_resultRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'stage_2_4_practice_result' ---
    for (const thisComponent of stage_2_4_practice_resultComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _practice_answer_allKeys;
var quiz_practiceComponents;
function quiz_practiceRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'quiz_practice' ---
    t = 0;
    quiz_practiceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    tree_2.setImage('tree.png');
    practice_answer.keys = undefined;
    practice_answer.rt = undefined;
    _practice_answer_allKeys = [];
    // keep track of which components have finished
    quiz_practiceComponents = [];
    quiz_practiceComponents.push(basket_2);
    quiz_practiceComponents.push(fireworks_2);
    quiz_practiceComponents.push(tree_2);
    quiz_practiceComponents.push(text_17);
    quiz_practiceComponents.push(text_21);
    quiz_practiceComponents.push(text_27);
    quiz_practiceComponents.push(practice_answer);
    quiz_practiceComponents.push(text_6);
    
    for (const thisComponent of quiz_practiceComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function quiz_practiceRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'quiz_practice' ---
    // get current time
    t = quiz_practiceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *basket_2* updates
    if (t >= 0.0 && basket_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      basket_2.tStart = t;  // (not accounting for frame time here)
      basket_2.frameNStart = frameN;  // exact frame index
      
      basket_2.setAutoDraw(true);
    }

    
    // *fireworks_2* updates
    if (t >= 0.0 && fireworks_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fireworks_2.tStart = t;  // (not accounting for frame time here)
      fireworks_2.frameNStart = frameN;  // exact frame index
      
      fireworks_2.setAutoDraw(true);
    }

    
    // *tree_2* updates
    if (t >= 0.0 && tree_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tree_2.tStart = t;  // (not accounting for frame time here)
      tree_2.frameNStart = frameN;  // exact frame index
      
      tree_2.setAutoDraw(true);
    }

    
    // *text_17* updates
    if (t >= 0.0 && text_17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_17.tStart = t;  // (not accounting for frame time here)
      text_17.frameNStart = frameN;  // exact frame index
      
      text_17.setAutoDraw(true);
    }

    
    // *text_21* updates
    if (t >= 0.0 && text_21.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_21.tStart = t;  // (not accounting for frame time here)
      text_21.frameNStart = frameN;  // exact frame index
      
      text_21.setAutoDraw(true);
    }

    
    // *text_27* updates
    if (t >= 0.0 && text_27.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_27.tStart = t;  // (not accounting for frame time here)
      text_27.frameNStart = frameN;  // exact frame index
      
      text_27.setAutoDraw(true);
    }

    
    // *practice_answer* updates
    if (t >= 0.0 && practice_answer.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      practice_answer.tStart = t;  // (not accounting for frame time here)
      practice_answer.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { practice_answer.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { practice_answer.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { practice_answer.clearEvents(); });
    }

    if (practice_answer.status === PsychoJS.Status.STARTED) {
      let theseKeys = practice_answer.getKeys({keyList: ['a', 'g', 'l'], waitRelease: false});
      _practice_answer_allKeys = _practice_answer_allKeys.concat(theseKeys);
      if (_practice_answer_allKeys.length > 0) {
        practice_answer.keys = _practice_answer_allKeys[_practice_answer_allKeys.length - 1].name;  // just the last key pressed
        practice_answer.rt = _practice_answer_allKeys[_practice_answer_allKeys.length - 1].rt;
        // was this correct?
        if (practice_answer.keys == 'a') {
            practice_answer.corr = 1;
        } else {
            practice_answer.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_6* updates
    if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index
      
      text_6.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of quiz_practiceComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function quiz_practiceRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'quiz_practice' ---
    for (const thisComponent of quiz_practiceComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (practice_answer.keys === undefined) {
      if (['None','none',undefined].includes('a')) {
         practice_answer.corr = 1;  // correct non-response
      } else {
         practice_answer.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(practice_answer.corr, level);
    }
    psychoJS.experiment.addData('practice_answer.keys', practice_answer.keys);
    psychoJS.experiment.addData('practice_answer.corr', practice_answer.corr);
    if (typeof practice_answer.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('practice_answer.rt', practice_answer.rt);
        routineTimer.reset();
        }
    
    practice_answer.stop();
    // Run 'End Routine' code from code_21
    if (practice_answer.corr) {
        console.log("correct answer");
        practice_loop.finished = true;
    }
    
    // the Routine "quiz_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var msg;
var feedback1Components;
function feedback1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback1' ---
    t = 0;
    feedback1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code
    if (practice_answer.corr) {
        msg = "Correct!";
    } else {
        msg = "Wrong! Re-starting practice";
    }
    
    text_10.setText(msg);
    // keep track of which components have finished
    feedback1Components = [];
    feedback1Components.push(text_10);
    
    for (const thisComponent of feedback1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function feedback1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback1' ---
    // get current time
    t = feedback1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_10* updates
    if (t >= 0.0 && text_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_10.tStart = t;  // (not accounting for frame time here)
      text_10.frameNStart = frameN;  // exact frame index
      
      text_10.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_10.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of feedback1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedback1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback1' ---
    for (const thisComponent of feedback1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_23_allKeys;
var memory_quizComponents;
function memory_quizRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'memory_quiz' ---
    t = 0;
    memory_quizClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_23.keys = undefined;
    key_resp_23.rt = undefined;
    _key_resp_23_allKeys = [];
    // keep track of which components have finished
    memory_quizComponents = [];
    memory_quizComponents.push(text_75);
    memory_quizComponents.push(key_resp_23);
    
    for (const thisComponent of memory_quizComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function memory_quizRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'memory_quiz' ---
    // get current time
    t = memory_quizClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_75* updates
    if (t >= 0.0 && text_75.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_75.tStart = t;  // (not accounting for frame time here)
      text_75.frameNStart = frameN;  // exact frame index
      
      text_75.setAutoDraw(true);
    }

    
    // *key_resp_23* updates
    if (t >= 0.0 && key_resp_23.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_23.tStart = t;  // (not accounting for frame time here)
      key_resp_23.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_23.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_23.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_23.clearEvents(); });
    }

    if (key_resp_23.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_23.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_23_allKeys = _key_resp_23_allKeys.concat(theseKeys);
      if (_key_resp_23_allKeys.length > 0) {
        key_resp_23.keys = _key_resp_23_allKeys[_key_resp_23_allKeys.length - 1].name;  // just the last key pressed
        key_resp_23.rt = _key_resp_23_allKeys[_key_resp_23_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of memory_quizComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function memory_quizRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'memory_quiz' ---
    for (const thisComponent of memory_quizComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_23.corr, level);
    }
    psychoJS.experiment.addData('key_resp_23.keys', key_resp_23.keys);
    if (typeof key_resp_23.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_23.rt', key_resp_23.rt);
        routineTimer.reset();
        }
    
    key_resp_23.stop();
    // the Routine "memory_quiz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_22_allKeys;
var reminder_second_phaseComponents;
function reminder_second_phaseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'reminder_second_phase' ---
    t = 0;
    reminder_second_phaseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_22.keys = undefined;
    key_resp_22.rt = undefined;
    _key_resp_22_allKeys = [];
    // keep track of which components have finished
    reminder_second_phaseComponents = [];
    reminder_second_phaseComponents.push(text_74);
    reminder_second_phaseComponents.push(key_resp_22);
    
    for (const thisComponent of reminder_second_phaseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function reminder_second_phaseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'reminder_second_phase' ---
    // get current time
    t = reminder_second_phaseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_74* updates
    if (t >= 0.0 && text_74.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_74.tStart = t;  // (not accounting for frame time here)
      text_74.frameNStart = frameN;  // exact frame index
      
      text_74.setAutoDraw(true);
    }

    
    // *key_resp_22* updates
    if (t >= 0.0 && key_resp_22.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_22.tStart = t;  // (not accounting for frame time here)
      key_resp_22.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_22.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_22.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_22.clearEvents(); });
    }

    if (key_resp_22.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_22.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_22_allKeys = _key_resp_22_allKeys.concat(theseKeys);
      if (_key_resp_22_allKeys.length > 0) {
        key_resp_22.keys = _key_resp_22_allKeys[_key_resp_22_allKeys.length - 1].name;  // just the last key pressed
        key_resp_22.rt = _key_resp_22_allKeys[_key_resp_22_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of reminder_second_phaseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reminder_second_phaseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'reminder_second_phase' ---
    for (const thisComponent of reminder_second_phaseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_22.corr, level);
    }
    psychoJS.experiment.addData('key_resp_22.keys', key_resp_22.keys);
    if (typeof key_resp_22.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_22.rt', key_resp_22.rt);
        routineTimer.reset();
        }
    
    key_resp_22.stop();
    // the Routine "reminder_second_phase" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_17_allKeys;
var instructions_quiz_1Components;
function instructions_quiz_1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions_quiz_1' ---
    t = 0;
    instructions_quiz_1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_17.keys = undefined;
    key_resp_17.rt = undefined;
    _key_resp_17_allKeys = [];
    // keep track of which components have finished
    instructions_quiz_1Components = [];
    instructions_quiz_1Components.push(text_43);
    instructions_quiz_1Components.push(key_resp_17);
    
    for (const thisComponent of instructions_quiz_1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instructions_quiz_1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions_quiz_1' ---
    // get current time
    t = instructions_quiz_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_43* updates
    if (t >= 0.0 && text_43.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_43.tStart = t;  // (not accounting for frame time here)
      text_43.frameNStart = frameN;  // exact frame index
      
      text_43.setAutoDraw(true);
    }

    
    // *key_resp_17* updates
    if (t >= 0.0 && key_resp_17.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_17.tStart = t;  // (not accounting for frame time here)
      key_resp_17.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_17.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_17.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_17.clearEvents(); });
    }

    if (key_resp_17.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_17.getKeys({keyList: ['a', 'b', 'c', 'd'], waitRelease: false});
      _key_resp_17_allKeys = _key_resp_17_allKeys.concat(theseKeys);
      if (_key_resp_17_allKeys.length > 0) {
        key_resp_17.keys = _key_resp_17_allKeys[_key_resp_17_allKeys.length - 1].name;  // just the last key pressed
        key_resp_17.rt = _key_resp_17_allKeys[_key_resp_17_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructions_quiz_1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var correct;
function instructions_quiz_1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions_quiz_1' ---
    for (const thisComponent of instructions_quiz_1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from code_27
    correct = 0;
    if ((key_resp_17.keys === "c")) {
        correct += 1;
    }
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_17.corr, level);
    }
    psychoJS.experiment.addData('key_resp_17.keys', key_resp_17.keys);
    if (typeof key_resp_17.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_17.rt', key_resp_17.rt);
        routineTimer.reset();
        }
    
    key_resp_17.stop();
    // the Routine "instructions_quiz_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_18_allKeys;
var instructions_quiz_2Components;
function instructions_quiz_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions_quiz_2' ---
    t = 0;
    instructions_quiz_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_18.keys = undefined;
    key_resp_18.rt = undefined;
    _key_resp_18_allKeys = [];
    // keep track of which components have finished
    instructions_quiz_2Components = [];
    instructions_quiz_2Components.push(text_70);
    instructions_quiz_2Components.push(key_resp_18);
    
    for (const thisComponent of instructions_quiz_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instructions_quiz_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions_quiz_2' ---
    // get current time
    t = instructions_quiz_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_70* updates
    if (t >= 0.0 && text_70.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_70.tStart = t;  // (not accounting for frame time here)
      text_70.frameNStart = frameN;  // exact frame index
      
      text_70.setAutoDraw(true);
    }

    
    // *key_resp_18* updates
    if (t >= 0.0 && key_resp_18.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_18.tStart = t;  // (not accounting for frame time here)
      key_resp_18.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_18.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_18.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_18.clearEvents(); });
    }

    if (key_resp_18.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_18.getKeys({keyList: ['a', 'b', 'c', 'd'], waitRelease: false});
      _key_resp_18_allKeys = _key_resp_18_allKeys.concat(theseKeys);
      if (_key_resp_18_allKeys.length > 0) {
        key_resp_18.keys = _key_resp_18_allKeys[_key_resp_18_allKeys.length - 1].name;  // just the last key pressed
        key_resp_18.rt = _key_resp_18_allKeys[_key_resp_18_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructions_quiz_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions_quiz_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions_quiz_2' ---
    for (const thisComponent of instructions_quiz_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from code_30
    if ((key_resp_18.keys === "c")) {
        correct += 1;
    }
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_18.corr, level);
    }
    psychoJS.experiment.addData('key_resp_18.keys', key_resp_18.keys);
    if (typeof key_resp_18.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_18.rt', key_resp_18.rt);
        routineTimer.reset();
        }
    
    key_resp_18.stop();
    // the Routine "instructions_quiz_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_19_allKeys;
var instructions_quiz_3Components;
function instructions_quiz_3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions_quiz_3' ---
    t = 0;
    instructions_quiz_3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_19.keys = undefined;
    key_resp_19.rt = undefined;
    _key_resp_19_allKeys = [];
    // keep track of which components have finished
    instructions_quiz_3Components = [];
    instructions_quiz_3Components.push(text_71);
    instructions_quiz_3Components.push(key_resp_19);
    
    for (const thisComponent of instructions_quiz_3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instructions_quiz_3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions_quiz_3' ---
    // get current time
    t = instructions_quiz_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_71* updates
    if (t >= 0.0 && text_71.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_71.tStart = t;  // (not accounting for frame time here)
      text_71.frameNStart = frameN;  // exact frame index
      
      text_71.setAutoDraw(true);
    }

    
    // *key_resp_19* updates
    if (t >= 0.0 && key_resp_19.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_19.tStart = t;  // (not accounting for frame time here)
      key_resp_19.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_19.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_19.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_19.clearEvents(); });
    }

    if (key_resp_19.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_19.getKeys({keyList: ['a', 'b', 'c', 'd'], waitRelease: false});
      _key_resp_19_allKeys = _key_resp_19_allKeys.concat(theseKeys);
      if (_key_resp_19_allKeys.length > 0) {
        key_resp_19.keys = _key_resp_19_allKeys[_key_resp_19_allKeys.length - 1].name;  // just the last key pressed
        key_resp_19.rt = _key_resp_19_allKeys[_key_resp_19_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructions_quiz_3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions_quiz_3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions_quiz_3' ---
    for (const thisComponent of instructions_quiz_3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from code_31
    if ((key_resp_19.keys === "b")) {
        correct += 1;
    }
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_19.corr, level);
    }
    psychoJS.experiment.addData('key_resp_19.keys', key_resp_19.keys);
    if (typeof key_resp_19.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_19.rt', key_resp_19.rt);
        routineTimer.reset();
        }
    
    key_resp_19.stop();
    // the Routine "instructions_quiz_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_20_allKeys;
var instructions_quiz_4Components;
function instructions_quiz_4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions_quiz_4' ---
    t = 0;
    instructions_quiz_4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_20.keys = undefined;
    key_resp_20.rt = undefined;
    _key_resp_20_allKeys = [];
    // keep track of which components have finished
    instructions_quiz_4Components = [];
    instructions_quiz_4Components.push(text_72);
    instructions_quiz_4Components.push(key_resp_20);
    
    for (const thisComponent of instructions_quiz_4Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instructions_quiz_4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions_quiz_4' ---
    // get current time
    t = instructions_quiz_4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_72* updates
    if (t >= 0.0 && text_72.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_72.tStart = t;  // (not accounting for frame time here)
      text_72.frameNStart = frameN;  // exact frame index
      
      text_72.setAutoDraw(true);
    }

    
    // *key_resp_20* updates
    if (t >= 0.0 && key_resp_20.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_20.tStart = t;  // (not accounting for frame time here)
      key_resp_20.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_20.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_20.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_20.clearEvents(); });
    }

    if (key_resp_20.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_20.getKeys({keyList: ['a', 'b', 'c', 'd'], waitRelease: false});
      _key_resp_20_allKeys = _key_resp_20_allKeys.concat(theseKeys);
      if (_key_resp_20_allKeys.length > 0) {
        key_resp_20.keys = _key_resp_20_allKeys[_key_resp_20_allKeys.length - 1].name;  // just the last key pressed
        key_resp_20.rt = _key_resp_20_allKeys[_key_resp_20_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructions_quiz_4Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions_quiz_4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions_quiz_4' ---
    for (const thisComponent of instructions_quiz_4Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from code_35
    if ((key_resp_20.keys === "b")) {
        correct += 1;
    }
    if ((correct === 4)) {
        instructions_get_right.finished = true;
        msg = "Correct! You can now move on";
    } else {
        msg = "Incorrect! You need to repeat the instructions.";
    }
    
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_20.corr, level);
    }
    psychoJS.experiment.addData('key_resp_20.keys', key_resp_20.keys);
    if (typeof key_resp_20.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_20.rt', key_resp_20.rt);
        routineTimer.reset();
        }
    
    key_resp_20.stop();
    // the Routine "instructions_quiz_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var result_quiz_instructionsComponents;
function result_quiz_instructionsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'result_quiz_instructions' ---
    t = 0;
    result_quiz_instructionsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.500000);
    // update component parameters for each repeat
    result_q_instr.setText(msg);
    // keep track of which components have finished
    result_quiz_instructionsComponents = [];
    result_quiz_instructionsComponents.push(result_q_instr);
    
    for (const thisComponent of result_quiz_instructionsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function result_quiz_instructionsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'result_quiz_instructions' ---
    // get current time
    t = result_quiz_instructionsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *result_q_instr* updates
    if (t >= 0.0 && result_q_instr.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      result_q_instr.tStart = t;  // (not accounting for frame time here)
      result_q_instr.frameNStart = frameN;  // exact frame index
      
      result_q_instr.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (result_q_instr.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      result_q_instr.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of result_quiz_instructionsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function result_quiz_instructionsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'result_quiz_instructions' ---
    for (const thisComponent of result_quiz_instructionsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_4_allKeys;
var time_limitComponents;
function time_limitRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'time_limit' ---
    t = 0;
    time_limitClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    time_limitComponents = [];
    time_limitComponents.push(text_102);
    time_limitComponents.push(key_resp_4);
    
    for (const thisComponent of time_limitComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function time_limitRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'time_limit' ---
    // get current time
    t = time_limitClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_102* updates
    if (t >= 0.0 && text_102.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_102.tStart = t;  // (not accounting for frame time here)
      text_102.frameNStart = frameN;  // exact frame index
      
      text_102.setAutoDraw(true);
    }

    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of time_limitComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function time_limitRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'time_limit' ---
    for (const thisComponent of time_limitComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_4.corr, level);
    }
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    // the Routine "time_limit" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_7_allKeys;
var instructions3Components;
function instructions3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions3' ---
    t = 0;
    instructions3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_7.keys = undefined;
    key_resp_7.rt = undefined;
    _key_resp_7_allKeys = [];
    // keep track of which components have finished
    instructions3Components = [];
    instructions3Components.push(text_7);
    instructions3Components.push(key_resp_7);
    
    for (const thisComponent of instructions3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instructions3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions3' ---
    // get current time
    t = instructions3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_7* updates
    if (t >= 0.0 && text_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_7.tStart = t;  // (not accounting for frame time here)
      text_7.frameNStart = frameN;  // exact frame index
      
      text_7.setAutoDraw(true);
    }

    
    // *key_resp_7* updates
    if (t >= 0 && key_resp_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_7.tStart = t;  // (not accounting for frame time here)
      key_resp_7.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_7.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.clearEvents(); });
    }

    if (key_resp_7.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_7.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_7_allKeys = _key_resp_7_allKeys.concat(theseKeys);
      if (_key_resp_7_allKeys.length > 0) {
        key_resp_7.keys = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].name;  // just the last key pressed
        key_resp_7.rt = _key_resp_7_allKeys[_key_resp_7_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructions3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions3' ---
    for (const thisComponent of instructions3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp_7.stop();
    // the Routine "instructions3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _click_action_allKeys;
var stage1Components;
function stage1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'stage1' ---
    t = 0;
    stage1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(7.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_12
    if ((action1 === 1)) {
        text_3.pos = [(- 0.4), (- 0.2)];
    } else {
        if ((action1 === 9)) {
            text_3.pos = [0.4, (- 0.2)];
        }
    }
    if ((((trial_learning_num + 1) % 28) === 0)) {
        learning_reward_goal = learning_reward_goal_list[counter_reward_learning];
        console.log(learning_reward_goal);
        counter_reward_learning += 1;
    }
    
    click_action.keys = undefined;
    click_action.rt = undefined;
    _click_action_allKeys = [];
    trident_start_learning.setPos([0, 0]);
    trident_start_learning.setImage(s1_image);
    text_3.setPos([0.0, (- 0.15)]);
    text_3.setText(action1);
    // keep track of which components have finished
    stage1Components = [];
    stage1Components.push(click_action);
    stage1Components.push(text_9);
    stage1Components.push(trident_start_learning);
    stage1Components.push(text_3);
    
    for (const thisComponent of stage1Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function stage1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'stage1' ---
    // get current time
    t = stage1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *click_action* updates
    if (t >= 0.2 && click_action.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      click_action.tStart = t;  // (not accounting for frame time here)
      click_action.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { click_action.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { click_action.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { click_action.clearEvents(); });
    }

    frameRemains = 0.2 + 6.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (click_action.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      click_action.status = PsychoJS.Status.FINISHED;
  }

    if (click_action.status === PsychoJS.Status.STARTED) {
      let theseKeys = click_action.getKeys({keyList: ['1', '9'], waitRelease: false});
      _click_action_allKeys = _click_action_allKeys.concat(theseKeys);
      if (_click_action_allKeys.length > 0) {
        click_action.keys = _click_action_allKeys[0].name;  // just the first key pressed
        click_action.rt = _click_action_allKeys[0].rt;
        // was this correct?
        if (click_action.keys == action1) {
            click_action.corr = 1;
        } else {
            click_action.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_9* updates
    if (t >= 0.0 && text_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_9.tStart = t;  // (not accounting for frame time here)
      text_9.frameNStart = frameN;  // exact frame index
      
      text_9.setAutoDraw(true);
    }

    frameRemains = 0.0 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_9.setAutoDraw(false);
    }
    
    // *trident_start_learning* updates
    if (t >= 0.0 && trident_start_learning.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trident_start_learning.tStart = t;  // (not accounting for frame time here)
      trident_start_learning.frameNStart = frameN;  // exact frame index
      
      trident_start_learning.setAutoDraw(true);
    }

    frameRemains = 0.0 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trident_start_learning.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trident_start_learning.setAutoDraw(false);
    }
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of stage1Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stage1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'stage1' ---
    for (const thisComponent of stage1Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (click_action.keys === undefined) {
      if (['None','none',undefined].includes(action1)) {
         click_action.corr = 1;  // correct non-response
      } else {
         click_action.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(click_action.corr, level);
    }
    psychoJS.experiment.addData('click_action.keys', click_action.keys);
    psychoJS.experiment.addData('click_action.corr', click_action.corr);
    if (typeof click_action.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('click_action.rt', click_action.rt);
        routineTimer.reset();
        }
    
    click_action.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var msg_incorrect;
var incorrect_answerComponents;
function incorrect_answerRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'incorrect_answer' ---
    t = 0;
    incorrect_answerClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_11
    if (click_action.corr) {
        trial_learning_num += 1;
        msg_incorrect = "correct";
        action_selection.finished = true;
        continueRoutine = false;
    } else {
        msg_incorrect = "You clicked the wrong button! If you click the wrong button 5 times, the game will stop and you will NOT GET PAID because you failed to follow instructions!";
        incorrect_actions += 1;
        continueRoutine = true;
    }
    
    incorrect_display.setText(msg_incorrect);
    // keep track of which components have finished
    incorrect_answerComponents = [];
    incorrect_answerComponents.push(incorrect_display);
    
    for (const thisComponent of incorrect_answerComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function incorrect_answerRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'incorrect_answer' ---
    // get current time
    t = incorrect_answerClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *incorrect_display* updates
    if (t >= 0.0 && incorrect_display.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      incorrect_display.tStart = t;  // (not accounting for frame time here)
      incorrect_display.frameNStart = frameN;  // exact frame index
      
      incorrect_display.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (incorrect_display.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      incorrect_display.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of incorrect_answerComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function incorrect_answerRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'incorrect_answer' ---
    for (const thisComponent of incorrect_answerComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _click_action_2_allKeys;
var stage2_2Components;
function stage2_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'stage2_2' ---
    t = 0;
    stage2_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(7.000000);
    // update component parameters for each repeat
    click_action_2.keys = undefined;
    click_action_2.rt = undefined;
    _click_action_2_allKeys = [];
    trident_start_learning_2.setImage(s2_image);
    text_109.setText(action2);
    // keep track of which components have finished
    stage2_2Components = [];
    stage2_2Components.push(click_action_2);
    stage2_2Components.push(text_108);
    stage2_2Components.push(trident_start_learning_2);
    stage2_2Components.push(text_109);
    
    for (const thisComponent of stage2_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function stage2_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'stage2_2' ---
    // get current time
    t = stage2_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *click_action_2* updates
    if (t >= 0.2 && click_action_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      click_action_2.tStart = t;  // (not accounting for frame time here)
      click_action_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { click_action_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { click_action_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { click_action_2.clearEvents(); });
    }

    frameRemains = 0.2 + 6.8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (click_action_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      click_action_2.status = PsychoJS.Status.FINISHED;
  }

    if (click_action_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = click_action_2.getKeys({keyList: ['2', '8'], waitRelease: false});
      _click_action_2_allKeys = _click_action_2_allKeys.concat(theseKeys);
      if (_click_action_2_allKeys.length > 0) {
        click_action_2.keys = _click_action_2_allKeys[0].name;  // just the first key pressed
        click_action_2.rt = _click_action_2_allKeys[0].rt;
        // was this correct?
        if (click_action_2.keys == action2) {
            click_action_2.corr = 1;
        } else {
            click_action_2.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_108* updates
    if (t >= 0.0 && text_108.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_108.tStart = t;  // (not accounting for frame time here)
      text_108.frameNStart = frameN;  // exact frame index
      
      text_108.setAutoDraw(true);
    }

    frameRemains = 0.0 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_108.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_108.setAutoDraw(false);
    }
    
    // *trident_start_learning_2* updates
    if (t >= 0.0 && trident_start_learning_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trident_start_learning_2.tStart = t;  // (not accounting for frame time here)
      trident_start_learning_2.frameNStart = frameN;  // exact frame index
      
      trident_start_learning_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trident_start_learning_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trident_start_learning_2.setAutoDraw(false);
    }
    
    // *text_109* updates
    if (t >= 0.0 && text_109.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_109.tStart = t;  // (not accounting for frame time here)
      text_109.frameNStart = frameN;  // exact frame index
      
      text_109.setAutoDraw(true);
    }

    frameRemains = 0.0 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_109.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_109.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of stage2_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stage2_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'stage2_2' ---
    for (const thisComponent of stage2_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // was no response the correct answer?!
    if (click_action_2.keys === undefined) {
      if (['None','none',undefined].includes(action2)) {
         click_action_2.corr = 1;  // correct non-response
      } else {
         click_action_2.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(click_action_2.corr, level);
    }
    psychoJS.experiment.addData('click_action_2.keys', click_action_2.keys);
    psychoJS.experiment.addData('click_action_2.corr', click_action_2.corr);
    if (typeof click_action_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('click_action_2.rt', click_action_2.rt);
        routineTimer.reset();
        }
    
    click_action_2.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var learning_trial_step2_to_step3Components;
function learning_trial_step2_to_step3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'learning_trial_step2_to_step3' ---
    t = 0;
    learning_trial_step2_to_step3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    stage2_learning_3.setImage(s3_image);
    // Run 'Begin Routine' code from code_53
    if ((incorrect_actions > 4)) {
        trials.finished = true;
        continueRoutine = false;
    }
    
    // keep track of which components have finished
    learning_trial_step2_to_step3Components = [];
    learning_trial_step2_to_step3Components.push(stage2_learning_3);
    
    for (const thisComponent of learning_trial_step2_to_step3Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function learning_trial_step2_to_step3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'learning_trial_step2_to_step3' ---
    // get current time
    t = learning_trial_step2_to_step3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *stage2_learning_3* updates
    if (t >= 0 && stage2_learning_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stage2_learning_3.tStart = t;  // (not accounting for frame time here)
      stage2_learning_3.frameNStart = frameN;  // exact frame index
      
      stage2_learning_3.setAutoDraw(true);
    }

    frameRemains = 0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (stage2_learning_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      stage2_learning_3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of learning_trial_step2_to_step3Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function learning_trial_step2_to_step3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'learning_trial_step2_to_step3' ---
    for (const thisComponent of learning_trial_step2_to_step3Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var number_correct;
var memory_qComponents;
function memory_qRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'memory_q' ---
    t = 0;
    memory_qClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.500000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_24
    if (((trial_learning_num % 28) === 0)) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    number_correct = 0;
    
    // keep track of which components have finished
    memory_qComponents = [];
    memory_qComponents.push(text_92);
    
    for (const thisComponent of memory_qComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function memory_qRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'memory_q' ---
    // get current time
    t = memory_qClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_92* updates
    if (t >= 0.0 && text_92.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_92.tStart = t;  // (not accounting for frame time here)
      text_92.frameNStart = frameN;  // exact frame index
      
      text_92.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_92.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_92.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of memory_qComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function memory_qRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'memory_q' ---
    for (const thisComponent of memory_qComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _resp4_allKeys;
var prediction4Components;
function prediction4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'prediction4' ---
    t = 0;
    prediction4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_4
    if (((trial_learning_num % 28) === 0)) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    number_correct = 0;
    
    picture_reward_goal.setImage(learning_reward_goal);
    resp4.keys = undefined;
    resp4.rt = undefined;
    _resp4_allKeys = [];
    // keep track of which components have finished
    prediction4Components = [];
    prediction4Components.push(outcome4);
    prediction4Components.push(picture_reward_goal);
    prediction4Components.push(resp4);
    prediction4Components.push(learning_rew_trident);
    prediction4Components.push(learning_rew_planet);
    prediction4Components.push(text_79);
    prediction4Components.push(text_85);
    
    for (const thisComponent of prediction4Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function prediction4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'prediction4' ---
    // get current time
    t = prediction4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *outcome4* updates
    if (t >= 0.0 && outcome4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      outcome4.tStart = t;  // (not accounting for frame time here)
      outcome4.frameNStart = frameN;  // exact frame index
      
      outcome4.setAutoDraw(true);
    }

    
    // *picture_reward_goal* updates
    if (t >= 0.0 && picture_reward_goal.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      picture_reward_goal.tStart = t;  // (not accounting for frame time here)
      picture_reward_goal.frameNStart = frameN;  // exact frame index
      
      picture_reward_goal.setAutoDraw(true);
    }

    
    // *resp4* updates
    if (t >= 0.0 && resp4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp4.tStart = t;  // (not accounting for frame time here)
      resp4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp4.clearEvents(); });
    }

    if (resp4.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp4.getKeys({keyList: ['1', '9'], waitRelease: false});
      _resp4_allKeys = _resp4_allKeys.concat(theseKeys);
      if (_resp4_allKeys.length > 0) {
        resp4.keys = _resp4_allKeys[_resp4_allKeys.length - 1].name;  // just the last key pressed
        resp4.rt = _resp4_allKeys[_resp4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *learning_rew_trident* updates
    if (t >= 0.0 && learning_rew_trident.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      learning_rew_trident.tStart = t;  // (not accounting for frame time here)
      learning_rew_trident.frameNStart = frameN;  // exact frame index
      
      learning_rew_trident.setAutoDraw(true);
    }

    
    // *learning_rew_planet* updates
    if (t >= 0.0 && learning_rew_planet.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      learning_rew_planet.tStart = t;  // (not accounting for frame time here)
      learning_rew_planet.frameNStart = frameN;  // exact frame index
      
      learning_rew_planet.setAutoDraw(true);
    }

    
    // *text_79* updates
    if (t >= 0.0 && text_79.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_79.tStart = t;  // (not accounting for frame time here)
      text_79.frameNStart = frameN;  // exact frame index
      
      text_79.setAutoDraw(true);
    }

    
    // *text_85* updates
    if (t >= 0.0 && text_85.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_85.tStart = t;  // (not accounting for frame time here)
      text_85.frameNStart = frameN;  // exact frame index
      
      text_85.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of prediction4Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prediction4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'prediction4' ---
    for (const thisComponent of prediction4Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp4.corr, level);
    }
    psychoJS.experiment.addData('resp4.keys', resp4.keys);
    if (typeof resp4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp4.rt', resp4.rt);
        routineTimer.reset();
        }
    
    resp4.stop();
    // the Routine "prediction4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var quiz_scoreComponents;
function quiz_scoreRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'quiz_score' ---
    t = 0;
    quiz_scoreClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_23
    if (((trial_learning_num % 28) === 0)) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    number_correct = 0;
    
    text_5.setText('You will see the correct score at the end of the game');
    // keep track of which components have finished
    quiz_scoreComponents = [];
    quiz_scoreComponents.push(text_5);
    
    for (const thisComponent of quiz_scoreComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function quiz_scoreRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'quiz_score' ---
    // get current time
    t = quiz_scoreClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_5.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of quiz_scoreComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function quiz_scoreRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'quiz_score' ---
    for (const thisComponent of quiz_scoreComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var take_a_breakComponents;
function take_a_breakRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'take_a_break' ---
    t = 0;
    take_a_breakClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.600000);
    // update component parameters for each repeat
    // keep track of which components have finished
    take_a_breakComponents = [];
    take_a_breakComponents.push(text_39);
    
    for (const thisComponent of take_a_breakComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function take_a_breakRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'take_a_break' ---
    // get current time
    t = take_a_breakClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_39* updates
    if (t >= 0.0 && text_39.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_39.tStart = t;  // (not accounting for frame time here)
      text_39.frameNStart = frameN;  // exact frame index
      
      text_39.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_39.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_39.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of take_a_breakComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function take_a_breakRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'take_a_break' ---
    for (const thisComponent of take_a_breakComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _resp4_3_allKeys;
var prediction5Components;
function prediction5RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'prediction5' ---
    t = 0;
    prediction5Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    picture_reward_goal_2.setImage(image2);
    resp4_3.keys = undefined;
    resp4_3.rt = undefined;
    _resp4_3_allKeys = [];
    learning_rew_trident_2.setImage(image1);
    // keep track of which components have finished
    prediction5Components = [];
    prediction5Components.push(outcome4_2);
    prediction5Components.push(picture_reward_goal_2);
    prediction5Components.push(resp4_3);
    prediction5Components.push(learning_rew_trident_2);
    prediction5Components.push(text_80);
    
    for (const thisComponent of prediction5Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function prediction5RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'prediction5' ---
    // get current time
    t = prediction5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *outcome4_2* updates
    if (t >= 0.0 && outcome4_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      outcome4_2.tStart = t;  // (not accounting for frame time here)
      outcome4_2.frameNStart = frameN;  // exact frame index
      
      outcome4_2.setAutoDraw(true);
    }

    
    // *picture_reward_goal_2* updates
    if (t >= 0.0 && picture_reward_goal_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      picture_reward_goal_2.tStart = t;  // (not accounting for frame time here)
      picture_reward_goal_2.frameNStart = frameN;  // exact frame index
      
      picture_reward_goal_2.setAutoDraw(true);
    }

    
    // *resp4_3* updates
    if (t >= 0.0 && resp4_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp4_3.tStart = t;  // (not accounting for frame time here)
      resp4_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp4_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp4_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp4_3.clearEvents(); });
    }

    if (resp4_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp4_3.getKeys({keyList: ['2', '8'], waitRelease: false});
      _resp4_3_allKeys = _resp4_3_allKeys.concat(theseKeys);
      if (_resp4_3_allKeys.length > 0) {
        resp4_3.keys = _resp4_3_allKeys[_resp4_3_allKeys.length - 1].name;  // just the last key pressed
        resp4_3.rt = _resp4_3_allKeys[_resp4_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *learning_rew_trident_2* updates
    if (t >= 0.0 && learning_rew_trident_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      learning_rew_trident_2.tStart = t;  // (not accounting for frame time here)
      learning_rew_trident_2.frameNStart = frameN;  // exact frame index
      
      learning_rew_trident_2.setAutoDraw(true);
    }

    
    // *text_80* updates
    if (t >= 0.0 && text_80.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_80.tStart = t;  // (not accounting for frame time here)
      text_80.frameNStart = frameN;  // exact frame index
      
      text_80.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of prediction5Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prediction5RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'prediction5' ---
    for (const thisComponent of prediction5Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(resp4_3.corr, level);
    }
    psychoJS.experiment.addData('resp4_3.keys', resp4_3.keys);
    if (typeof resp4_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp4_3.rt', resp4_3.rt);
        routineTimer.reset();
        }
    
    resp4_3.stop();
    // the Routine "prediction5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_11_allKeys;
var instructions_reward_stageComponents;
function instructions_reward_stageRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions_reward_stage' ---
    t = 0;
    instructions_reward_stageClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_38
    if ((incorrect_actions > 4)) {
        continueRoutine = false;
    }
    
    key_resp_11.keys = undefined;
    key_resp_11.rt = undefined;
    _key_resp_11_allKeys = [];
    // keep track of which components have finished
    instructions_reward_stageComponents = [];
    instructions_reward_stageComponents.push(instructions_rewardstage);
    instructions_reward_stageComponents.push(key_resp_11);
    
    for (const thisComponent of instructions_reward_stageComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instructions_reward_stageRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions_reward_stage' ---
    // get current time
    t = instructions_reward_stageClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructions_rewardstage* updates
    if (t >= 0.0 && instructions_rewardstage.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_rewardstage.tStart = t;  // (not accounting for frame time here)
      instructions_rewardstage.frameNStart = frameN;  // exact frame index
      
      instructions_rewardstage.setAutoDraw(true);
    }

    
    // *key_resp_11* updates
    if (t >= 0.0 && key_resp_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_11.tStart = t;  // (not accounting for frame time here)
      key_resp_11.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_11.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_11.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_11.clearEvents(); });
    }

    if (key_resp_11.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_11.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_11_allKeys = _key_resp_11_allKeys.concat(theseKeys);
      if (_key_resp_11_allKeys.length > 0) {
        key_resp_11.keys = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].name;  // just the last key pressed
        key_resp_11.rt = _key_resp_11_allKeys[_key_resp_11_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructions_reward_stageComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions_reward_stageRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions_reward_stage' ---
    for (const thisComponent of instructions_reward_stageComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp_11.stop();
    // the Routine "instructions_reward_stage" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_35_allKeys;
var instructions_planning_2phaseComponents;
function instructions_planning_2phaseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions_planning_2phase' ---
    t = 0;
    instructions_planning_2phaseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_50
    if ((incorrect_actions > 4)) {
        continueRoutine = false;
    }
    
    key_resp_35.keys = undefined;
    key_resp_35.rt = undefined;
    _key_resp_35_allKeys = [];
    // keep track of which components have finished
    instructions_planning_2phaseComponents = [];
    instructions_planning_2phaseComponents.push(instructions_rewardstage_2);
    instructions_planning_2phaseComponents.push(key_resp_35);
    
    for (const thisComponent of instructions_planning_2phaseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instructions_planning_2phaseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions_planning_2phase' ---
    // get current time
    t = instructions_planning_2phaseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructions_rewardstage_2* updates
    if (t >= 0.0 && instructions_rewardstage_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructions_rewardstage_2.tStart = t;  // (not accounting for frame time here)
      instructions_rewardstage_2.frameNStart = frameN;  // exact frame index
      
      instructions_rewardstage_2.setAutoDraw(true);
    }

    
    // *key_resp_35* updates
    if (t >= 0.0 && key_resp_35.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_35.tStart = t;  // (not accounting for frame time here)
      key_resp_35.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_35.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_35.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_35.clearEvents(); });
    }

    if (key_resp_35.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_35.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_35_allKeys = _key_resp_35_allKeys.concat(theseKeys);
      if (_key_resp_35_allKeys.length > 0) {
        key_resp_35.keys = _key_resp_35_allKeys[_key_resp_35_allKeys.length - 1].name;  // just the last key pressed
        key_resp_35.rt = _key_resp_35_allKeys[_key_resp_35_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructions_planning_2phaseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions_planning_2phaseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions_planning_2phase' ---
    for (const thisComponent of instructions_planning_2phaseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp_35.stop();
    // the Routine "instructions_planning_2phase" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_9_allKeys;
var i2_rewardComponents;
function i2_rewardRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'i2_reward' ---
    t = 0;
    i2_rewardClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_39
    if ((incorrect_actions > 4)) {
        continueRoutine = false;
    }
    
    key_resp_9.keys = undefined;
    key_resp_9.rt = undefined;
    _key_resp_9_allKeys = [];
    // keep track of which components have finished
    i2_rewardComponents = [];
    i2_rewardComponents.push(text_42);
    i2_rewardComponents.push(key_resp_9);
    
    for (const thisComponent of i2_rewardComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function i2_rewardRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'i2_reward' ---
    // get current time
    t = i2_rewardClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_42* updates
    if (t >= 0.0 && text_42.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_42.tStart = t;  // (not accounting for frame time here)
      text_42.frameNStart = frameN;  // exact frame index
      
      text_42.setAutoDraw(true);
    }

    
    // *key_resp_9* updates
    if (t >= 0.0 && key_resp_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_9.tStart = t;  // (not accounting for frame time here)
      key_resp_9.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_9.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_9.clearEvents(); });
    }

    if (key_resp_9.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_9.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_9_allKeys = _key_resp_9_allKeys.concat(theseKeys);
      if (_key_resp_9_allKeys.length > 0) {
        key_resp_9.keys = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].name;  // just the last key pressed
        key_resp_9.rt = _key_resp_9_allKeys[_key_resp_9_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of i2_rewardComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function i2_rewardRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'i2_reward' ---
    for (const thisComponent of i2_rewardComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp_9.stop();
    // the Routine "i2_reward" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _resp4_2_allKeys;
var _key_resp_3_allKeys;
var practice_view_reward_infoComponents;
function practice_view_reward_infoRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'practice_view_reward_info' ---
    t = 0;
    practice_view_reward_infoClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_40
    if ((incorrect_actions > 4)) {
        continueRoutine = false;
    }
    
    resp4_2.keys = undefined;
    resp4_2.rt = undefined;
    _resp4_2_allKeys = [];
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    practice_view_reward_infoComponents = [];
    practice_view_reward_infoComponents.push(im1_example_choicephase);
    practice_view_reward_infoComponents.push(resp4_2);
    practice_view_reward_infoComponents.push(im2_example_choicephase);
    practice_view_reward_infoComponents.push(example_trial_choice_phase);
    practice_view_reward_infoComponents.push(im1_rewvalue);
    practice_view_reward_infoComponents.push(im2_rewvalue);
    practice_view_reward_infoComponents.push(text_28);
    practice_view_reward_infoComponents.push(key_resp_3);
    
    for (const thisComponent of practice_view_reward_infoComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function practice_view_reward_infoRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'practice_view_reward_info' ---
    // get current time
    t = practice_view_reward_infoClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *im1_example_choicephase* updates
    if (t >= 0.0 && im1_example_choicephase.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      im1_example_choicephase.tStart = t;  // (not accounting for frame time here)
      im1_example_choicephase.frameNStart = frameN;  // exact frame index
      
      im1_example_choicephase.setAutoDraw(true);
    }

    
    // *resp4_2* updates
    if (t >= 0.0 && resp4_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      resp4_2.tStart = t;  // (not accounting for frame time here)
      resp4_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { resp4_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { resp4_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { resp4_2.clearEvents(); });
    }

    if (resp4_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = resp4_2.getKeys({keyList: ['space'], waitRelease: false});
      _resp4_2_allKeys = _resp4_2_allKeys.concat(theseKeys);
      if (_resp4_2_allKeys.length > 0) {
        resp4_2.keys = _resp4_2_allKeys[_resp4_2_allKeys.length - 1].name;  // just the last key pressed
        resp4_2.rt = _resp4_2_allKeys[_resp4_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *im2_example_choicephase* updates
    if (t >= 0.0 && im2_example_choicephase.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      im2_example_choicephase.tStart = t;  // (not accounting for frame time here)
      im2_example_choicephase.frameNStart = frameN;  // exact frame index
      
      im2_example_choicephase.setAutoDraw(true);
    }

    
    // *example_trial_choice_phase* updates
    if (t >= 0.0 && example_trial_choice_phase.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      example_trial_choice_phase.tStart = t;  // (not accounting for frame time here)
      example_trial_choice_phase.frameNStart = frameN;  // exact frame index
      
      example_trial_choice_phase.setAutoDraw(true);
    }

    
    // *im1_rewvalue* updates
    if (t >= 0.0 && im1_rewvalue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      im1_rewvalue.tStart = t;  // (not accounting for frame time here)
      im1_rewvalue.frameNStart = frameN;  // exact frame index
      
      im1_rewvalue.setAutoDraw(true);
    }

    
    // *im2_rewvalue* updates
    if (t >= 0.0 && im2_rewvalue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      im2_rewvalue.tStart = t;  // (not accounting for frame time here)
      im2_rewvalue.frameNStart = frameN;  // exact frame index
      
      im2_rewvalue.setAutoDraw(true);
    }

    
    // *text_28* updates
    if (t >= 2.0 && text_28.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_28.tStart = t;  // (not accounting for frame time here)
      text_28.frameNStart = frameN;  // exact frame index
      
      text_28.setAutoDraw(true);
    }

    
    // *key_resp_3* updates
    if (t >= 2.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.clearEvents(); });
    }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of practice_view_reward_infoComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_view_reward_infoRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'practice_view_reward_info' ---
    for (const thisComponent of practice_view_reward_infoComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    resp4_2.stop();
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "practice_view_reward_info" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_12_allKeys;
var instructions_planningComponents;
function instructions_planningRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instructions_planning' ---
    t = 0;
    instructions_planningClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_41
    if ((incorrect_actions > 4)) {
        continueRoutine = false;
    }
    
    key_resp_12.keys = undefined;
    key_resp_12.rt = undefined;
    _key_resp_12_allKeys = [];
    // keep track of which components have finished
    instructions_planningComponents = [];
    instructions_planningComponents.push(text_66);
    instructions_planningComponents.push(key_resp_12);
    instructions_planningComponents.push(text_24);
    
    for (const thisComponent of instructions_planningComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function instructions_planningRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instructions_planning' ---
    // get current time
    t = instructions_planningClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_66* updates
    if (t >= 0.0 && text_66.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_66.tStart = t;  // (not accounting for frame time here)
      text_66.frameNStart = frameN;  // exact frame index
      
      text_66.setAutoDraw(true);
    }

    
    // *key_resp_12* updates
    if (t >= 1.5 && key_resp_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_12.tStart = t;  // (not accounting for frame time here)
      key_resp_12.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_12.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_12.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_12.clearEvents(); });
    }

    if (key_resp_12.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_12.getKeys({keyList: ['left', 'right', 'space'], waitRelease: false});
      _key_resp_12_allKeys = _key_resp_12_allKeys.concat(theseKeys);
      if (_key_resp_12_allKeys.length > 0) {
        key_resp_12.keys = _key_resp_12_allKeys[_key_resp_12_allKeys.length - 1].name;  // just the last key pressed
        key_resp_12.rt = _key_resp_12_allKeys[_key_resp_12_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_24* updates
    if (t >= 1.5 && text_24.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_24.tStart = t;  // (not accounting for frame time here)
      text_24.frameNStart = frameN;  // exact frame index
      
      text_24.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of instructions_planningComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions_planningRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instructions_planning' ---
    for (const thisComponent of instructions_planningComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_12.corr, level);
    }
    psychoJS.experiment.addData('key_resp_12.keys', key_resp_12.keys);
    if (typeof key_resp_12.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_12.rt', key_resp_12.rt);
        routineTimer.reset();
        }
    
    key_resp_12.stop();
    // the Routine "instructions_planning" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_15_allKeys;
var start_planning_trialsComponents;
function start_planning_trialsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'start_planning_trials' ---
    t = 0;
    start_planning_trialsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_42
    if ((incorrect_actions > 4)) {
        continueRoutine = false;
    }
    
    key_resp_15.keys = undefined;
    key_resp_15.rt = undefined;
    _key_resp_15_allKeys = [];
    // keep track of which components have finished
    start_planning_trialsComponents = [];
    start_planning_trialsComponents.push(text_67);
    start_planning_trialsComponents.push(key_resp_15);
    
    for (const thisComponent of start_planning_trialsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function start_planning_trialsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'start_planning_trials' ---
    // get current time
    t = start_planning_trialsClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_67* updates
    if (t >= 0.0 && text_67.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_67.tStart = t;  // (not accounting for frame time here)
      text_67.frameNStart = frameN;  // exact frame index
      
      text_67.setAutoDraw(true);
    }

    
    // *key_resp_15* updates
    if (t >= 0.0 && key_resp_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_15.tStart = t;  // (not accounting for frame time here)
      key_resp_15.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_15.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_15.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_15.clearEvents(); });
    }

    if (key_resp_15.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_15.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_15_allKeys = _key_resp_15_allKeys.concat(theseKeys);
      if (_key_resp_15_allKeys.length > 0) {
        key_resp_15.keys = _key_resp_15_allKeys[_key_resp_15_allKeys.length - 1].name;  // just the last key pressed
        key_resp_15.rt = _key_resp_15_allKeys[_key_resp_15_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of start_planning_trialsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function start_planning_trialsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'start_planning_trials' ---
    for (const thisComponent of start_planning_trialsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_15.corr, level);
    }
    psychoJS.experiment.addData('key_resp_15.keys', key_resp_15.keys);
    if (typeof key_resp_15.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_15.rt', key_resp_15.rt);
        routineTimer.reset();
        }
    
    key_resp_15.stop();
    // the Routine "start_planning_trials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_24_allKeys;
var info_choicephaseComponents;
function info_choicephaseRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'info_choicephase' ---
    t = 0;
    info_choicephaseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_43
    if ((incorrect_actions > 4)) {
        PR_vs_SR.finished = true;
        continueRoutine = false;
    }
    
    im1_planning.setImage(r1);
    im2_planning.setImage(r2);
    im1_rewvalue_planning.setText(r1_num);
    im2_rewvalue_planning.setText(r2_num);
    key_resp_24.keys = undefined;
    key_resp_24.rt = undefined;
    _key_resp_24_allKeys = [];
    im3_planning.setImage(r3);
    im4_planning.setImage(r4);
    im3_num_planning.setText(r3_num);
    im4_num_planning.setText(r4_num);
    // keep track of which components have finished
    info_choicephaseComponents = [];
    info_choicephaseComponents.push(im1_planning);
    info_choicephaseComponents.push(im2_planning);
    info_choicephaseComponents.push(example_trial_choice_phase_2);
    info_choicephaseComponents.push(im1_rewvalue_planning);
    info_choicephaseComponents.push(im2_rewvalue_planning);
    info_choicephaseComponents.push(text_29);
    info_choicephaseComponents.push(key_resp_24);
    info_choicephaseComponents.push(im3_planning);
    info_choicephaseComponents.push(im4_planning);
    info_choicephaseComponents.push(im3_num_planning);
    info_choicephaseComponents.push(im4_num_planning);
    
    for (const thisComponent of info_choicephaseComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function info_choicephaseRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'info_choicephase' ---
    // get current time
    t = info_choicephaseClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *im1_planning* updates
    if (t >= 0.0 && im1_planning.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      im1_planning.tStart = t;  // (not accounting for frame time here)
      im1_planning.frameNStart = frameN;  // exact frame index
      
      im1_planning.setAutoDraw(true);
    }

    
    // *im2_planning* updates
    if (t >= 0.0 && im2_planning.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      im2_planning.tStart = t;  // (not accounting for frame time here)
      im2_planning.frameNStart = frameN;  // exact frame index
      
      im2_planning.setAutoDraw(true);
    }

    
    // *example_trial_choice_phase_2* updates
    if (t >= 0.0 && example_trial_choice_phase_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      example_trial_choice_phase_2.tStart = t;  // (not accounting for frame time here)
      example_trial_choice_phase_2.frameNStart = frameN;  // exact frame index
      
      example_trial_choice_phase_2.setAutoDraw(true);
    }

    
    // *im1_rewvalue_planning* updates
    if (t >= 0.0 && im1_rewvalue_planning.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      im1_rewvalue_planning.tStart = t;  // (not accounting for frame time here)
      im1_rewvalue_planning.frameNStart = frameN;  // exact frame index
      
      im1_rewvalue_planning.setAutoDraw(true);
    }

    
    // *im2_rewvalue_planning* updates
    if (t >= 0.0 && im2_rewvalue_planning.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      im2_rewvalue_planning.tStart = t;  // (not accounting for frame time here)
      im2_rewvalue_planning.frameNStart = frameN;  // exact frame index
      
      im2_rewvalue_planning.setAutoDraw(true);
    }

    
    // *text_29* updates
    if (t >= 2.0 && text_29.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_29.tStart = t;  // (not accounting for frame time here)
      text_29.frameNStart = frameN;  // exact frame index
      
      text_29.setAutoDraw(true);
    }

    
    // *key_resp_24* updates
    if (t >= 2.0 && key_resp_24.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_24.tStart = t;  // (not accounting for frame time here)
      key_resp_24.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_24.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_24.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_24.clearEvents(); });
    }

    if (key_resp_24.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_24.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_24_allKeys = _key_resp_24_allKeys.concat(theseKeys);
      if (_key_resp_24_allKeys.length > 0) {
        key_resp_24.keys = _key_resp_24_allKeys[_key_resp_24_allKeys.length - 1].name;  // just the last key pressed
        key_resp_24.rt = _key_resp_24_allKeys[_key_resp_24_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *im3_planning* updates
    if (t >= 0.0 && im3_planning.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      im3_planning.tStart = t;  // (not accounting for frame time here)
      im3_planning.frameNStart = frameN;  // exact frame index
      
      im3_planning.setAutoDraw(true);
    }

    
    // *im4_planning* updates
    if (t >= 0.0 && im4_planning.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      im4_planning.tStart = t;  // (not accounting for frame time here)
      im4_planning.frameNStart = frameN;  // exact frame index
      
      im4_planning.setAutoDraw(true);
    }

    
    // *im3_num_planning* updates
    if (t >= 0.0 && im3_num_planning.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      im3_num_planning.tStart = t;  // (not accounting for frame time here)
      im3_num_planning.frameNStart = frameN;  // exact frame index
      
      im3_num_planning.setAutoDraw(true);
    }

    
    // *im4_num_planning* updates
    if (t >= 0.0 && im4_num_planning.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      im4_num_planning.tStart = t;  // (not accounting for frame time here)
      im4_num_planning.frameNStart = frameN;  // exact frame index
      
      im4_num_planning.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of info_choicephaseComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function info_choicephaseRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'info_choicephase' ---
    for (const thisComponent of info_choicephaseComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_24.corr, level);
    }
    psychoJS.experiment.addData('key_resp_24.keys', key_resp_24.keys);
    if (typeof key_resp_24.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_24.rt', key_resp_24.rt);
        routineTimer.reset();
        }
    
    key_resp_24.stop();
    // the Routine "info_choicephase" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_25_allKeys;
var stage1_choice_enactComponents;
function stage1_choice_enactRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'stage1_choice_enact' ---
    t = 0;
    stage1_choice_enactClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_48
    if ((incorrect_actions > 4)) {
        PR_vs_SR.finished = true;
        continueRoutine = false;
    }
    
    key_resp_25.keys = undefined;
    key_resp_25.rt = undefined;
    _key_resp_25_allKeys = [];
    // keep track of which components have finished
    stage1_choice_enactComponents = [];
    stage1_choice_enactComponents.push(text_81);
    stage1_choice_enactComponents.push(key_resp_25);
    
    for (const thisComponent of stage1_choice_enactComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function stage1_choice_enactRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'stage1_choice_enact' ---
    // get current time
    t = stage1_choice_enactClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_81* updates
    if (t >= 0.0 && text_81.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_81.tStart = t;  // (not accounting for frame time here)
      text_81.frameNStart = frameN;  // exact frame index
      
      text_81.setAutoDraw(true);
    }

    
    // *key_resp_25* updates
    if (t >= 0.2 && key_resp_25.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_25.tStart = t;  // (not accounting for frame time here)
      key_resp_25.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_25.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_25.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_25.clearEvents(); });
    }

    if (key_resp_25.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_25.getKeys({keyList: ['1', '9', '2', '8'], waitRelease: false});
      _key_resp_25_allKeys = _key_resp_25_allKeys.concat(theseKeys);
      if (_key_resp_25_allKeys.length > 0) {
        key_resp_25.keys = _key_resp_25_allKeys[_key_resp_25_allKeys.length - 1].name;  // just the last key pressed
        key_resp_25.rt = _key_resp_25_allKeys[_key_resp_25_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of stage1_choice_enactComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stage1_choice_enactRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'stage1_choice_enact' ---
    for (const thisComponent of stage1_choice_enactComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_25.corr, level);
    }
    psychoJS.experiment.addData('key_resp_25.keys', key_resp_25.keys);
    if (typeof key_resp_25.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_25.rt', key_resp_25.rt);
        routineTimer.reset();
        }
    
    key_resp_25.stop();
    // the Routine "stage1_choice_enact" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_36_allKeys;
var stage2_choice_enactComponents;
function stage2_choice_enactRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'stage2_choice_enact' ---
    t = 0;
    stage2_choice_enactClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_54
    if ((incorrect_actions > 4)) {
        PR_vs_SR.finished = true;
        continueRoutine = false;
    }
    
    key_resp_36.keys = undefined;
    key_resp_36.rt = undefined;
    _key_resp_36_allKeys = [];
    // keep track of which components have finished
    stage2_choice_enactComponents = [];
    stage2_choice_enactComponents.push(text_82);
    stage2_choice_enactComponents.push(key_resp_36);
    
    for (const thisComponent of stage2_choice_enactComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function stage2_choice_enactRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'stage2_choice_enact' ---
    // get current time
    t = stage2_choice_enactClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_82* updates
    if (t >= 0.0 && text_82.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_82.tStart = t;  // (not accounting for frame time here)
      text_82.frameNStart = frameN;  // exact frame index
      
      text_82.setAutoDraw(true);
    }

    
    // *key_resp_36* updates
    if (t >= 0 && key_resp_36.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_36.tStart = t;  // (not accounting for frame time here)
      key_resp_36.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_36.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_36.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_36.clearEvents(); });
    }

    if (key_resp_36.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_36.getKeys({keyList: ['1', '9', '2', '8'], waitRelease: false});
      _key_resp_36_allKeys = _key_resp_36_allKeys.concat(theseKeys);
      if (_key_resp_36_allKeys.length > 0) {
        key_resp_36.keys = _key_resp_36_allKeys[_key_resp_36_allKeys.length - 1].name;  // just the last key pressed
        key_resp_36.rt = _key_resp_36_allKeys[_key_resp_36_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of stage2_choice_enactComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stage2_choice_enactRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'stage2_choice_enact' ---
    for (const thisComponent of stage2_choice_enactComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_36.corr, level);
    }
    psychoJS.experiment.addData('key_resp_36.keys', key_resp_36.keys);
    if (typeof key_resp_36.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_36.rt', key_resp_36.rt);
        routineTimer.reset();
        }
    
    key_resp_36.stop();
    // the Routine "stage2_choice_enact" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_16_allKeys;
var final_stage5Components;
function final_stage5RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'final_stage5' ---
    t = 0;
    final_stage5Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_49
    if ((incorrect_actions > 4)) {
        PR_vs_SR.finished = true;
        continueRoutine = false;
    }
    
    key_resp_16.keys = undefined;
    key_resp_16.rt = undefined;
    _key_resp_16_allKeys = [];
    // keep track of which components have finished
    final_stage5Components = [];
    final_stage5Components.push(text_68);
    final_stage5Components.push(text_30);
    final_stage5Components.push(key_resp_16);
    
    for (const thisComponent of final_stage5Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function final_stage5RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'final_stage5' ---
    // get current time
    t = final_stage5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_68* updates
    if (t >= 0 && text_68.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_68.tStart = t;  // (not accounting for frame time here)
      text_68.frameNStart = frameN;  // exact frame index
      
      text_68.setAutoDraw(true);
    }

    frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_68.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_68.setAutoDraw(false);
    }
    
    // *text_30* updates
    if (t >= 1.6 && text_30.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_30.tStart = t;  // (not accounting for frame time here)
      text_30.frameNStart = frameN;  // exact frame index
      
      text_30.setAutoDraw(true);
    }

    
    // *key_resp_16* updates
    if (t >= 1.75 && key_resp_16.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_16.tStart = t;  // (not accounting for frame time here)
      key_resp_16.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_16.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_16.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_16.clearEvents(); });
    }

    if (key_resp_16.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_16.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_16_allKeys = _key_resp_16_allKeys.concat(theseKeys);
      if (_key_resp_16_allKeys.length > 0) {
        key_resp_16.keys = _key_resp_16_allKeys[_key_resp_16_allKeys.length - 1].name;  // just the last key pressed
        key_resp_16.rt = _key_resp_16_allKeys[_key_resp_16_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of final_stage5Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function final_stage5RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'final_stage5' ---
    for (const thisComponent of final_stage5Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp_16.stop();
    // the Routine "final_stage5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_8_allKeys;
var transition_revaluationComponents;
function transition_revaluationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'transition_revaluation' ---
    t = 0;
    transition_revaluationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_44
    if ((incorrect_actions > 4)) {
        continueRoutine = false;
    }
    
    key_resp_8.keys = undefined;
    key_resp_8.rt = undefined;
    _key_resp_8_allKeys = [];
    // keep track of which components have finished
    transition_revaluationComponents = [];
    transition_revaluationComponents.push(text_25);
    transition_revaluationComponents.push(text_26);
    transition_revaluationComponents.push(key_resp_8);
    transition_revaluationComponents.push(trident_reval);
    transition_revaluationComponents.push(watch_reval);
    transition_revaluationComponents.push(right_arrow);
    transition_revaluationComponents.push(planet_reval);
    transition_revaluationComponents.push(right_arrow2);
    transition_revaluationComponents.push(fox_reval);
    transition_revaluationComponents.push(text_94);
    
    for (const thisComponent of transition_revaluationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function transition_revaluationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'transition_revaluation' ---
    // get current time
    t = transition_revaluationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_25* updates
    if (t >= 0.0 && text_25.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_25.tStart = t;  // (not accounting for frame time here)
      text_25.frameNStart = frameN;  // exact frame index
      
      text_25.setAutoDraw(true);
    }

    
    // *text_26* updates
    if (t >= 0.0 && text_26.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_26.tStart = t;  // (not accounting for frame time here)
      text_26.frameNStart = frameN;  // exact frame index
      
      text_26.setAutoDraw(true);
    }

    
    // *key_resp_8* updates
    if (t >= 2.5 && key_resp_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_8.tStart = t;  // (not accounting for frame time here)
      key_resp_8.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_8.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_8.clearEvents(); });
    }

    if (key_resp_8.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_8.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_8_allKeys = _key_resp_8_allKeys.concat(theseKeys);
      if (_key_resp_8_allKeys.length > 0) {
        key_resp_8.keys = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].name;  // just the last key pressed
        key_resp_8.rt = _key_resp_8_allKeys[_key_resp_8_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *trident_reval* updates
    if (t >= 0.0 && trident_reval.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trident_reval.tStart = t;  // (not accounting for frame time here)
      trident_reval.frameNStart = frameN;  // exact frame index
      
      trident_reval.setAutoDraw(true);
    }

    
    // *watch_reval* updates
    if (t >= 0.0 && watch_reval.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      watch_reval.tStart = t;  // (not accounting for frame time here)
      watch_reval.frameNStart = frameN;  // exact frame index
      
      watch_reval.setAutoDraw(true);
    }

    
    // *right_arrow* updates
    if (t >= 0.0 && right_arrow.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      right_arrow.tStart = t;  // (not accounting for frame time here)
      right_arrow.frameNStart = frameN;  // exact frame index
      
      right_arrow.setAutoDraw(true);
    }

    
    // *planet_reval* updates
    if (t >= 0.0 && planet_reval.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      planet_reval.tStart = t;  // (not accounting for frame time here)
      planet_reval.frameNStart = frameN;  // exact frame index
      
      planet_reval.setAutoDraw(true);
    }

    
    // *right_arrow2* updates
    if (t >= 0.0 && right_arrow2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      right_arrow2.tStart = t;  // (not accounting for frame time here)
      right_arrow2.frameNStart = frameN;  // exact frame index
      
      right_arrow2.setAutoDraw(true);
    }

    
    // *fox_reval* updates
    if (t >= 0.0 && fox_reval.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fox_reval.tStart = t;  // (not accounting for frame time here)
      fox_reval.frameNStart = frameN;  // exact frame index
      
      fox_reval.setAutoDraw(true);
    }

    
    // *text_94* updates
    if (t >= 2.5 && text_94.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_94.tStart = t;  // (not accounting for frame time here)
      text_94.frameNStart = frameN;  // exact frame index
      
      text_94.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of transition_revaluationComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function transition_revaluationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'transition_revaluation' ---
    for (const thisComponent of transition_revaluationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_8.corr, level);
    }
    psychoJS.experiment.addData('key_resp_8.keys', key_resp_8.keys);
    if (typeof key_resp_8.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_8.rt', key_resp_8.rt);
        routineTimer.reset();
        }
    
    key_resp_8.stop();
    // the Routine "transition_revaluation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_29_allKeys;
var info_choice_revaluation_2Components;
function info_choice_revaluation_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'info_choice_revaluation_2' ---
    t = 0;
    info_choice_revaluation_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_45
    if ((incorrect_actions > 4)) {
        transition_revaluation_round.finished = true;
        continueRoutine = false;
    }
    
    im1_planning_2.setImage(r1);
    im2_planning_2.setImage(r2);
    im1_rewvalue_planning_2.setText(r1_num);
    im2_rewvalue_planning_2.setText(r2_num);
    key_resp_29.keys = undefined;
    key_resp_29.rt = undefined;
    _key_resp_29_allKeys = [];
    // keep track of which components have finished
    info_choice_revaluation_2Components = [];
    info_choice_revaluation_2Components.push(im1_planning_2);
    info_choice_revaluation_2Components.push(im2_planning_2);
    info_choice_revaluation_2Components.push(example_trial_choice_phase_4);
    info_choice_revaluation_2Components.push(im1_rewvalue_planning_2);
    info_choice_revaluation_2Components.push(im2_rewvalue_planning_2);
    info_choice_revaluation_2Components.push(text_93);
    info_choice_revaluation_2Components.push(key_resp_29);
    
    for (const thisComponent of info_choice_revaluation_2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function info_choice_revaluation_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'info_choice_revaluation_2' ---
    // get current time
    t = info_choice_revaluation_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *im1_planning_2* updates
    if (t >= 0.0 && im1_planning_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      im1_planning_2.tStart = t;  // (not accounting for frame time here)
      im1_planning_2.frameNStart = frameN;  // exact frame index
      
      im1_planning_2.setAutoDraw(true);
    }

    
    // *im2_planning_2* updates
    if (t >= 0.0 && im2_planning_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      im2_planning_2.tStart = t;  // (not accounting for frame time here)
      im2_planning_2.frameNStart = frameN;  // exact frame index
      
      im2_planning_2.setAutoDraw(true);
    }

    
    // *example_trial_choice_phase_4* updates
    if (t >= 0.0 && example_trial_choice_phase_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      example_trial_choice_phase_4.tStart = t;  // (not accounting for frame time here)
      example_trial_choice_phase_4.frameNStart = frameN;  // exact frame index
      
      example_trial_choice_phase_4.setAutoDraw(true);
    }

    
    // *im1_rewvalue_planning_2* updates
    if (t >= 0.0 && im1_rewvalue_planning_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      im1_rewvalue_planning_2.tStart = t;  // (not accounting for frame time here)
      im1_rewvalue_planning_2.frameNStart = frameN;  // exact frame index
      
      im1_rewvalue_planning_2.setAutoDraw(true);
    }

    
    // *im2_rewvalue_planning_2* updates
    if (t >= 0.0 && im2_rewvalue_planning_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      im2_rewvalue_planning_2.tStart = t;  // (not accounting for frame time here)
      im2_rewvalue_planning_2.frameNStart = frameN;  // exact frame index
      
      im2_rewvalue_planning_2.setAutoDraw(true);
    }

    
    // *text_93* updates
    if (t >= 2.0 && text_93.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_93.tStart = t;  // (not accounting for frame time here)
      text_93.frameNStart = frameN;  // exact frame index
      
      text_93.setAutoDraw(true);
    }

    
    // *key_resp_29* updates
    if (t >= 2.0 && key_resp_29.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_29.tStart = t;  // (not accounting for frame time here)
      key_resp_29.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_29.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_29.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_29.clearEvents(); });
    }

    if (key_resp_29.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_29.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_29_allKeys = _key_resp_29_allKeys.concat(theseKeys);
      if (_key_resp_29_allKeys.length > 0) {
        key_resp_29.keys = _key_resp_29_allKeys[_key_resp_29_allKeys.length - 1].name;  // just the last key pressed
        key_resp_29.rt = _key_resp_29_allKeys[_key_resp_29_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of info_choice_revaluation_2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function info_choice_revaluation_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'info_choice_revaluation_2' ---
    for (const thisComponent of info_choice_revaluation_2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_29.corr, level);
    }
    psychoJS.experiment.addData('key_resp_29.keys', key_resp_29.keys);
    if (typeof key_resp_29.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_29.rt', key_resp_29.rt);
        routineTimer.reset();
        }
    
    key_resp_29.stop();
    // the Routine "info_choice_revaluation_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _transition_reval_choice_allKeys;
var choice_transistion_revalComponents;
function choice_transistion_revalRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'choice_transistion_reval' ---
    t = 0;
    choice_transistion_revalClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_52
    if ((incorrect_actions > 4)) {
        transition_revaluation_round.finished = true;
        continueRoutine = false;
    }
    
    transition_reval_choice.keys = undefined;
    transition_reval_choice.rt = undefined;
    _transition_reval_choice_allKeys = [];
    // keep track of which components have finished
    choice_transistion_revalComponents = [];
    choice_transistion_revalComponents.push(text_105);
    choice_transistion_revalComponents.push(transition_reval_choice);
    
    for (const thisComponent of choice_transistion_revalComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function choice_transistion_revalRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'choice_transistion_reval' ---
    // get current time
    t = choice_transistion_revalClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_105* updates
    if (t >= 0.0 && text_105.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_105.tStart = t;  // (not accounting for frame time here)
      text_105.frameNStart = frameN;  // exact frame index
      
      text_105.setAutoDraw(true);
    }

    
    // *transition_reval_choice* updates
    if (t >= 0.2 && transition_reval_choice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      transition_reval_choice.tStart = t;  // (not accounting for frame time here)
      transition_reval_choice.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { transition_reval_choice.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { transition_reval_choice.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { transition_reval_choice.clearEvents(); });
    }

    if (transition_reval_choice.status === PsychoJS.Status.STARTED) {
      let theseKeys = transition_reval_choice.getKeys({keyList: ['1', '9', '2', '8'], waitRelease: false});
      _transition_reval_choice_allKeys = _transition_reval_choice_allKeys.concat(theseKeys);
      if (_transition_reval_choice_allKeys.length > 0) {
        transition_reval_choice.keys = _transition_reval_choice_allKeys[_transition_reval_choice_allKeys.length - 1].name;  // just the last key pressed
        transition_reval_choice.rt = _transition_reval_choice_allKeys[_transition_reval_choice_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of choice_transistion_revalComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function choice_transistion_revalRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'choice_transistion_reval' ---
    for (const thisComponent of choice_transistion_revalComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(transition_reval_choice.corr, level);
    }
    psychoJS.experiment.addData('transition_reval_choice.keys', transition_reval_choice.keys);
    if (typeof transition_reval_choice.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('transition_reval_choice.rt', transition_reval_choice.rt);
        routineTimer.reset();
        }
    
    transition_reval_choice.stop();
    // the Routine "choice_transistion_reval" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _transition_reval_choice_2_allKeys;
var choice_transition2Components;
function choice_transition2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'choice_transition2' ---
    t = 0;
    choice_transition2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_55
    if ((incorrect_actions > 4)) {
        transition_revaluation_round.finished = true;
        continueRoutine = false;
    }
    
    transition_reval_choice_2.keys = undefined;
    transition_reval_choice_2.rt = undefined;
    _transition_reval_choice_2_allKeys = [];
    // keep track of which components have finished
    choice_transition2Components = [];
    choice_transition2Components.push(text_106);
    choice_transition2Components.push(transition_reval_choice_2);
    
    for (const thisComponent of choice_transition2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function choice_transition2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'choice_transition2' ---
    // get current time
    t = choice_transition2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_106* updates
    if (t >= 0.0 && text_106.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_106.tStart = t;  // (not accounting for frame time here)
      text_106.frameNStart = frameN;  // exact frame index
      
      text_106.setAutoDraw(true);
    }

    
    // *transition_reval_choice_2* updates
    if (t >= 0 && transition_reval_choice_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      transition_reval_choice_2.tStart = t;  // (not accounting for frame time here)
      transition_reval_choice_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { transition_reval_choice_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { transition_reval_choice_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { transition_reval_choice_2.clearEvents(); });
    }

    if (transition_reval_choice_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = transition_reval_choice_2.getKeys({keyList: ['1', '9', '2', '8'], waitRelease: false});
      _transition_reval_choice_2_allKeys = _transition_reval_choice_2_allKeys.concat(theseKeys);
      if (_transition_reval_choice_2_allKeys.length > 0) {
        transition_reval_choice_2.keys = _transition_reval_choice_2_allKeys[_transition_reval_choice_2_allKeys.length - 1].name;  // just the last key pressed
        transition_reval_choice_2.rt = _transition_reval_choice_2_allKeys[_transition_reval_choice_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of choice_transition2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function choice_transition2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'choice_transition2' ---
    for (const thisComponent of choice_transition2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(transition_reval_choice_2.corr, level);
    }
    psychoJS.experiment.addData('transition_reval_choice_2.keys', transition_reval_choice_2.keys);
    if (typeof transition_reval_choice_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('transition_reval_choice_2.rt', transition_reval_choice_2.rt);
        routineTimer.reset();
        }
    
    transition_reval_choice_2.stop();
    // the Routine "choice_transition2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_34_allKeys;
var final_stage_TrComponents;
function final_stage_TrRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'final_stage_Tr' ---
    t = 0;
    final_stage_TrClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_51
    if ((incorrect_actions > 4)) {
        transition_revaluation_round.finished = true;
        continueRoutine = false;
    }
    
    key_resp_34.keys = undefined;
    key_resp_34.rt = undefined;
    _key_resp_34_allKeys = [];
    // keep track of which components have finished
    final_stage_TrComponents = [];
    final_stage_TrComponents.push(text_103);
    final_stage_TrComponents.push(text_104);
    final_stage_TrComponents.push(key_resp_34);
    
    for (const thisComponent of final_stage_TrComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function final_stage_TrRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'final_stage_Tr' ---
    // get current time
    t = final_stage_TrClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_103* updates
    if (t >= 0 && text_103.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_103.tStart = t;  // (not accounting for frame time here)
      text_103.frameNStart = frameN;  // exact frame index
      
      text_103.setAutoDraw(true);
    }

    frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_103.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_103.setAutoDraw(false);
    }
    
    // *text_104* updates
    if (t >= 1.6 && text_104.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_104.tStart = t;  // (not accounting for frame time here)
      text_104.frameNStart = frameN;  // exact frame index
      
      text_104.setAutoDraw(true);
    }

    
    // *key_resp_34* updates
    if (t >= 1.75 && key_resp_34.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_34.tStart = t;  // (not accounting for frame time here)
      key_resp_34.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_34.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_34.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_34.clearEvents(); });
    }

    if (key_resp_34.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_34.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_34_allKeys = _key_resp_34_allKeys.concat(theseKeys);
      if (_key_resp_34_allKeys.length > 0) {
        key_resp_34.keys = _key_resp_34_allKeys[_key_resp_34_allKeys.length - 1].name;  // just the last key pressed
        key_resp_34.rt = _key_resp_34_allKeys[_key_resp_34_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of final_stage_TrComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function final_stage_TrRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'final_stage_Tr' ---
    for (const thisComponent of final_stage_TrComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp_34.stop();
    // the Routine "final_stage_Tr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var reward_totalComponents;
function reward_totalRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'reward_total' ---
    t = 0;
    reward_totalClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.500000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_46
    if ((incorrect_actions > 4)) {
        continueRoutine = false;
    }
    
    // keep track of which components have finished
    reward_totalComponents = [];
    reward_totalComponents.push(text_84);
    
    for (const thisComponent of reward_totalComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function reward_totalRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'reward_total' ---
    // get current time
    t = reward_totalClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_84* updates
    if (t >= 0.0 && text_84.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_84.tStart = t;  // (not accounting for frame time here)
      text_84.frameNStart = frameN;  // exact frame index
      
      text_84.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_84.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_84.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of reward_totalComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reward_totalRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'reward_total' ---
    for (const thisComponent of reward_totalComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var doneComponents;
function doneRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'done' ---
    t = 0;
    doneClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(6.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code_47
    if ((incorrect_actions > 4)) {
        continueRoutine = false;
    }
    
    // keep track of which components have finished
    doneComponents = [];
    doneComponents.push(text_62);
    
    for (const thisComponent of doneComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function doneRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'done' ---
    // get current time
    t = doneClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_62* updates
    if (t >= 0.0 && text_62.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_62.tStart = t;  // (not accounting for frame time here)
      text_62.frameNStart = frameN;  // exact frame index
      
      text_62.setAutoDraw(true);
    }

    frameRemains = 0.0 + 6.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_62.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_62.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of doneComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function doneRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'done' ---
    for (const thisComponent of doneComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
