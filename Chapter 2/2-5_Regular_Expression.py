#정규 표현식(Regular Expression)

import re

#.은 한 개의 임의의 문자를 나타냅니다. 예를 들어서 정규 표현식이 a.c라고 합시다. a와 c 사이에는 어떤 1개의 문자라도 올 수 있습니다. akc, azc, avc, a5c, a!c와 같은 형태는 모두 a.c의 정규 표현식과 매치됩니다.
r = re.compile("a.c")
r.search("kkk") # 아무런 결과도 출력되지 않는다.
r.search("abc")


#?는 ?앞의 문자가 존재할 수도 있고 존재하지 않을 수도 있는 경우를 나타냅니다. 예를 들어서 정규 표현식이 ab?c라고 합시다. 이 경우 이 정규 표현식에서의 b는 있다고 취급할 수도 있고, 없다고 취급할 수도 있습니다. 즉, abc와 ac 모두 매치할 수 있습니다.
r = re.compile("ab?c")
r.search("abbc") # 아무런 결과도 출력되지 않는다.
r.search("abc")

#*은 바로 앞의 문자가 0개 이상일 경우를 나타냅니다. 앞의 문자는 존재하지 않을 수도 있으며, 또는 여러 개일 수도 있습니다. 정규 표현식이 ab*c라면 ac, abc, abbc, abbbc 등과 매치할 수 있으며 b의 개수는 무수히 많을 수 있습니다.
r = re.compile("ab*c")
r.search("a") # 아무런 결과도 출력되지 않는다.
r.search("ac")

#+는 *와 유사합니다. 다른 점은 앞의 문자가 최소 1개 이상이어야 합니다. 정규 표현식이 ab+c라고 한다면 ac는 매치되지 않습니다. 하지만 abc, abbc, abbbc 등과 매치할 수 있으며 b의 개수는 무수히 많을 수 있습니다.
r = re.compile("ab+c")
r.search("ac") # 아무런 결과도 출력되지 않는다.
r.search("abc") 

#^는 시작되는 문자열을 지정합니다. 정규표현식이 ^ab라면 문자열 ab로 시작되는 경우 매치합니다.
r = re.compile("^ab")

#문자에 해당 기호를 붙이면, 해당 문자를 숫자만큼 반복한 것을 나타냅니다. 예를 들어서 정규 표현식이 ab{2}c라면 a와 c 사이에 b가 존재하면서 b가 2개인 문자열에 대해서 매치합니다.
r = re.compile("ab{2}c")

#{숫자1, 숫자2} 기호
#문자에 해당 기호를 붙이면, 해당 문자를 숫자1 이상 숫자2 이하만큼 반복합니다. 예를 들어서 정규 표현식이 ab{2,8}c라면 a와 c 사이에 b가 존재하면서 b는 2개 이상 8개 이하인 문자열에 대해서 매치합니다.
r = re.compile("ab{2,8}c")

from nltk.tokenize import RegexpTokenizer

text = "Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop"

tokenizer1 = RegexpTokenizer("[\w]+")
tokenizer2 = RegexpTokenizer("\s+", gaps=True)

print(tokenizer1.tokenize(text))
print(tokenizer2.tokenize(text))

