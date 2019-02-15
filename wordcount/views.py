from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, "wordcount/about.html")

# views 즉, MVC 모델에서의 컨트롤러는 비즈니스 로직을 수행한 후 결과 페이지로 이동시키며 처리결과를 동적으로 반영하는 역할을 수행
def count(request):
    full_text = request.GET['fulltext'] 
    # request에서 fulltext라는 입력필드에서 입력받은 값을 GET 방식으로 가져옴 (GET 방식은 HTTP 메소드 중 하나)

    # 문장을 파싱하고 단어의 수를 세는 처리    
    word_list = full_text.split() # 띄어쓰기를 기준으로 문장을 자름(파싱)
    word_dictionary = {} # 포함된 단어의 사전을 구현 (중복없음)
    for word in word_list:
        if word in word_dictionary:
            # Increase count
            word_dictionary[word] += 1
        else:
            # Add to the word dictionary (discover new word)
            word_dictionary[word] = 1

    return render(request, "wordcount/count.html", {'fulltext' : full_text, 'total' : len(word_list), 'dictionary' : word_dictionary.items()})
    # 약간 JSON 통신방식과 비슷한데 full_text의 값을 fulltext라는 변수에 담아 랜더링함 (DOM 트리 구성)