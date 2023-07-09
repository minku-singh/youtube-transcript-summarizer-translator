

from googletrans import Translator

translater = Translator()
hindi_summary = translater.translate("आप कैसे हो", dest="en")

marathi_summary = translater.translate("Hello, I am fine", dest="mr")


print(hindi_summary.text, marathi_summary.text)