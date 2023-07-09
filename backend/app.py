from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
from googletrans import Translator

app = Flask(__name__)

@app.get('/summary')
def summary_api():
    url = request.args.get('url', '')
    video_id = url.split('=')[1]
    summary = get_summary(get_transcript(video_id))
    return summary, 200

def get_transcript(video_id):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = ' '.join([d['text'] for d in transcript_list])
    return transcript

def get_summary(transcript):
    summariser = pipeline('summarization')
    summary = ''
    for i in range(0, (len(transcript)//1000)+1):
        summary_text = summariser(transcript[i*1000:(i+1)*1000])[0]['summary_text']
        summary = summary + summary_text + ' '
    return summary


@app.get('/summary-hindi')
def summary_api_hindi():
    url = request.args.get('url', '')
    video_id = url.split('=')[1]
    translator = Translator()
    summary = get_summary_hindi(get_transcript_hindi(video_id))
    # summary_slice = summary[1:50]
    hindi_summary = translator.translate(summary, dest="hi")
    return hindi_summary.text

def get_transcript_hindi(video_id):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = ' '.join([d['text'] for d in transcript_list])
    return transcript

def get_summary_hindi(transcript):
    summariser = pipeline('summarization')
    summary = ''
    for i in range(0, (len(transcript)//1000)+1):
        summary_text = summariser(transcript[i*1000:(i+1)*1000])[0]['summary_text']
        summary = summary + summary_text + ' '
    return summary
    
 
@app.get('/summary-marathi')
def summary_api_marathi():
    url = request.args.get('url', '')
    video_id = url.split('=')[1]
    translator = Translator()
    summary = get_summary_marathi(get_transcript_marathi(video_id))
    # summary_slice = summary[1:50]
    marathi_summary = translator.translate(summary, dest="mr")
    return marathi_summary.text

def get_transcript_marathi(video_id):
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    transcript = ' '.join([d['text'] for d in transcript_list])
    return transcript

def get_summary_marathi(transcript):
    summariser = pipeline('summarization')
    summary = ''
    for i in range(0, (len(transcript)//1000)+1):
        summary_text = summariser(transcript[i*1000:(i+1)*1000])[0]['summary_text']
        summary = summary + summary_text + ' '
    return summary

if __name__ == '__main__':
    app.run()