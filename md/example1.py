text =  '''
# 見出し1
## 見出し2
### 見出し3

**太字**

*斜字*

~~削除します~~

***
線を引く
---

* 箇条書き1
* 箇条書き2
  * 箇条書き2.1
  * 箇条書き2.2
* 箇条書き3
    * 箇条書き3.1

1. 数字付き1
1. 数字付き2

ソースコードも書ける。実行はできない。

【Python】
```python
# コメント
import numpy
import pandas

print('Hello World')
```

【C言語】
```c
// コメント
#include

int main(){
    printf("Hello World")
}
```

'''

file_path = "./test.md"

with open(file_path, 'w') as file:
    file.write(text)
