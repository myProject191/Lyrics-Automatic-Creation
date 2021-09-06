import markovify
import MeCab

def sentence(filename):

    # Load file
    text_file = open("data/" + filename + ".txt", "r")
    text = text_file.read()

    # Parse text using MeCab
    parsed_text = MeCab.Tagger('-Owakati').parse(text)

    # Build model
    text_model = markovify.Text(parsed_text, state_size=2, well_formed=False)

    sentence = ["","","","",""]
    
    # Output
    for i in range(5):
        j = int(i)
        sentence[j] = text_model.make_short_sentence(100, 20, tries=100).replace(' ', '')
    
    print(sentence)
    return(sentence)


def artist_name(num):
    lists = ["Official髭男dism","米津玄師","back number","Mr.Children","嵐","King Gnu","ポルノグラフィティ","安室奈美恵"]
    number = int(num)
    return(lists[number])