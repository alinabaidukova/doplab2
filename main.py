from pydub import AudioSegment

sound = AudioSegment.from_file("song.wav") #AudioSegment - модуль для работы с аудио

def speed(sound, speed):    #2 аргумента (аудио и скорость)
    sound_num = sound._spawn(sound.raw_data, overrides={"frame_rate": int(sound.frame_rate * speed)})   #spawn=новое уадио, sound.raw_data=исходное, происходит умножение исходной частоты на скорость
    return sound_num.set_frame_rate(sound.frame_rate)   #set_frame_rate возвращается исходную частоту, делается для сохранения качества звучание
slow = speed(sound, 0.3)
fast = speed(sound, 1.5)

slow.export('slow.wav', format = 'wav')
fast.export('fast.wav', format = 'wav')

#ошибка при выполнение выдаётся из-за неустановленных программ ffmpeg или avconv. Но код работает, тк используется встроенная версия ffmpeg