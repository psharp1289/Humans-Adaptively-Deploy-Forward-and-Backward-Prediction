/*************** 
 * Study3 Test *
 ***************/

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

// store info about the experiment session:
let expName = 'study3';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

// Start code blocks for 'Before Experiment'
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
flowScheduler.add(instructions_get_rightLoopBegin, instructions_get_rightLoopScheduler);
flowScheduler.add(instructions_get_rightLoopScheduler);
flowScheduler.add(instructions_get_rightLoopEnd);
flowScheduler.add(time_limitRoutineBegin());
flowScheduler.add(time_limitRoutineEachFrame());
flowScheduler.add(time_limitRoutineEnd());
flowScheduler.add(instructions3RoutineBegin());
flowScheduler.add(instructions3RoutineEachFrame());
flowScheduler.add(instructions3RoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(instructions_reward_stageRoutineBegin());
flowScheduler.add(instructions_reward_stageRoutineEachFrame());
flowScheduler.add(instructions_reward_stageRoutineEnd());
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
flowScheduler.add(PR_vs_SRLoopBegin, PR_vs_SRLoopScheduler);
flowScheduler.add(PR_vs_SRLoopScheduler);
flowScheduler.add(PR_vs_SRLoopEnd);
flowScheduler.add(transition_revaluationRoutineBegin());
flowScheduler.add(transition_revaluationRoutineEachFrame());
flowScheduler.add(transition_revaluationRoutineEnd());
const transition_revaluation_roundLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(transition_revaluation_roundLoopBegin, transition_revaluation_roundLoopScheduler);
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
    {'name': 'Study3_learningtrials.csv', 'path': 'Study3_learningtrials.csv'},
    {'name': 'consent2.png', 'path': 'consent2.png'},
    {'name': 'tree.png', 'path': 'tree.png'},
    {'name': 'train.png', 'path': 'train.png'},
    {'name': 'bell.png', 'path': 'bell.png'},
    {'name': 'planet.png', 'path': 'planet.png'},
    {'name': 'fox.png', 'path': 'fox.png'},
    {'name': 'right.png', 'path': 'right.png'},
    {'name': 'choicephase_afterevaluation.xlsx', 'path': 'choicephase_afterevaluation.xlsx'},
    {'name': 'fireworks.png', 'path': 'fireworks.png'},
    {'name': 'compass.png', 'path': 'compass.png'},
    {'name': 'apple.png', 'path': 'apple.png'},
    {'name': 'wm.png', 'path': 'wm.png'},
    {'name': 'new_choicephase.xlsx', 'path': 'new_choicephase.xlsx'},
    {'name': 'unicorn.png', 'path': 'unicorn.png'},
    {'name': 'houses.png', 'path': 'houses.png'},
    {'name': 'tophat.png', 'path': 'tophat.png'},
    {'name': 'trident.png', 'path': 'trident.png'},
    {'name': 'basket.png', 'path': 'basket.png'},
    {'name': 'window.png', 'path': 'window.png'},
    {'name': 'consent1.png', 'path': 'consent1.png'},
    {'name': 'snorkel.png', 'path': 'snorkel.png'},
    {'name': 'hammer.png', 'path': 'hammer.png'},
    {'name': 'north.png', 'path': 'north.png'},
    {'name': 'watch.png', 'path': 'watch.png'},
    {'name': 'stage2_4_practice.csv', 'path': 'stage2_4_practice.csv'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.DEBUG);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.1.3';
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
var learning_reward_startingstate_list;
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
var picture_image;
var text_3;
var incorrect_answerClock;
var incorrect_display;
var learning_trial_sequenceClock;
var stage1_learning;
var text_78;
var stage2_learning;
var text_80;
var stage3_learning;
var memory_qClock;
var text_92;
var prediction4Clock;
var outcome4;
var picture_reward_goal;
var resp4;
var memory_image1;
var memory_image2;
var text_79;
var text_85;
var quiz_scoreClock;
var text_5;
var take_a_breakClock;
var text_39;
var instructions_reward_stageClock;
var instructions_rewardstage;
var key_resp_11;
var i2_rewardClock;
var text_42;
var key_resp_9;
var practice_view_reward_infoClock;
var im1_example_choicephase;
var resp4_2;
var im2_example_choicephase;
var example_trial_choice_phase;
var im1_rewvalue;
var text_28;
var key_resp_3;
var image_19;
var instructions_planningClock;
var text_66;
var houses_choice_practice;
var train_choice_practice;
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
var goal_image;
var im3_num_planning;
var stage1_choice_enactClock;
var text_81;
var image1test;
var image2test;
var key_resp_25;
var text_31;
var text_82;
var final_stage5Clock;
var text_68;
var text_30;
var key_resp_16;
var transition_revaluationClock;
var text_25;
var text_26;
var key_resp_8;
var tree_reval;
var trident_reval;
var right_arrow;
var fox_reval;
var right_arrow2;
var planet_reval;
var text_94;
var info_choice_revaluation_2Clock;
var im1_planning_2;
var im2_planning_2;
var example_trial_choice_phase_4;
var im1_rewvalue_planning_2;
var text_93;
var key_resp_29;
var goal_transition_reval;
var choice_transistion_revalClock;
var text_105;
var trident_choice_3;
var planet_choice_3;
var transition_reval_choice;
var text_106;
var text_107;
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
function experimentInit() {
  // Initialize components for Routine "consent"
  consentClock = new util.Clock();
  image_11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_11', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0.05], size : [0.65, 0.75],
    color : new util.Color([1, 1, 1]), opacity : undefined,
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
    color : new util.Color([1, 1, 1]), opacity : undefined,
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
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  // Initialize components for Routine "instructions"
  instructionsClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'In this task, you will learn how to navigate a picture game. Each time you navigate in the game, you have a single choice to make. Each choice you make will take you from one picture to another. \n\nIn the first part of this task you must learn how often other pictures tend to appear after starting at an initial picture. For example, you might need to learn how often you see an apple after starting at an image of a tree. \n\nThus, this task requires you to learn probabilities of image transitions. The probability of seeing an apple after a tree might be very different from the probability of seeing the apple after a rock. \n\nAfter this learning phase, you can use this knowledge to plan how to win points in a final phase. Importantly, you can earn money based on these points. You will be instructed later exactly how to win points. \n\nPress Space to continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
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
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  trident_start = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trident_start', units : undefined, 
    image : 'trident.png', mask : undefined,
    ori : 0.0, pos : [(- 0.4), (- 0.1)], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  planet_start = new visual.ImageStim({
    win : psychoJS.window,
    name : 'planet_start', units : undefined, 
    image : 'planet.png', mask : undefined,
    ori : 0.0, pos : [0.4, (- 0.1)], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  instructions_decisionrules = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_decisionrules',
    text: 'The first decision will say “START”. Here, choosing 1 will ALWAYS get you to the TRIDENT, choosing 9 will ALWAYS get you to the PLANET.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.4], height: 0.04,  wrapWidth: undefined, ori: 0.0,
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
    color: new util.Color('black'),  opacity: undefined,
    depth: -7.0 
  });
  
  // Initialize components for Routine "stage2_4_instructions"
  stage2_4_instructionsClock = new util.Clock();
  responseleft = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: 'After choosing the trident or the planet, you will see a series of TWO MORE IMAGES. Your goal is to remember which images tend to come after you start at either the trident or the planet image. \n\nTo show you what this looks like, you will do a practice round. You will be tested to see if you remember which images come after the starting image. Good luck! \n\nPress SPACE to continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.0], height: 0.04,  wrapWidth: undefined, ori: 0.0,
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
    color : new util.Color([1, 1, 1]), opacity : undefined,
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
    color : new util.Color([1, 1, 1]), opacity : undefined,
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
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  image_12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_12', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : undefined,
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
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  fireworks_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fireworks_2', units : undefined, 
    image : 'fireworks.png', mask : undefined,
    ori : 0.0, pos : [0, (- 0.05)], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  tree_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'tree_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.6, (- 0.05)], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
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
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_17 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions_quiz_2"
  instructions_quiz_2Clock = new util.Clock();
  text_70 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_70',
    text: 'Instructions Quiz\n\n1. How are the second and third images different from the first?\n\na. you get to select actions at the second and third images \n\nb.these images are new every time\n\nc. you need to learn which second and third images you tend to see after taking an action at a starting image, but you don’t take any actions once you’re at the second and third images.\n\nd. you need to learn which second and third images you tend to see after taking an action at a starting image, and you MUST take NEW actions once you’re at the second image to see the third image.\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.038,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_18 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instructions_quiz_3"
  instructions_quiz_3Clock = new util.Clock();
  text_71 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_71',
    text: 'Instructions Quiz\n\n1. What happens during the reward quiz?\n\na.you must recall how the pictures look\n\nb. you are told that a picture has money hiding in it, and you must choose the action that has the best chance of getting you there. 5 of these rounds the computer chooses AT RANDOM will determine how much money you win!\n\nc. you must recall images you most likely DO NOT see after taking an action at a starting image\n\nd. you are told that a picture has money hiding in it, and you must choose the action that has the best chance of getting you there. Your TOTAL SCORE on these rounds will determine how much money you win!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.038,  wrapWidth: undefined, ori: 0.0,
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
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  key_resp_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  quiz1list = ["apple.png", "trident.png", "fireworks.png", "fox.png", "bowling.png"];
  quiz2list = ["window.png", "bell.png", "tree.png", "watch.png"];
  q1left_correct = ["1", "3", "5", "2", "7"];
  q1right_correct = ["2", "4", "7", "3", "8"];
  q2left_correct = ["5", "1", "6", "2"];
  q2right_correct = ["6", "3", "5", "4"];
  learning_reward_goal_list = ["planet.png", "planet.png", "planet.png", "trident.png", "trident.png", "planet.png", "planet.png", "trident.png", "planet.png", "trident.png", "trident.png", "trident.png", "planet.png", "planet.png", "trident.png", "planet.png", "planet.png", "trident.png"];
  learning_reward_startingstate_list = [["north.png", "hammer.png"], ["window.png", "apple.png"], ["snorkel.png", "compass.png"], ["tophat.png", "apple.png"], ["snorkel.png", "houses.png"], ["north.png", "compass.png"], ["train.png", "houses.png"], ["window.png", "compass.png"], ["train.png", "hammer.png"], ["snorkel.png", "compass.png"], ["tophat.png", "compass.png"], ["north.png", "houses.png"], ["window.png", "hammer.png"], ["tophat.png", "apple.png"], ["train.png", "houses.png"], ["window.png", "hammer.png"], ["train.png", "apple.png"], ["snorkel.png", "apple.png"]];
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
    text: 'Choose the number that appears below one of the images:',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.4], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  picture_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'picture_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.35, 0.35],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.25)], height: 0.07,  wrapWidth: undefined, ori: 0.0,
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
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "learning_trial_sequence"
  learning_trial_sequenceClock = new util.Clock();
  stage1_learning = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stage1_learning', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  text_78 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_78',
    text: 'Moving to next image…',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  stage2_learning = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stage2_learning', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  text_80 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_80',
    text: 'Moving to the next image…',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  stage3_learning = new visual.ImageStim({
    win : psychoJS.window,
    name : 'stage3_learning', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
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
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  picture_reward_goal = new visual.ImageStim({
    win : psychoJS.window,
    name : 'picture_reward_goal', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0.17], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  resp4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  memory_image1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'memory_image1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.25), (- 0.1)], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  memory_image2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'memory_image2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.25, (- 0.1)], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
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
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "instructions_reward_stage"
  instructions_reward_stageClock = new util.Clock();
  instructions_rewardstage = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructions_rewardstage',
    text: 'Now it’s time to use what you learned to get rewards. Each time you enter the picture world to win money, you will be told the planet or trident will give you points, and starting images you can choose from to try to get those points!\n\nYou will always be shown two images to try to reach either the planet or trident. You must use the probabilities you learned in training to make the best choice.\n\nPress Space to continue ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  key_resp_11 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "i2_reward"
  i2_rewardClock = new util.Clock();
  text_42 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_42',
    text: 'After you select one of the two starting images to try to reach the trident or planet images to try to win points, you will not see any more images aftewards. This prevents you from learning anything else at this phase, as you need to use what you already learned to plan accordingly. The computer will simulate which images you reached and calculate your points, but this will not be shown to you. Instead you will be told how many points you won after this phase is over.\n\nPress Space to Continue\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.035,  wrapWidth: undefined, ori: 0.0,
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
    ori : 0.0, pos : [(- 0.3), 0.15], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  resp4_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  im2_example_choicephase = new visual.ImageStim({
    win : psychoJS.window,
    name : 'im2_example_choicephase', units : undefined, 
    image : 'tree.png', mask : undefined,
    ori : 0.0, pos : [0.3, 0.15], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  example_trial_choice_phase = new visual.TextStim({
    win: psychoJS.window,
    name: 'example_trial_choice_phase',
    text: 'What image gets to the BOTTOM goal more?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.4], height: 0.055,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  im1_rewvalue = new visual.TextStim({
    win: psychoJS.window,
    name: 'im1_rewvalue',
    text: 'Win 100 points!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.28)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -5.0 
  });
  
  text_28 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_28',
    text: 'Press Space To Continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.32)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -6.0 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  image_19 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_19', units : undefined, 
    image : 'planet.png', mask : undefined,
    ori : 0.0, pos : [0, (- 0.15)], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  // Initialize components for Routine "instructions_planning"
  instructions_planningClock = new util.Clock();
  text_66 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_66',
    text: 'When you have decided how to act after seeing all information, you will choose either between the two starting images!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.3], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  houses_choice_practice = new visual.ImageStim({
    win : psychoJS.window,
    name : 'houses_choice_practice', units : undefined, 
    image : 'watch.png', mask : undefined,
    ori : 0.0, pos : [0.3, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  train_choice_practice = new visual.ImageStim({
    win : psychoJS.window,
    name : 'train_choice_practice', units : undefined, 
    image : 'tree.png', mask : undefined,
    ori : 0.0, pos : [(- 0.3), 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  key_resp_12 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_24 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_24',
    text: 'Press Space to Continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.35)], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -5.0 
  });
  
  // Initialize components for Routine "start_planning_trials"
  start_planning_trialsClock = new util.Clock();
  text_67 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_67',
    text: 'You are now ready to start the task, using the knowledge you learned about how to navigate through the pictures. Good luck!\n\nIf you get to the goal, you will win 100 points!\n\nPress Space to begin',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
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
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  im2_planning = new visual.ImageStim({
    win : psychoJS.window,
    name : 'im2_planning', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.2, 0.15], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  example_trial_choice_phase_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'example_trial_choice_phase_2',
    text: 'What image gets to the BOTTOM goal more?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.35], height: 0.05,  wrapWidth: undefined, ori: 0.0,
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
    color: new util.Color('black'),  opacity: undefined,
    depth: -6.0 
  });
  
  key_resp_24 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  goal_image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'goal_image', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, (- 0.12)], size : [0.28, 0.28],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  im3_num_planning = new visual.TextStim({
    win: psychoJS.window,
    name: 'im3_num_planning',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -9.0 
  });
  
  // Initialize components for Routine "stage1_choice_enact"
  stage1_choice_enactClock = new util.Clock();
  text_81 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_81',
    text: 'Make your decision',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  image1test = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image1test', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.3), 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  image2test = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image2test', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.3, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  key_resp_25 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_31 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_31',
    text: 'Press 1',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.3), (- 0.2)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -5.0 
  });
  
  text_82 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_82',
    text: 'Press 9',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.3, (- 0.2)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -6.0 
  });
  
  // Initialize components for Routine "final_stage5"
  final_stage5Clock = new util.Clock();
  text_68 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_68',
    text: 'Computer simulating images to calculate reward…',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
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
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  text_26 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_26',
    text: 'The picture world you learned has CHANGED! Now, the TREE leads only to the TRIDENT, and the FOX leads only to the PLANET. Look below and use this new information to win more money next!\n\n\n ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.2], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -2.0 
  });
  
  key_resp_8 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  tree_reval = new visual.ImageStim({
    win : psychoJS.window,
    name : 'tree_reval', units : undefined, 
    image : 'tree.png', mask : undefined,
    ori : 0.0, pos : [(- 0.2), 0], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -4.0 
  });
  trident_reval = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trident_reval', units : undefined, 
    image : 'trident.png', mask : undefined,
    ori : 0.0, pos : [0.2, 0], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  right_arrow = new visual.ImageStim({
    win : psychoJS.window,
    name : 'right_arrow', units : undefined, 
    image : 'right.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.16, 0.16],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -6.0 
  });
  fox_reval = new visual.ImageStim({
    win : psychoJS.window,
    name : 'fox_reval', units : undefined, 
    image : 'fox.png', mask : undefined,
    ori : 0.0, pos : [(- 0.2), (- 0.25)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  right_arrow2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'right_arrow2', units : undefined, 
    image : 'right.png', mask : undefined,
    ori : 0.0, pos : [0, (- 0.25)], size : [0.16, 0.16],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -8.0 
  });
  planet_reval = new visual.ImageStim({
    win : psychoJS.window,
    name : 'planet_reval', units : undefined, 
    image : 'planet.png', mask : undefined,
    ori : 0.0, pos : [0.2, (- 0.25)], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : undefined,
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
    color: new util.Color('black'),  opacity: undefined,
    depth: -10.0 
  });
  
  // Initialize components for Routine "info_choice_revaluation_2"
  info_choice_revaluation_2Clock = new util.Clock();
  im1_planning_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'im1_planning_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.2), 0.15], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  im2_planning_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'im2_planning_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.2, 0.15], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  example_trial_choice_phase_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'example_trial_choice_phase_4',
    text: 'What image gets to the BOTTOM goal more?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.35], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -3.0 
  });
  
  im1_rewvalue_planning_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'im1_rewvalue_planning_2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.3)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -4.0 
  });
  
  text_93 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_93',
    text: 'Press Space To Continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.045,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -5.0 
  });
  
  key_resp_29 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  goal_transition_reval = new visual.ImageStim({
    win : psychoJS.window,
    name : 'goal_transition_reval', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, (- 0.12)], size : [0.28, 0.28],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -7.0 
  });
  // Initialize components for Routine "choice_transistion_reval"
  choice_transistion_revalClock = new util.Clock();
  text_105 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_105',
    text: 'Make your decision',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0.4], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  trident_choice_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'trident_choice_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [(- 0.3), 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  planet_choice_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'planet_choice_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0.3, 0], size : [0.25, 0.25],
    color : new util.Color([1, 1, 1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  transition_reval_choice = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_106 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_106',
    text: 'Press 1',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.3), (- 0.2)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -5.0 
  });
  
  text_107 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_107',
    text: 'Press 9',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.3, (- 0.2)], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('black'),  opacity: undefined,
    depth: -6.0 
  });
  
  // Initialize components for Routine "final_stage_Tr"
  final_stage_TrClock = new util.Clock();
  text_103 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_103',
    text: 'Computer simulating images to calculate reward…',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
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
    color: new util.Color('black'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var instructions_get_right;
var currentLoop;
function instructions_get_rightLoopBegin(instructions_get_rightLoopScheduler) {
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
  instructions_get_right.forEach(function() {
    const snapshot = instructions_get_right.getSnapshot();

    instructions_get_rightLoopScheduler.add(importConditions(snapshot));
    instructions_get_rightLoopScheduler.add(consentRoutineBegin(snapshot));
    instructions_get_rightLoopScheduler.add(consentRoutineEachFrame(snapshot));
    instructions_get_rightLoopScheduler.add(consentRoutineEnd(snapshot));
    instructions_get_rightLoopScheduler.add(consent1RoutineBegin(snapshot));
    instructions_get_rightLoopScheduler.add(consent1RoutineEachFrame(snapshot));
    instructions_get_rightLoopScheduler.add(consent1RoutineEnd(snapshot));
    instructions_get_rightLoopScheduler.add(instructionsRoutineBegin(snapshot));
    instructions_get_rightLoopScheduler.add(instructionsRoutineEachFrame(snapshot));
    instructions_get_rightLoopScheduler.add(instructionsRoutineEnd(snapshot));
    instructions_get_rightLoopScheduler.add(instruction2RoutineBegin(snapshot));
    instructions_get_rightLoopScheduler.add(instruction2RoutineEachFrame(snapshot));
    instructions_get_rightLoopScheduler.add(instruction2RoutineEnd(snapshot));
    instructions_get_rightLoopScheduler.add(stage1_instructionsRoutineBegin(snapshot));
    instructions_get_rightLoopScheduler.add(stage1_instructionsRoutineEachFrame(snapshot));
    instructions_get_rightLoopScheduler.add(stage1_instructionsRoutineEnd(snapshot));
    instructions_get_rightLoopScheduler.add(stage2_4_instructionsRoutineBegin(snapshot));
    instructions_get_rightLoopScheduler.add(stage2_4_instructionsRoutineEachFrame(snapshot));
    instructions_get_rightLoopScheduler.add(stage2_4_instructionsRoutineEnd(snapshot));
    const practice_loopLoopScheduler = new Scheduler(psychoJS);
    instructions_get_rightLoopScheduler.add(practice_loopLoopBegin, practice_loopLoopScheduler);
    instructions_get_rightLoopScheduler.add(practice_loopLoopScheduler);
    instructions_get_rightLoopScheduler.add(practice_loopLoopEnd);
    instructions_get_rightLoopScheduler.add(memory_quizRoutineBegin(snapshot));
    instructions_get_rightLoopScheduler.add(memory_quizRoutineEachFrame(snapshot));
    instructions_get_rightLoopScheduler.add(memory_quizRoutineEnd(snapshot));
    instructions_get_rightLoopScheduler.add(reminder_second_phaseRoutineBegin(snapshot));
    instructions_get_rightLoopScheduler.add(reminder_second_phaseRoutineEachFrame(snapshot));
    instructions_get_rightLoopScheduler.add(reminder_second_phaseRoutineEnd(snapshot));
    instructions_get_rightLoopScheduler.add(instructions_quiz_1RoutineBegin(snapshot));
    instructions_get_rightLoopScheduler.add(instructions_quiz_1RoutineEachFrame(snapshot));
    instructions_get_rightLoopScheduler.add(instructions_quiz_1RoutineEnd(snapshot));
    instructions_get_rightLoopScheduler.add(instructions_quiz_2RoutineBegin(snapshot));
    instructions_get_rightLoopScheduler.add(instructions_quiz_2RoutineEachFrame(snapshot));
    instructions_get_rightLoopScheduler.add(instructions_quiz_2RoutineEnd(snapshot));
    instructions_get_rightLoopScheduler.add(instructions_quiz_3RoutineBegin(snapshot));
    instructions_get_rightLoopScheduler.add(instructions_quiz_3RoutineEachFrame(snapshot));
    instructions_get_rightLoopScheduler.add(instructions_quiz_3RoutineEnd(snapshot));
    instructions_get_rightLoopScheduler.add(instructions_quiz_4RoutineBegin(snapshot));
    instructions_get_rightLoopScheduler.add(instructions_quiz_4RoutineEachFrame(snapshot));
    instructions_get_rightLoopScheduler.add(instructions_quiz_4RoutineEnd(snapshot));
    instructions_get_rightLoopScheduler.add(result_quiz_instructionsRoutineBegin(snapshot));
    instructions_get_rightLoopScheduler.add(result_quiz_instructionsRoutineEachFrame(snapshot));
    instructions_get_rightLoopScheduler.add(result_quiz_instructionsRoutineEnd(snapshot));
    instructions_get_rightLoopScheduler.add(endLoopIteration(instructions_get_rightLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var practice_loop;
function practice_loopLoopBegin(practice_loopLoopScheduler) {
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
  practice_loop.forEach(function() {
    const snapshot = practice_loop.getSnapshot();

    practice_loopLoopScheduler.add(importConditions(snapshot));
    const trials_3LoopScheduler = new Scheduler(psychoJS);
    practice_loopLoopScheduler.add(trials_3LoopBegin, trials_3LoopScheduler);
    practice_loopLoopScheduler.add(trials_3LoopScheduler);
    practice_loopLoopScheduler.add(trials_3LoopEnd);
    practice_loopLoopScheduler.add(quiz_practiceRoutineBegin(snapshot));
    practice_loopLoopScheduler.add(quiz_practiceRoutineEachFrame(snapshot));
    practice_loopLoopScheduler.add(quiz_practiceRoutineEnd(snapshot));
    practice_loopLoopScheduler.add(feedback1RoutineBegin(snapshot));
    practice_loopLoopScheduler.add(feedback1RoutineEachFrame(snapshot));
    practice_loopLoopScheduler.add(feedback1RoutineEnd(snapshot));
    practice_loopLoopScheduler.add(endLoopIteration(practice_loopLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var trials_3;
function trials_3LoopBegin(trials_3LoopScheduler) {
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
  trials_3.forEach(function() {
    const snapshot = trials_3.getSnapshot();

    trials_3LoopScheduler.add(importConditions(snapshot));
    trials_3LoopScheduler.add(stage_2_4_practiceRoutineBegin(snapshot));
    trials_3LoopScheduler.add(stage_2_4_practiceRoutineEachFrame(snapshot));
    trials_3LoopScheduler.add(stage_2_4_practiceRoutineEnd(snapshot));
    trials_3LoopScheduler.add(stage_2_4_practice_resultRoutineBegin(snapshot));
    trials_3LoopScheduler.add(stage_2_4_practice_resultRoutineEachFrame(snapshot));
    trials_3LoopScheduler.add(stage_2_4_practice_resultRoutineEnd(snapshot));
    trials_3LoopScheduler.add(endLoopIteration(trials_3LoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trials_3LoopEnd() {
  psychoJS.experiment.removeLoop(trials_3);

  return Scheduler.Event.NEXT;
}


function practice_loopLoopEnd() {
  psychoJS.experiment.removeLoop(practice_loop);

  return Scheduler.Event.NEXT;
}


function instructions_get_rightLoopEnd() {
  psychoJS.experiment.removeLoop(instructions_get_right);

  return Scheduler.Event.NEXT;
}


var trials;
function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'Study3_learningtrials.csv',
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials.forEach(function() {
    const snapshot = trials.getSnapshot();

    trialsLoopScheduler.add(importConditions(snapshot));
    const action_selectionLoopScheduler = new Scheduler(psychoJS);
    trialsLoopScheduler.add(action_selectionLoopBegin, action_selectionLoopScheduler);
    trialsLoopScheduler.add(action_selectionLoopScheduler);
    trialsLoopScheduler.add(action_selectionLoopEnd);
    trialsLoopScheduler.add(learning_trial_sequenceRoutineBegin(snapshot));
    trialsLoopScheduler.add(learning_trial_sequenceRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(learning_trial_sequenceRoutineEnd(snapshot));
    trialsLoopScheduler.add(memory_qRoutineBegin(snapshot));
    trialsLoopScheduler.add(memory_qRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(memory_qRoutineEnd(snapshot));
    trialsLoopScheduler.add(prediction4RoutineBegin(snapshot));
    trialsLoopScheduler.add(prediction4RoutineEachFrame(snapshot));
    trialsLoopScheduler.add(prediction4RoutineEnd(snapshot));
    trialsLoopScheduler.add(quiz_scoreRoutineBegin(snapshot));
    trialsLoopScheduler.add(quiz_scoreRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(quiz_scoreRoutineEnd(snapshot));
    trialsLoopScheduler.add(take_a_breakRoutineBegin(snapshot));
    trialsLoopScheduler.add(take_a_breakRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(take_a_breakRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


var action_selection;
function action_selectionLoopBegin(action_selectionLoopScheduler) {
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
  action_selection.forEach(function() {
    const snapshot = action_selection.getSnapshot();

    action_selectionLoopScheduler.add(importConditions(snapshot));
    action_selectionLoopScheduler.add(stage1RoutineBegin(snapshot));
    action_selectionLoopScheduler.add(stage1RoutineEachFrame(snapshot));
    action_selectionLoopScheduler.add(stage1RoutineEnd(snapshot));
    action_selectionLoopScheduler.add(incorrect_answerRoutineBegin(snapshot));
    action_selectionLoopScheduler.add(incorrect_answerRoutineEachFrame(snapshot));
    action_selectionLoopScheduler.add(incorrect_answerRoutineEnd(snapshot));
    action_selectionLoopScheduler.add(endLoopIteration(action_selectionLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function action_selectionLoopEnd() {
  psychoJS.experiment.removeLoop(action_selection);

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var PR_vs_SR;
function PR_vs_SRLoopBegin(PR_vs_SRLoopScheduler) {
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
  PR_vs_SR.forEach(function() {
    const snapshot = PR_vs_SR.getSnapshot();

    PR_vs_SRLoopScheduler.add(importConditions(snapshot));
    PR_vs_SRLoopScheduler.add(info_choicephaseRoutineBegin(snapshot));
    PR_vs_SRLoopScheduler.add(info_choicephaseRoutineEachFrame(snapshot));
    PR_vs_SRLoopScheduler.add(info_choicephaseRoutineEnd(snapshot));
    PR_vs_SRLoopScheduler.add(stage1_choice_enactRoutineBegin(snapshot));
    PR_vs_SRLoopScheduler.add(stage1_choice_enactRoutineEachFrame(snapshot));
    PR_vs_SRLoopScheduler.add(stage1_choice_enactRoutineEnd(snapshot));
    PR_vs_SRLoopScheduler.add(final_stage5RoutineBegin(snapshot));
    PR_vs_SRLoopScheduler.add(final_stage5RoutineEachFrame(snapshot));
    PR_vs_SRLoopScheduler.add(final_stage5RoutineEnd(snapshot));
    PR_vs_SRLoopScheduler.add(endLoopIteration(PR_vs_SRLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function PR_vs_SRLoopEnd() {
  psychoJS.experiment.removeLoop(PR_vs_SR);

  return Scheduler.Event.NEXT;
}


var transition_revaluation_round;
function transition_revaluation_roundLoopBegin(transition_revaluation_roundLoopScheduler) {
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
  transition_revaluation_round.forEach(function() {
    const snapshot = transition_revaluation_round.getSnapshot();

    transition_revaluation_roundLoopScheduler.add(importConditions(snapshot));
    transition_revaluation_roundLoopScheduler.add(info_choice_revaluation_2RoutineBegin(snapshot));
    transition_revaluation_roundLoopScheduler.add(info_choice_revaluation_2RoutineEachFrame(snapshot));
    transition_revaluation_roundLoopScheduler.add(info_choice_revaluation_2RoutineEnd(snapshot));
    transition_revaluation_roundLoopScheduler.add(choice_transistion_revalRoutineBegin(snapshot));
    transition_revaluation_roundLoopScheduler.add(choice_transistion_revalRoutineEachFrame(snapshot));
    transition_revaluation_roundLoopScheduler.add(choice_transistion_revalRoutineEnd(snapshot));
    transition_revaluation_roundLoopScheduler.add(final_stage_TrRoutineBegin(snapshot));
    transition_revaluation_roundLoopScheduler.add(final_stage_TrRoutineEachFrame(snapshot));
    transition_revaluation_roundLoopScheduler.add(final_stage_TrRoutineEnd(snapshot));
    transition_revaluation_roundLoopScheduler.add(endLoopIteration(transition_revaluation_roundLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function transition_revaluation_roundLoopEnd() {
  psychoJS.experiment.removeLoop(transition_revaluation_round);

  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _consent1_next_allKeys;
var consentComponents;
function consentRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'consent'-------
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
    
    consentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function consentRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'consent'-------
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
    consentComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function consentRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'consent'-------
    consentComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('consent1_next.keys', consent1_next.keys);
    if (typeof consent1_next.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('consent1_next.rt', consent1_next.rt);
        routineTimer.reset();
        }
    
    consent1_next.stop();
    // the Routine "consent" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _consent1_next_2_allKeys;
var consent1Components;
function consent1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'consent1'-------
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
    
    consent1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function consent1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'consent1'-------
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
    consent1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function consent1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'consent1'-------
    consent1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('consent1_next_2.keys', consent1_next_2.keys);
    if (typeof consent1_next_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('consent1_next_2.rt', consent1_next_2.rt);
        routineTimer.reset();
        }
    
    consent1_next_2.stop();
    if ((consent1_next_2.keys === "n")) {
        psychoJS.quit();
    }
    
    // the Routine "consent1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var instructionsComponents;
function instructionsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instructions'-------
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
    
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructionsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instructions'-------
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
    instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructionsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instructions'-------
    instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var instruction2Components;
function instruction2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instruction2'-------
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
    
    instruction2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instruction2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instruction2'-------
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
    instruction2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instruction2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instruction2'-------
    instruction2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "instruction2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _keyboard_entry_instr1_allKeys;
var stage1_instructionsComponents;
function stage1_instructionsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'stage1_instructions'-------
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
    
    stage1_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function stage1_instructionsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'stage1_instructions'-------
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
    stage1_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stage1_instructionsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'stage1_instructions'-------
    stage1_instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "stage1_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _responseleft_allKeys;
var stage2_4_instructionsComponents;
function stage2_4_instructionsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'stage2_4_instructions'-------
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
    
    stage2_4_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function stage2_4_instructionsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'stage2_4_instructions'-------
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
    stage2_4_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stage2_4_instructionsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'stage2_4_instructions'-------
    stage2_4_instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "stage2_4_instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_10_allKeys;
var stage_2_4_practiceComponents;
function stage_2_4_practiceRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'stage_2_4_practice'-------
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
    
    stage_2_4_practiceComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function stage_2_4_practiceRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'stage_2_4_practice'-------
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
    stage_2_4_practiceComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stage_2_4_practiceRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'stage_2_4_practice'-------
    stage_2_4_practiceComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_10.keys', key_resp_10.keys);
    if (typeof key_resp_10.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_10.rt', key_resp_10.rt);
        routineTimer.reset();
        }
    
    key_resp_10.stop();
    // the Routine "stage_2_4_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var stage_2_4_practice_resultComponents;
function stage_2_4_practice_resultRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'stage_2_4_practice_result'-------
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
    
    stage_2_4_practice_resultComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function stage_2_4_practice_resultRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'stage_2_4_practice_result'-------
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
    stage_2_4_practice_resultComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stage_2_4_practice_resultRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'stage_2_4_practice_result'-------
    stage_2_4_practice_resultComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _practice_answer_allKeys;
var quiz_practiceComponents;
function quiz_practiceRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'quiz_practice'-------
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
    
    quiz_practiceComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function quiz_practiceRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'quiz_practice'-------
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
    quiz_practiceComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function quiz_practiceRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'quiz_practice'-------
    quiz_practiceComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (practice_answer.keys === undefined) {
      if (['None','none',undefined].includes('a')) {
         practice_answer.corr = 1;  // correct non-response
      } else {
         practice_answer.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('practice_answer.keys', practice_answer.keys);
    psychoJS.experiment.addData('practice_answer.corr', practice_answer.corr);
    if (typeof practice_answer.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('practice_answer.rt', practice_answer.rt);
        routineTimer.reset();
        }
    
    practice_answer.stop();
    if (practice_answer.corr) {
        console.log("correct answer");
        practice_loop.finished = true;
    }
    
    // the Routine "quiz_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var msg;
var feedback1Components;
function feedback1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'feedback1'-------
    t = 0;
    feedback1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    if (practice_answer.corr) {
        msg = "Correct!";
    } else {
        msg = "Wrong! Re-starting practice";
    }
    
    text_10.setText(msg);
    // keep track of which components have finished
    feedback1Components = [];
    feedback1Components.push(text_10);
    
    feedback1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function feedback1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'feedback1'-------
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
    feedback1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedback1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'feedback1'-------
    feedback1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_23_allKeys;
var memory_quizComponents;
function memory_quizRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'memory_quiz'-------
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
    
    memory_quizComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function memory_quizRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'memory_quiz'-------
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
    memory_quizComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function memory_quizRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'memory_quiz'-------
    memory_quizComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_23.keys', key_resp_23.keys);
    if (typeof key_resp_23.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_23.rt', key_resp_23.rt);
        routineTimer.reset();
        }
    
    key_resp_23.stop();
    // the Routine "memory_quiz" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_22_allKeys;
var reminder_second_phaseComponents;
function reminder_second_phaseRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'reminder_second_phase'-------
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
    
    reminder_second_phaseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function reminder_second_phaseRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'reminder_second_phase'-------
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
    reminder_second_phaseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reminder_second_phaseRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'reminder_second_phase'-------
    reminder_second_phaseComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_22.keys', key_resp_22.keys);
    if (typeof key_resp_22.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_22.rt', key_resp_22.rt);
        routineTimer.reset();
        }
    
    key_resp_22.stop();
    // the Routine "reminder_second_phase" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_17_allKeys;
var instructions_quiz_1Components;
function instructions_quiz_1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instructions_quiz_1'-------
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
    
    instructions_quiz_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructions_quiz_1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instructions_quiz_1'-------
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
    instructions_quiz_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
  return function () {
    //------Ending Routine 'instructions_quiz_1'-------
    instructions_quiz_1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    correct = 0;
    if ((key_resp_17.keys === "c")) {
        correct += 1;
    }
    
    psychoJS.experiment.addData('key_resp_17.keys', key_resp_17.keys);
    if (typeof key_resp_17.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_17.rt', key_resp_17.rt);
        routineTimer.reset();
        }
    
    key_resp_17.stop();
    // the Routine "instructions_quiz_1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_18_allKeys;
var instructions_quiz_2Components;
function instructions_quiz_2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instructions_quiz_2'-------
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
    
    instructions_quiz_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructions_quiz_2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instructions_quiz_2'-------
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
    instructions_quiz_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions_quiz_2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instructions_quiz_2'-------
    instructions_quiz_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    if ((key_resp_18.keys === "c")) {
        correct += 1;
    }
    
    psychoJS.experiment.addData('key_resp_18.keys', key_resp_18.keys);
    if (typeof key_resp_18.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_18.rt', key_resp_18.rt);
        routineTimer.reset();
        }
    
    key_resp_18.stop();
    // the Routine "instructions_quiz_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_19_allKeys;
var instructions_quiz_3Components;
function instructions_quiz_3RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instructions_quiz_3'-------
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
    
    instructions_quiz_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructions_quiz_3RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instructions_quiz_3'-------
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
    instructions_quiz_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions_quiz_3RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instructions_quiz_3'-------
    instructions_quiz_3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    if ((key_resp_19.keys === "b")) {
        correct += 1;
    }
    
    psychoJS.experiment.addData('key_resp_19.keys', key_resp_19.keys);
    if (typeof key_resp_19.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_19.rt', key_resp_19.rt);
        routineTimer.reset();
        }
    
    key_resp_19.stop();
    // the Routine "instructions_quiz_3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_20_allKeys;
var instructions_quiz_4Components;
function instructions_quiz_4RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instructions_quiz_4'-------
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
    
    instructions_quiz_4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructions_quiz_4RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instructions_quiz_4'-------
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
    instructions_quiz_4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions_quiz_4RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instructions_quiz_4'-------
    instructions_quiz_4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    if ((key_resp_20.keys === "b")) {
        correct += 1;
    }
    if ((correct === 4)) {
        instructions_get_right.finished = true;
        msg = "Correct! You can now move on";
    } else {
        msg = "Incorrect! You need to repeat the instructions.";
    }
    
    psychoJS.experiment.addData('key_resp_20.keys', key_resp_20.keys);
    if (typeof key_resp_20.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_20.rt', key_resp_20.rt);
        routineTimer.reset();
        }
    
    key_resp_20.stop();
    // the Routine "instructions_quiz_4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var result_quiz_instructionsComponents;
function result_quiz_instructionsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'result_quiz_instructions'-------
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
    
    result_quiz_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function result_quiz_instructionsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'result_quiz_instructions'-------
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
    result_quiz_instructionsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function result_quiz_instructionsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'result_quiz_instructions'-------
    result_quiz_instructionsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_4_allKeys;
var time_limitComponents;
function time_limitRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'time_limit'-------
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
    
    time_limitComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function time_limitRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'time_limit'-------
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
    time_limitComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function time_limitRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'time_limit'-------
    time_limitComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        routineTimer.reset();
        }
    
    key_resp_4.stop();
    // the Routine "time_limit" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_7_allKeys;
var instructions3Components;
function instructions3RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instructions3'-------
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
    
    instructions3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructions3RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instructions3'-------
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
    instructions3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions3RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instructions3'-------
    instructions3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "instructions3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var im1_memory;
var im2_memory;
var _click_action_allKeys;
var stage1Components;
function stage1RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'stage1'-------
    t = 0;
    stage1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(7.000000);
    // update component parameters for each repeat
    if ((((trial_learning_num + 1) % 28) === 0)) {
        learning_reward_goal = learning_reward_goal_list[counter_reward_learning];
        im1_memory = learning_reward_startingstate_list[counter_reward_learning][0];
        im2_memory = learning_reward_startingstate_list[counter_reward_learning][1];
        counter_reward_learning += 1;
    }
    
    click_action.keys = undefined;
    click_action.rt = undefined;
    _click_action_allKeys = [];
    picture_image.setImage(s1_image);
    text_3.setText(action1);
    // keep track of which components have finished
    stage1Components = [];
    stage1Components.push(click_action);
    stage1Components.push(text_9);
    stage1Components.push(picture_image);
    stage1Components.push(text_3);
    
    stage1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function stage1RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'stage1'-------
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
    
    // *picture_image* updates
    if (t >= 0.0 && picture_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      picture_image.tStart = t;  // (not accounting for frame time here)
      picture_image.frameNStart = frameN;  // exact frame index
      
      picture_image.setAutoDraw(true);
    }

    frameRemains = 0.0 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (picture_image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      picture_image.setAutoDraw(false);
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
    stage1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stage1RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'stage1'-------
    stage1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (click_action.keys === undefined) {
      if (['None','none',undefined].includes(action1)) {
         click_action.corr = 1;  // correct non-response
      } else {
         click_action.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('click_action.keys', click_action.keys);
    psychoJS.experiment.addData('click_action.corr', click_action.corr);
    if (typeof click_action.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('click_action.rt', click_action.rt);
        routineTimer.reset();
        }
    
    click_action.stop();
    return Scheduler.Event.NEXT;
  };
}


var msg_incorrect;
var incorrect_answerComponents;
function incorrect_answerRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'incorrect_answer'-------
    t = 0;
    incorrect_answerClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
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
    
    incorrect_answerComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function incorrect_answerRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'incorrect_answer'-------
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
    incorrect_answerComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function incorrect_answerRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'incorrect_answer'-------
    incorrect_answerComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var learning_trial_sequenceComponents;
function learning_trial_sequenceRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'learning_trial_sequence'-------
    t = 0;
    learning_trial_sequenceClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(7.600000);
    // update component parameters for each repeat
    stage1_learning.setImage(s1_image);
    stage2_learning.setImage(s2_image);
    stage3_learning.setImage(s3_image);
    if ((incorrect_actions > 4)) {
        trials.finished = true;
        continueRoutine = false;
    }
    
    // keep track of which components have finished
    learning_trial_sequenceComponents = [];
    learning_trial_sequenceComponents.push(stage1_learning);
    learning_trial_sequenceComponents.push(text_78);
    learning_trial_sequenceComponents.push(stage2_learning);
    learning_trial_sequenceComponents.push(text_80);
    learning_trial_sequenceComponents.push(stage3_learning);
    
    learning_trial_sequenceComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function learning_trial_sequenceRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'learning_trial_sequence'-------
    // get current time
    t = learning_trial_sequenceClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *stage1_learning* updates
    if (t >= 0.0 && stage1_learning.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stage1_learning.tStart = t;  // (not accounting for frame time here)
      stage1_learning.frameNStart = frameN;  // exact frame index
      
      stage1_learning.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (stage1_learning.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      stage1_learning.setAutoDraw(false);
    }
    
    // *text_78* updates
    if (t >= 2.1 && text_78.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_78.tStart = t;  // (not accounting for frame time here)
      text_78.frameNStart = frameN;  // exact frame index
      
      text_78.setAutoDraw(true);
    }

    frameRemains = 2.1 + 0.6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_78.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_78.setAutoDraw(false);
    }
    
    // *stage2_learning* updates
    if (t >= 2.8 && stage2_learning.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stage2_learning.tStart = t;  // (not accounting for frame time here)
      stage2_learning.frameNStart = frameN;  // exact frame index
      
      stage2_learning.setAutoDraw(true);
    }

    frameRemains = 2.8 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (stage2_learning.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      stage2_learning.setAutoDraw(false);
    }
    
    // *text_80* updates
    if (t >= 4.9 && text_80.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_80.tStart = t;  // (not accounting for frame time here)
      text_80.frameNStart = frameN;  // exact frame index
      
      text_80.setAutoDraw(true);
    }

    frameRemains = 4.9 + 0.6 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_80.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_80.setAutoDraw(false);
    }
    
    // *stage3_learning* updates
    if (t >= 5.6 && stage3_learning.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      stage3_learning.tStart = t;  // (not accounting for frame time here)
      stage3_learning.frameNStart = frameN;  // exact frame index
      
      stage3_learning.setAutoDraw(true);
    }

    frameRemains = 5.6 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (stage3_learning.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      stage3_learning.setAutoDraw(false);
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
    learning_trial_sequenceComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function learning_trial_sequenceRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'learning_trial_sequence'-------
    learning_trial_sequenceComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var number_correct;
var memory_qComponents;
function memory_qRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'memory_q'-------
    t = 0;
    memory_qClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.500000);
    // update component parameters for each repeat
    if (((trial_learning_num % 28) === 0)) {
        continueRoutine = true;
    } else {
        continueRoutine = false;
    }
    number_correct = 0;
    
    // keep track of which components have finished
    memory_qComponents = [];
    memory_qComponents.push(text_92);
    
    memory_qComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function memory_qRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'memory_q'-------
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
    memory_qComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function memory_qRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'memory_q'-------
    memory_qComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _resp4_allKeys;
var prediction4Components;
function prediction4RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'prediction4'-------
    t = 0;
    prediction4Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
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
    memory_image1.setImage(im1_memory);
    memory_image2.setImage(im2_memory);
    // keep track of which components have finished
    prediction4Components = [];
    prediction4Components.push(outcome4);
    prediction4Components.push(picture_reward_goal);
    prediction4Components.push(resp4);
    prediction4Components.push(memory_image1);
    prediction4Components.push(memory_image2);
    prediction4Components.push(text_79);
    prediction4Components.push(text_85);
    
    prediction4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function prediction4RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'prediction4'-------
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
    
    
    // *memory_image1* updates
    if (t >= 0.0 && memory_image1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      memory_image1.tStart = t;  // (not accounting for frame time here)
      memory_image1.frameNStart = frameN;  // exact frame index
      
      memory_image1.setAutoDraw(true);
    }

    
    // *memory_image2* updates
    if (t >= 0.0 && memory_image2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      memory_image2.tStart = t;  // (not accounting for frame time here)
      memory_image2.frameNStart = frameN;  // exact frame index
      
      memory_image2.setAutoDraw(true);
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
    prediction4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prediction4RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'prediction4'-------
    prediction4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('resp4.keys', resp4.keys);
    if (typeof resp4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('resp4.rt', resp4.rt);
        routineTimer.reset();
        }
    
    resp4.stop();
    // the Routine "prediction4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var quiz_scoreComponents;
function quiz_scoreRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'quiz_score'-------
    t = 0;
    quiz_scoreClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
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
    
    quiz_scoreComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function quiz_scoreRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'quiz_score'-------
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
    quiz_scoreComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function quiz_scoreRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'quiz_score'-------
    quiz_scoreComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var take_a_breakComponents;
function take_a_breakRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'take_a_break'-------
    t = 0;
    take_a_breakClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(0.600000);
    // update component parameters for each repeat
    // keep track of which components have finished
    take_a_breakComponents = [];
    take_a_breakComponents.push(text_39);
    
    take_a_breakComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function take_a_breakRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'take_a_break'-------
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
    take_a_breakComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function take_a_breakRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'take_a_break'-------
    take_a_breakComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_11_allKeys;
var instructions_reward_stageComponents;
function instructions_reward_stageRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instructions_reward_stage'-------
    t = 0;
    instructions_reward_stageClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
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
    
    instructions_reward_stageComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructions_reward_stageRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instructions_reward_stage'-------
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
    instructions_reward_stageComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions_reward_stageRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instructions_reward_stage'-------
    instructions_reward_stageComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "instructions_reward_stage" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_9_allKeys;
var i2_rewardComponents;
function i2_rewardRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'i2_reward'-------
    t = 0;
    i2_rewardClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
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
    
    i2_rewardComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function i2_rewardRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'i2_reward'-------
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
    i2_rewardComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function i2_rewardRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'i2_reward'-------
    i2_rewardComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "i2_reward" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _resp4_2_allKeys;
var _key_resp_3_allKeys;
var practice_view_reward_infoComponents;
function practice_view_reward_infoRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'practice_view_reward_info'-------
    t = 0;
    practice_view_reward_infoClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
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
    practice_view_reward_infoComponents.push(text_28);
    practice_view_reward_infoComponents.push(key_resp_3);
    practice_view_reward_infoComponents.push(image_19);
    
    practice_view_reward_infoComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function practice_view_reward_infoRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'practice_view_reward_info'-------
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
    
    
    // *image_19* updates
    if (t >= 0.0 && image_19.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_19.tStart = t;  // (not accounting for frame time here)
      image_19.frameNStart = frameN;  // exact frame index
      
      image_19.setAutoDraw(true);
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
    practice_view_reward_infoComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function practice_view_reward_infoRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'practice_view_reward_info'-------
    practice_view_reward_infoComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        routineTimer.reset();
        }
    
    key_resp_3.stop();
    // the Routine "practice_view_reward_info" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_12_allKeys;
var instructions_planningComponents;
function instructions_planningRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instructions_planning'-------
    t = 0;
    instructions_planningClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    if ((incorrect_actions > 4)) {
        continueRoutine = false;
    }
    
    key_resp_12.keys = undefined;
    key_resp_12.rt = undefined;
    _key_resp_12_allKeys = [];
    // keep track of which components have finished
    instructions_planningComponents = [];
    instructions_planningComponents.push(text_66);
    instructions_planningComponents.push(houses_choice_practice);
    instructions_planningComponents.push(train_choice_practice);
    instructions_planningComponents.push(key_resp_12);
    instructions_planningComponents.push(text_24);
    
    instructions_planningComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructions_planningRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instructions_planning'-------
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

    
    // *houses_choice_practice* updates
    if (t >= 0.0 && houses_choice_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      houses_choice_practice.tStart = t;  // (not accounting for frame time here)
      houses_choice_practice.frameNStart = frameN;  // exact frame index
      
      houses_choice_practice.setAutoDraw(true);
    }

    
    // *train_choice_practice* updates
    if (t >= 0.0 && train_choice_practice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      train_choice_practice.tStart = t;  // (not accounting for frame time here)
      train_choice_practice.frameNStart = frameN;  // exact frame index
      
      train_choice_practice.setAutoDraw(true);
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
    instructions_planningComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructions_planningRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instructions_planning'-------
    instructions_planningComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_12.keys', key_resp_12.keys);
    if (typeof key_resp_12.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_12.rt', key_resp_12.rt);
        routineTimer.reset();
        }
    
    key_resp_12.stop();
    // the Routine "instructions_planning" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_15_allKeys;
var start_planning_trialsComponents;
function start_planning_trialsRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'start_planning_trials'-------
    t = 0;
    start_planning_trialsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
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
    
    start_planning_trialsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function start_planning_trialsRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'start_planning_trials'-------
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
    start_planning_trialsComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function start_planning_trialsRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'start_planning_trials'-------
    start_planning_trialsComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_15.keys', key_resp_15.keys);
    if (typeof key_resp_15.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_15.rt', key_resp_15.rt);
        routineTimer.reset();
        }
    
    key_resp_15.stop();
    // the Routine "start_planning_trials" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_24_allKeys;
var info_choicephaseComponents;
function info_choicephaseRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'info_choicephase'-------
    t = 0;
    info_choicephaseClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
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
    goal_image.setImage(r3);
    im3_num_planning.setText(r3_num);
    // keep track of which components have finished
    info_choicephaseComponents = [];
    info_choicephaseComponents.push(im1_planning);
    info_choicephaseComponents.push(im2_planning);
    info_choicephaseComponents.push(example_trial_choice_phase_2);
    info_choicephaseComponents.push(im1_rewvalue_planning);
    info_choicephaseComponents.push(im2_rewvalue_planning);
    info_choicephaseComponents.push(text_29);
    info_choicephaseComponents.push(key_resp_24);
    info_choicephaseComponents.push(goal_image);
    info_choicephaseComponents.push(im3_num_planning);
    
    info_choicephaseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function info_choicephaseRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'info_choicephase'-------
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
    
    
    // *goal_image* updates
    if (t >= 0.0 && goal_image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      goal_image.tStart = t;  // (not accounting for frame time here)
      goal_image.frameNStart = frameN;  // exact frame index
      
      goal_image.setAutoDraw(true);
    }

    
    // *im3_num_planning* updates
    if (t >= 0.0 && im3_num_planning.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      im3_num_planning.tStart = t;  // (not accounting for frame time here)
      im3_num_planning.frameNStart = frameN;  // exact frame index
      
      im3_num_planning.setAutoDraw(true);
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
    info_choicephaseComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function info_choicephaseRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'info_choicephase'-------
    info_choicephaseComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_24.keys', key_resp_24.keys);
    if (typeof key_resp_24.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_24.rt', key_resp_24.rt);
        routineTimer.reset();
        }
    
    key_resp_24.stop();
    // the Routine "info_choicephase" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_25_allKeys;
var stage1_choice_enactComponents;
function stage1_choice_enactRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'stage1_choice_enact'-------
    t = 0;
    stage1_choice_enactClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    if ((incorrect_actions > 4)) {
        PR_vs_SR.finished = true;
        continueRoutine = false;
    }
    
    image1test.setImage(r1);
    image2test.setImage(r2);
    key_resp_25.keys = undefined;
    key_resp_25.rt = undefined;
    _key_resp_25_allKeys = [];
    // keep track of which components have finished
    stage1_choice_enactComponents = [];
    stage1_choice_enactComponents.push(text_81);
    stage1_choice_enactComponents.push(image1test);
    stage1_choice_enactComponents.push(image2test);
    stage1_choice_enactComponents.push(key_resp_25);
    stage1_choice_enactComponents.push(text_31);
    stage1_choice_enactComponents.push(text_82);
    
    stage1_choice_enactComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function stage1_choice_enactRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'stage1_choice_enact'-------
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

    
    // *image1test* updates
    if (t >= 0.0 && image1test.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image1test.tStart = t;  // (not accounting for frame time here)
      image1test.frameNStart = frameN;  // exact frame index
      
      image1test.setAutoDraw(true);
    }

    
    // *image2test* updates
    if (t >= 0.0 && image2test.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image2test.tStart = t;  // (not accounting for frame time here)
      image2test.frameNStart = frameN;  // exact frame index
      
      image2test.setAutoDraw(true);
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
      let theseKeys = key_resp_25.getKeys({keyList: ['1', '9'], waitRelease: false});
      _key_resp_25_allKeys = _key_resp_25_allKeys.concat(theseKeys);
      if (_key_resp_25_allKeys.length > 0) {
        key_resp_25.keys = _key_resp_25_allKeys[_key_resp_25_allKeys.length - 1].name;  // just the last key pressed
        key_resp_25.rt = _key_resp_25_allKeys[_key_resp_25_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_31* updates
    if (t >= 0.0 && text_31.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_31.tStart = t;  // (not accounting for frame time here)
      text_31.frameNStart = frameN;  // exact frame index
      
      text_31.setAutoDraw(true);
    }

    
    // *text_82* updates
    if (t >= 0.0 && text_82.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_82.tStart = t;  // (not accounting for frame time here)
      text_82.frameNStart = frameN;  // exact frame index
      
      text_82.setAutoDraw(true);
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
    stage1_choice_enactComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stage1_choice_enactRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'stage1_choice_enact'-------
    stage1_choice_enactComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_25.keys', key_resp_25.keys);
    if (typeof key_resp_25.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_25.rt', key_resp_25.rt);
        routineTimer.reset();
        }
    
    key_resp_25.stop();
    // the Routine "stage1_choice_enact" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_16_allKeys;
var final_stage5Components;
function final_stage5RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'final_stage5'-------
    t = 0;
    final_stage5Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
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
    
    final_stage5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function final_stage5RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'final_stage5'-------
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
    final_stage5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function final_stage5RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'final_stage5'-------
    final_stage5Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "final_stage5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_8_allKeys;
var transition_revaluationComponents;
function transition_revaluationRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'transition_revaluation'-------
    t = 0;
    transition_revaluationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
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
    transition_revaluationComponents.push(tree_reval);
    transition_revaluationComponents.push(trident_reval);
    transition_revaluationComponents.push(right_arrow);
    transition_revaluationComponents.push(fox_reval);
    transition_revaluationComponents.push(right_arrow2);
    transition_revaluationComponents.push(planet_reval);
    transition_revaluationComponents.push(text_94);
    
    transition_revaluationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function transition_revaluationRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'transition_revaluation'-------
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
    
    
    // *tree_reval* updates
    if (t >= 0.0 && tree_reval.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tree_reval.tStart = t;  // (not accounting for frame time here)
      tree_reval.frameNStart = frameN;  // exact frame index
      
      tree_reval.setAutoDraw(true);
    }

    
    // *trident_reval* updates
    if (t >= 0.0 && trident_reval.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trident_reval.tStart = t;  // (not accounting for frame time here)
      trident_reval.frameNStart = frameN;  // exact frame index
      
      trident_reval.setAutoDraw(true);
    }

    
    // *right_arrow* updates
    if (t >= 0.0 && right_arrow.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      right_arrow.tStart = t;  // (not accounting for frame time here)
      right_arrow.frameNStart = frameN;  // exact frame index
      
      right_arrow.setAutoDraw(true);
    }

    
    // *fox_reval* updates
    if (t >= 0.0 && fox_reval.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fox_reval.tStart = t;  // (not accounting for frame time here)
      fox_reval.frameNStart = frameN;  // exact frame index
      
      fox_reval.setAutoDraw(true);
    }

    
    // *right_arrow2* updates
    if (t >= 0.0 && right_arrow2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      right_arrow2.tStart = t;  // (not accounting for frame time here)
      right_arrow2.frameNStart = frameN;  // exact frame index
      
      right_arrow2.setAutoDraw(true);
    }

    
    // *planet_reval* updates
    if (t >= 0.0 && planet_reval.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      planet_reval.tStart = t;  // (not accounting for frame time here)
      planet_reval.frameNStart = frameN;  // exact frame index
      
      planet_reval.setAutoDraw(true);
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
    transition_revaluationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function transition_revaluationRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'transition_revaluation'-------
    transition_revaluationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_8.keys', key_resp_8.keys);
    if (typeof key_resp_8.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_8.rt', key_resp_8.rt);
        routineTimer.reset();
        }
    
    key_resp_8.stop();
    // the Routine "transition_revaluation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_29_allKeys;
var info_choice_revaluation_2Components;
function info_choice_revaluation_2RoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'info_choice_revaluation_2'-------
    t = 0;
    info_choice_revaluation_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    if ((incorrect_actions > 4)) {
        transition_revaluation_round.finished = true;
        continueRoutine = false;
    }
    
    im1_planning_2.setImage(r1);
    im2_planning_2.setImage(r2);
    im1_rewvalue_planning_2.setText(r3_num);
    key_resp_29.keys = undefined;
    key_resp_29.rt = undefined;
    _key_resp_29_allKeys = [];
    goal_transition_reval.setImage(r3);
    // keep track of which components have finished
    info_choice_revaluation_2Components = [];
    info_choice_revaluation_2Components.push(im1_planning_2);
    info_choice_revaluation_2Components.push(im2_planning_2);
    info_choice_revaluation_2Components.push(example_trial_choice_phase_4);
    info_choice_revaluation_2Components.push(im1_rewvalue_planning_2);
    info_choice_revaluation_2Components.push(text_93);
    info_choice_revaluation_2Components.push(key_resp_29);
    info_choice_revaluation_2Components.push(goal_transition_reval);
    
    info_choice_revaluation_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function info_choice_revaluation_2RoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'info_choice_revaluation_2'-------
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
    
    
    // *goal_transition_reval* updates
    if (t >= 0.0 && goal_transition_reval.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      goal_transition_reval.tStart = t;  // (not accounting for frame time here)
      goal_transition_reval.frameNStart = frameN;  // exact frame index
      
      goal_transition_reval.setAutoDraw(true);
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
    info_choice_revaluation_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function info_choice_revaluation_2RoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'info_choice_revaluation_2'-------
    info_choice_revaluation_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('key_resp_29.keys', key_resp_29.keys);
    if (typeof key_resp_29.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_29.rt', key_resp_29.rt);
        routineTimer.reset();
        }
    
    key_resp_29.stop();
    // the Routine "info_choice_revaluation_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _transition_reval_choice_allKeys;
var choice_transistion_revalComponents;
function choice_transistion_revalRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'choice_transistion_reval'-------
    t = 0;
    choice_transistion_revalClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    if ((incorrect_actions > 4)) {
        transition_revaluation_round.finished = true;
        continueRoutine = false;
    }
    
    trident_choice_3.setImage(r1);
    planet_choice_3.setImage(r2);
    transition_reval_choice.keys = undefined;
    transition_reval_choice.rt = undefined;
    _transition_reval_choice_allKeys = [];
    // keep track of which components have finished
    choice_transistion_revalComponents = [];
    choice_transistion_revalComponents.push(text_105);
    choice_transistion_revalComponents.push(trident_choice_3);
    choice_transistion_revalComponents.push(planet_choice_3);
    choice_transistion_revalComponents.push(transition_reval_choice);
    choice_transistion_revalComponents.push(text_106);
    choice_transistion_revalComponents.push(text_107);
    
    choice_transistion_revalComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function choice_transistion_revalRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'choice_transistion_reval'-------
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

    
    // *trident_choice_3* updates
    if (t >= 0.0 && trident_choice_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trident_choice_3.tStart = t;  // (not accounting for frame time here)
      trident_choice_3.frameNStart = frameN;  // exact frame index
      
      trident_choice_3.setAutoDraw(true);
    }

    
    // *planet_choice_3* updates
    if (t >= 0.0 && planet_choice_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      planet_choice_3.tStart = t;  // (not accounting for frame time here)
      planet_choice_3.frameNStart = frameN;  // exact frame index
      
      planet_choice_3.setAutoDraw(true);
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
      let theseKeys = transition_reval_choice.getKeys({keyList: ['1', '9'], waitRelease: false});
      _transition_reval_choice_allKeys = _transition_reval_choice_allKeys.concat(theseKeys);
      if (_transition_reval_choice_allKeys.length > 0) {
        transition_reval_choice.keys = _transition_reval_choice_allKeys[_transition_reval_choice_allKeys.length - 1].name;  // just the last key pressed
        transition_reval_choice.rt = _transition_reval_choice_allKeys[_transition_reval_choice_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *text_106* updates
    if (t >= 0.0 && text_106.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_106.tStart = t;  // (not accounting for frame time here)
      text_106.frameNStart = frameN;  // exact frame index
      
      text_106.setAutoDraw(true);
    }

    
    // *text_107* updates
    if (t >= 0.0 && text_107.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_107.tStart = t;  // (not accounting for frame time here)
      text_107.frameNStart = frameN;  // exact frame index
      
      text_107.setAutoDraw(true);
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
    choice_transistion_revalComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function choice_transistion_revalRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'choice_transistion_reval'-------
    choice_transistion_revalComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('transition_reval_choice.keys', transition_reval_choice.keys);
    if (typeof transition_reval_choice.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('transition_reval_choice.rt', transition_reval_choice.rt);
        routineTimer.reset();
        }
    
    transition_reval_choice.stop();
    // the Routine "choice_transistion_reval" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_34_allKeys;
var final_stage_TrComponents;
function final_stage_TrRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'final_stage_Tr'-------
    t = 0;
    final_stage_TrClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
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
    
    final_stage_TrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function final_stage_TrRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'final_stage_Tr'-------
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
    final_stage_TrComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function final_stage_TrRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'final_stage_Tr'-------
    final_stage_TrComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "final_stage_Tr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var reward_totalComponents;
function reward_totalRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'reward_total'-------
    t = 0;
    reward_totalClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.500000);
    // update component parameters for each repeat
    if ((incorrect_actions > 4)) {
        continueRoutine = false;
    }
    
    // keep track of which components have finished
    reward_totalComponents = [];
    reward_totalComponents.push(text_84);
    
    reward_totalComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function reward_totalRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'reward_total'-------
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
    reward_totalComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function reward_totalRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'reward_total'-------
    reward_totalComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var doneComponents;
function doneRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'done'-------
    t = 0;
    doneClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(6.000000);
    // update component parameters for each repeat
    if ((incorrect_actions > 4)) {
        continueRoutine = false;
    }
    
    // keep track of which components have finished
    doneComponents = [];
    doneComponents.push(text_62);
    
    doneComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function doneRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'done'-------
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
    doneComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function doneRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'done'-------
    doneComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
