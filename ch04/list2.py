# listc = []
# print(listc)
# listc.append(300)
# print(listc)
# listc.append("python")
# print(listc)
# listc.append(3.7)
# print(listc,"\n--------------------")

# subject = ['국어', '수학', '영어', '국사']
# print(subject)
# subject.append('영어')
# print(subject)
# subject.remove('영어')
# print(subject,"\n-------------------")

clovers = ["clover1", 'clover2', 'clover3']
#제거 키워드
del clovers[1]
print(clovers)
del clovers[1]
print(clovers)
#여러값 추가
clovers.extend(['clover10','clover20'])
print(clovers)
#특정 위치 값 추가
clovers.insert(0,'clover5')
print(clovers)