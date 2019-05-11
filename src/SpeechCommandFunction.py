

import aubio
import numpy as num
import pyaudio
import speech_recognition as sr
# import SpeechRecognition as sr



BUFFER_SIZE             = 2048
CHANNELS                = 1
FORMAT                  = pyaudio.paFloat32
METHOD                  = "default"
SAMPLE_RATE             = 44100
HOP_SIZE                = BUFFER_SIZE//2
PERIOD_SIZE_IN_FRAME    = HOP_SIZE


def initAudio():
    # Initiating PyAudio object.
    pA = pyaudio.PyAudio()
    # Open the microphone stream.
    mic = pA.open(format=FORMAT, channels=CHANNELS,
        rate=SAMPLE_RATE, input=True,
        frames_per_buffer=PERIOD_SIZE_IN_FRAME)

    # Initiating Aubio's pitch detection object.
    pDetection = aubio.pitch(METHOD, BUFFER_SIZE,
        HOP_SIZE, SAMPLE_RATE)
    # Set unit.
    pDetection.set_unit("Hz")
    # Frequency under -40 dB will considered
    # as a silence.
    pDetection.set_silence(-40)
    
    return mic,pDetection


def SpeechRecognition(mic, pDetection):
    # Always listening to the microphone.
    data = mic.read(PERIOD_SIZE_IN_FRAME)
                    # Convert into number that Aubio understand.
    samples = num.fromstring(data,
    dtype=aubio.float_type)
                    # Finally get the pitch.
    pitch = pDetection(samples)[0]
                    # Compute the energy (volume)
                    # of the current frame.
    volume = num.sum(samples**2)/len(samples)
            
    volume = "{:3f}".format(volume)
                    
#                     if(float(volume) > 0.000020):
            #             print("Am thanh ######### ",float(volume))
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak into the microphone")
        audio = r.listen(source)
    try:
        speechCommand = r.recognize_google(audio)
        print("Transcription: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        speechCommand = ' I can not understand '
        print("Audio unintelligible")
    except sr.RequestError as e:
        speechCommand = ''
        print("Cannot obtain results; {0}".format(e))

    
    return speechCommand    
    
    

