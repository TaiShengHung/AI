
# coding: utf-8

# In[1]:


# Jieba5 增加停用字
#encoding=utf-8
import jieba

# 設定繁體中文詞庫
jieba.set_dictionary('dictionary/dict.txt.big.txt')  

# 增加自定義停用詞
jieba.load_userdict('dictionary/user_dict.txt')

# 打開停用字詞典
with open('dictionary/stopword.txt', 'r', encoding='utf-8-sig') as file:
    stops = file.read().split('\n')  # 將停用詞儲存在stops串列中
print("停用詞:"+'|' . join(stops))
    
sentence = "吳智鴻，來到國立臺中教育大學數位系就讀碩士。"

#jieba.add_word('數位系')
#jieba.add_word('凱特琳')
#jieba.del_word('自定义词')

# 預設模式斷詞
breakword = jieba.cut(sentence, cut_all=False)
final_words = []   #儲存最後的詞
#拆解句子為字詞
for word in breakword:     # 拆解句子為字詞
    if word not in stops:  #不是停用詞
        final_words.append(word)
print("去除停用:" + '|' . join(final_words))

breakword = jieba.cut(sentence, cut_all=False)
print("預設模式:" + '|' . join(breakword))    

# 全文模式斷詞
breakword = jieba.cut(sentence, cut_all=True)
print("全文模式:" + '|' . join(breakword))

# 搜尋引擎模式斷詞
breakword = jieba.cut_for_search(sentence)
print("搜尋引擎:" + '|' . join(breakword))

