#ik heb gewoon positieve waarden gebruikt
PositiveWordsDutch = [
	"comfortabel", "duurzaam", "elegant", "energiek", "flexibel", "fris", "gewild", "innovatief", "kwalitatief", "lichtgewicht", "modieus", "prestatiegericht", "stijlvol", "trendy", "uniek", "veelzijdig", "verfijnd", "vernieuwend", "vlekbestendig", "waterdicht", "ademend", "aanpasbaar", "dynamisch", "exceptioneel", "fantastisch", "fluweelzacht", "futuristisch", "goed passend", "heerlijk", "hip", "hoogwaardig", "ideaal", "indrukwekkend", "inspirerend", "krachtig", "luxe", "modern", "onderscheidend", "opmerkelijk", "origineel", "robuust", "sensationeel", "sportief", "subliem", "superefficiënt", "superieur", "topkwaliteit", "ultralicht", "uniek design", "veelbelovend", "vederlicht", "verbluffend", "verfijnd design", "vlekwerend", "vloeiend", "volledig op maat gemaakt", "warm", "weelderig", "wendbaar", "zeer comfortabel", "zorgvuldig gemaakt"
]
NegativeWordsDutch = [
	"oncomfortabel",
"slijtage-gevoelig",
"lomp",
"slap",
"stinkend",
"gewoontjes",
"verouderd",
"onpraktisch",
"zwaar",
"ouderwets",
"inefficiënt",
"lelijk",
"onprettig",
"niet-ademend",
"onhandig",
"ongemakkelijk",
"versleten",
"onveilig",
"saai",
"niet-duurzaam",
"onbetrouwbaar",
"mislukt design",
"onstabiel",
"niet-modieus",
"te strak",
"niet-functioneel",
"irriterend",
"teleurstellend",
"niet-aanpasbaar",
"beperkt",
"niet-slijtvast",
"beperkte grip",
"onhandelbaar",
"onbekwaam",
"niet-veelzijdig",
"ongeschikt",
"niet-waterdicht",
"onstabiele grip",
"oncomfortabel design",
"niet-stijlvol",
"teleurstellende kwaliteit",
"niet-robuust",
"niet-inspirerend",
"onveilig ontwerp",
"niet-prestatiegericht",
"onpraktisch ontwerp",
"niet-luxe",
"onplezierig",
"niet-origineel",
"onprofessioneel",
"niet-sportief",
"onvoldoende ondersteuning",
"niet-efficiënt",
"onhandige pasvorm",
"niet-goed passend",
"onduurzaam",
"niet-veerkrachtig",
"onbevredigend",
"onpraktisch materiaal",
"oncomfortabele zool",
"niet-flatterend",
"niet-vernieuwend",
"onduidelijk design",
"niet-ademende voering",
"onduidelijke maatvoering",
"onhandige sluiting",
"niet-zorgvuldig gemaakt",
"niet-veilig",
"onpraktisch gebruik",
"onverantwoord ontwerp",
"niet tevreden",
"spuuglelijk",
"waardeloos",
"te duur",
"het niet waard"

]



import re
from pathlib import Path
txt = Path('reviewsAdidas.txt').read_text()
print(txt)

text_matches = re.findall(r'"text":"(.*?)"', txt)


with open('results.txt', 'w') as f:
    for match in text_matches:
        if any(word in match for word in PositiveWordsDutch):
            f.write("positive ++\n")
        elif any(word in match for word in NegativeWordsDutch):
            f.write("negative --\n")
        else:
            f.write("neutral\n")
            
positive_counts = {word: 0 for word in PositiveWordsDutch}
negative_counts = {word: 0 for word in NegativeWordsDutch}

for match in text_matches:
    for word in PositiveWordsDutch:
        if word in match:
            positive_counts[word] += 1
    for word in NegativeWordsDutch:
        if word in match:
            negative_counts[word] += 1

print("Positive words counts:")
for word, count in positive_counts.items():
    print(f"{word}: {count}")

print("\nNegative words counts:")
for word, count in negative_counts.items():
    print(f"{word}: {count}")