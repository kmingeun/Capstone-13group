from pydub import AudioSegment

# 여러 개의 음성 파일을 불러옵니다.
part1 = AudioSegment.from_file("output1.wav")
part2 = AudioSegment.from_file("output2.wav")
part3 = AudioSegment.from_file("output3.wav")


# 음성 파일을 순서대로 합칩니다.
combined = part1 + part2 + part3 

# 합친 음성 파일을 저장합니다.
combined.export("C:/Users/ens95/Desktop/fairy_tail/combined2.wav", format="wav")
