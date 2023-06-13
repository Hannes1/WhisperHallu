from transcribeHallu import transcribePrompt

##### Need to be adapted for each language ####
lng="en"
prompt= "Whisper, Ok. "\
	+"A pertinent sentence for your purpose in your language. "\
	+"Ok, Whisper. Whisper, Ok. "\
	+"Ok, Whisper. Whisper, Ok. "\
	+"Please find here, an unlikely ordinary sentence. "\
	+"This is to avoid a repetition to be deleted. "\
	+"Ok, Whisper. "
path="data/test.mp3"

#Example 
#lng="uk"
#prompt= "Whisper, Ok. "\
#	+"Доречне речення вашою мовою для вашої мети. "\
#	+"Ok, Whisper. Whisper, Ok. "\
#	+"Ok, Whisper. Whisper, Ok. "\
#	+"Будь ласка, знайдіть тут навряд чи звичайне речення. "\
#	+"Це зроблено для того, щоб уникнути повторення, яке потрібно видалити. "\
#	+"Ok, Whisper. "
#path="/path/to/your/uk/sound/file"
result = transcribePrompt(path=path, lng=lng, prompt=prompt)