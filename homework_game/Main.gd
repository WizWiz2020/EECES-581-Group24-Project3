extends Control

var funds := 0.0
var reputation := 0
var income_per_second := 0.0

var answer_value := 0.0
var a := 0
var b := 0

@onready var funds_label = $MainPanel/StatsPanel/FundsLabel
@onready var income_label = $MainPanel/StatsPanel/IncomeLabel
@onready var reputation_label = $MainPanel/StatsPanel/ReputationLabel

@onready var question_label = $MainPanel/HomeworkPanel/QuestionLabel
@onready var answer_input: LineEdit  = $MainPanel/HomeworkPanel/AnswerInput
@onready var submit_button = $MainPanel/HomeworkPanel/SubmitButton
@onready var message_label = $MainPanel/HomeworkPanel/MessageLabel


func _ready():
	generate_question()
	update_ui()
	
	submit_button.pressed.connect(submit_answer)


func generate_question():
	a = randi_range(1, 10)
	b = randi_range(1, 10)


func submit_answer():
	if not answer_input.text.is_valid_int():
		message_label.text = "Enter a number."
		return
	
	if int(answer_input.text) == a + b:
		funds += answer_value
		reputation += 1
		message_label.text = "Correct! +$%d and +1 reputation." % answer_value
	else:
		reputation = max(0, reputation - 1)
		message_label.text = "Incorrect. -1 reputation."
	
	answer_input.clear()
	generate_question()
	update_ui()


func update_ui():
	funds_label.text = "Funds: $%0.0f" % funds
	income_label.text = "Income/sec: $%0.0f" % income_per_second
	reputation_label.text = "Reputation: %d" % reputation
	
	question_label.text = "What is %d + %d?" % [a, b]
