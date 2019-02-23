# **멋쟁이 사저처럼 7기 운영진 교육 과제 제출용 _ Word Count**

------

## 추가적으로 개선할 사항

#### 1. 폰트 적용

#### 2. 부트스트랩 예제 및 컴포넌트 적용

#### 3. 기존의 단어 수만 세는 것 외에 공백을 제외하거나 포함한 총 글자 수를 세어줌

```python
def result(request): 

​    text = request.GET['fulltext']

​    

​    length = list(text)

​    count = length.count(' ')

​    for x in range(0,count):

​        length.remove(' ')

​    words = text.split()

​    word_dictionary = {}

​    for word in words:

​        if word in word_dictionary:

​            word_dictionary[word] += 1

​        else:

​            word_dictionary[word] = 1

​    return render(request, 'result.html', {'full': text, 'total' : len(words), 'dictionary': word_dictionary.items(), 'textlength': len(length),'totaltextlength': len(text) })

​    

def count(request):

​    full_text = request.GET['fulltext']

​    word_list = full_text.split()

​    return render(request, 'wordcount/count.html', {'fulltext': full_text, 'total': len(word_list) })
```





## Home

![home](https://github.com/DustinYook/DjangoWordCount/blob/master/home.PNG)



## About

![about](https://github.com/DustinYook/DjangoWordCount/blob/master/about.PNG)



## Count

![result](https://github.com/DustinYook/DjangoWordCount/blob/master/count.PNG)
